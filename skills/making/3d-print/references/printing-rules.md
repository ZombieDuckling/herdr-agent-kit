# Printing rules (fixed MVP profile)

## Fixed print target

| Setting  | Value                       |
|----------|-----------------------------|
| Printer  | Bambu Lab A1 Mini           |
| Nozzle   | 0.4 mm (stock)              |
| Filament | Bambu PLA Basic             |
| Process  | 0.20 mm Standard            |
| Bed      | Textured PEI Plate          |
| Volume   | 180 × 180 × 180 mm          |

These are baked into the toolchain (`profiles/*.json`, pinned to Bambu
Studio v02.07.01.62). Do not offer other printers, nozzles, materials, AMS
or multi-color — answer that the MVP is fixed to this combination.

## Confirmation gate

Slice only after the user *explicitly* asks for the print file. Treat as
confirmation: «печатаем», «готово, делай файл», «всё подходит», «готовь к
печати», "print it", "make the file". Not confirmation: likes, compliments,
"выглядит хорошо", silence. If ambiguous — ask one short question.

## Pipeline and checks (what `print3d slice` guarantees)

`model.py → final.stl → Bambu Studio CLI → final.3mf`, then: exit code 0,
file exists and is non-empty, is a valid ZIP with a 3MF payload. Project
status becomes `ready`. On failure: status `failed`, `final.stl` and
`output/slicer.log` are kept for diagnosis — never send them as a result.

## Delivering the result

Send the `.3mf` file itself (Telegram attachment), then a short message in
The user's language:

> Готово. Файл нарезан под:
> A1 Mini · сопло 0,4 мм · Bambu PLA Basic · слой 0,20 мм.
>
> Скопируй файл на microSD и запускай печать.

Useful to add when relevant: approximate object footprint in mm, that the
first layer orientation matches the preview, and that PLA likes a clean
plate.

## Out of scope (refuse politely)

Direct LAN/cloud printing, MakerWorld upload, AMS/multi-color, other
filaments/nozzles, automatic model splitting, food-safe/structural
certification claims.
