#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : usbutils
Version  : 009
Release  : 13
URL      : https://www.kernel.org/pub/linux/utils/usb/usbutils/usbutils-009.tar.xz
Source0  : https://www.kernel.org/pub/linux/utils/usb/usbutils/usbutils-009.tar.xz
Summary  : USB device database
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: usbutils-bin
Requires: usbutils-doc
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(libusb-1.0)

%description
first get usbhid-dump:
git submodule init
git submodule update
initialize autobuild with:
autoreconf --install --symlink
configure with:
./configure
build with:
make

%package bin
Summary: bin components for the usbutils package.
Group: Binaries

%description bin
bin components for the usbutils package.


%package dev
Summary: dev components for the usbutils package.
Group: Development
Requires: usbutils-bin
Provides: usbutils-devel

%description dev
dev components for the usbutils package.


%package doc
Summary: doc components for the usbutils package.
Group: Documentation

%description doc
doc components for the usbutils package.


%prep
%setup -q -n usbutils-009

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1511458511
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1511458511
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/lsusb
/usr/bin/lsusb.py
/usr/bin/usb-devices
/usr/bin/usbhid-dump

%files dev
%defattr(-,root,root,-)
/usr/lib64/pkgconfig/usbutils.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man8/*
