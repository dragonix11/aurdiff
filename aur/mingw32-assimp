# Contributor: Daniel Kirchner <daniel at ekpyron dot org>
# Maintainer: Davorin Učakar <davorin.ucakar@gmail.com>

pkgname=mingw32-assimp
_basename=assimp
pkgver=3.0.1270
pkgrel=1
pkgdesc="Portable Open Source library to import various well-known 3D model formats in an uniform manner (mingw32)"
arch=('any')
license=('BSD')
depends=('mingw32-zlib')
makedepends=('cmake' 'mingw32-gcc')
url=('http://assimp.sourceforge.net/index.html')
source=("http://downloads.sourceforge.net/project/assimp/assimp-3.0/assimp--${pkgver}-source-only.zip")
options=(!strip !buildflags)
sha1sums=('e80a3a4326b649ed6585c0ce312ed6dd68942834')

_targetarch=i486-mingw32

build() 
{
  cd ${srcdir}

  rm -rf build && mkdir build && cd build

  cmake \
    -D BUILD_ASSIMP_TOOLS=OFF \
    -D ENABLE_BOOST_WORKAROUND=ON \
    -D CMAKE_INSTALL_PREFIX="/usr/${_targetarch}" \
    -D CMAKE_BUILD_TYPE=Release \
    -D CMAKE_SYSTEM_NAME=Windows \
    -D CMAKE_RC_COMPILER=/usr/bin/${_targetarch}-windres \
    -D CMAKE_C_COMPILER=/usr/bin/${_targetarch}-gcc \
    -D CMAKE_CXX_COMPILER=/usr/bin/${_targetarch}-g++ \
    -D CMAKE_FIND_ROOT_PATH=/usr/${_targetarch} \
    ../${_basename}--${pkgver}-source-only
  make 
}

package() 
{
  cd ${srcdir}/build

  make DESTDIR=$pkgdir install
  mkdir ${pkgdir}/usr/${_targetarch}/bin
  mv ${pkgdir}/usr/${_targetarch}/lib/*.dll ${pkgdir}/usr/${_targetarch}/bin

  install -Dm644 ${srcdir}/${_basename}--${pkgver}-source-only/LICENSE \
		 ${pkgdir}/usr/share/licenses/${pkgname}/LICENSE
}
