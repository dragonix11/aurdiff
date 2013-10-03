# Maintainer: Andrew Grigorev <andrew@ei-grad.ru>

pkgname=python-termbox-git
pkgver=20131003
pkgrel=2
pkgdesc="Library that helps making Terminal-based Pseudo-GUIs (ncurses-like, but simpler)"
arch=('i686' 'x86_64')
url="http://code.google.com/p/termbox/"
license=('custom')
depends=('python')
makedepends=('git' 'pyrex')

_gitroot='git://github.com/nsf/termbox.git'
_gitname='termbox'

build() {
  cd "$srcdir"
  msg "Connecting to GIT server...."

  if [ -d $_gitname ] ; then
    cd $_gitname && git pull origin
    msg "The local files are updated."
  else
    git clone $_gitroot $_gitname
  fi

  msg "GIT checkout done or server timeout"
  msg "Starting make..."

  rm -rf "$srcdir/$_gitname-build"
  git clone "$srcdir/$_gitname" "$srcdir/$_gitname-build"
  cd "$srcdir/$_gitname-build"

  python setup.py build
}

package() {
  cd "$srcdir/$_gitname-build"
  python setup.py install --root="$pkgdir" --optimize=1
} 

