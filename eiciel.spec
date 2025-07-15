Summary:	Graphical access control list (ACL) editor
Summary(pl.UTF-8):	Graficzny edytor list kontroli dostępu (ACL)
Name:		eiciel
Version:	0.10.0
Release:	1
License:	GPL v2+
Group:		Applications/File
#Source0Download: https://rofi.roger-ferrer.org/eiciel/download/
Source0:	https://rofi.roger-ferrer.org/eiciel/files/%{name}-%{version}.tar.xz
# Source0-md5:	7f6d7846a3908a205c1968c220b25d34
Patch0:		%{name}-pl.po.patch
URL:		http://rofi.roger-ferrer.org/eiciel/
BuildRequires:	acl-devel
BuildRequires:	desktop-file-utils
BuildRequires:	gettext-tools
BuildRequires:	libstdc++-devel >= 6:7
BuildRequires:	glibmm2.68-devel >= 2.68
BuildRequires:	gtkmm4-devel >= 4.6
BuildRequires:	meson >= 0.57
BuildRequires:	ninja >= 1.5
# libnautilus-extension-4
BuildRequires:	nautilus-devel >= 43
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	gtkmm4 >= 4.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Graphical editor for access control lists (ACL) and extended
attributes (XATTR), either as an extension within Nautilus, or as a
standalone utility.

%description -l pl.UTF-8
eiciel to graficzny edytor list kontroli dostępu (ACL) i rozszerzonych
atrybutów (XATTR), działający jako rozszerzenie Nautilus lub
samodzielne narzędzie.

%package -n nautilus-extension-%{name}
Summary:	Eiciel Nautilus extension
Summary(pl.UTF-8):	Rozszerzenie Eiciel dla Nautilusa
Group:		Applications/File
Requires:	%{name} = %{version}-%{release}
Requires:	nautilus >= 43

%description -n nautilus-extension-%{name}
Eiciel Nautilus extension.

%description -n nautilus-extension-%{name} -l pl.UTF-8
Rozszerzenie Eiciel dla Nautilusa.

%prep
%setup -q
%patch -P0 -p1

%build
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README.md
%attr(755,root,root) %{_bindir}/eiciel
%{_datadir}/metainfo/org.roger_ferrer.Eiciel.appdata.xml
%{_desktopdir}/org.roger_ferrer.Eiciel.desktop
%{_iconsdir}/hicolor/*x*/apps/eiciel.png
%{_iconsdir}/hicolor/scalable/apps/icon_eiciel.svg
%{_mandir}/man1/eiciel.1*

%files -n nautilus-extension-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/nautilus/extensions-4/libeiciel-nautilus.so
