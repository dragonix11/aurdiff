# Maintainer: Jonathan Kotta <jpkotta at gmail dot com>

pkgname=python-astroid-hg
pkgver=20130916
pkgrel=2
pkgdesc="Provides an AST representation for Python code."
arch=('any')
url="http://www.pylint.org/astroid"
license=('LGPL')
makedepends=('python' 'mercurial')
source=()
md5sums=()

depends=('python' 'python-logilab-common')
replaces=('python-logilab-astng')
provides=('python-astroid')
conflicts=('python-logilab-astng' 'python-astroid')

build() {

  cd "${srcdir}"
  if [ -d astroid ] ; then
    (cd astroid ; hg pull -u || return 1)
  else
    hg clone "https://bitbucket.org/logilab/astroid" astroid || return 1
  fi
  
  cd astroid
  python3 setup.py build
}

package_python-astroid-hg() {
  cd "${srcdir}"/astroid

  python3 setup.py install --optimize=1 --skip-build --prefix=/usr --root="${pkgdir}"

  # fix permissions ...
  find "${pkgdir}" -type f -exec chmod +r {} \;
}
