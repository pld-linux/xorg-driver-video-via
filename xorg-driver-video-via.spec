Summary:	X.org video driver for VIA chipsets with onboard unichrome graphics
Summary(pl):	Sterownik obrazu X.org dla uk³adów zintegrowanych VIA
Name:		xorg-driver-video-via
Version:	0.1.33.2
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/X11R7.0/src/driver/xf86-video-via-%{version}.tar.bz2
# Source0-md5:	b003e299f15e3f62850c40e941afe0ec
URL:		http://xorg.freedesktop.org/
BuildRequires:	Mesa-libGL-devel
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libdrm-devel >= 2.0
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXvMC-devel
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xf86driproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	xorg-xserver-server-devel >= 0.99.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for VIA chipsets with onboard unichrome graphics.
It supports VIA CLE266, KM400/KN400 chipsets. K8M800/K8N800, PM8X0 and
CN400 support is still under development.

%description -l pl
Sterownik obrazu X.org dla zintegrowanych uk³adów graficznych VIA.
Obs³uguje uk³ady VIA CLE266, KM400/KN400. Obs³uga K8M800/K8N800, PM8X0
i CN400 jest jeszcze w trakcie pisania.

%prep
%setup -q -n xf86-video-via-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la \
	$RPM_BUILD_ROOT%{_libdir}/libviaXvMC*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/via_drv.so
%ifarch %{ix86} %{x8664}
%attr(755,root,root) %{_libdir}/libviaXvMC.so.*.*.*
%attr(755,root,root) %{_libdir}/libviaXvMCPro.so.*.*.*
%endif
%{_mandir}/man4/via.4*
