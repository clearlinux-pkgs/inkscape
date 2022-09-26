#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : inkscape
Version  : 1.2.1
Release  : 45
URL      : https://inkscape.org/gallery/item/34673/inkscape-1.2.1.tar.xz
Source0  : https://inkscape.org/gallery/item/34673/inkscape-1.2.1.tar.xz
Summary  : Professional vector graphics editor
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 GPL-3.0 LGPL-2.1 LGPL-3.0 MIT MPL-1.1 OFL-1.1
BuildRequires : ImageMagick
BuildRequires : ImageMagick-dev
BuildRequires : aspell-dev
BuildRequires : atkmm-dev
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : cairo-dev
BuildRequires : cmake
BuildRequires : dbus-dev
BuildRequires : docbook-xml
BuildRequires : double-conversion-dev
BuildRequires : gettext-dev
BuildRequires : glibc-dev
BuildRequires : glibmm-dev
BuildRequires : googletest-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : gtkmm2-dev
BuildRequires : gtkmm3-dev
BuildRequires : intltool
BuildRequires : intltool-dev
BuildRequires : lcms2-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86vm-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libpng-dev
BuildRequires : libwpg-dev
BuildRequires : libxml2-dev
BuildRequires : libxslt-bin
BuildRequires : libxslt-dev
BuildRequires : pango-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(atomic_ops)
BuildRequires : pkgconfig(bdw-gc)
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gsl)
BuildRequires : pkgconfig(gspell-1)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libcdr-0.1)
BuildRequires : pkgconfig(librevenge-0.0)
BuildRequires : pkgconfig(librevenge-stream-0.0)
BuildRequires : pkgconfig(libsoup-2.4)
BuildRequires : pkgconfig(libvisio-0.1)
BuildRequires : pkgconfig(libwpg-0.3)
BuildRequires : pkgconfig(poppler)
BuildRequires : pkgconfig(poppler-glib)
BuildRequires : pkgconfig(readline)
BuildRequires : popt-dev
BuildRequires : potrace-dev
BuildRequires : pypi(poetry_core)
BuildRequires : pypi-cython
BuildRequires : python3
BuildRequires : python3-dev
BuildRequires : zlib-dev
Patch1: 0001-CMake-add-dependency-on-pofiles-for-default_template.patch

%description
Inkscape is professional quality vector graphics software which runs on
Windows, Mac OS X and GNU/Linux. It is used by design professionals and
hobbyists worldwide, for creating a wide variety of graphics such as
illustrations, icons, logos, diagrams, maps and web graphics. Inkscape uses the
W3C open standard SVG (Scalable Vector Graphics) as its native format, and is
free and open-source software.

%prep
%setup -q -n inkscape-1.2.1_2022-07-14_9c6d41e410
cd %{_builddir}/inkscape-1.2.1_2022-07-14_9c6d41e410
%patch1 -p1

%build
## build_prepend content
export CXXFLAGS="$CXXFLAGS -Wno-error=nonnull -Wno-nonnull"
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1662050198
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake .. -DWITH_DBUS=ON \
-DCMAKE_INSTALL_LIBDIR=lib64
make  %{?_smp_mflags}  -O
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
## build_prepend content
export CXXFLAGS="$CXXFLAGS -Wno-error=nonnull -Wno-nonnull"
## build_prepend end
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -ffat-lto-objects -flto=auto -march=x86-64-v3 -msse2avx -mtune=skylake "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -ffat-lto-objects -flto=auto -march=x86-64-v3 -msse2avx -mtune=skylake "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -ffat-lto-objects -flto=auto -march=x86-64-v3 -msse2avx -mtune=skylake "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -ffat-lto-objects -flto=auto -march=x86-64-v3 -msse2avx -mtune=skylake "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake .. -DWITH_DBUS=ON \
-DCMAKE_INSTALL_LIBDIR=lib64
make  %{?_smp_mflags}  -O
popd
mkdir -p clr-build-avx512
pushd clr-build-avx512
## build_prepend content
export CXXFLAGS="$CXXFLAGS -Wno-error=nonnull -Wno-nonnull"
## build_prepend end
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v4 -ffat-lto-objects -flto=auto -march=x86_64-v4 -msse2avx -mtune=skylake "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v4 -ffat-lto-objects -flto=auto -march=x86_64-v4 -msse2avx -mtune=skylake "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v4 -ffat-lto-objects -flto=auto -march=x86_64-v4 -msse2avx -mtune=skylake "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v4 -ffat-lto-objects -flto=auto -march=x86_64-v4 -msse2avx -mtune=skylake "
export CFLAGS="$CFLAGS -march=x86-64-v4 -m64 -Wl,-z,x86-64-v4 "
export CXXFLAGS="$CXXFLAGS -march=x86-64-v4 -m64 -Wl,-z,x86-64-v4 "
export FFLAGS="$FFLAGS -march=x86-64-v4 -m64 -Wl,-z,x86-64-v4 "
export FCFLAGS="$FCFLAGS -march=x86-64-v4 -m64 "
%cmake .. -DWITH_DBUS=ON \
-DCMAKE_INSTALL_LIBDIR=lib64
make  %{?_smp_mflags}  -O
popd

%install
export SOURCE_DATE_EPOCH=1662050198
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/inkscape
cp %{_builddir}/inkscape-%{version}_2022-07-14_9c6d41e410/CMakeScripts/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/inkscape/ff3ed70db4739b3c6747c7f624fe2bad70802987 || :
cp %{_builddir}/inkscape-%{version}_2022-07-14_9c6d41e410/COPYING %{buildroot}/usr/share/package-licenses/inkscape/e9982175c2726ba1063e41ec2fad9c5e1e2f60c1 || :
cp %{_builddir}/inkscape-%{version}_2022-07-14_9c6d41e410/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/inkscape/b86df424f2aef1ecbaded5e64543891e21fa881f || :
cp %{_builddir}/inkscape-%{version}_2022-07-14_9c6d41e410/LICENSES/GPL-2.0.txt %{buildroot}/usr/share/package-licenses/inkscape/86191ae5b891f816f9a3dd21ab55002122dd7651 || :
cp %{_builddir}/inkscape-%{version}_2022-07-14_9c6d41e410/LICENSES/GPL-3.0-or-later.txt %{buildroot}/usr/share/package-licenses/inkscape/46cd8571ad470b0aaca803b9c9bf68078e3732a9 || :
cp %{_builddir}/inkscape-%{version}_2022-07-14_9c6d41e410/LICENSES/GPL-3.0.txt %{buildroot}/usr/share/package-licenses/inkscape/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/inkscape-%{version}_2022-07-14_9c6d41e410/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/inkscape/1173a04f617603e4ca31baf10bdf64dd12ab6a97 || :
cp %{_builddir}/inkscape-%{version}_2022-07-14_9c6d41e410/LICENSES/LGPL-2.1.txt %{buildroot}/usr/share/package-licenses/inkscape/ec9647c584b2643c86beef5d4888c1ba66784d57 || :
cp %{_builddir}/inkscape-%{version}_2022-07-14_9c6d41e410/LICENSES/LGPL-3.0-or-later.txt %{buildroot}/usr/share/package-licenses/inkscape/2c44314e318a9f91eef499856d0680012dd2fd56 || :
cp %{_builddir}/inkscape-%{version}_2022-07-14_9c6d41e410/LICENSES/LGPL-3.0.txt %{buildroot}/usr/share/package-licenses/inkscape/a8a12e6867d7ee39c21d9b11a984066099b6fb6b || :
cp %{_builddir}/inkscape-%{version}_2022-07-14_9c6d41e410/LICENSES/MPL-1.1.txt %{buildroot}/usr/share/package-licenses/inkscape/5bcb33f2fded13179cea6ac04abea4322905b61b || :
cp %{_builddir}/inkscape-%{version}_2022-07-14_9c6d41e410/LICENSES/OFL-1.1.txt %{buildroot}/usr/share/package-licenses/inkscape/3d26ef78de688b41b93a839580a6ba974817798e || :
cp %{_builddir}/inkscape-%{version}_2022-07-14_9c6d41e410/share/doc/LICENSE %{buildroot}/usr/share/package-licenses/inkscape/48627efeaa5f25a96bc3309a41302db6610057eb || :
cp %{_builddir}/inkscape-%{version}_2022-07-14_9c6d41e410/share/extensions/LICENSE.txt %{buildroot}/usr/share/package-licenses/inkscape/86191ae5b891f816f9a3dd21ab55002122dd7651 || :
cp %{_builddir}/inkscape-%{version}_2022-07-14_9c6d41e410/share/extensions/other/clipart/LICENSE.txt %{buildroot}/usr/share/package-licenses/inkscape/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/inkscape-%{version}_2022-07-14_9c6d41e410/share/extensions/other/gcodetools/LICENSE.txt %{buildroot}/usr/share/package-licenses/inkscape/86191ae5b891f816f9a3dd21ab55002122dd7651 || :
cp %{_builddir}/inkscape-%{version}_2022-07-14_9c6d41e410/share/themes/LICENSE.txt %{buildroot}/usr/share/package-licenses/inkscape/b86df424f2aef1ecbaded5e64543891e21fa881f || :
cp %{_builddir}/inkscape-%{version}_2022-07-14_9c6d41e410/src/3rdparty/2geom/COPYING-LGPL-2.1 %{buildroot}/usr/share/package-licenses/inkscape/7898de9d8a0026da533e44a786a17e435d7697f0 || :
cp %{_builddir}/inkscape-%{version}_2022-07-14_9c6d41e410/src/3rdparty/2geom/COPYING-MPL-1.1 %{buildroot}/usr/share/package-licenses/inkscape/aba8d76d0af67d57da3c3c321caa59f3d242386b || :
cp %{_builddir}/inkscape-%{version}_2022-07-14_9c6d41e410/src/3rdparty/2geom/LICENSE.md %{buildroot}/usr/share/package-licenses/inkscape/a5ebeacb0adf789eb0f6152b145f37b54767190f || :
cp %{_builddir}/inkscape-%{version}_2022-07-14_9c6d41e410/src/3rdparty/adaptagrams/libavoid/LICENSE.LGPL %{buildroot}/usr/share/package-licenses/inkscape/a3e68c396609d16f6816c6945afc803c13632d05 || :
cp %{_builddir}/inkscape-%{version}_2022-07-14_9c6d41e410/src/3rdparty/adaptagrams/libvpsc/COPYING %{buildroot}/usr/share/package-licenses/inkscape/ed328ea8eb39f368373b8b02adfbb23db3f860ac || :
cp %{_builddir}/inkscape-%{version}_2022-07-14_9c6d41e410/src/3rdparty/cairo/COPYING-LGPL-2.1 %{buildroot}/usr/share/package-licenses/inkscape/8088b44375ef05202c0fca4e9e82d47591563609 || :
cp %{_builddir}/inkscape-%{version}_2022-07-14_9c6d41e410/src/3rdparty/cairo/COPYING-MPL-1.1 %{buildroot}/usr/share/package-licenses/inkscape/aba8d76d0af67d57da3c3c321caa59f3d242386b || :
cp %{_builddir}/inkscape-%{version}_2022-07-14_9c6d41e410/src/3rdparty/cairo/perf/COPYING %{buildroot}/usr/share/package-licenses/inkscape/2cc384b53d50baa25a960aa83b0ac0edca682fa7 || :
cp %{_builddir}/inkscape-%{version}_2022-07-14_9c6d41e410/src/3rdparty/cairo/test/COPYING %{buildroot}/usr/share/package-licenses/inkscape/a4233e56493311ffd59845410b6e156f03b07335 || :
cp %{_builddir}/inkscape-%{version}_2022-07-14_9c6d41e410/src/3rdparty/cairo/test/pdiff/gpl.txt %{buildroot}/usr/share/package-licenses/inkscape/9a13113b89f7985efe22a28b8e4ad1ace7f2b5d1 || :
cp %{_builddir}/inkscape-%{version}_2022-07-14_9c6d41e410/src/3rdparty/cairo/util/cairo-script/COPYING %{buildroot}/usr/share/package-licenses/inkscape/d888f729a340181e37b0b2fb25c2942d5005e6a2 || :
cp %{_builddir}/inkscape-%{version}_2022-07-14_9c6d41e410/src/3rdparty/cairo/util/cairo-trace/COPYING %{buildroot}/usr/share/package-licenses/inkscape/0315f8fa18770a489890f8448111722aca24b8ec || :
cp %{_builddir}/inkscape-%{version}_2022-07-14_9c6d41e410/src/3rdparty/cairo/util/cairo-trace/COPYING-GPL-3 %{buildroot}/usr/share/package-licenses/inkscape/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/inkscape-%{version}_2022-07-14_9c6d41e410/testfiles/rendering_tests/fonts/LICENSES %{buildroot}/usr/share/package-licenses/inkscape/d7a08db444b06a236030a28b1ba914ffbc2cde33 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build-avx512
%make_install_v4  || :
popd
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
