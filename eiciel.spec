Summary:	Graphical access control list (ACL) editor
Summary(pl.UTF-8):	Graficzny edytor list kontroli dostępu (ACL)
Name:		eiciel
Version:	0.9.8.1
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	http://rofi.roger-ferrer.org/eiciel/download/%{name}-%{version}.tar.bz2
# Source0-md5:	2c9c459f0604ce03ec49bb425cc42681
Source1:	%{name}-pl.po
Patch0:		%{name}-pl.po.patch
URL:		http://rofi.roger-ferrer.org/eiciel/
BuildRequires:	acl-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	desktop-file-utils
BuildRequires:	gettext-tools
BuildRequires:	glitz-devel
BuildRequires:	gtkmm3-devel
BuildRequires:	libtool
BuildRequires:	nautilus-devel >= 3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		ext_dir	%(pkg-config --variable=extensiondir libnautilus-extension)

%description
Graphical editor for access control lists (ACL) and extended
attributes (XATTR), either as an extension within Nautilus, or as a
standalone utility.

%description -l pl.UTF-8
eiciel to graficzny edytor list kontroli dostępu (ACL) i rozszerzonych
atrybutów (XATTR), działający jako rozszerzenie Nautilus lub
samodzielne narzędzie.

%prep
%setup -q
%patch0 -p1
cp -p %{SOURCE1} po/pl.po

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}
rm po/*.gmo
%{__make} -C po update-gmo

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{ext_dir}/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/gnome/help/%{name}
%{_desktopdir}/*%{name}*
%{_mandir}/man1/%{name}*
%{ext_dir}/lib%{name}*
