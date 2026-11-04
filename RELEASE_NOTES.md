Refines one rounded inner-wall corner in the two shared 2 x 4 wing subparts,
`s/41770as01.dat` and `s/41770bs01.dat`. The correction follows the nominal
four-LDU offset of the existing 1:4 wall; every incident face and edge uses
the same refined vertex. Original authors and licenses are preserved, and
the modified subparts are marked unofficial.

Both 41769/41770 hands and a/b moulds inherit the correction. Nominal stud-seat
intrusion falls from 0.003893418760 to 0.000235175697 LDU, within the unchanged
0.001-LDU source roundoff. All eight affected descendants pass independent
closed-mesh, material, free-space, original-surface coverage and bounds checks;
their surface certificates have zero uncovered triangles.

Both hands, both moulds and 63330/63333 also pass production builders with
Shadow fork commit 0cfb26187631c6b62759b265d27bcaedaae7c2f9, which adds
independently verified missing seats at z=10. This geometry release does not
itself add connector data or relax checks. No 3933/3934 repair, physical measurement or assembly validation
is claimed. Earlier source corrections and unofficial additions are unchanged.

Source identity: `2026-09+bw.4`, based on official 2026-09. The complete archive
keeps the standard `ldraw/parts/` and `ldraw/p/` layout. Nothing has been submitted
to the upstream Parts Tracker. See CHANGES.md for numerical evidence and scope.
