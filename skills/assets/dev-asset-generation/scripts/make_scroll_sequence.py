#!/usr/bin/env python3
"""Create a deterministic scroll-scrub image sequence from two keyframes.

This is the reliable baseline path for scroll-driven cinematic sections:
- start/end keyframes can come from AI generation, screenshots, or video frames
- ffmpeg normalizes them to the same size
- ffmpeg blends/interpolates a numbered WebP/JPEG sequence
- generated frames are ready for a canvas/img scroll scrubber

It is not optical-flow/generative interpolation. It is intentionally boring and
reliable. Upgrade the middle-frame generator later (RIFE/ComfyUI/video model),
keep the same output contract: numbered frames in an output directory.
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path


def run(cmd: list[str]) -> None:
    proc = subprocess.run(cmd, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if proc.returncode != 0:
        print(proc.stdout, file=sys.stderr)
        raise SystemExit(proc.returncode)


def ffprobe_size(path: Path) -> str:
    proc = subprocess.run(
        [
            "ffprobe", "-v", "error", "-select_streams", "v:0",
            "-show_entries", "stream=width,height", "-of", "csv=s=x:p=0", str(path)
        ],
        text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )
    return proc.stdout.strip() if proc.returncode == 0 else "unknown"


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate numbered frames for scroll-scrub motion")
    parser.add_argument("--start", required=True, help="Start keyframe image path")
    parser.add_argument("--end", required=True, help="End keyframe image path")
    parser.add_argument("--out-dir", required=True, help="Output directory for numbered frames")
    parser.add_argument("--frames", type=int, default=72, help="Number of frames to export")
    parser.add_argument("--width", type=int, default=1440, help="Output width")
    parser.add_argument("--height", type=int, default=810, help="Output height")
    parser.add_argument("--fps", type=int, default=24, help="Virtual FPS for ffmpeg timing")
    parser.add_argument("--format", choices=["webp", "jpg", "png"], default="webp")
    parser.add_argument("--quality", type=int, default=82, help="WebP/JPEG quality-ish value")
    parser.add_argument("--prefix", default="frame", help="Frame filename prefix")
    parser.add_argument("--manifest", default="manifest.json", help="Manifest filename inside out-dir")
    parser.add_argument("--clean", action="store_true", help="Delete out-dir before generating")
    args = parser.parse_args()

    if not shutil.which("ffmpeg"):
        raise SystemExit("ffmpeg is required but was not found in PATH")

    start = Path(args.start).expanduser().resolve()
    end = Path(args.end).expanduser().resolve()
    out_dir = Path(args.out_dir).expanduser().resolve()
    if not start.is_file():
        raise SystemExit(f"Start frame not found: {start}")
    if not end.is_file():
        raise SystemExit(f"End frame not found: {end}")
    if args.frames < 2:
        raise SystemExit("--frames must be >= 2")
    if args.clean and out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    duration = args.frames / args.fps
    w, h = args.width, args.height
    ext = args.format
    # Some Homebrew/macOS ffmpeg builds decode WebP but do not ship the libwebp encoder.
    # Fall back to JPEG rather than failing the workflow; the manifest reports the actual format.
    if ext == "webp":
        encoders = subprocess.run(["ffmpeg", "-hide_banner", "-encoders"], text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout
        if "libwebp" not in encoders and " webp" not in encoders:
            print("warning: ffmpeg has no WebP encoder; falling back to jpg", file=sys.stderr)
            ext = "jpg"
    pattern = out_dir / f"{args.prefix}-%04d.{ext}"

    # Normalize both inputs to identical geometry, then blend over time.
    # T is timestamp in seconds, so alpha = T / duration.
    scale_crop = f"scale={w}:{h}:force_original_aspect_ratio=increase,crop={w}:{h},setsar=1"
    blend_expr = f"A*(1-T/{duration})+B*(T/{duration})"
    vf = (
        f"[0:v]{scale_crop}[a];"
        f"[1:v]{scale_crop}[b];"
        f"[a][b]blend=all_expr='{blend_expr}',fps={args.fps},trim=duration={duration},setpts=PTS-STARTPTS[out]"
    )

    cmd = [
        "ffmpeg", "-y",
        "-loop", "1", "-t", f"{duration:.6f}", "-i", str(start),
        "-loop", "1", "-t", f"{duration:.6f}", "-i", str(end),
        "-filter_complex", vf,
        "-map", "[out]",
    ]
    if ext == "webp":
        cmd += ["-c:v", "libwebp", "-q:v", str(args.quality), "-compression_level", "4"]
    elif ext == "jpg":
        cmd += ["-q:v", str(max(2, min(31, 31 - round(args.quality / 4))))]
    cmd += ["-frames:v", str(args.frames), str(pattern)]
    run(cmd)

    frames = sorted(out_dir.glob(f"{args.prefix}-*.{ext}"))
    if len(frames) != args.frames:
        raise SystemExit(f"Expected {args.frames} frames, found {len(frames)} in {out_dir}")

    manifest = {
        "success": True,
        "start": str(start),
        "end": str(end),
        "start_size": ffprobe_size(start),
        "end_size": ffprobe_size(end),
        "out_dir": str(out_dir),
        "frame_count": len(frames),
        "width": w,
        "height": h,
        "fps": args.fps,
        "format": ext,
        "pattern": f"{args.prefix}-%04d.{ext}",
        "frames": [p.name for p in frames],
    }
    (out_dir / args.manifest).write_text(json.dumps(manifest, indent=2))
    print(json.dumps(manifest, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
