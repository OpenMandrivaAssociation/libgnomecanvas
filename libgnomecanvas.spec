%define api_version	2
%define lib_major	0
%define libname %mklibname gnomecanvas %{api_version} %{lib_major}
%define libnamedev %mklibname -d gnomecanvas %{api_version}

Summary:	GnomeCanvas widget
Name:		libgnomecanvas
Version:	2.30.3
Release:	6
License:	LGPLv2+
Group:		System/Libraries
URL:		http://www.gnome.org/

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
Provides:	%{name}%{api_version} = %{version}-%{release}

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
Obsoletes:	%{mklibname -d gnomecanvas 2 0} < 2.30.3-5

%description -n %{libnamedev}
The GNOME canvas is an engine for structured graphics that offers a rich
imaging model, high performance rendering, and a powerful, high-level API.
It offers a choice of two rendering back-ends, one based on Xlib for
extremely fast display, and another based on Libart, a sophisticated,
antialiased, alpha-compositing engine. Applications have a choice between
the Xlib imaging model or a superset of the PostScript imaging model,
depending on the level of graphic sophistication required.

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
%{_libdir}/libgnomecanvas-%{api_version}.so.%{lib_major}*

%files -n %{libnamedev}
%doc ChangeLog NEWS README AUTHORS
%doc %{_datadir}/gtk-doc/html/*
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*



%changelog
* Wed Feb 15 2012 Matthew Dawkins <mattydaw@mandriva.org> 2.30.3-5
+ Revision: 774291
- rebuild for ffi5

* Thu Nov 17 2011 Matthew Dawkins <mattydaw@mandriva.org> 2.30.3-4
+ Revision: 731442
- added back accidentally removed api_version macro
- added BR libpng12
- rebuild
- removed defattr
- removed demos build
- removed docs build
- removed .la files
- disabled static build
- removed old ldconfig scriptlets
- removed reqs from devel pkgs in the devel pkg
- removed reqs for libs in the lib pkg
- converted BRs to pkgconfig provides
- why did the lib pkg need the locales files
- removed mkrel
- removed BuildRoot
- cleaned up spec
- removed clean section

* Mon Sep 19 2011 Götz Waschk <waschk@mandriva.org> 2.30.3-3
+ Revision: 700344
- rebuild

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 2.30.3-2
+ Revision: 661465
- mass rebuild

* Mon Jan 31 2011 Götz Waschk <waschk@mandriva.org> 2.30.3-1
+ Revision: 634482
- update to new version 2.30.3

* Mon Sep 27 2010 Götz Waschk <waschk@mandriva.org> 2.30.2-1mdv2011.0
+ Revision: 581474
- update to new version 2.30.2

* Thu Apr 01 2010 Götz Waschk <waschk@mandriva.org> 2.30.1-1mdv2010.1
+ Revision: 530706
- update to new version 2.30.1

* Tue Mar 30 2010 Götz Waschk <waschk@mandriva.org> 2.30.0-1mdv2010.1
+ Revision: 529730
- new version
- drop libglade support

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 2.26.0-3mdv2010.1
+ Revision: 520840
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 2.26.0-2mdv2010.0
+ Revision: 425551
- rebuild

* Tue Mar 17 2009 Götz Waschk <waschk@mandriva.org> 2.26.0-1mdv2009.1
+ Revision: 356682
- update to new version 2.26.0

* Sun Feb 01 2009 Götz Waschk <waschk@mandriva.org> 2.25.90-1mdv2009.1
+ Revision: 336053
- update to new version 2.25.90

* Fri Nov 07 2008 Oden Eriksson <oeriksson@mandriva.com> 2.20.1.1-4mdv2009.1
+ Revision: 300762
- rebuilt against new libxcb

* Wed Jul 30 2008 Götz Waschk <waschk@mandriva.org> 2.20.1.1-3mdv2009.0
+ Revision: 254723
- update license
- fix build
- update build deps

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Mar 26 2008 Emmanuel Andry <eandry@mandriva.org> 2.20.1.1-2mdv2008.1
+ Revision: 190543
- Fix lib group

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Oct 20 2007 Götz Waschk <waschk@mandriva.org> 2.20.1.1-1mdv2008.1
+ Revision: 100700
- new version

* Sat Oct 13 2007 Götz Waschk <waschk@mandriva.org> 2.20.1-1mdv2008.0
+ Revision: 98030
- new version

* Sun Sep 30 2007 Anssi Hannula <anssi@mandriva.org> 2.20.0-3mdv2008.0
+ Revision: 94039
- add a conflict on old 32bit libgnomecanvas2_0 on 64bit libgnomecanvas to
  ensure smooth upgrade on biarch systems

* Thu Sep 27 2007 Frederic Crozat <fcrozat@mandriva.com> 2.20.0-2mdv2008.0
+ Revision: 93299
- Add provides for obsoletes package, fix big transaction when upgrading

* Mon Sep 17 2007 Götz Waschk <waschk@mandriva.org> 2.20.0-1mdv2008.0
+ Revision: 89359
- new version

* Wed Aug 15 2007 Götz Waschk <waschk@mandriva.org> 2.19.2-1mdv2008.0
+ Revision: 63643
- new version
- new devel name

* Fri Jul 20 2007 Götz Waschk <waschk@mandriva.org> 2.19.1-3mdv2008.0
+ Revision: 53755
- add conflict for upgrades

* Thu Jul 19 2007 Götz Waschk <waschk@mandriva.org> 2.19.1-2mdv2008.0
+ Revision: 53448
- split out translation files to extra package

* Wed Jul 11 2007 Götz Waschk <waschk@mandriva.org> 2.19.1-1mdv2008.0
+ Revision: 51217
- new version
- drop patch

* Tue Jul 10 2007 Götz Waschk <waschk@mandriva.org> 2.19.0-2mdv2008.0
+ Revision: 50943
- fix pkgconfig file

* Tue Jul 10 2007 Götz Waschk <waschk@mandriva.org> 2.19.0-1mdv2008.0
+ Revision: 50919
- fix buildrequires
- new version


* Sun Jan 14 2007 Götz Waschk <waschk@mandriva.org> 2.14.0-2mdv2007.0
+ Revision: 108959
- Import libgnomecanvas

* Sun Jan 14 2007 Götz Waschk <waschk@mandriva.org> 2.14.0-2mdv2007.1
- Rebuild

* Thu Apr 13 2006 Frederic Crozat <fcrozat@mandriva.com> 2.14.0-1mdk
- Release 2.14.0
- remove patch0 (merged upstream)

* Thu Feb 23 2006 Frederic Crozat <fcrozat@mandriva.com> 2.12.0-3mdk
- use mkrel

* Tue Oct 18 2005 Frederic Crozat <fcrozat@mandriva.com> 2.12.0-2mdk
- Patch0 (CVS): fix slowness is pixbuf rendering

* Thu Oct 06 2005 Frederic Crozat <fcrozat@mandriva.com> 2.12.0-1mdk
- Release 2.10.0

* Thu May 26 2005 G�tz Waschk <waschk@mandriva.org> 2.10.2-1mdk
- reenable libtoolize
- drop merged patch
- New release 2.10.2

* Wed May 25 2005 Frederic Crozat <fcrozat@mandriva.com> 2.10.1-2mdk 
- Patch0: fix crash from evolution (Mdk bug #16145)

* Sat May 21 2005 G�tz Waschk <waschk@mandriva.org> 2.10.1-1mdk
- New release 2.10.1

* Wed Apr 20 2005 Frederic Crozat <fcrozat@mandriva.com> 2.1.0-1mdk 
- Release 2.10.0 (based on G�tz Waschk package)

* Tue Oct 19 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.8.0-1mdk
- New release 2.8.0

* Thu Apr 22 2004 Goetz Waschk <waschk@linux-mandrake.com> 2.6.1.1-1mdk
- New release 2.6.1.1

* Wed Apr 21 2004 Goetz Waschk <goetz@mandrakesoft.com> 2.6.1-1mdk
- New release 2.6.1

* Thu Apr 08 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.6.0-2mdk
- Enforce libglade 2.3.x dependency

* Tue Apr 06 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.6.0-1mdk
- Release 2.6.0 (with G�tz Waschk help)
- update file list

