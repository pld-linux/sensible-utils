Summary:	Utilities for sensible alternative selection
Summary(pl.UTF-8):	Narzędzia do wyboru sensownej alternatywy
Name:		sensible-utils
Version:	0.0.9
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	http://ftp.debian.org/debian/pool/main/s/sensible-utils/%{name}_%{version}.tar.gz
# Source0-md5:	559012932ffa95a7bbd8f8423869b652
URL:		http://packages.debian.org/search?keywords=sensible-utils
Conflicts:	debianutils < 3.0.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a number of small utilities which are used by
programs to sensibly select and spawn an appropriate browser, editor,
or pager.

%description -l pl.UTF-8
Pakiet ten dostarcza kilka małych narzędzi, które są używane przez
programy do sensownego wyboru oraz uruchamiania odpowiedniej
przeglądarki, edytora lub czytnika.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc debian/changelog
%attr(755,root,root) %{_bindir}/select-editor
%attr(755,root,root) %{_bindir}/sensible-browser
%attr(755,root,root) %{_bindir}/sensible-editor
%attr(755,root,root) %{_bindir}/sensible-pager
%{_mandir}/man1/select-editor.1*
%{_mandir}/man1/sensible-editor.1*
%lang(de) %{_mandir}/de/man1/sensible-editor.1*
%lang(es) %{_mandir}/es/man1/sensible-editor.1*
%lang(fr) %{_mandir}/fr/man1/sensible-editor.1*
%lang(it) %{_mandir}/it/man1/sensible-editor.1*
%lang(ja) %{_mandir}/ja/man1/sensible-editor.1*
%lang(pl) %{_mandir}/pl/man1/sensible-editor.1*
