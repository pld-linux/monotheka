Summary:	Simple application to organize and keep track of your movie catalogue
Summary(pl.UTF-8):	Prosta aplikacja organizująca i zarządzająca katalogiem filmów
Name:		monotheka
Version:	0.0.6
Release:	3
License:	GPL
Group:		X11/Applications
Source0:	http://forge.novell.com/modules/xfcontent/private.php/monotheka/0.1-ALPHA/%{name}-%{version}.tar.gz
# Source0-md5:	80c4ea1288dc0f98623f52d6beddd8bd
# TODO check this, no idea what is the original reason!
Patch0:		%{name}-mono-mint.patch
Patch1:		%{name}-MovieDatabase.patch
Patch2:		%{name}-desktop.patch
Patch3:		%{name}-evolution.patch
URL:		http://monotheka.mdk.org.pl/
BuildRequires:	dotnet-gtk-sharp-gnome-devel >= 1.0.4
BuildRequires:	mono-csharp >= 1.0.6
BuildRequires:	sqlite-devel >= 2.8
BuildRequires:	rpmbuild(monoautodeps)
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

%description -l pl.UTF-8
Zamysłem jest stworzenie najbardziej seksownej i pełnej możliwości
aplikacji dla kolekcjonerów filmów integrującej się ze środowiskiem
GNOME, pozostającej jednocześnie prostą i łatwą do użycia.

By to osiągnąć, dostarczany jest kompletny interfejs wtyczek. Wtyczki
są odpowiedzialne za import/eksport kolekcji, jak też za automatyczne
wypełnianie informacji o filmach z zewnętrznych źródeł (IMDB, FilmWeb)
w celu przyspieszenia katalogowania filmów.

Aktualne możliwości:
- dodawanie/edycja/usuwanie filmów,
- przeszukiwanie bazy danych w celu znalezienia filmów danego
  reżysera, filmów powstałych w danym roku, itp.,
- konfigurowalny wygląd,
- interfejs wtyczek do importowania danych,
- interfejs wtyczek do eksportowania danych,
- interfejs wtyczek do automatycznego uzupełniania informacji z
  zewnętrznych źródeł,
- inteligentny system pamiętania wartości. Pamiętane jest, co zostało
  wpisane w różne okna dialogowe,
- oznaczanie filmów w kolekcji (rzadkie, uszkodzona płyta, potrzebna
  kopia, itp.),
- oznaczanie filmów różnymi kolorami (nowe, pożyczone,
  przetrzymywane),
- zarządzanie pożyczającymi.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

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
%{_desktopdir}/*.desktop
