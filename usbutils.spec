#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : usbutils
Version  : 014
Release  : 21
URL      : https://mirrors.kernel.org/pub/linux/utils/usb/usbutils/usbutils-014.tar.xz
Source0  : https://mirrors.kernel.org/pub/linux/utils/usb/usbutils/usbutils-014.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+ GPL-3.0
Requires: usbutils-bin = %{version}-%{release}
Requires: usbutils-license = %{version}-%{release}
Requires: usbutils-man = %{version}-%{release}
BuildRequires : clr-hardware-files
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(libusb-1.0)

%description
No detailed description available

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
%setup -q -n usbutils-014
cd %{_builddir}/usbutils-014

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1628268720
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%configure --disable-static --datadir=/usr/share/hwdata
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1628268720
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/usbutils
cp %{_builddir}/usbutils-014/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/usbutils/55ecbe8d9853ba75e3ce95a3a60f70bb728d51ac
cp %{_builddir}/usbutils-014/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/usbutils/c0a595d97337dfa9f56fc0f71fbd8013b1d4cb27
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
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
/usr/share/man/man1/usb-devices.1
/usr/share/man/man8/lsusb.8
/usr/share/man/man8/usbhid-dump.8
