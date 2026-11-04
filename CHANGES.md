# Changes from the official library

## 2026-09+bw.4 — 2026-11-04

Refine the common inner-wall corner in `parts/s/41770as01.dat` and
`parts/s/41770bs01.dat` from `(14.38, y, 34.03)` to
`(14.3844, y, 34.03)`, consistently across adjoining faces and edges.
The outer wall has slope 1:4; its nominal four-LDU normal offset gives
`x = z/4 + 10 - sqrt(17)`, or 14.3843943744 at this Z. Preserve original
authors, licenses and history; mark the modified shared subparts unofficial.

Both 41769/41770 hands and a/b moulds inherit the correction. Nominal stud-seat
intrusion falls from 0.003893418760 to 0.000235175697 LDU, within the unchanged
0.001-LDU source roundoff. All eight affected descendants (41769, 41769a/b,
41770, 41770a/b, 63330 and 63333) pass closed-mesh decomposition, material and
free-space probes, original-mesh surface coverage and bounds checks. Their
surface certificates have zero uncovered triangles.

Full production builders also pass for both hands, both moulds and the
63330/63333 descendants when paired with Shadow fork commit
0cfb26187631c6b62759b265d27bcaedaae7c2f9, which adds independently verified
missing seats at z=10. This geometry release does not itself add Shadow data
or relax checks. No physical measurement or assembly validation is claimed. No 3933/3934 geometry is changed. The 45677/11253 corrections and
unofficial additions from earlier releases remain unchanged.

Evidence and the separately reviewable source patch:
[Brick Wrangler house wedge source task](https://github.com/shangaslammi/brick-wrangler/blob/codex/house-catalog-tooling/reports/tasks/house-wedge-mesh.md).
The source record identifies this release as `2026-09+bw.4`, based on official
2026-09. Nothing has been submitted to the upstream Parts Tracker.

## 2026-09+bw.3 — 2026-10-22

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

## 2026-09+bw.2 — 2026-10-21

Correct `parts/11253.dat` (Minifig Roller Skate). Four top faces and their
type-2 boundary edges took a direct chord between two vertices while adjacent
inside faces followed an existing intermediate vertex 0.00376348 LDU off that
chord. Split each quad into three triangles through the existing vertex and
split its edge to match. No coordinates or idealized socket dimensions are
invented. Preserve the original author/license; mark the modified part unofficial.

The nominal stud-space intrusion falls from 0.00368364 to 0.00002009 LDU,
below Brick Wrangler's existing mesh roundoff. Checked experimental proxies
cover all 694 corrected source triangles. This source correction alone does
not fix the collision proxy's missing underside seat; that remains separate
proxy-generation work. The earlier 45677 corrections are unchanged.

Evidence and proposed geometry patch:
[Brick Wrangler source investigation](https://github.com/shangaslammi/brick-wrangler/blob/codex/omr-collision-pilot/reports/tasks/omr-source-mesh-followup.md).
No claw-plate triangulation change is included, and nothing has been submitted
to the upstream Parts Tracker.

## 2026-09+bw.1 — 2026-10-21

Only `parts/45677.dat` geometry changes; all other upstream files are unchanged.

1. **Socket contours:** explicit wall coordinates used 0.92, 0.38 and 0.70
   unit-circle factors, while their own radius-6 cap primitives use 0.9239,
   0.3827 and 0.7071. Match shared wall/roof/line vertices to those cap edges.
   This removes about 0.0591 LDU of source-surface intrusion into a standard stud.
2. **Underside seams:** join shared endpoints that disagreed by 0.01–0.02 LDU.
   Use the existing wall heights consistently across adjoining faces and lines.
3. **Rear ledge:** move the shared vertices at (±26.1, y, −67) to
   (±26, y, −67), on the diagonal joining (±20, −70) and (±40, −60).
   This closes the ledge/wall mismatch that blocked 0.5 LDU decomposition.

These corrections were isolated in an eight-variant experiment against the
original 2026-09 source. Corrected proxies cover all 1,082 corrected triangles
and pass existing material/free-space probes at both 1 and 0.5 LDU resolutions.
The contour correction clears the OMR 4883-1 wedge/plate contact. Four repeated
wedge/slope contacts also clear when the separately identified scaled-stud
proxy-recognition defect in part 3660 is corrected; that proxy change is not
part of this source fork.

Evidence and reproduction:
[Brick Wrangler source study](https://github.com/shangaslammi/brick-wrangler/blob/codex/omr-collision-pilot/reports/tasks/omr-wedge-source.md).
Physical measurements have not been made. The fixes reconcile inconsistent
source geometry; they do not certify the entire part mesh or assembly motion.
