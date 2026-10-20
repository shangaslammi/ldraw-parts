# Changes from the official library

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
