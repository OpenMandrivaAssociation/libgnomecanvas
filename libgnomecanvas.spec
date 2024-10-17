%define api	2
%define major	0
%define libname %mklibname gnomecanvas %{api} %{major}
%define devname %mklibname -d gnomecanvas %{api}

Summary:	GnomeCanvas widget
Name:		libgnomecanvas
Version:	2.30.3
Release:	20
License:	LGPLv2+
Group:		System/Libraries
Url:		https://www.gnome.org/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2

BuildRequires:	bison
BuildRequires:	intltool
BuildRequires:	pkgconfig(gail) >= 1.9.0
BuildRequires:	pkgconfig(glib-2.0) >= 2.10.0
BuildRequires:	pkgconfig(gtk+-2.0) >= 2.2.0
BuildRequires:	pkgconfig(libart-2.0) >= 2.3.8
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(pango) >= 1.0.1
BuildRequires:	pkgconfig(pangoft2) >= 1.0.1

%description
The GNOME canvas is an engine for structured graphics that offers a rich
imaging model, high performance rendering, and a powerful, high-level API.
It offers a choice of two rendering back-ends, one based on Xlib for
extremely fast display, and another based on Libart, a sophisticated,
antialiased, alpha-compositing engine. Applications have a choice between
the Xlib imaging model or a superset of the PostScript imaging model,
depending on the level of graphic sophistication required.

%package -n %{libname}
Summary:	%{summary}
Group:		%{group}
Provides:	%{name}%{api} = %{version}-%{release}

%description -n %{libname}
This package contains the main canvas library.

%package -n %{devname}
Summary:	Development libraries and include files for GnomeCanvas widget
Group:		Development/GNOME and GTK+
Provides:	%{name}%{api}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}
Obsoletes:	%{mklibname -d gnomecanvas 2 0} < 2.30.3-5

%description -n %{devname}
This package contains development library and header files for %{name}.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static

%make LIBS=-lm

%install
%makeinstall_std

%find_lang %{name}-2.0

%files  -f %{name}-2.0.lang

%files -n %{libname}
%{_libdir}/libgnomecanvas-%{api}.so.%{major}*

%files -n %{devname}
%doc ChangeLog NEWS README AUTHORS
%doc %{_datadir}/gtk-doc/html/*
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*

