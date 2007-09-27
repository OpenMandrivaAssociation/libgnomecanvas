# enable_gtkdoc: toggle if gtkdoc stuff should be rebuilt
#	0 = no
#	1 = yes
%define enable_gtkdoc	1

# install_demo: toggle if demo program should be installed
#	0 = no
#	1 = yes
%define install_demo	0

# End of user configurable section
%{?_without_gtkdoc: %{expand: %%define enable_gtkdoc 0}}
%{?_with_gtkdoc: %{expand: %%define enable_gtkdoc 1}}

%{?_without_demo: %{expand: %%define install_demo 0}}
%{?_with_demo: %{expand: %%define install_demo 1}}

%define req_gtk_version		2.0.3
%define req_libart_version	2.3.8
%define req_pango_version	1.0.1
%define req_libglade_version	2.3.0

%define api_version	2
%define lib_major	0
%define libname	%mklibname gnomecanvas %{api_version} %{lib_major}
%define libnamedev %mklibname -d gnomecanvas %{api_version}

Summary:	GnomeCanvas widget
Name:		libgnomecanvas
Version: 2.20.0
Release: %mkrel 2
License:	LGPL
Group:		Graphical desktop/GNOME
URL:		http://www.gnome.org/
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
BuildRequires:	bison
BuildRequires:	libgtk+2-devel >= %{req_gtk_version}
BuildRequires:	libart_lgpl-devel >= %{req_libart_version}
BuildRequires:	libpango-devel >= %{req_pango_version}
BuildRequires:	libglade2.0-devel >= %{req_libglade_version}
BuildRequires:	libgail-devel
BuildRequires:	perl-XML-Parser
%if %enable_gtkdoc
BuildRequires:	gtk-doc
%endif
%if %install_demo
Requires:	%{libname} = %{version}-%{release}
%endif
Conflicts: %libname < 2.19.1-2mdv2008.0

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
Provides:	%{name}%{api_version} = %{version}-%{release}
Requires:	libart_lgpl >= %{req_libart_version}
Requires:	libgtk+2 >= %{req_gtk_version}
Requires:	libpango >= %{req_pango_version}
Requires:	libglade2.0 >= %{req_libglade_version}
Requires:	%name >= %version

%description -n %{libname}
The GNOME canvas is an engine for structured graphics that offers a rich
imaging model, high performance rendering, and a powerful, high-level API.
It offers a choice of two rendering back-ends, one based on Xlib for
extremely fast display, and another based on Libart, a sophisticated,
antialiased, alpha-compositing engine. Applications have a choice between
the Xlib imaging model or a superset of the PostScript imaging model,
depending on the level of graphic sophistication required.

This package contains the main canvas library.


%package -n %{libnamedev}
Summary:	Development libraries and include files for GnomeCanvas widget
Group:		Development/GNOME and GTK+
Provides:	%{name}%{api_version}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}
Requires:	libgtk+2-devel >= %{req_gtk_version}
Requires:	libart_lgpl-devel >= %{req_libart_version}
Obsoletes:  %mklibname -d gnomecanvas %{api_version} %{lib_major}
Provides:  %mklibname -d gnomecanvas %{api_version} %{lib_major}

%description -n %{libnamedev}
The GNOME canvas is an engine for structured graphics that offers a rich
imaging model, high performance rendering, and a powerful, high-level API.
It offers a choice of two rendering back-ends, one based on Xlib for
extremely fast display, and another based on Libart, a sophisticated,
antialiased, alpha-compositing engine. Applications have a choice between
the Xlib imaging model or a superset of the PostScript imaging model,
depending on the level of graphic sophistication required.

This package contains static library and header files for %{name}.

%prep
%setup -q

%build

%configure2_5x \
%if %enable_gtkdoc
	--enable-gtk-doc
%else
	--enable-gtk-doc=no
%endif

%make

%install
rm -rf %{buildroot}
%makeinstall_std

# install demo executable
%if %install_demo
( cd demos
  mkdir -p %{buildroot}%{_bindir}
  sh ../libtool --mode=install %{_bindir}/install canvas_demo %{buildroot}%{_bindir}/canvas_demo
)
%endif

%{find_lang} %{name}-2.0

# remove unpackaged files 
rm -f $RPM_BUILD_ROOT%{_libdir}/libglade/2.0/*.{la,a}

%clean
rm -rf %{buildroot}

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%if %install_demo
%files
%defattr(-,root,root)
%{_bindir}/canvas_demo
%endif

%files  -f %{name}-2.0.lang

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libgnomecanvas-%{api_version}.so.%{lib_major}*
%{_libdir}/libglade/2.0/*.so

%files -n %{libnamedev}
%defattr(-,root,root)
%doc ChangeLog NEWS README AUTHORS
%doc %{_datadir}/gtk-doc/html/*
%{_includedir}/*
%{_libdir}/lib*.so
%attr(644,root,root) %{_libdir}/lib*.la
%{_libdir}/lib*.a
%{_libdir}/pkgconfig/*


