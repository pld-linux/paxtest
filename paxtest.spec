Summary:	PaXtest - a tool which tests the protection provided by PaX
Summary(pl.UTF-8):	PaXtest - narzędzie testujące mechanizm obronny PaX
Name:		paxtest
Version:	0.9.7
%define		pre	pre5
Release:	0.%{pre}.1
License:	GPL v2
Group:		Applications/System
Source0:	http://www.grsecurity.net/~paxguy1/%{name}-%{version}-%{pre}.tar.gz
# Source0-md5:	146f941482f1d6e526d9af99723f2c95
Patch0:		%{name}-Makefile.patch
BuildRequires:	paxctl
URL:		http://pax.grsecurity.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PaXtest is a tool which tests the protection provided by PaX. It is a
regression test suite that tries to do all kinds of dirty tricks and
then reports what worked and what did not. Anything that PaXtest can
do, an attacker can do too. PaXtest can be used to test other kernel
patches as well (such as the OpenWall patch, exec-shield and OpenBSD).

PaXtest v0.9.6 features a so called kiddie and a blackhat mode. The
kiddie mode simulates a not so clever script kiddie. It tries to use
conventional methods to test the security. The blackhat mode however
simulates a more clever attacker. It tries to do clever tricks to get
around the kernel protection.

%description -l pl.UTF-8
PaXtest to narzędzie testujące mechanizmy ochrony dostarczane przez
PaX. Jest to zestaw testów regresji próbujących wykonać wszystkie
rodzaje brzydkich sztuczek, a następnie raportujące, które z nich
zadziałały, a które nie. Wszystko co może zrobić PaXtest, może zrobić
także atakujący. PaXtest może być używany także do testowania innych
łat na jądra (takich jak OpenWall czy exec-shield w OpenBSD).

PaXtest w wersji 0.9.6 wprowadza tak zwane tryby dzieciaka i
włamywacza. Ten pierwszy symuluje niezbyt mądrego "script kiddie",
próbuje używać konwencjonalnych metod przy testowaniu zabezpieczeń.
Tryb "blackhat" symuluje bardziej sprytnego włamywacza, próbuje
wykonać sprytne sztuczki, aby obejść mechanizmy ochrony.

%prep
%setup -q -n %{name}-%{version}-%{pre}
%patch0 -p1

%build
# pass CFLAGS,LDFLAGS in env not as make arguments, so += can work
CFLAGS="%{rpmcflags}" \
LDFLAGS="%{rpmldflags}" \
%{__make} generic \
	CC="%{__cc}" \
	RUNDIR="%{_bindir}"

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
%doc README debian/changelog results
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so
