# Maintainer: Alexey < koiwai at yandex dot com >

pkgname=curseofwar-git
_gitname=curseofwar
pkgver=0.0.0
pkgrel=3
pkgdesc="A fast-paced RTS/Action game with ncurses interface"
arch=("i686" "x86_64")
url="http://a-nikolaev.github.io/curseofwar/"
license=('GPL')
depends=('ncurses')
conflicts=('curseofwar' 'curseofwar-with-sdl-git')
makedepends=('gcc' 'git')
source=('git://github.com/a-nikolaev/curseofwar.git')
md5sums=('SKIP')

pkgver() {
  cd $_gitname
  echo $(git rev-list --count HEAD).$(git rev-parse --short HEAD)
}

build() {
	cd "$srcdir/$_gitname"
#	./configure --prefix=/usr
	make
}

package() {
	cd "$srcdir/$_gitname"
	make DESTDIR="$pkgdir/" install
}
