# Maintainer: Elie Bouttier <elie@bouttier.eu.org>
# Contributor: Pierre Carrier <pierre@gcarrier.fr>
_ghuser=freelan-developers
pkgname=libfscp
pkgver=2.1
_pkgid=04154d5
pkgrel=1
pkgdesc="A library that implements the FreeLAN Secure Channel Protocol"
arch=(i686 x86_64)
url="http://www.freelan.org/"
license=('GPL')
depends=('boost-libs' 'libcryptoplus')
makedepends=('scons' 'freelan-buildtools' 'boost' 'libcryptoplus')
source=("https://github.com/$_ghuser/$pkgname/tarball/$pkgver")
md5sums=('1a0705d53d3f6cfcab657bfca2876edd')

build() {
  cd "$srcdir/$_ghuser-$pkgname-$_pkgid"
  scons
}

package() {
  cd "$srcdir/$_ghuser-$pkgname-$_pkgid"
  scons install prefix="$pkgdir/usr"
}
