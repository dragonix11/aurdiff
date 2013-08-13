aurdiff - Record PKGBUILD history
---

Arch's AUR are great, especially with yaourt, but keeping up with PKGBUILD updates is tiring
because we don't have access to diffs, only full files. Wouldn't it be great if you could say, upon
updates, stuff like "oh, the package maintainer has only updated version numbers. Since I've already
reviewed the previous PKGBUILD to make sure it wasn't malicious, I don't have to review it again"?

Well I thought so. That's what this package is for. It regularly fetches the latest updated from the
AUR and commits them to this git repo. This way, you can access those PKGBUILD history.
