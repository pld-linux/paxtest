Summary:	PaXtest is a tool which tests the protection provided by PaX
Name:		paxtest
Version:	0.9.6
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://www.adamantix.org/paxtest/%{name}-%{version}.tar.gz
# Source0-md5:	6e48b4b7c82160c841a6aed81e4bc8b3
Patch0:		%{name}-Makefile.patch
BuildRequires:	paxctl
URL:		http://www.adamantix.org/paxtest/
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%description -l pl
PaXtest to narzêdzie testuj±ce mechanizmy ochrony dostarczane przez
PaX. Jest to zestaw testów regresji próbuj±cych wykonaæ wszystkie
rodzaje brzydkich sztuczek, a nastêpnie raportuj±ce, które z nich
zadzia³a³y, a które nie. Wszystko co mo¿e zrobiæ PaXtest, mo¿e zrobiæ
tak¿e atakuj±cy. PaXtest mo¿e byæ u¿ywany tak¿e do testowania innych
³at na j±dra (takich jak OpenWall czy exec-shield w OpenBSD).

PaXtest w wersji 0.9.6 wprowadza tak zwane tryby dzieciaka i
w³amywacza. Ten pierwszy symuluje niezbyt m±drego "script kiddie",
próbuje u¿ywaæ konwencjonalnych metod przy testowaniu zabezpieczeñ.
Tryb "blackhat" symuluje bardziej sprytnego w³amywacza, próbuje
wykonaæ sprytne sztuczki, aby obej¶æ mechanizmy ochrony.

%prep
%setup -q
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
