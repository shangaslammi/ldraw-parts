# LDraw parts for Brick Wrangler

A maintained source fork of the [official LDraw parts library](https://library.ldraw.org/),
used by [Brick Wrangler](https://github.com/shangaslammi/brick-wrangler).
This is not an official LDraw distribution or an LDraw-endorsed project.

Base: official **2026-09**, imported unchanged on the `upstream` branch.
Fork release: **2026-09+bw.2**. Download
[`complete.zip`](https://github.com/shangaslammi/ldraw-parts/releases/latest/download/complete.zip)
or point `BRICKWRANGLER_LDRAW` at this checkout.

The fork keeps corrections small and independently reviewable. `parts/45677.dat`
has three corrections: its socket walls now match the radius-6 cap primitives;
adjacent underside seam vertices agree; and the rear ledge meets its diagonal
walls. The original author and license are retained, the changed part is marked
unofficial, and each change has a history entry. `parts/11253.dat` also joins
four mismatched roller-skate face boundaries using its existing vertices.
See [CHANGES.md](CHANGES.md).

## Upstream

The parts' upstream is the LDraw Parts Library, not a GitHub repository.
Corrections can be proposed through the [LDraw Parts Tracker](https://library.ldraw.org/tracker).
Our correction commits and numerical evidence are suitable starting points for
that review. Nothing has been submitted upstream yet.

## Releases and updates

`brickwrangler-source.json` records the upstream release, fork version and
repository. Every published source change gets a new `YYYY-RR+bw.N` version;
never replace an existing release's archive with different geometry. Brick
Wrangler includes this version in build provenance and geometry cache keys.

To publish a committed release:

```sh
python3 tools/package_release.py
git tag 2026-09+bw.2
git push origin main upstream --tags
gh release create 2026-09+bw.2 dist/complete.zip --title '2026-09+bw.2' --notes-file RELEASE_NOTES.md
```

`tools/package_release.py` packages the full official inventory plus the source
record. It reads corrected contents from the working branch, refuses uncommitted
changes, and keeps archive order/timestamps deterministic.

For an upstream update, import the new official archive on `upstream`, then
merge that branch into `main`, resolving modified parts explicitly. Update the
source record, rerun mesh and assembly checks, and publish a new fork version.
There is no automatic sync that could overwrite local corrections.

## Attribution and license

LDraw geometry belongs to its individual authors, identified in the source
headers. Preserve those headers and history when redistributing or editing.
The imported [CAreadme.txt](CAreadme.txt), [CAlicense.txt](CAlicense.txt) and
[CAlicense4.txt](CAlicense4.txt) contain the upstream notices and licenses.
Modified portions added by this project are licensed under CC BY 4.0, as recorded
in the part's history. Original dual-licensed material retains its original
terms. Fork documentation and packaging code are also CC BY 4.0.
