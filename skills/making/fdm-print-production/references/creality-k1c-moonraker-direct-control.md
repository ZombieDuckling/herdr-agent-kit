# Creality K1C Moonraker direct-control workflow

This reference captures a tested path for direct control of a Creality K1C that exposes Moonraker/Nexusp on the LAN. Use it as a pattern, not as a hardcoded assumption for every printer.

## Discovery

1. Find the LAN subnet and ARP neighbors.
2. Look for Creality Print device records, commonly under macOS Application Support. A K1C record may include fields such as `address`, `model`, and `mac`.
3. Probe open ports read-only. A K1C may expose:
   - `7125` — Moonraker-compatible API
   - `8000` — WebRTC camera page
   - `80`, `8081`, `9999`, `22` — vendor/auxiliary services

Useful read-only Moonraker probes:

```sh
curl http://PRINTER:7125/server/info
curl http://PRINTER:7125/printer/info
curl 'http://PRINTER:7125/printer/objects/query?print_stats&virtual_sdcard&toolhead&extruder&heater_bed&webhooks'
curl 'http://PRINTER:7125/server/files/list?root=gcodes'
```

## Slicing

Moonraker starts G-code, not raw STL. For Creality Print on macOS, the app binary can also act as a slicer CLI:

```sh
'/Applications/Creality Print.app/Contents/MacOS/CrealityPrint' \
  --slice 0 \
  --outputdir "$OUT" \
  --load-settings "$MACHINE;$PROCESS" \
  --load-filaments "$FILAMENT" \
  --arrange 1 \
  --ensure-on-bed \
  "$STL"
```

Validate the generated G-code before upload. Capture at least:

- generated-by slicer line
- `START_PRINT` temperatures
- estimated time
- filament length/weight
- layer count/object height from metadata after upload

## Upload/start

Upload without auto-start first:

```sh
curl -X POST \
  -F "file=@$GCODE;filename=$REMOTE" \
  -F "root=gcodes" \
  -F "print=false" \
  "http://PRINTER:7125/server/files/upload"
```

Then confirm metadata and start the exact path returned by upload:

```sh
curl --get --data-urlencode "filename=$RETURNED_PATH" \
  "http://PRINTER:7125/server/files/metadata"

curl -X POST -H 'Content-Type: application/json' \
  -d "{\"filename\":\"$RETURNED_PATH\"}" \
  "http://PRINTER:7125/printer/print/start"
```

Pitfall: some Moonraker/Nexusp implementations create a nested path if both a path and filename are supplied. If start fails with “Unable to open file”, list/metadata the uploaded item and start the exact nested path returned by the API.

## Monitoring

Poll this object set:

```sh
curl 'http://PRINTER:7125/printer/objects/query?print_stats&virtual_sdcard&extruder&heater_bed&toolhead&webhooks'
```

Do not treat early `state=printing` as proof of extrusion. K1C may report printing during heat-up/calibration. Wait for at least one of:

- `print_duration > 0`
- `filament_used > 0`
- `virtual_sdcard.progress` advances beyond the static warm-up position

## Camera

The K1C camera page may be WebRTC at:

```text
http://PRINTER:8000/
POST /call/webrtc_local
```

It is not necessarily an MJPEG/JPEG endpoint. Browser pages may show a black captured frame even when telemetry is valid. If camera capture is not independently verified, report telemetry separately from visual evidence.
