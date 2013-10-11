# Maintainer: Jean-Alexandre Anglès d'Auriac <jagw40k@free.fr>

pkgname=buuficontheme
pkgver=3.10
pkgrel=1
pkgdesc="An icon theme for Gnome based on the Buuf iconset by Mattahan"
arch=('any')
url="http://buuficontheme.free.fr"
license=('cc-by-nc-sa')
depends=('hicolor-icon-theme')
optdepends=()
source=($pkgname-$pkgver.tar.xz::http://buuficontheme.free.fr/buuf$pkgver.tar.xz)
md5sums=('1d8c9c16557252bfe9b090076988503a')

build() {
  cd .
}

package() {
  mkdir -p "${pkgdir}/usr/share/icons/${pkgname}/"
  cp -r ${srcdir}/buuf${pkgver}/* "${pkgdir}/usr/share/icons/${pkgname}/"
}
