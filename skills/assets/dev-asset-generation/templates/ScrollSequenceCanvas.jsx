import { useEffect, useMemo, useRef } from 'react';

/**
 * ScrollSequenceCanvas
 *
 * Props:
 * - frameBase: URL prefix ending before the number, e.g. "/sequence/wash/frame-"
 * - frameCount: number of frames, e.g. 72
 * - extension: "webp" | "jpg" | "png"
 * - pad: filename numeric padding, default 4 -> 0001
 * - heightVh: scroll distance/pin height, default 360
 *
 * Expected files:
 * /sequence/wash/frame-0001.webp ... frame-0072.webp
 */
export default function ScrollSequenceCanvas({
  frameBase = '/sequence/wash/frame-',
  frameCount = 72,
  extension = 'webp',
  pad = 4,
  heightVh = 360,
  children,
}) {
  const sectionRef = useRef(null);
  const canvasRef = useRef(null);
  const imagesRef = useRef([]);
  const currentFrameRef = useRef(-1);

  const frameUrls = useMemo(() => {
    return Array.from({ length: frameCount }, (_, i) => {
      const n = String(i + 1).padStart(pad, '0');
      return `${frameBase}${n}.${extension}`;
    });
  }, [frameBase, frameCount, extension, pad]);

  useEffect(() => {
    let cancelled = false;
    imagesRef.current = frameUrls.map((src, index) => {
      const img = new Image();
      img.decoding = 'async';
      img.loading = index < 6 ? 'eager' : 'lazy';
      img.src = src;
      return img;
    });

    const first = imagesRef.current[0];
    first.onload = () => {
      if (!cancelled) drawFrame(0);
    };
    if (first.complete) drawFrame(0);

    function resizeCanvas() {
      const canvas = canvasRef.current;
      if (!canvas) return;
      const dpr = Math.min(window.devicePixelRatio || 1, 2);
      canvas.width = Math.floor(canvas.clientWidth * dpr);
      canvas.height = Math.floor(canvas.clientHeight * dpr);
      drawFrame(currentFrameRef.current < 0 ? 0 : currentFrameRef.current);
    }

    function drawFrame(index) {
      const canvas = canvasRef.current;
      const img = imagesRef.current[index];
      if (!canvas || !img || !img.complete || !img.naturalWidth) return;
      const ctx = canvas.getContext('2d');
      const cw = canvas.width;
      const ch = canvas.height;
      const scale = Math.max(cw / img.naturalWidth, ch / img.naturalHeight);
      const w = img.naturalWidth * scale;
      const h = img.naturalHeight * scale;
      const x = (cw - w) / 2;
      const y = (ch - h) / 2;
      ctx.clearRect(0, 0, cw, ch);
      ctx.drawImage(img, x, y, w, h);
      currentFrameRef.current = index;
    }

    function onScroll() {
      const section = sectionRef.current;
      if (!section) return;
      const rect = section.getBoundingClientRect();
      const scrollable = rect.height - window.innerHeight;
      const progress = Math.min(1, Math.max(0, -rect.top / scrollable));
      const next = Math.round(progress * (frameCount - 1));
      if (next !== currentFrameRef.current) drawFrame(next);
    }

    resizeCanvas();
    onScroll();
    window.addEventListener('resize', resizeCanvas, { passive: true });
    window.addEventListener('scroll', onScroll, { passive: true });
    return () => {
      cancelled = true;
      window.removeEventListener('resize', resizeCanvas);
      window.removeEventListener('scroll', onScroll);
    };
  }, [frameUrls, frameCount]);

  return (
    <section ref={sectionRef} className="scroll-sequence" style={{ '--sequence-height': `${heightVh}vh` }}>
      <div className="scroll-sequence__sticky">
        <canvas ref={canvasRef} className="scroll-sequence__canvas" aria-hidden="true" />
        <div className="scroll-sequence__content">{children}</div>
      </div>
    </section>
  );
}
