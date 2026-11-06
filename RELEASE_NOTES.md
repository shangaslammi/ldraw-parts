# LDraw 2026-10+bw.2 for Brick Wrangler

Correct the two short stud-dent wall extensions in the shared 2 x 2 wing
subpart `s/51739s01.dat` using that subpart's own radius-six cylinder facets
and existing exterior wall. Maximum vertex movement is 0.003122191 LDU.
Update the adjoining faces, edges and wall transforms consistently; preserve
the original author, licence and history, and mark the changed subpart unofficial.

Both hands (`24299`, `24307`), their `p01` prints and `51739` inherit the
correction. All five descendants pass material/free-space probes and continuous
corrected-source surface coverage. Both original OMR 31072 wedge contacts now
validate; source-supported blocked controls remain blocked. No Shadow
connections, tolerance or source-roundoff policy changes. The geometry follows
existing source facets; it is not an independent physical measurement.

This release retains the complete official 2026-10 base, the previous four
source corrections and all unrelated unofficial imports unchanged. The
unverified `27261` alternative diagonal is not included. It creates the new
immutable identity `2026-10+bw.2`; previous archives remain unchanged.
Nothing has been submitted upstream. See `CHANGES.md` for the derivation and limits.
