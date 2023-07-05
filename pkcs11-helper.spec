#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
#
Name     : pkcs11-helper
Version  : 1.29.0
Release  : 13
URL      : https://github.com/OpenSC/pkcs11-helper/releases/download/pkcs11-helper-1.29.0/pkcs11-helper-1.29.0.tar.bz2
Source0  : https://github.com/OpenSC/pkcs11-helper/releases/download/pkcs11-helper-1.29.0/pkcs11-helper-1.29.0.tar.bz2
Summary  : PKCS#11 helper library
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0
Requires: pkcs11-helper-lib = %{version}-%{release}
Requires: pkcs11-helper-license = %{version}-%{release}
Requires: pkcs11-helper-man = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : openssl-dev
BuildRequires : pkgconfig(gnutls)
BuildRequires : pkgconfig(libcrypto)
BuildRequires : pkgconfig(nss)
BuildRequires : pkgconfig(openssl)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Add-Require-to-pkcs11-helper-on-gnutls-libcrypto.patch

%description
The pkcs11-helper library allows using multiple PKCS#11 providers at
the same  time, selecting keys by id, label or certificate subject,
handling  card removal and card insert events, handling card re-insert
to a  different slot, supporting session expiration serialization and
much more, all using a simple API.

%package dev
Summary: dev components for the pkcs11-helper package.
Group: Development
Requires: pkcs11-helper-lib = %{version}-%{release}
Provides: pkcs11-helper-devel = %{version}-%{release}
Requires: pkcs11-helper = %{version}-%{release}

%description dev
dev components for the pkcs11-helper package.


%package doc
Summary: doc components for the pkcs11-helper package.
Group: Documentation
Requires: pkcs11-helper-man = %{version}-%{release}

%description doc
doc components for the pkcs11-helper package.


%package lib
Summary: lib components for the pkcs11-helper package.
Group: Libraries
Requires: pkcs11-helper-license = %{version}-%{release}

%description lib
lib components for the pkcs11-helper package.


%package license
Summary: license components for the pkcs11-helper package.
Group: Default

%description license
license components for the pkcs11-helper package.


%package man
Summary: man components for the pkcs11-helper package.
Group: Default

%description man
man components for the pkcs11-helper package.


%prep
%setup -q -n pkcs11-helper-1.29.0
cd %{_builddir}/pkcs11-helper-1.29.0
%patch -P 1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1688579200
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1688579200
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pkcs11-helper
cp %{_builddir}/pkcs11-helper-%{version}/COPYING %{buildroot}/usr/share/package-licenses/pkcs11-helper/cd2cbb12b3b9e8d38503591ede835d70de9a3b08 || :
cp %{_builddir}/pkcs11-helper-%{version}/COPYING.BSD %{buildroot}/usr/share/package-licenses/pkcs11-helper/43ded7db4128951bf7f85fa4b56da2fe822f8eb7 || :
cp %{_builddir}/pkcs11-helper-%{version}/COPYING.GPL %{buildroot}/usr/share/package-licenses/pkcs11-helper/bd040aef1740f62ce7275c20b40e0d87811d80f6 || :
cp %{_builddir}/pkcs11-helper-%{version}/distro/debian/copyright %{buildroot}/usr/share/package-licenses/pkcs11-helper/370f4923a0ff14d216752b3699c5ccd2cd4a34b1 || :
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/pkcs11-helper-1.0/pkcs11.h
/usr/include/pkcs11-helper-1.0/pkcs11h-certificate.h
/usr/include/pkcs11-helper-1.0/pkcs11h-core.h
/usr/include/pkcs11-helper-1.0/pkcs11h-data.h
/usr/include/pkcs11-helper-1.0/pkcs11h-def.h
/usr/include/pkcs11-helper-1.0/pkcs11h-engines.h
/usr/include/pkcs11-helper-1.0/pkcs11h-openssl.h
/usr/include/pkcs11-helper-1.0/pkcs11h-token.h
/usr/include/pkcs11-helper-1.0/pkcs11h-version.h
/usr/lib64/libpkcs11-helper.so
/usr/lib64/pkgconfig/libpkcs11-helper-1.pc
/usr/share/aclocal/*.m4

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/pkcs11\-helper/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libpkcs11-helper.so.1
/usr/lib64/libpkcs11-helper.so.1.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pkcs11-helper/370f4923a0ff14d216752b3699c5ccd2cd4a34b1
/usr/share/package-licenses/pkcs11-helper/43ded7db4128951bf7f85fa4b56da2fe822f8eb7
/usr/share/package-licenses/pkcs11-helper/bd040aef1740f62ce7275c20b40e0d87811d80f6
/usr/share/package-licenses/pkcs11-helper/cd2cbb12b3b9e8d38503591ede835d70de9a3b08

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/pkcs11-helper-1.8
