#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v20
# autospec commit: f35655a
#
Name     : usbutils
Version  : 018
Release  : 24
URL      : https://mirrors.kernel.org/pub/linux/utils/usb/usbutils/usbutils-018.tar.gz
Source0  : https://mirrors.kernel.org/pub/linux/utils/usb/usbutils/usbutils-018.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+ GPL-3.0
Requires: usbutils-bin = %{version}-%{release}
Requires: usbutils-license = %{version}-%{release}
Requires: usbutils-man = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : clr-hardware-files
BuildRequires : libusb-dev
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(libusb-1.0)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
<!---
SPDX-License-Identifier: GPL-2.0-or-later
-->
# usbutils
This is a collection of USB tools for use on Linux and BSD systems to
query what type of USB devices are connected to the system.  This is to
be run on a USB host (i.e. a machine you plug USB devices into), not on
a USB device (i.e. a device you plug into a USB host.)

%package bin
Summary: bin components for the usbutils package.
Group: Binaries
Requires: usbutils-license = %{version}-%{release}

%description bin
bin components for the usbutils package.


%package extras
Summary: extras components for the usbutils package.
Group: Default

%description extras
extras components for the usbutils package.


%package license
Summary: license components for the usbutils package.
Group: Default

%description license
license components for the usbutils package.


%package man
Summary: man components for the usbutils package.
Group: Default

%description man
man components for the usbutils package.


%prep
%setup -q -n usbutils-018
cd %{_builddir}/usbutils-018
pushd ..
cp -a usbutils-018 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1729610511
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
meson --libdir=lib64 --prefix=/usr --buildtype=plain --datadir=/usr/share/hwdata  builddir
ninja -v -C builddir
GOAMD64=v3
CFLAGS="$CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -march=x86-64-v3 " meson --libdir=lib64 --prefix=/usr --buildtype=plain --datadir=/usr/share/hwdata  builddiravx2
ninja -v -C builddiravx2

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
mkdir -p %{buildroot}/usr/share/package-licenses/usbutils
cp %{_builddir}/usbutils-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/usbutils/55ecbe8d9853ba75e3ce95a3a60f70bb728d51ac || :
cp %{_builddir}/usbutils-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/usbutils/55ecbe8d9853ba75e3ce95a3a60f70bb728d51ac || :
cp %{_builddir}/usbutils-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/usbutils/c0a595d97337dfa9f56fc0f71fbd8013b1d4cb27 || :
GOAMD64=v3
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
GOAMD64=v2
DESTDIR=%{buildroot} ninja -C builddir install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/lsusb
/V3/usr/bin/usbhid-dump
/usr/bin/lsusb
/usr/bin/usb-devices
/usr/bin/usbhid-dump

%files extras
%defattr(-,root,root,-)
/usr/bin/lsusb.py

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/usbutils/55ecbe8d9853ba75e3ce95a3a60f70bb728d51ac
/usr/share/package-licenses/usbutils/c0a595d97337dfa9f56fc0f71fbd8013b1d4cb27

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/lsusb.py.1
/usr/share/man/man1/usb-devices.1
/usr/share/man/man8/lsusb.8
/usr/share/man/man8/usbhid-dump.8
