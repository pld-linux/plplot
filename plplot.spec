#
# Conditional build:
%bcond_without	gnome		# don't build gnome driver
%bcond_with	java		# build Java binding
%bcond_without	svga		# don't build linuxvga driver
#
Summary:	PLplot - a library of functions that are useful for making scientific plots
Summary(pl):	PLplot - biblioteka funkcji przydatnych do tworzenia wykres�w naukowych
Name:		plplot
Version:	5.3.1
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/plplot/%{name}-%{version}.tar.gz
# Source0-md5:	3487a6b2a78a064188a80f244b341d33
Patch0:		%{name}-FHS.patch
URL:		http://plplot.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.8.3
BuildRequires:	cd-devel >= 1.3-2
BuildRequires:	docbook-style-dsssl
BuildRequires:	freetype-devel >= 2.1.0
BuildRequires:	gcc-g77
BuildRequires:	gd-devel
%{?with_gnome:BuildRequires:	gnome-libs-devel}
%{?with_gnome:BuildRequires:	gtk+-devel >= 1.2.7}
BuildRequires:	itcl-devel
BuildRequires:	jadetex
%{?with_java:BuildRequires:	jdk}
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	octave-devel
BuildRequires:	perl-XML-Parser
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	python-numpy-devel
BuildRequires:	qhull-devel
BuildRequires:	rpm-pythonprov
%{?with_svga:BuildRequires:	svgalib-devel}
# checked for but not used (generated files included in sources)
#BuildRequires:	swig
BuildRequires:	tcl-devel
BuildRequires:	tetex-dvips
BuildRequires:	texinfo
BuildRequires:	tk-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ulibdir	%{_prefix}/lib

%description
PLplot is a library of functions that are useful for making scientific
plots. It can be used from within compiled languages such as C, C++,
FORTRAN and Java, and interactively from interpreted languages such as
Octave, Python, Perl and Tcl.

The PLplot library can be used to create standard X-Y plots, semilog
plots, log-log plots, contour plots, 3D surface plots, mesh plots, bar
charts and pie charts. Multiple graphs (of the same or different
sizes) may be placed on a single page with multiple lines in each
graph.

A variety of output file devices such as PostScript, PNG, JPEG,
LaTeX and others, as well as interactive devices such as xwin,
tk, xterm and Tektronics devices are supported. New devices can
be easily added by writing a small number of device dependent
routines.

%description -l pl
PLplot to biblioteka funkcji przydatnych do tworzenia wykres�w
naukowych. Mo�e by� u�ywana z poziomu j�zyk�w kompilowanych takich
jak C, C++, FORTRAN czy Java, albo interaktywnie z poziomu j�zyk�w
interpretowanych takich jak Octave, Python, Perl czy Tcl.

Bibliotek� PLplot mo�na wykorzysta� do tworzenia standardowych
wykres�w X-Y, wykres�w p�logarytmicznych, wykres�w konturowych,
wykres�w powierzchni tr�jwymiarowych, wykres�w siatek, wykres�w
s�upkowych i ko�owych. Na jednej stronie mo�na umie�ci� wiele wykres�w
(o tych samych lub r�nych rozmiarach), na jednym wykresie mo�e by�
wiele linii.

Obs�ugiwanych jest wiele urz�dze� wyj�ciowych, w tym PostScript, PNG,
JPEG, LaTeX i inne, a tak�e urz�dzenia interaktywne, takie jak xwin,
tk, xterm i Tektronics. Nowe urz�dzenia mo�na �atwo doda� pisz�c par�
zale�nych od urz�dzenia funkcji.

%package driver-gd
Summary:	GD driver for PLplot library
Summary(pl):	Sterownik GD dla biblioteki PLplot
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description driver-gd
GD driver for PLplot library. It supports JPEG and PNG output formats.

%description driver-gd -l pl
Sterownik GD dla biblioteki PLplot. Obs�uguje formaty wyj�cia JPEG i
PNG.

%package driver-linuxvga
Summary:	linuxvga driver for PLplot library
Summary(pl):	Sterownik linuxvga dla biblioteki PLplot
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description driver-linuxvga
linuxvga driver for PLplot library. It supports svgalib output.

%description driver-gd -l pl
Sterownik linuxvga dla biblioteki PLplot. Obs�uguje wyj�cie poprzez
svgalib.

%package driver-gnome
Summary:	GNOME driver for PLplot library
Summary(pl):	Sterownik GNOME dla biblioteki PLplot
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description driver-gnome
GNOME driver for PLplot library. It supports GnomeCanvas output.

%description driver-gnome -l pl
Sterownik GNOME dla biblioteki PLplot. Obs�uguje wyj�cie do widgetu
GnomeCanvas.

%package driver-ntk
Summary:	ntk driver for PLplot library
Summary(pl):	Sterownik ntk dla biblioteki PLplot
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description driver-ntk
ntk (new tk) driver for PLplot library. It supports Tcl/Tk output.

%description driver-ntk -l pl
Sterownik ntk (new tk) dla biblioteki PLplot. Obs�uguje wyj�cie
poprzez Tcl/Tk.

%package driver-tk
Summary:	Tk drivers for PLplot library
Summary(pl):	Sterowniki Tk dla biblioteki PLplot
Group:		Libraries
Requires:	%{name}-tcl = %{version}-%{release}

%description driver-tk
Tk and tkwin drivers for PLplot library. They support Tcl/Tk output.

%description driver-ntk -l pl
Sterownik Tk i tkwin dla biblioteki PLplot. Obs�uguj� wyj�cie poprzez
Tcl/Tk.

%package driver-xwin
Summary:	xwin driver for PLplot library
Summary(pl):	Sterownik xwin dla biblioteki PLplot
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description driver-xwin
xwin driver for PLplot library. It supports X Window System output.

%description driver-xwin -l pl
Sterownik ntk (new tk) dla biblioteki PLplot. Obs�uguje wyj�cie do
okna systemu X Window.

%package devel
Summary:	Header files for PLplot library
Summary(pl):	Pliki nag��wkowe biblioteki PLplot
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	freetype-devel >= 2.1
Requires:	qhull-devel

%description devel
Header files for PLplot library.

%description devel -l pl
Pliki nag��wkowe biblioteki PLplot.

%package static
Summary:	Static PLplot library
Summary(pl):	Statyczna biblioteka PLplot
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static PLplot library.

%description static -l pl
Statyczna biblioteka PLplot.

%package c++
Summary:	PLplot library - C++ binding
Summary(pl):	Biblioteka PLplot - wi�zanie dla C++
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description c++
PLplot library - C++ binding.

%description c++ -l pl
Biblioteka PLplot - wi�zanie dla C++.

%package c++-devel
Summary:	PLplot library - C++ binding development files
Summary(pl):	Biblioteka PLplot - pliki programistyczne wi�zania dla C++
Group:		Development/Libraries
Requires:	%{name}-c++ = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	libstdc++-devel

%description c++-devel
PLplot library - C++ binding development files.

%description c++-devel -l pl
Biblioteka PLplot - pliki programistyczne wi�zania dla C++.

%package c++-static
Summary:	PLplot library - C++ binding static library
Summary(pl):	Biblioteka PLplot - biblioteka statyczna wi�zania dla C++
Group:		Development/Libraries
Requires:	%{name}-c++-devel = %{version}-%{release}

%description c++-static
PLplot library - C++ binding static library.

%description c++-static -l pl
Biblioteka PLplot - biblioteka statyczna wi�zania dla C++.

%package f77
Summary:	PLplot library - FORTRAN 77 binding
Summary(pl):	Biblioteka PLplot - wi�zanie dla j�zyka FORTRAN 77
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description f77
PLplot library - FORTRAN 77 binding.

%description f77 -l pl
Biblioteka PLplot - wi�zanie dla j�zyka FORTRAN 77.

%package f77-devel
Summary:	PLplot library - FORTRAN 77 binding development files
Summary(pl):	Biblioteka PLplot - pliki programistyczne wi�zania dla j�zyka FORTRAN 77
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-f77 = %{version}-%{release}
Requires:	gcc-g77

%description f77-devel
PLplot library - FORTRAN 77 binding development files.

%description f77-devel -l pl
Biblioteka PLplot - pliki programistyczne wi�zania dla j�zyka FORTRAN
77.

%package f77-static
Summary:	PLplot library - FORTRAN 77 binding static library
Summary(pl):	Biblioteka PLplot - biblioteka statyczna wi�zania dla j�zyka FORTRAN 77
Group:		Development/Libraries
Requires:	%{name}-f77-devel = %{version}-%{release}

%description f77-static
PLplot library - FORTRAN 77 binding static library.

%description f77-static -l pl
Biblioteka PLplot - biblioteka statyczna wi�zania dla j�zyka FORTRAN
77.

%package java
Summary:	PLplot library - Java binding
Summary(pl):	Biblioteka PLplot - wi�zanie dla Javy
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description java
PLplot library - Java binding.

%description java -l pl
Biblioteka PLplot - wi�zanie dla Javy.

%package java-devel
Summary:	PLplot library - Java binding development files
Summary(pl):	Biblioteka PLplot - pliki programistyczne wi�zania dla Javy
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-java = %{version}-%{release}
Obsoletes:	plplot-java-static

%description java-devel
PLplot library - Java binding development files.

%description java -l pl
Biblioteka PLplot - pliki programistyczne wi�zania dla Javy.

%package tcl
Summary:	PLplot library - Tcl/Tk binding
Summary(pl):	Biblioteka PLplot - wi�zanie dla Tcl/Tk
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description tcl
PLplot library - Tcl/Tk binding.

%description tcl -l pl
Biblioteka PLplot - wi�zanie dla Tcl/Tk.

%package tcl-devel
Summary:	PLplot library - Tcl/Tk binding development files
Summary(pl):	Biblioteka PLplot - pliki programistyczne wi�zania dla Tcl/Tk
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-tcl = %{version}-%{release}
Requires:	itcl-devel

%description tcl-devel
PLplot library - Tcl/Tk binding development files.

%description tcl-devel -l pl
Biblioteka PLplot - pliki programistyczne wi�zania dla Tcl/Tk.

%package tcl-static
Summary:	PLplot library - Tcl/Tk binding static library
Summary(pl):	Biblioteka PLplot - biblioteka statyczna wi�zania dla Tcl/Tk
Group:		Development/Libraries
Requires:	%{name}-tcl-devel = %{version}-%{release}

%description tcl-static
PLplot library - Tcl/Tk binding static library.

%description tcl-static -l pl
Biblioteka PLplot - biblioteka statyczna wi�zania dla Tcl/Tk.

%package octave
Summary:	PLplot library - Octave binding
Summary(pl):	Biblioteka PLplot - wi�zanie dla j�zyka Octave
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description octave
PLplot library - Octave binding.

%description octave -l pl
Biblioteka PLplot - wi�zanie dla j�zyka Octave.

%package octave-examples
Summary:	PLplot library - examples for Octave binding
Summary(pl):	Biblioteka PLplot - przyk�ady do wi�zania dla j�zyka Octave
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-octave = %{version}-%{release}

%description octave-examples
PLplot library - examples for Octave binding.

%description octave-examples -l pl
Biblioteka PLplot - przyk�ady do wi�zania dla j�zyka Octave.

%package -n python-plplot
Summary:	PLplot library - Python binding
Summary(pl):	Biblioteka PLplot - wi�zanie dla Pythona
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
%pyrequires_eq	python-libs

%description -n python-plplot
PLplot library - Python binding.

%description -n python-plplot -l pl
Biblioteka PLplot - wi�zanie dla Pythona.

%package -n python-plplot-examples
Summary:	PLplot library - Python binding examples
Summary(pl):	Biblioteka PLplot - przyk�ady do wi�zania dla Pythona
Group:		Libraries/Python
Requires:	%{name}-devel = %{version}-%{release}
Requires:	python-plplot = %{version}-%{release}

%description -n python-plplot-examples
PLplot library - Python binding examples.

%description -n python-plplot-examples -l pl
Biblioteka PLplot - przyk�ady do wi�zania dla Pythona.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.* libltdl
%{__libtoolize}
%{__aclocal} -I cf
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	DATA_DIR="%{_libdir}/%{name}%{version}/data" \
	PYTHON_INC_DIR=/usr/include/python%{py_ver} \
	TCLLIBDIR="%{_ulibdir}" \
	TKLIBDIR="%{_ulibdir}" \
	ITCLLIBDIR="%{_ulibdir}" \
	ITKLIBDIR="%{_ulibdir}" \
	%{!?with_svga:--disable-linuxvga} \
	--enable-conex \
	--enable-dg300 \
	%{?with_gnome:--enable-gnome} \
	--enable-imp \
	%{?with_java:JAVA_HOME=/usr/%{_lib}/java} \
	%{!?with_java:--disable-java} \
	--enable-ljii \
	--enable-ljiip \
	--enable-mskermit \
	--enable-ntk \
	--enable-octave \
	--enable-tek4010 \
	--enable-tek4010f \
	--enable-tek4107 \
	--enable-tek4107f \
	--enable-versaterm \
	--enable-vlt \
	--enable-xterm \
	--with-pkg-config \
	--with-pthreads

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}
mv -f $RPM_BUILD_ROOT%{_libdir}/plplot%{version}/data/examples \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
mv -f $RPM_BUILD_ROOT%{_docdir}/plplot installed-docs
%if %{with java}
# java must stay in libdir - JNI wrapper included
mv -f $RPM_BUILD_ROOT%{_libdir}/java/plplot/examples \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/java
mv -f $RPM_BUILD_ROOT%{_libdir}/java/plplot/core/README.javaAPI installed-docs
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	c++ -p /sbin/ldconfig
%postun	c++ -p /sbin/ldconfig

%post	f77 -p /sbin/ldconfig
%postun	f77 -p /sbin/ldconfig

%post	tcl -p /sbin/ldconfig
%postun	tcl -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog Copyright FAQ NEWS PROBLEMS README SERVICE TODO* ToDo
%doc installed-docs/{README.1st.csa,README.1st.nn,README.csa,README.nn,README.drivers}
%attr(755,root,root) %{_bindir}/plm2gif
%attr(755,root,root) %{_bindir}/plpr
%attr(755,root,root) %{_bindir}/plrender
%attr(755,root,root) %{_bindir}/pltek
%attr(755,root,root) %{_bindir}/pstex2eps
%attr(755,root,root) %{_libdir}/libcsirocsa.so.*.*.*
%attr(755,root,root) %{_libdir}/libcsironn.so.*.*.*
%attr(755,root,root) %{_libdir}/libplplotd.so.*.*.*
%{_mandir}/man1/plm2gif.1*
%{_mandir}/man1/plpr.1*
%{_mandir}/man1/plrender.1*
%{_mandir}/man1/pltek.1*
%{_mandir}/man1/pstex2eps.1*
%dir %{_libdir}/plplot%{version}
%{_libdir}/plplot%{version}/data
%dir %{_libdir}/plplot%{version}/driversd
# drivers list; *.la are used (by libltdl)
%attr(755,root,root) %{_libdir}/plplot%{version}/driversd/cgm.so
%{_libdir}/plplot%{version}/driversd/cgm.la
%{_libdir}/plplot%{version}/driversd/cgm.rc
%attr(755,root,root) %{_libdir}/plplot%{version}/driversd/dg300.so
%{_libdir}/plplot%{version}/driversd/dg300.la
%{_libdir}/plplot%{version}/driversd/dg300.rc
%attr(755,root,root) %{_libdir}/plplot%{version}/driversd/hpgl.so
%{_libdir}/plplot%{version}/driversd/hpgl.la
%{_libdir}/plplot%{version}/driversd/hpgl.rc
%attr(755,root,root) %{_libdir}/plplot%{version}/driversd/impress.so
%{_libdir}/plplot%{version}/driversd/impress.la
%{_libdir}/plplot%{version}/driversd/impress.rc
%attr(755,root,root) %{_libdir}/plplot%{version}/driversd/ljii.so
%{_libdir}/plplot%{version}/driversd/ljii.la
%{_libdir}/plplot%{version}/driversd/ljii.rc
%attr(755,root,root) %{_libdir}/plplot%{version}/driversd/ljiip.so
%{_libdir}/plplot%{version}/driversd/ljiip.la
%{_libdir}/plplot%{version}/driversd/ljiip.rc
%attr(755,root,root) %{_libdir}/plplot%{version}/driversd/mem.so
%{_libdir}/plplot%{version}/driversd/mem.la
%{_libdir}/plplot%{version}/driversd/mem.rc
%attr(755,root,root) %{_libdir}/plplot%{version}/driversd/null.so
%{_libdir}/plplot%{version}/driversd/null.la
%{_libdir}/plplot%{version}/driversd/null.rc
%attr(755,root,root) %{_libdir}/plplot%{version}/driversd/pbm.so
%{_libdir}/plplot%{version}/driversd/pbm.la
%{_libdir}/plplot%{version}/driversd/pbm.rc
%attr(755,root,root) %{_libdir}/plplot%{version}/driversd/plmeta.so
%{_libdir}/plplot%{version}/driversd/plmeta.la
%{_libdir}/plplot%{version}/driversd/plmeta.rc
%attr(755,root,root) %{_libdir}/plplot%{version}/driversd/ps.so
%{_libdir}/plplot%{version}/driversd/ps.la
%{_libdir}/plplot%{version}/driversd/ps.rc
%attr(755,root,root) %{_libdir}/plplot%{version}/driversd/pstex.so
%{_libdir}/plplot%{version}/driversd/pstex.la
%{_libdir}/plplot%{version}/driversd/pstex.rc
%attr(755,root,root) %{_libdir}/plplot%{version}/driversd/tek.so
%{_libdir}/plplot%{version}/driversd/tek.la
%{_libdir}/plplot%{version}/driversd/tek.rc
%attr(755,root,root) %{_libdir}/plplot%{version}/driversd/xfig.so
%{_libdir}/plplot%{version}/driversd/xfig.la
%{_libdir}/plplot%{version}/driversd/xfig.rc

%files driver-gd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/plplot%{version}/driversd/gd.so
%{_libdir}/plplot%{version}/driversd/gd.la
%{_libdir}/plplot%{version}/driversd/gd.rc

%if %{with gnome}
%files driver-gnome
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/plplot%{version}/driversd/gnome.so
%{_libdir}/plplot%{version}/driversd/gnome.la
%{_libdir}/plplot%{version}/driversd/gnome.rc
%endif

%if %{with svga}
%files driver-linuxvga
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/plplot%{version}/driversd/linuxvga.so
%{_libdir}/plplot%{version}/driversd/linuxvga.la
%{_libdir}/plplot%{version}/driversd/linuxvga.rc
%endif

%files driver-ntk
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/plplot%{version}/driversd/ntk.so
%{_libdir}/plplot%{version}/driversd/ntk.la
%{_libdir}/plplot%{version}/driversd/ntk.rc

%files driver-tk
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/plplot%{version}/driversd/tk.so
%{_libdir}/plplot%{version}/driversd/tk.la
%{_libdir}/plplot%{version}/driversd/tk.rc
%attr(755,root,root) %{_libdir}/plplot%{version}/driversd/tkwin.so
%{_libdir}/plplot%{version}/driversd/tkwin.la
%{_libdir}/plplot%{version}/driversd/tkwin.rc

%files driver-xwin
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/plplot%{version}/driversd/xwin.so
%{_libdir}/plplot%{version}/driversd/xwin.la
%{_libdir}/plplot%{version}/driversd/xwin.rc

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/plplot-config
%attr(755,root,root) %{_bindir}/plplot_libtool
%attr(755,root,root) %{_libdir}/libcsirocsa.so
%attr(755,root,root) %{_libdir}/libcsironn.so
%attr(755,root,root) %{_libdir}/libplplotd.so
%{_libdir}/libcsirocsa.la
%{_libdir}/libcsironn.la
%{_libdir}/libplplotd.la
%{_includedir}/plplot
%exclude %{_includedir}/plplot/pltcl.h
%exclude %{_includedir}/plplot/pltk.h
%exclude %{_includedir}/plplot/tclMatrix.h
%{_pkgconfigdir}/plplotd.pc
%{_mandir}/man1/plplot_libtool.1*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/plplot-test.sh
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/test_c.sh
%{_examplesdir}/%{name}-%{version}/Makefile
%{_examplesdir}/%{name}-%{version}/c
# perl examples use PDL::Graphics::PLplot module found in perl-PDL
%{_examplesdir}/%{name}-%{version}/perl

%files static
%defattr(644,root,root,755)
%{_libdir}/libcsirocsa.a
%{_libdir}/libcsironn.a
%{_libdir}/libplplotd.a

%files c++
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libplplotcxxd.so.*.*.*

%files c++-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libplplotcxxd.so
%{_libdir}/libplplotcxxd.la
%{_pkgconfigdir}/plplotd-c++.pc
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/test_cxx.sh
%{_examplesdir}/%{name}-%{version}/c++

%files c++-static
%defattr(644,root,root,755)
%{_libdir}/libplplotcxxd.a

%files f77
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libplplotf77cd.so.*.*.*
%attr(755,root,root) %{_libdir}/libplplotf77d.so.*.*.*

%files f77-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libplplotf77cd.so
%attr(755,root,root) %{_libdir}/libplplotf77d.so
%{_libdir}/libplplotf77cd.la
%{_libdir}/libplplotf77d.la
%{_pkgconfigdir}/plplotd-f77.pc
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/test_f77.sh
%{_examplesdir}/%{name}-%{version}/f77

%files f77-static
%defattr(644,root,root,755)
%{_libdir}/libplplotf77cd.a
%{_libdir}/libplplotf77d.a

%if %{with java}
%files java
%defattr(644,root,root,755)
%doc installed-docs/README.javaAPI
%dir %{_libdir}/java/plplot
%dir %{_libdir}/java/plplot/core
%attr(755,root,root) %{_libdir}/java/plplot/core/*.so
%{_libdir}/java/plplot/core/*.class
%{_libdir}/java/plplot/core/*.java

%files java-devel
%defattr(644,root,root,755)
%doc installed-docs/README.javaAPI
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/test_java.sh
%{_examplesdir}/%{name}-%{version}/java
%endif

%files tcl
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pltcl
%attr(755,root,root) %{_bindir}/plserver
%attr(755,root,root) %{_libdir}/libplplottcltkd.so.*.*.*
%attr(755,root,root) %{_libdir}/libtclmatrixd.so.*.*.*
%{_mandir}/man1/pltcl.1*
%{_mandir}/man1/plserver.1*

%files tcl-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libplplottcltkd.so
%attr(755,root,root) %{_libdir}/libtclmatrixd.so
%{_libdir}/libplplottcltkd.la
%{_libdir}/libtclmatrixd.la
%{_includedir}/plplot/pltcl.h
%{_includedir}/plplot/pltk.h
%{_includedir}/plplot/tclMatrix.h
%{_pkgconfigdir}/plplotd-tcl.pc
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/test_tcl.sh
%{_examplesdir}/%{name}-%{version}/tcl
%{_examplesdir}/%{name}-%{version}/tk

%files tcl-static
%defattr(644,root,root,755)
%{_libdir}/libplplottcltkd.a
%{_libdir}/libtclmatrixd.a

%files octave
%defattr(644,root,root,755)
%doc bindings/octave/{BUGS,FGA,README,ToDo,USAGE,plplot_octave_txt}
%attr(755,root,root) %{_libdir}/octave/*/oct/*/plplot_octave.oct
%{_datadir}/octave/site/m/PLplot
%{_datadir}/plplot_octave

%files octave-examples
%defattr(644,root,root,755)
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/test_octave.sh
%{_examplesdir}/%{name}-%{version}/octave

%files -n python-plplot
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/_plplotcmodule.so
%attr(755,root,root) %{py_sitedir}/plplot_widgetmodule.so
%{py_sitedir}/plplot.py
%{py_sitedir}/plplotc.py

%files -n python-plplot-examples
%defattr(644,root,root,755)
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/test_python.sh
%{_examplesdir}/%{name}-%{version}/python
