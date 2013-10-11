# Contributor: graysky <graysky AT archlinux dot us>
pkgname=pulseaudio_ctl
pkgver=1.20
pkgrel=1
pkgdesc='Control pulseaudio volume from the shell or mapped to keyboard shortcuts.  No need for alsa-utils.'
arch=('any')
license=('GPL')
depends=('pulseaudio')
url=https://bbs.archlinux.org/viewtopic.php?id=124513
source=("http://repo-ck.com/source/$pkgname/$pkgname-$pkgver.tar.xz")
sha256sums=('5ed393ae4fc6dc992aaabe84431ce1719f9a06665adf990b5066a696f7bb4851')
install=readme.install

package() {
	cd "$pkgname-$pkgver"
	for i in mute_toggle vol_up vol_down; do
		install -Dm755 $i "$pkgdir/usr/bin/$i"
	done
}

# vim:set ts=2 sw=2 et:
