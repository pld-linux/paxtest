Summary:	PaXtest is a tool which tests the protection provided by PaX
Name:		paxtest
Version:	0.9.6
Release:	0.8
License:	GPL v2
Group:		Applications/System
Source0:	http://www.adamantix.org/paxtest/%{name}-%{version}.tar.gz
# Source0-md5:	6e48b4b7c82160c841a6aed81e4bc8b3
Patch0:		%{name}-Makefile.patch
BuildRequires:	chpax
URL:		http://www.adamantix.org/paxtest/
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PaXtest is a tool which tests the protection provided by PaX. It is a
regression test suite that tries to do all kinds of dirtry tricks and
then reports what worked and what did not. Anything that PaXtest can
do, an attacker can do too. PaXtest can be used to test other kernel
patches as well (such as the OpenWall patch, exec-shield and OpenBSD).

PaXtest v0.9.6 features a so called kiddie and a blackhat mode. The
kiddie mode simulates a not so clever script kiddie. It tries to use
conventional methods to test the security. The blackhat mode however
simulates a more clever attacker. It tries to do clever tricks to get
around the kernel protection.

%prep
%setup -q
%patch0 -p1

%build
CFLAGS="%{rpmcflags}"; export CFLAGS
LDFLAGS="%{rpmldflags}"; export LDFLAGS
%{__make} generic RUNDIR="%{_bindir}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -f Makefile.generic install \
    DESTDIR=$RPM_BUILD_ROOT \
    BINDIR=%{_bindir} \
    LIBDIR=%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*
