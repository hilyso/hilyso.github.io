name:       openssl     
Version:    1.1.1w
Release:    1%{?dist}
Summary:    Utilities from the general purpose cryptography library with TLS implementation
Group:      System Environment/Libraries
License:    GPLv2+
URL:        https://www.openssl.org/
Source0:    https://www.openssl.org/source/%{name}-%{version}.tar.gz
BuildRequires:  make gcc perl perl-WWW-Curl 
Requires:   %{name} = %{version}-%{release}
BuildRoot:  %_topdir/BUILDROOT

%global openssldir /usr/openssl

%description
The OpenSSL toolkit provides support for secure communications between
machines. OpenSSL includes a certificate management tool and shared
libraries which provide various cryptographic algorithms and
protocols.


%package devel
Summary: Development files for programs which will use the openssl library
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
%description devel
OpenSSL RPM for version 1.1.1w on Centos (development package)

%prep
%setup -q

%build
./config --prefix=%{openssldir} --openssldir=%{openssldir}
make %{?_smp_mflags}

%install
[ "%{buildroot}" != "/" ] && %{__rm} -rf %{buildroot}
%make_install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}
ln -sf %{openssldir}/lib/libssl.so.1.1 %{buildroot}%{_libdir}
ln -sf %{openssldir}/lib/libcrypto.so.1.1 %{buildroot}%{_libdir}
ln -sf %{openssldir}/bin/openssl %{buildroot}%{_bindir}

%clean
[ "%{buildroot}" != "/" ] && %{__rm} -rf %{buildroot}

%files
%{openssldir}
%defattr(-,root,root)
%{_bindir}/openssl
%{_libdir}/libcrypto.so.1.1
%{_libdir}/libssl.so.1.1

%files devel
%{openssldir}/include/*
%defattr(-,root,root)

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%changelog
* Fri Mar 08 2024 wanghuaizhuang <wangjingming@live.cn>
- Build for CentOS7.9
