# LDraw 2026-10+bw.1 for Brick Wrangler

Merge the complete official 2026-10 library, released 2026-10-26, onto the
maintained fork. The unchanged official base is separately committed as
`21f2b40a` on `upstream-2026-10`. Its 37,448 files exactly match the official
complete archive; applying the official update to 2026-09 gives the same tree.
There are 259 changed/added paths including configuration and release notes,
with no removed files.

Sixteen add/add overlaps are prior unofficial imports now certified upstream.
Resolve each to the exact official file: normalized geometry and BFC/TEXMAP
records are identical. All four locally corrected files (`45677`, `11253`,
`s/41770as01`, `s/41770bs01`) remain byte-for-byte unchanged from bw.4.
Unrelated unofficial additions remain intact. No current Parts Tracker source
supersedes these corrections or fixes the held house candidates.

The recursive source audit identifies one physically affected curated part,
`42022`, and twelve byte-affected print identities. The changed print surface
is `88930py0`; `88930pz4` changes conditional edges only. LDConfig changes only
AVATAR metadata; colour definitions are unchanged. Catalogue validation and
print-equivalence results are recorded in the Brick Wrangler upstream task.

Additionally refresh the already imported unofficial menu tile print
`26603p0d` from Philippe Hurbain's 2026-10-23 Parts Tracker correction. Its mug
interior now uses the intended main colour. The tracker has no current hold;
the single dependency `s/26603s01.dat` is unchanged. The exact updated print
passes Brick Wrangler's existing bidirectional surface-equivalence check
against catalogue base `26603`. Preserve attribution, license and unofficial
status, with a dated fork import history line. Other pending tracker geometry
revisions are not included.

This is a new immutable source identity, `2026-10+bw.1`; previous archives are
unchanged. It includes official fixes without claiming new catalogue coverage
for every newly released part. No source correction is submitted upstream.

