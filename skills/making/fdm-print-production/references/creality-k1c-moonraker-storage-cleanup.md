# Creality K1C / Moonraker printer storage cleanup

Use when the printer touchscreen reports low memory/storage or shows stale print-job folders after many prints.

## Known device shape from session

- Creality K1C/K1C-0CF3 was reachable on LAN at `<printer-ip>`.
- Moonraker/Klipper-compatible API exposed on `http://<printer-ip>:7125`.
- Internal storage reported by `GET /machine/system_info`:
  - `sd_info.capacity`: about `3.2 GiB`
  - `sd_info.total_bytes`: `3409444864`
- Printer RAM is separate and small (~200 MB); the common failure is gcode/log storage, not RAM.

## Safe sequence

1. Confirm this is the printer, not the Mac:

```bash
HOST=<printer-ip>
curl -sS "http://$HOST:7125/printer/info" | python3 -m json.tool
curl -sS "http://$HOST:7125/server/info" | python3 -m json.tool
```

Look for hostname/model, e.g. `K1C-0CF3`, and `klippy_state: ready`.

2. Confirm it is idle before deletion:

```bash
curl -sS "http://$HOST:7125/printer/objects/query?print_stats&virtual_sdcard" | python3 -m json.tool
```

Proceed only if `print_stats.state` is `standby`/idle and `virtual_sdcard.is_active` is `false`.

3. List stored print files:

```bash
curl -sS "http://$HOST:7125/server/files/list?root=gcodes" > /tmp/k1c-gcodes.json
python3 - <<'PY'
import json
files=json.load(open('/tmp/k1c-gcodes.json')).get('result', [])
print('count', len(files), 'total_mb', round(sum(int(f.get('size') or 0) for f in files)/1024/1024,2))
for f in sorted(files, key=lambda x:int(x.get('size') or 0), reverse=True):
    p=f.get('path') or f.get('filename') or f.get('name') or ''
    print(f'{int(f.get("size") or 0)/1024/1024:7.2f} MB {p}')
PY
```

4. Back up before deleting user print-history files:

```bash
BACKUP="$HOME/3d-printer-backups/K1C-0CF3-user-gcodes-purge-$(date +%Y%m%d-%H%M%S)"
mkdir -p "$BACKUP/gcodes"
```

Download each target with `GET /server/files/gcodes/<url-encoded-path>` and verify local size before deletion.

5. Delete normal filenames with Moonraker HTTP DELETE:

```bash
curl -X DELETE "http://$HOST:7125/server/files/gcodes/<url-encoded-path>"
```

## Creality special-character delete bug

Creality's Moonraker fork may fail to delete filenames with spaces, `+`, etc. The error can look like:

```text
HTTP 400 file no exits at '/usr/data/printer_data/gcodes/CREALITY%20Printer%20Accessory...'
```

This is not necessarily a stale touchscreen cache and a reboot alone does not remove the backend file. Workaround:

1. Rename the stubborn file to a simple temporary name using `POST /server/files/move` with raw JSON paths.
2. Delete the sanitized name with regular DELETE.

Example:

```python
import json, urllib.request, urllib.parse
host='<printer-ip>'
old='CREALITY Printer Accessory Tool Box_08161304.gcode'
safe='_purge_01.gcode'

payload={'source':'gcodes/'+old, 'dest':'gcodes/'+safe}
req=urllib.request.Request(
    f'http://{host}:7125/server/files/move',
    data=json.dumps(payload).encode(),
    headers={'Content-Type':'application/json'},
    method='POST',
)
urllib.request.urlopen(req, timeout=30).read()

encoded=urllib.parse.quote(safe, safe='/')
delreq=urllib.request.Request(
    f'http://{host}:7125/server/files/gcodes/{encoded}',
    method='DELETE',
)
urllib.request.urlopen(delreq, timeout=30).read()
```

## Factory/sample files to keep if the user asks to preserve defaults

In the observed K1C, the user wanted to keep factory/sample/benchmark-looking files such as:

- `3DBenchy_PLA_19m.gcode`
- `600S-TEST_Hyper PLA_7m.gcode`
- `Delta filament barrel base_Hyper PLA_49m.gcode`
- `Flexi-Rex_PLA_38m19s.gcode`
- `Logo filament barrel base_Hyper PLA_54m.gcode`

Everything else in `gcodes` can be treated as user print-history only after explicit user approval.

## Logs can also consume storage

`logs` may contain hundreds of MB of rotated `klippy.log.YYYY-MM-DD` and dated service logs. Safe pattern:

- Back up large rotated logs first.
- Delete rotated logs only, not active logs like `klippy.log`, `nexusp.log`, `onyxp.log`, etc.
- Re-list `root=logs` after cleanup and report freed MB.

## Final verification

Always re-list after deleting and report:

- remaining gcode count
- remaining gcode total MB
- kept files
- backup directory

If the touchscreen still shows empty folders but `/server/files/list?root=gcodes` is clean, it is probably UI cache. A printer restart may clear the display, but backend verification is authoritative.