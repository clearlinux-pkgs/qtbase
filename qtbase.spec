#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : qtbase
Version  : 5.15.2
Release  : 56
URL      : https://download.qt.io/official_releases/qt/5.15/5.15.2/submodules/qtbase-everywhere-src-5.15.2.tar.xz
Source0  : https://download.qt.io/official_releases/qt/5.15/5.15.2/submodules/qtbase-everywhere-src-5.15.2.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 Artistic-2.0 BSD-2-Clause BSD-3-Clause CC0-1.0 FTL GFDL-1.3 GPL-2.0 GPL-3.0 ISC LGPL-3.0 Libpng MIT MIT-feh MPL-2.0-no-copyleft-exception OFL-1.0 Unicode-DFS-2016 W3C-19980720 Zlib bzip2-1.0.6
Requires: qtbase-extras
Requires: shared-mime-info
BuildRequires : Vulkan-Headers-dev
BuildRequires : Vulkan-Loader-dev
BuildRequires : Vulkan-Tools
BuildRequires : buildreq-cmake
BuildRequires : cups-dev
BuildRequires : double-conversion-dev
BuildRequires : fontconfig-dev
BuildRequires : libXrender-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : mariadb-dev
BuildRequires : openssl-dev
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(freetype2)
BuildRequires : pkgconfig(gl)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(icu-i18n)
BuildRequires : pkgconfig(icu-uc)
BuildRequires : pkgconfig(krb5-gssapi)
BuildRequires : pkgconfig(libinput)
BuildRequires : pkgconfig(libpcre2-16)
BuildRequires : pkgconfig(libproxy-1.0)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(md4c)
BuildRequires : pkgconfig(sm)
BuildRequires : pkgconfig(xcb-icccm)
BuildRequires : pkgconfig(xcb-image)
BuildRequires : pkgconfig(xcb-keysyms)
BuildRequires : pkgconfig(xcb-renderutil)
BuildRequires : pkgconfig(xi)
BuildRequires : pkgconfig(xkbcommon)
BuildRequires : pkgconfig(xkbcommon-x11)
BuildRequires : postgresql-dev
BuildRequires : sqlite-autoconf-dev
BuildRequires : systemd-dev
BuildRequires : zstd-dev
Patch1: qtbase-stable-branch.patch
Patch2: 0001-Force-configure-not-to-bail-out-on-unknown-cmdline-o.patch
Patch3: tell-the-truth-about-private-api.patch

%description
program used to generate qkeymapper_x11_p.cpp

%prep
%setup -q -n qtbase-everywhere-src-5.15.2
cd %{_builddir}/qtbase-everywhere-src-5.15.2
%patch1 -p1
%patch2 -p1
%patch3 -p1
pushd ..
cp -a qtbase-everywhere-src-5.15.2 buildavx2
popd

%build
## build_prepend content
export MAKEFLAGS=%{?_smp_mflags}
if ! grep -wq avx2 /proc/cpuinfo; then
echo >&2 "Building Qt with AVX2 support requires a CPU with AVX2 support."
exit 1
fi
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1643731285
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
%configure  -v \
-opensource -confirm-license \
-release -optimized-tools \
-archdatadir /usr/lib64/qt5 \
-datadir /usr/share/qt5 \
-docdir /usr/share/doc/qt5 \
-headerdir /usr/include/qt5 \
-sysconfdir /etc/xdg \
-no-separate-debug-info \
-no-use-gold-linker \
-no-strip -no-rpath -no-pch \
-no-compile-examples \
-accessibility \
-cups \
-dbus-linked \
-fontconfig \
-glib \
-libproxy \
-no-mimetype-database \
-no-qml-debug \
-plugin-sql-mysql \
-plugin-sql-psql \
-plugin-sql-sqlite \
-reduce-relocations \
-silent \
-sm \
-system-doubleconversion \
-system-freetype \
-system-harfbuzz \
-system-pcre \
-system-libjpeg \
-system-libpng \
-system-sqlite \
-system-zlib \
-xinput2 \
-xkb \
QMAKE_CFLAGS="$CFLAGS" \
QMAKE_CXXFLAGS="$CXXFLAGS" \
QMAKE_LFLAGS="$CXXFLAGS"
## make_prepend content
(cd src && ../bin/qmake -config ltcg -config fat-static-lto)
## make_prepend end
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
## build_prepend content
export MAKEFLAGS=%{?_smp_mflags}
if ! grep -wq avx2 /proc/cpuinfo; then
echo >&2 "Building Qt with AVX2 support requires a CPU with AVX2 support."
exit 1
fi
## build_prepend end
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%configure  -v \
-opensource -confirm-license \
-release -optimized-tools \
-archdatadir /usr/lib64/qt5 \
-datadir /usr/share/qt5 \
-docdir /usr/share/doc/qt5 \
-headerdir /usr/include/qt5 \
-sysconfdir /etc/xdg \
-no-separate-debug-info \
-no-use-gold-linker \
-no-strip -no-rpath -no-pch \
-no-compile-examples \
-accessibility \
-cups \
-dbus-linked \
-fontconfig \
-glib \
-libproxy \
-no-mimetype-database \
-no-qml-debug \
-plugin-sql-mysql \
-plugin-sql-psql \
-plugin-sql-sqlite \
-reduce-relocations \
-silent \
-sm \
-system-doubleconversion \
-system-freetype \
-system-harfbuzz \
-system-pcre \
-system-libjpeg \
-system-libpng \
-system-sqlite \
-system-zlib \
-xinput2 \
-xkb \
QMAKE_CFLAGS="$CFLAGS" \
QMAKE_CXXFLAGS="$CXXFLAGS" \
QMAKE_LFLAGS="$CXXFLAGS"
## make_prepend content
(cd src && ../bin/qmake -config ltcg -config fat-static-lto)
## make_prepend end
make  %{?_smp_mflags}
popd
%install
export SOURCE_DATE_EPOCH=1643731285
rm -rf %{buildroot}
## install_prepend content
pushd src/openglextensions
make clean
../../bin/qmake QMAKE_CXXFLAGS+=-fno-lto      # Can't have LTO (static)
make
popd
pushd ../buildavx2/src/openglextensions
make clean
../../bin/qmake QMAKE_CXXFLAGS+=-fno-lto      # Can't have LTO (static)
make
popd
## install_prepend end
mkdir -p %{buildroot}/usr/share/package-licenses/qtbase
cp %{_builddir}/qtbase-everywhere-src-5.15.2/LICENSE.FDL %{buildroot}/usr/share/package-licenses/qtbase/61907422fefcd2313a9b570c31d203a6dbebd333
cp %{_builddir}/qtbase-everywhere-src-5.15.2/LICENSE.GPL2 %{buildroot}/usr/share/package-licenses/qtbase/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/qtbase-everywhere-src-5.15.2/LICENSE.GPL3 %{buildroot}/usr/share/package-licenses/qtbase/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/qtbase-everywhere-src-5.15.2/LICENSE.GPL3-EXCEPT %{buildroot}/usr/share/package-licenses/qtbase/e93757aefa405f2c9a8a55e780ae9c39542dfc3a
cp %{_builddir}/qtbase-everywhere-src-5.15.2/LICENSE.LGPL3 %{buildroot}/usr/share/package-licenses/qtbase/f45ee1c765646813b442ca58de72e20a64a7ddba
cp %{_builddir}/qtbase-everywhere-src-5.15.2/LICENSE.LGPLv3 %{buildroot}/usr/share/package-licenses/qtbase/21c9a9f31dd8a6784a5ac2836db33acb977532af
cp %{_builddir}/qtbase-everywhere-src-5.15.2/src/3rdparty/VulkanMemoryAllocator/LICENSE.txt %{buildroot}/usr/share/package-licenses/qtbase/0b1915e91547db9410bb79b90639f6aaab28f08c
cp %{_builddir}/qtbase-everywhere-src-5.15.2/src/3rdparty/android/LICENSE %{buildroot}/usr/share/package-licenses/qtbase/b622f8ec37b3b644621a5f5f672c41ab286ca5d9
cp %{_builddir}/qtbase-everywhere-src-5.15.2/src/3rdparty/angle/KHRONOS_LICENSE %{buildroot}/usr/share/package-licenses/qtbase/1eaf111c5aedd47ff01c20f4a8dcc338436af285
cp %{_builddir}/qtbase-everywhere-src-5.15.2/src/3rdparty/angle/LICENSE %{buildroot}/usr/share/package-licenses/qtbase/dc421334344c2641f0a20caf1ecf4abb9c846c1e
cp %{_builddir}/qtbase-everywhere-src-5.15.2/src/3rdparty/angle/SYSTEMINFO_LICENSE %{buildroot}/usr/share/package-licenses/qtbase/e92dbdd87a40618fea1cfb376f4456d0b2ee8836
cp %{_builddir}/qtbase-everywhere-src-5.15.2/src/3rdparty/angle/TRACEEVENT_LICENSE %{buildroot}/usr/share/package-licenses/qtbase/0ea65384e282e2244c42de4fb6957386e27b0db5
cp %{_builddir}/qtbase-everywhere-src-5.15.2/src/3rdparty/angle/src/common/third_party/smhasher/LICENSE %{buildroot}/usr/share/package-licenses/qtbase/819e6935c5ac3ae7bcb7470cb81c07cc383e80eb
cp %{_builddir}/qtbase-everywhere-src-5.15.2/src/3rdparty/angle/src/third_party/compiler/LICENSE %{buildroot}/usr/share/package-licenses/qtbase/dbb4b3a7c493484294639613ed59f1f5e7f94ada
cp %{_builddir}/qtbase-everywhere-src-5.15.2/src/3rdparty/angle/src/third_party/libXNVCtrl/LICENSE %{buildroot}/usr/share/package-licenses/qtbase/665f7371da2b70dc3908c7c1e8b43bbbada8e4c3
cp %{_builddir}/qtbase-everywhere-src-5.15.2/src/3rdparty/double-conversion/LICENSE %{buildroot}/usr/share/package-licenses/qtbase/8d434c9c1704b544a8b0652efbc323380b67f9bc
cp %{_builddir}/qtbase-everywhere-src-5.15.2/src/3rdparty/easing/LICENSE %{buildroot}/usr/share/package-licenses/qtbase/adcc167d614e95a64b755f09d48b61ba85d6e104
cp %{_builddir}/qtbase-everywhere-src-5.15.2/src/3rdparty/forkfd/LICENSE %{buildroot}/usr/share/package-licenses/qtbase/8fa90a82c684d365e3ee08e257ddfeb11a34daab
cp %{_builddir}/qtbase-everywhere-src-5.15.2/src/3rdparty/freebsd/LICENSE %{buildroot}/usr/share/package-licenses/qtbase/322ce1982143941e7bb72f3f61c7087c46ca3c27
cp %{_builddir}/qtbase-everywhere-src-5.15.2/src/3rdparty/freetype/BDF-LICENSE.txt %{buildroot}/usr/share/package-licenses/qtbase/1ff1aac950759024e9a9f72d47d394e7b4452c6a
cp %{_builddir}/qtbase-everywhere-src-5.15.2/src/3rdparty/freetype/LICENSE.txt %{buildroot}/usr/share/package-licenses/qtbase/cd290e37e15d49aabe6dcfa048f4e0165b9f0c07
cp %{_builddir}/qtbase-everywhere-src-5.15.2/src/3rdparty/freetype/PCF-LICENSE.txt %{buildroot}/usr/share/package-licenses/qtbase/6b644a7011be79d1a8ee1cbafa513ce7c533ecf0
cp %{_builddir}/qtbase-everywhere-src-5.15.2/src/3rdparty/freetype/ZLIB-LICENSE.txt %{buildroot}/usr/share/package-licenses/qtbase/c3cd964db231b42526c782d5ad7f8d564269b6d5
cp %{_builddir}/qtbase-everywhere-src-5.15.2/src/3rdparty/freetype/docs/GPLv2.TXT %{buildroot}/usr/share/package-licenses/qtbase/dac7127c82749e3107b53530289e1cd548860868
cp %{_builddir}/qtbase-everywhere-src-5.15.2/src/3rdparty/freetype/docs/LICENSE.TXT %{buildroot}/usr/share/package-licenses/qtbase/64b7f213ddd72695d94866a1a9532ee5b3a472a8
cp %{_builddir}/qtbase-everywhere-src-5.15.2/src/3rdparty/gradle/LICENSE-GRADLEW.txt %{buildroot}/usr/share/package-licenses/qtbase/a52be3a58ec2d18904191c16274cec7d58893d6f
cp %{_builddir}/qtbase-everywhere-src-5.15.2/src/3rdparty/harfbuzz-ng/COPYING %{buildroot}/usr/share/package-licenses/qtbase/e911adf5641a09f13fdd5d59962ad37da043df79
cp %{_builddir}/qtbase-everywhere-src-5.15.2/src/3rdparty/harfbuzz/COPYING %{buildroot}/usr/share/package-licenses/qtbase/7925382f0cd147aad205ce1a1c6b8f2017ef7d63
cp %{_builddir}/qtbase-everywhere-src-5.15.2/src/3rdparty/iaccessible2/LICENSE %{buildroot}/usr/share/package-licenses/qtbase/ba3bd36a0ef297a2572863c14637ff032a55d29b
cp %{_builddir}/qtbase-everywhere-src-5.15.2/src/3rdparty/icc/LICENSE.txt %{buildroot}/usr/share/package-licenses/qtbase/af6b93eb335e20dd1fd54208f939dd06042c53d2
cp %{_builddir}/qtbase-everywhere-src-5.15.2/src/3rdparty/libjpeg/LICENSE %{buildroot}/usr/share/package-licenses/qtbase/473c07302a0759fd751db4017db57fd17163169b
cp %{_builddir}/qtbase-everywhere-src-5.15.2/src/3rdparty/libpng/LICENSE %{buildroot}/usr/share/package-licenses/qtbase/fc3951ba26fe1914759f605696a1d23e3b41766f
cp %{_builddir}/qtbase-everywhere-src-5.15.2/src/3rdparty/md4c/LICENSE.md %{buildroot}/usr/share/package-licenses/qtbase/41c7975f32d14d2ab4a1f243d11fb9797bff40d4
cp %{_builddir}/qtbase-everywhere-src-5.15.2/src/3rdparty/pcre2/LICENCE %{buildroot}/usr/share/package-licenses/qtbase/b055467930e33d0ffda06b6ca23246ea705c1db7
cp %{_builddir}/qtbase-everywhere-src-5.15.2/src/3rdparty/pcre2/LICENCE-SLJIT %{buildroot}/usr/share/package-licenses/qtbase/e9cb7b4dfa8168c3e4041aa6dc2c48a619f3b76b
cp %{_builddir}/qtbase-everywhere-src-5.15.2/src/3rdparty/pixman/LICENSE %{buildroot}/usr/share/package-licenses/qtbase/16da0e0dcdc8ca9463ff2b8cb37072ee522b0924
cp %{_builddir}/qtbase-everywhere-src-5.15.2/src/3rdparty/rfc6234/LICENSE %{buildroot}/usr/share/package-licenses/qtbase/f62f428fcb4bca5ae06b01409d5a5923163ce4dc
cp %{_builddir}/qtbase-everywhere-src-5.15.2/src/3rdparty/sha3/BRG_ENDIAN_LICENSE %{buildroot}/usr/share/package-licenses/qtbase/0446b384f361f9601238bc2f2e7bd7a833b99288
cp %{_builddir}/qtbase-everywhere-src-5.15.2/src/3rdparty/sha3/CC0_LICENSE %{buildroot}/usr/share/package-licenses/qtbase/60f8838aed230fff6697f59ea3a732f18c723c3d
cp %{_builddir}/qtbase-everywhere-src-5.15.2/src/3rdparty/tinycbor/LICENSE %{buildroot}/usr/share/package-licenses/qtbase/744aeb214e5bd02d894c0390cb505be56847b6be
cp %{_builddir}/qtbase-everywhere-src-5.15.2/src/3rdparty/wasm/DEJAVU-LICENSE %{buildroot}/usr/share/package-licenses/qtbase/2cba132501cc69b943061ac075153ad475c7e72a
cp %{_builddir}/qtbase-everywhere-src-5.15.2/src/3rdparty/xcb/LICENSE %{buildroot}/usr/share/package-licenses/qtbase/e35a38f4b6d9b8fa47bdc313b42ea1930b94a72f
cp %{_builddir}/qtbase-everywhere-src-5.15.2/src/3rdparty/zlib/LICENSE %{buildroot}/usr/share/package-licenses/qtbase/dc3faa3029d99c3532e8262c2452afd5e11e4918
cp %{_builddir}/qtbase-everywhere-src-5.15.2/src/corelib/codecs/QBIG5CODEC_LICENSE.txt %{buildroot}/usr/share/package-licenses/qtbase/5f1f3a3317504f51b562784738656be8593c7ffa
cp %{_builddir}/qtbase-everywhere-src-5.15.2/src/corelib/codecs/QBKCODEC_LICENSE.txt %{buildroot}/usr/share/package-licenses/qtbase/472d1249930e41755894c5336b785c2753d704a2
cp %{_builddir}/qtbase-everywhere-src-5.15.2/src/corelib/codecs/QEUCJPCODEC_LICENSE.txt %{buildroot}/usr/share/package-licenses/qtbase/70fabf2a986af11354277144546150a1c9783cac
cp %{_builddir}/qtbase-everywhere-src-5.15.2/src/corelib/codecs/QEUCKRCODEC_LICENSE.txt %{buildroot}/usr/share/package-licenses/qtbase/1118a9b7fdff2e9a736acfe764d3d993715e85bb
cp %{_builddir}/qtbase-everywhere-src-5.15.2/src/corelib/codecs/QJISCODEC_LICENSE.txt %{buildroot}/usr/share/package-licenses/qtbase/70fabf2a986af11354277144546150a1c9783cac
cp %{_builddir}/qtbase-everywhere-src-5.15.2/src/corelib/codecs/QSJISCODEC_LICENSE.txt %{buildroot}/usr/share/package-licenses/qtbase/70fabf2a986af11354277144546150a1c9783cac
cp %{_builddir}/qtbase-everywhere-src-5.15.2/src/corelib/codecs/QTSCIICODEC_LICENSE.txt %{buildroot}/usr/share/package-licenses/qtbase/866627e250d50de077ffe78efa8f585f87238180
cp %{_builddir}/qtbase-everywhere-src-5.15.2/src/corelib/io/PSL-LICENSE.txt %{buildroot}/usr/share/package-licenses/qtbase/d7e3ed5ac149ac1e2d2e0f4daff081c1dafef1c0
cp %{_builddir}/qtbase-everywhere-src-5.15.2/src/corelib/kernel/QEVENTDISPATCHER_CF_LICENSE.txt %{buildroot}/usr/share/package-licenses/qtbase/fee647168efa75e63122586106fb721b55ee7651
cp %{_builddir}/qtbase-everywhere-src-5.15.2/src/corelib/text/UNICODE_LICENSE.txt %{buildroot}/usr/share/package-licenses/qtbase/0ebb44ae26c47deeb726b398121a3d2321731b2a
cp %{_builddir}/qtbase-everywhere-src-5.15.2/src/dbus/LIBDBUS-1-LICENSE.txt %{buildroot}/usr/share/package-licenses/qtbase/5afaf3263848300e6daf9a5cc3761eddb9969946
cp %{_builddir}/qtbase-everywhere-src-5.15.2/src/gui/opengl/KHRONOS_LICENSE.txt %{buildroot}/usr/share/package-licenses/qtbase/6c978ae82e85830764c8683ee4df810c4360c547
cp %{_builddir}/qtbase-everywhere-src-5.15.2/src/gui/painting/QIMAGETRANSFORM_LICENSE.txt %{buildroot}/usr/share/package-licenses/qtbase/c7e2ab75c7671491b36e306057bf0f14aa62845c
cp %{_builddir}/qtbase-everywhere-src-5.15.2/src/gui/painting/WEBGRADIENTS_LICENSE.txt %{buildroot}/usr/share/package-licenses/qtbase/69e3487e6a838e7c9357d55578f64d5995f7e711
cp %{_builddir}/qtbase-everywhere-src-5.15.2/src/gui/painting/XCONSORTIUM_LICENSE.txt %{buildroot}/usr/share/package-licenses/qtbase/ce3735fb4741c499f9ddf89f0dfc0eb9964d1e25
cp %{_builddir}/qtbase-everywhere-src-5.15.2/src/gui/text/AGLFN_LICENSE.txt %{buildroot}/usr/share/package-licenses/qtbase/e87d28b43a11605664d10cc7190e454e256684f7
cp %{_builddir}/qtbase-everywhere-src-5.15.2/src/gui/vulkan/KHRONOS_LICENSE.txt %{buildroot}/usr/share/package-licenses/qtbase/889f531eb3d7093dee85d5c3afc1340055740678
cp %{_builddir}/qtbase-everywhere-src-5.15.2/src/plugins/platforms/cocoa/COCOA_LICENSE.txt %{buildroot}/usr/share/package-licenses/qtbase/fee647168efa75e63122586106fb721b55ee7651
cp %{_builddir}/qtbase-everywhere-src-5.15.2/src/testlib/3rdparty/CYCLE_LICENSE.txt %{buildroot}/usr/share/package-licenses/qtbase/c0955b5351b1dcafdd0b9bb2d7e84fe0e3d731ca
cp %{_builddir}/qtbase-everywhere-src-5.15.2/src/testlib/3rdparty/LINUX_LICENSE.txt %{buildroot}/usr/share/package-licenses/qtbase/99fccba07bdc277439b88e03af273819d29764c7
cp %{_builddir}/qtbase-everywhere-src-5.15.2/src/testlib/3rdparty/VALGRIND_LICENSE.txt %{buildroot}/usr/share/package-licenses/qtbase/c7ace52554ee70719c6b493bf87781cdabb6549a
cp %{_builddir}/qtbase-everywhere-src-5.15.2/src/tools/moc/util/licenseheader.txt %{buildroot}/usr/share/package-licenses/qtbase/b4be9db792cd4bb77ab866ab90d06c4b24a6bcbe
cp %{_builddir}/qtbase-everywhere-src-5.15.2/tests/auto/corelib/serialization/qxmlstream/XML-Test-Suite-LICENSE.txt %{buildroot}/usr/share/package-licenses/qtbase/d134e46110f1cb9253ba4542a2d8770179429da4
pushd ../buildavx2/
%make_install_v3
popd
%make_install
## Remove excluded files
rm -f %{buildroot}*/usr/bin/haswell/qmake
## install_append content
rm -f %{buildroot}/usr/bin/haswell/*.pl
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
