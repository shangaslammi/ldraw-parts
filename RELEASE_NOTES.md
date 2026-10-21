Adds 327 Rebrickable-advertised LDraw IDs absent from official 2026-09,
with their required unofficial dependencies from the LDraw Parts Tracker.
The archive gains 571 files: 359 parts (327 selected IDs and 32 dependencies),
164 subparts, 21 primitives and 27 texture images. Original author, license,
and unofficial status headers are retained, with a dated fork history line.

Of 435 advertised values considered, 85 are excluded because the file or a
required dependency carries a hold vote, 21 are absent from the unofficial
archive, and two are non-filename placeholders. Every included file parses
and its references resolve with the existing official files retained.
No existing library file is replaced; earlier 45677 and 11253 corrections
remain byte-for-byte unchanged. Seven referenced paths have differing
tracker updates, which are excluded in favour of the existing files.

The source record identifies this release as `2026-09+bw.3`.
`complete.zip` retains the standard `ldraw/parts/` and `ldraw/p/` layout.
The packaging helper now includes tracked additions as well as every file
in the official base, preserving the existing deterministic ZIP settings.
These are unofficial source files, not a new claim of physical/proxy validation.
See UNOFFICIAL_IMPORT.md for selection, exclusions and conflict details.
