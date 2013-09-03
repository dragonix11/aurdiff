#Maintainer: Johannes Visintini <arch at joker234.de>
pkgname=shellex
pkgver=0.1 # don't forget to change sha1sums (with makepkg -g) if you update this
pkgrel=1
pkgdesc="shell-based launcher"
arch=('i686' 'x86_64')
url='https://github.com/Merovius/shellex'
license=('BSD')
depends=('rxvt-unicode' 'zsh' 'perl-x11-protocol' 'xorg-xrandr')
makedepends=('wget' 'asciidoc' 'docbook-xsl' 'tar')
source=(https://github.com/Merovius/$pkgname/archive/$pkgver.tar.gz)
sha1sums=('074f6869a95b7bbdbf2e494c0600ab4b6978e66d')
conflicts=('shellex-git')

build() {
	cd "$pkgname-$pkgver"
	make
	make -C doc/man
}

package() {
	cd "$pkgname-$pkgver"
	make DESTDIR="$pkgdir/" install

	install -Dm644 doc/man/shellex.1 \
		${pkgdir}/usr/share/man/man1/shellex.1

	install -Dm644 LICENSE \
		${pkgdir}/usr/share/licenses/${pkgname}/LICENSE

	make clean
}
