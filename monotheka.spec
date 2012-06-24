%include	/usr/lib/rpm/macros.mono
Summary:	Simple application to organize and keep track of your movie catalogue
Summary(pl):	Prosta aplikacja organizuj�ca i zarz�dzaj�ca katalogiem film�w
Name:		monotheka
Version:	0.0.5
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://forge.novell.com/modules/xfcontent/private.php/monotheka/0.1-ALPHA/%{name}-%{version}.tar.gz
# Source0-md5:	2997b9e7e97feb4c249f0b72c6baaa4c
Patch0:		%{name}-avi-title.patch
Patch1:		%{name}-imdb-shell.patch
Patch2:		%{name}-avi-close.patch
# TODO check this, no idea what is the original reason!
Patch3:		%{name}-mono-mint.patch
URL:		http://monotheka.mdk.org.pl/
BuildRequires:	dotnet-gtk-sharp-gnome-devel >= 1.0.4
BuildRequires:	mono-csharp >= 1.0.6
BuildRequires:	sqlite-devel >= 2.8
BuildRequires:	rpm-build >= 4.4.2-0.3
Requires:	sqlite >= 2.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The idea is to make the most sexy & featurefull movie-collector's
application for the GNOME desktop, while keeping it simple and easy to
use.

To achieve that we provide a complete plugin interface. Plugins are
responsible for importing/exporting the collection and also for
auto-filling the movie data from external sources (ie. IMDB) so you
can quickly catalogue your movies.

Current Features:

- Add/Edit/Delete movies
- Search through database to quickly list (& sort) movies by director,
  movies by year etc.
- Customizable view
- Plugin interface to import data
- Plugin interface to export data.
- Plugin interface to auto-fill movie data from external sources
- Intelligent "remember values" system. Once you enter something
  (director, borrower, country...) in to any combobox it stays there.
- Flagging movies in the collection (rare, broken cd, copy needed,
  etc.)
- Movies are highlighted with custom colors (new, borrowed,
  overborrowed)
- Borrowers management

%description -l pl
Zamys�em jest stworzenie najbardziej seksownej i pe�nej mo�liwo�ci
aplikacji dla kolekcjoner�w film�w integruj�cej si� ze �rodowiskiem
GNOME, pozostaj�cej jednocze�nie prost� i �atw� do u�ycia.

By to osi�gn��, dostarczany jest kompletny interfejs wtyczek. Wtyczki
s� odpowiedzialne za import/eksport kolekcji, jak te� za automatyczne
wype�nianie informacji o filmach z zewn�trznych �r�de� (IMDB, FilmWeb)
w celu przyspieszenia katalogowania film�w.

Aktualne mo�liwo�ci:
- dodawanie/edycja/usuwanie film�w,
- przeszukiwanie bazy danych w celu znalezienia film�w danego
  re�ysera, film�w powsta�ych w danym roku, itp.,
- konfigurowalny wygl�d,
- interfejs wtyczek do importowania danych,
- interfejs wtyczek do eksportowania danych,
- interfejs wtyczek do automatycznego uzupe�niania informacji z
  zewn�trznych �r�de�,
- inteligentny system pami�tania warto�ci. Pami�tane jest, co zosta�o
  wpisane w r�ne okna dialogowe,
- oznaczanie film�w w kolekcji (rzadkie, uszkodzona p�yta, potrzebna
  kopia, itp.),
- oznaczanie film�w r�nymi kolorami (nowe, po�yczone,
  przetrzymywane),
- zarz�dzanie po�yczaj�cymi.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

sed -i -e 's@#/bin/bash@#!/bin/bash@' configure
sed -i -e 's@#/bin/bash@#!/bin/sh@' System/monotheka.in

%build
./configure \
	--prefix=%{_prefix} \
	--nosleep

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# TODO check this!
if [ %{_lib} = lib64 ]; then
	mv $RPM_BUILD_ROOT{%{_prefix}/lib,%{_libdir}}
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS FAQ HACKING
%attr(755,root,root) %{_bindir}/*
%{_libdir}/Monotheka
%{_pkgconfigdir}/*
%{_pixmapsdir}/*
%{_desktopdir}/*
