Summary:	X.org video driver for VIA chipsets with onboard unichrome graphics
Summary(pl):	Sterownik obrazu X.org dla uk³adów zintegrowanych VIA
Name:		xorg-driver-video-via
Version:	0.2.1
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-via-%{version}.tar.bz2
# Source0-md5:	7c92846dcf363204f7530fa0fa621e43
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
BuildRequires:	xorg-xserver-server-devel >= 1.0.99.901
Requires:	xorg-xserver-server >= 1.0.99.901
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for VIA chipsets with onboard unichrome graphics.
It supports VIA CLE266, KM400/KN400, K8M800/K8N800, PM8X0 and
CN400 chipsets.

%description -l pl
Sterownik obrazu X.org dla zintegrowanych uk³adów graficznych VIA.
Obs³uguje uk³ady VIA CLE266, KM400/KN400, K8M800/K8N800, PM8X0 i
CN400.

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
