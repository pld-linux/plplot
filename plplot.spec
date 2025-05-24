# TODO:
# - fix building with installed plplot/plplot-devel (tries to use installed drivers for dyn_test)
# - bindings: tk-x-plat?
# - package shapelib support
# NOTES (see cmake/modules/drivers-init.cmake for some issue notes):
# aqt driver is Darwin-only
# wingcc driver is Windows-only
# cgm driver has severe valgrind issues (as of 5.11.1)
# gd driver is not maintained
# plmeta is disabled due to "some issues" (as of 5.11.1)
# pstex driver deprecated in favour of psttf and pscairo
#
# Conditional build:
%bcond_with	perl_pdl	# Perl/PDL examples in tests (only)
%bcond_without	ada		# Ada binding
%bcond_with	d		# D binding
%bcond_without	java		# Java binding
%bcond_without	itcl		# [incr Tcl]/[incr Tk] support in Tcl/Tk binding
%bcond_without	lua		# Lua binding
%bcond_without	ocaml		# OCaml binding
%bcond_with	ocaml_cairo	# OCaml-Cairo component
%bcond_without	ocaml_opt	# OCaml native optimized binaries (bytecode is always built)
%bcond_without	octave		# Octave bindings
%bcond_without	pyqt		# PyQt5 support
%bcond_with	cgm		# CGM driver, libnistcd library
%bcond_with	plmeta		# plmeta driver, plrender program, {plm2gir,plpr} scripts
%bcond_with	shapelib	# shapelib support
#
# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} arm aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif
%ifarch sparc64 x32
%undefine	with_ada
%endif

Summary:	PLplot - a library of functions that are useful for making scientific plots
Summary(pl.UTF-8):	PLplot - biblioteka funkcji przydatnych do tworzenia wykresów naukowych
Name:		plplot
Version:	5.15.0
Release:	21
License:	LGPL v2+
Group:		Libraries
Source0:	https://downloads.sourceforge.net/plplot/%{name}-%{version}.tar.gz
# Source0-md5:	36aec5bfadc2e207cf8ee39f573c9303
Patch0:		%{name}-no-DISPLAY.patch
Patch1:		%{name}-plmeta.patch
Patch2:		%{name}-d.patch
Patch3:		qt-5.15.patch
Patch4:		%{name}-sip-build-support.patch
Patch5:		python3.13.patch
URL:		http://plplot.sourceforge.net/
BuildRequires:	Qt5Gui-devel >= 5
BuildRequires:	Qt5PrintSupport-devel >= 5
BuildRequires:	Qt5Svg-devel >= 5
BuildRequires:	agg-devel
%{?with_ocaml_cairo:BuildRequires:	cairo-devel}
BuildRequires:	cmake >= 3.13.2
BuildRequires:	docbook-style-dsssl
%{?with_d:BuildRequires:	dmd}
BuildRequires:	fftw3-devel
BuildRequires:	fftw3-single-devel
BuildRequires:	freetype-devel >= 2.1.0
%{?with_ada:BuildRequires:	gcc-ada >= 5:4.1}
BuildRequires:	gcc-c++
BuildRequires:	gcc-fortran
%{?with_itcl:BuildRequires:	itcl-devel >= 3.4.1}
%{?with_itcl:BuildRequires:	itk-devel >= 3.4}
BuildRequires:	jadetex
%{?with_java:BuildRequires:	jdk}
%{?with_java:BuildRequires:	jpackage-utils}
BuildRequires:	lapack-devel
BuildRequires:	libLASi-devel
BuildRequires:	libharu-devel >= 2.1.0
BuildRequires:	libjpeg-devel
BuildRequires:	libltdl-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
%{?with_lua:BuildRequires:	lua51 >= 5.1}
%{?with_lua:BuildRequires:	lua51-devel >= 5.1}
%{?with_octave:BuildRequires:	octave-devel >= 2:3.4.2}
BuildRequires:	pango-devel
%{?with_perl_pdl:BuildRequires:	perl-PDL}
BuildRequires:	perl-XML-DOM
BuildRequires:	perl-XML-Parser
BuildRequires:	perl-XML-SAX-Expat
BuildRequires:	pkgconfig
BuildRequires:	pango-devel
%if %{with pyqt}
BuildRequires:	python3-PyQt-builder
BuildRequires:	python3-PyQt5-uic
BuildRequires:	python3-PyQt5-sip
%endif
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-numpy-devel >= 15.3
BuildRequires:	qhull-devel >= 2011.1
BuildRequires:	qt5-build >= 5
BuildRequires:	qt5-qmake >= 5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.016
BuildRequires:	sed >= 4.0
%{?with_shapelib:BuildRequires:	shapelib-devel}
%if %{with pyqt}
BuildRequires:	python3-PyQt5-devel
BuildRequires:	sip6
%endif
BuildRequires:	swig
BuildRequires:	swig-python
BuildRequires:	tcl-devel >= 8.5
BuildRequires:	tetex-dvips
BuildRequires:	texinfo
BuildRequires:	tk-devel >= 8.5
BuildRequires:	wxGTK3-unicode-devel >= 2.6.0
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libX11-devel
%if %{with ocaml}
BuildRequires:	ocaml
%if %{with ocaml_cairo}
BuildRequires:	ocaml-cairo2-devel
BuildRequires:	ocaml-cairo2-gtk-devel
%endif
BuildRequires:	ocaml-idl-devel
BuildRequires:	ocaml-findlib
BuildRequires:	ocaml-lablgtk2-devel
%endif
BuildConflicts:	plplot
BuildConflicts:	plplot-devel
Obsoletes:	plplot-f77 < 5.10.0-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		octave_oct_sitedir	%(octave-config --oct-site-dir)
%define		octave_m_sitedir	%(octave-config --m-site-dir)

%define		gcc_target	%(%{__cc} -dumpmachine)
%define		ada_incdir	%{_libdir}/gcc/%{gcc_target}/%{cc_version}/adainclude
%define		ada_objdir	%{_libdir}/gcc/%{gcc_target}/%{cc_version}/adalib

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

A variety of output file devices such as PostScript, PNG, JPEG, LaTeX
and others, as well as interactive devices such as xwin, tk, xterm and
Tektronics devices are supported. New devices can be easily added by
writing a small number of device dependent routines.

%description -l pl.UTF-8
PLplot to biblioteka funkcji przydatnych do tworzenia wykresów
naukowych. Może być używana z poziomu języków kompilowanych takich jak
C, C++, FORTRAN czy Java, albo interaktywnie z poziomu języków
interpretowanych takich jak Octave, Python, Perl czy Tcl.

Bibliotekę PLplot można wykorzystać do tworzenia standardowych
wykresów X-Y, wykresów półlogarytmicznych, wykresów konturowych,
wykresów powierzchni trójwymiarowych, wykresów siatek, wykresów
słupkowych i kołowych. Na jednej stronie można umieścić wiele wykresów
(o tych samych lub różnych rozmiarach), na jednym wykresie może być
wiele linii.

Obsługiwanych jest wiele urządzeń wyjściowych, w tym PostScript, PNG,
JPEG, LaTeX i inne, a także urządzenia interaktywne, takie jak xwin,
tk, xterm i Tektronics. Nowe urządzenia można łatwo dodać pisząc parę
zależnych od urządzenia funkcji.

%package driver-ntk
Summary:	ntk driver for PLplot library
Summary(pl.UTF-8):	Sterownik ntk dla biblioteki PLplot
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description driver-ntk
ntk (new tk) driver for PLplot library. It supports Tcl/Tk output.

%description driver-ntk -l pl.UTF-8
Sterownik ntk (new tk) dla biblioteki PLplot. Obsługuje wyjście
poprzez Tcl/Tk.

%package driver-pdf
Summary:	pdf driver for PLplot library
Summary(pl.UTF-8):	Sterownik pdf dla biblioteki PLplot
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libharu >= 2.1.0

%description driver-pdf
pdf driver for PLplot library. It's PDF driver using Haru library.

%description driver-pdf -l pl.UTF-8
Sterownik pdf dla biblioteki PLplot. Jest to sterownik PDF
wykorzystujący bibliotekę Haru.

%package driver-psttf
Summary:	psttf driver for PLplot library
Summary(pl.UTF-8):	Sterownik psttf dla biblioteki PLplot
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description driver-psttf
psttf driver for PLplot library. It's PostScript driver using LASi to
provide fonts.

%description driver-psttf -l pl.UTF-8
Sterownik psttf dla biblioteki PLplot. Jest to sterownik
postscriptowy, wykorzystujący LASi do obsługi fontów.

%package driver-tk
Summary:	Tk drivers for PLplot library
Summary(pl.UTF-8):	Sterowniki Tk dla biblioteki PLplot
Group:		Libraries
Requires:	%{name}-tcl = %{version}-%{release}

%description driver-tk
Tk and tkwin drivers for PLplot library. They support Tcl/Tk output.

%description driver-tk -l pl.UTF-8
Sterownik Tk i tkwin dla biblioteki PLplot. Obsługują wyjście poprzez
Tcl/Tk.

%package driver-cairo
Summary:	Cairo driver for PLplot library
Summary(pl.UTF-8):	Sterownik cairo dla biblioteki PLplot
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description driver-cairo
Cairo driver for PLplot library. It supports JPEG and PNG output
formats.

%description driver-cairo -l pl.UTF-8
Sterownik cairo dla biblioteki PLplot. Obsługuje formaty wyjścia JPEG
i PNG.

%package driver-qt5
Summary:	Qt5 driver for PLplot library
Summary(pl.UTF-8):	Sterownik Qt5 dla biblioteki PLplot
Group:		Libraries
Requires:	%{name}-qt5 = %{version}-%{release}
Obsoletes:	plplot-driver-qt4 < 5.14.0-4

%description driver-qt5
Qt5 driver for PLplot library. Supports Qt5 output.

%description driver-qt5 -l pl.UTF-8
Sterownik Qt5 dla biblioteki PLplot. Obsługuje wyjście poprzez Qt5.

%package driver-wxwidgets
Summary:	wxWidgets driver for PLplot library
Summary(pl.UTF-8):	Sterownik wxWidgets dla biblioteki PLplot
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description driver-wxwidgets
wxWidgets driver for PLplot library. Supports wxWidgets output.

%description driver-wxwidgets -l pl.UTF-8
Sterownik wxWidgets dla biblioteki PLplot. Obsługuje wyjście poprzez
wxWidgets.

%package driver-xwin
Summary:	xwin driver for PLplot library
Summary(pl.UTF-8):	Sterownik xwin dla biblioteki PLplot
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description driver-xwin
xwin driver for PLplot library. It supports X Window System output.

%description driver-xwin -l pl.UTF-8
Sterownik ntk (new tk) dla biblioteki PLplot. Obsługuje wyjście do
okna systemu X Window.

%package devel
Summary:	Header files for PLplot library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki PLplot
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	freetype-devel >= 2.1
Requires:	qhull-devel
Obsoletes:	plplot-f77-devel < 5.10.0-2
Obsoletes:	plplot-static < 5.9.6

%description devel
Header files for PLplot library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki PLplot.

%package c++
Summary:	PLplot library - C++ binding
Summary(pl.UTF-8):	Biblioteka PLplot - wiązanie dla C++
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description c++
PLplot library - C++ binding.

%description c++ -l pl.UTF-8
Biblioteka PLplot - wiązanie dla C++.

%package c++-devel
Summary:	PLplot library - C++ binding development files
Summary(pl.UTF-8):	Biblioteka PLplot - pliki programistyczne wiązania dla C++
Group:		Development/Libraries
Requires:	%{name}-c++ = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	libstdc++-devel
Obsoletes:	plplot-c++-static < 5.9.6

%description c++-devel
PLplot library - C++ binding development files.

%description c++-devel -l pl.UTF-8
Biblioteka PLplot - pliki programistyczne wiązania dla C++.

%package d-devel
Summary:	PLplot library - D binding
Summary(pl.UTF-8):	Biblioteka PLplot - wiązanie dla języka D
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description d-devel
PLplot library - D binding.

%description d-devel -l pl.UTF-8
Biblioteka PLplot - wiązanie dla języka D.

%package fortran
Summary:	PLplot library - FORTRAN 95 binding
Summary(pl.UTF-8):	Biblioteka PLplot - wiązanie dla języka FORTRAN 95
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	plplot-f95 < 5.14.0

%description fortran
PLplot library - FORTRAN 95 binding.

%description fortran -l pl.UTF-8
Biblioteka PLplot - wiązanie dla języka FORTRAN 95.

%package fortran-devel
Summary:	PLplot library - FORTRAN 95 binding development files
Summary(pl.UTF-8):	Biblioteka PLplot - pliki programistyczne wiązania dla języka FORTRAN 95
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-fortran = %{version}-%{release}
Requires:	gcc-fortran
Obsoletes:	plplot-f95-devel < 5.14.0

%description fortran-devel
PLplot library - FORTRAN 95 binding development files.

%description fortran-devel -l pl.UTF-8
Biblioteka PLplot - pliki programistyczne wiązania dla języka FORTRAN
95.

%package ada
Summary:	PLplot library - Ada binding
Summary(pl.UTF-8):	Biblioteka PLplot - wiązanie dla Ady
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description ada
PLplot library - Ada binding.

%description ada -l pl.UTF-8
Biblioteka PLplot - wiązanie dla Ady.

%package ada-devel
Summary:	PLplot library - Ada binding development files
Summary(pl.UTF-8):	Biblioteka PLplot - pliki programistyczne wiązania dla Ady
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-ada = %{version}-%{release}

%description ada-devel
PLplot library - Ada binding development files.

%description ada-devel -l pl.UTF-8
Biblioteka PLplot - pliki programistyczne wiązania dla Ady.

%package java
Summary:	PLplot library - Java binding
Summary(pl.UTF-8):	Biblioteka PLplot - wiązanie dla Javy
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description java
PLplot library - Java binding.

%description java -l pl.UTF-8
Biblioteka PLplot - wiązanie dla Javy.

%package java-devel
Summary:	PLplot library - Java binding development files
Summary(pl.UTF-8):	Biblioteka PLplot - pliki programistyczne wiązania dla Javy
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-java = %{version}-%{release}
Obsoletes:	plplot-java-static < 5.9.6

%description java-devel
PLplot library - Java binding development files.

%description java-devel -l pl.UTF-8
Biblioteka PLplot - pliki programistyczne wiązania dla Javy.

%package tcl
Summary:	PLplot library - Tcl/Tk binding
Summary(pl.UTF-8):	Biblioteka PLplot - wiązanie dla Tcl/Tk
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description tcl
PLplot library - Tcl/Tk binding.

%description tcl -l pl.UTF-8
Biblioteka PLplot - wiązanie dla Tcl/Tk.

%package tcl-devel
Summary:	PLplot library - Tcl/Tk binding development files
Summary(pl.UTF-8):	Biblioteka PLplot - pliki programistyczne wiązania dla Tcl/Tk
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-tcl = %{version}-%{release}
%{?with_itcl:Requires:	itcl-devel}
Obsoletes:	plplot-tcl-static < 5.9.6

%description tcl-devel
PLplot library - Tcl/Tk binding development files.

%description tcl-devel -l pl.UTF-8
Biblioteka PLplot - pliki programistyczne wiązania dla Tcl/Tk.

%package qt5
Summary:	PLplot library - Qt5 binding
Summary(pl.UTF-8):	Biblioteka PLplot - wiązanie dla Qt5
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	plplot-qt4 < 5.14.0-4

%description qt5
PLplot library - Qt5 binding.

%description qt5 -l pl.UTF-8
Biblioteka PLplot - wiązanie dla Qt5.

%package qt5-devel
Summary:	PLplot library - Qt5 binding development files
Summary(pl.UTF-8):	Biblioteka PLplot - pliki programistyczne wiązania dla Qt5
Group:		Development/Libraries
Requires:	%{name}-qt5 = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	Qt5Gui-devel >= 5
Requires:	Qt5PrintSupport-devel >= 5
Requires:	Qt5Svg-devel >= 5
Obsoletes:	plplot-qt4-devel < 5.14.0-4

%description qt5-devel
PLplot library - Qt5 binding development files.

%description qt5-devel -l pl.UTF-8
Biblioteka PLplot - pliki programistyczne wiązania dla Qt5.

%package wxwidgets
Summary:	PLplot library - wxWidgets binding
Summary(pl.UTF-8):	Biblioteka PLplot - wiązanie dla wxWidgets
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	wxGTK3-unicode >= 2.6.0

%description wxwidgets
PLplot library - wxwidgets binding.

%description wxwidgets -l pl.UTF-8
Biblioteka PLplot - wiązanie dla wxWidgets.

%package wxwidgets-devel
Summary:	PLplot library - wxWidgets binding development files
Summary(pl.UTF-8):	Biblioteka PLplot - pliki programistyczne wiązania dla wxWidgets
Group:		Development/Libraries
Requires:	%{name}-wxwidgets = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	wxGTK3-unicode-devel >= 2.6.0

%description wxwidgets-devel
PLplot library - wxWidgets binding development files.

%description wxwidgets-devel -l pl.UTF-8
Biblioteka PLplot - pliki programistyczne wiązania dla wxWidgets.

%package octave
Summary:	PLplot library - Octave binding
Summary(pl.UTF-8):	Biblioteka PLplot - wiązanie dla języka Octave
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description octave
PLplot library - Octave binding.

%description octave -l pl.UTF-8
Biblioteka PLplot - wiązanie dla języka Octave.

%package octave-examples
Summary:	PLplot library - examples for Octave binding
Summary(pl.UTF-8):	Biblioteka PLplot - przykłady do wiązania dla języka Octave
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-octave = %{version}-%{release}

%description octave-examples
PLplot library - examples for Octave binding.

%description octave-examples -l pl.UTF-8
Biblioteka PLplot - przykłady do wiązania dla języka Octave.

%package -n lua-plplot
Summary:	Lua binding for PLplot library
Summary(pl.UTF-8):	Wiązanie języka Lua do biblioteki PLplot
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}
Requires:	lua51-libs >= 5.1

%description -n lua-plplot
Lua binding for PLplot library.

%description -n lua-plplot -l pl.UTF-8
Wiązanie języka Lua do biblioteki PLplot.

%package -n ocaml-plplot
Summary:	OCaml binding for PLplot library
Summary(pl.UTF-8):	Wiązanie języka OCaml do biblioteki PLplot
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml-runtime

%description -n ocaml-plplot
OCaml binding for PLplot library.

%description -n ocaml-plplot -l pl.UTF-8
Wiązanie języka OCaml do biblioteki PLplot.

%package -n ocaml-plplot-devel
Summary:	Development files for OCaml binding for PLplot library
Summary(pl.UTF-8):	Wiązanie języka OCaml do biblioteki PLplot - pliki programistyczne
Group:		Development/Libraries
Requires:	ocaml-plplot = %{version}-%{release}
%requires_eq	ocaml

%description -n ocaml-plplot-devel
Development files for OCaml binding for PLplot library.

%description -n ocaml-plplot-devel -l pl.UTF-8
Wiązanie języka OCaml do biblioteki PLplot - pliki programistyczne.

%package -n ocaml-plcairo
Summary:	PLcairo - Cairo extras for OCaml binding for PLplot library
Summary(pl.UTF-8):	PLcairo - dodatki Cairo do wiązania języka OCaml do biblioteki PLplot
Group:		Libraries
Requires:	ocaml-plplot = %{version}-%{release}
Requires:	ocaml-cairo2
Requires:	ocaml-cairo2-gtk
%requires_eq	ocaml-runtime

%description -n ocaml-plcairo
PLcairo - Cairo extras for OCaml binding for PLplot library.

%description -n ocaml-plcairo -l pl.UTF-8
PLcairo - dodatki Cairo do wiązania języka OCaml do biblioteki PLplot.

%package -n ocaml-plcairo-devel
Summary:	Development files for PLcairo OCaml library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki OCamla PLcairo
Group:		Development/Libraries
Requires:	ocaml-cairo2-devel
Requires:	ocaml-cairo2-gtk-devel
Requires:	ocaml-plcairo = %{version}-%{release}
Requires:	ocaml-plplot-devel = %{version}-%{release}
%requires_eq	ocaml

%description -n ocaml-plcairo-devel
Development files for PLcairo OCaml library.

%description -n ocaml-plcairo-devel -l pl.UTF-8
Pliki programistyczne biblioteki OCamla PLcairo.

%package -n python3-plplot
Summary:	PLplot library - Python binding
Summary(pl.UTF-8):	Biblioteka PLplot - wiązanie dla Pythona
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-tcl = %{version}-%{release}
%pyrequires_eq	python3-libs
Requires:	python3-numpy
Obsoletes:	python-plplot < 5.15.0-7

%description -n python3-plplot
PLplot library - Python binding.

%description -n python3-plplot -l pl.UTF-8
Biblioteka PLplot - wiązanie dla Pythona.

%package -n python3-plplot-qt5
Summary:	PLplot library - PyQt5 binding
Summary(pl.UTF-8):	Biblioteka PLplot - wiązanie dla PyQt5
Group:		Libraries/Python
Requires:	python3-plplot = %{version}-%{release}
%pyrequires_eq	python3-libs
Requires:	python3-numpy
Obsoletes:	python-plplot-qt4 < 5.14.0-4
Obsoletes:	python-plplot-qt5 < 5.15.0-7

%description -n python3-plplot-qt5
PLplot library - Python/PyQt5 binding.

%description -n python3-plplot-qt5 -l pl.UTF-8
Biblioteka PLplot - wiązanie dla Pythona/PyQt5.

%package -n python3-plplot-examples
Summary:	PLplot library - Python binding examples
Summary(pl.UTF-8):	Biblioteka PLplot - przykłady do wiązania dla Pythona
Group:		Libraries/Python
Requires:	%{name}-devel = %{version}-%{release}
Requires:	python3-plplot = %{version}-%{release}
Obsoletes:	python-plplot-examples < 5.15.0-7

%description -n python3-plplot-examples
PLplot library - Python binding examples.

%description -n python3-plplot-examples -l pl.UTF-8
Biblioteka PLplot - przykłady do wiązania dla Pythona.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1

%{__sed} -E -i -e '1s,#!\s*/usr/bin/env\s+python2(\s|$),#!%{__python3}\1,' \
		-e '1s,#!\s*/usr/bin/env\s+python(\s|$),#!%{__python3}\1,' \
		-e '1s,#!\s*/usr/bin/python(\s|$),#!%{__python3}\1,' \
      examples/python/* \

%build
# required for cmake to find JNI headers/libs when lib64 is in use
%{?with_java:export JAVA_HOME=%{_jvmlibdir}/java}
_numpy_cflags="$(/usr/bin/numpy-config --cflags)"
export CFLAGS="%{rpmcflags} $_numpy_cflags"
export CXXFLAGS="%{rpmcxxflags} $_numpy_cflags"
# NOTE: no %{_libdir}/jni in PLD, use plain %{_libdir}
%cmake -B build \
%if %{with ada}
	-DENABLE_ada=ON \
	-DADA_INCLUDE_DIR=%{ada_incdir} \
	-DADA_LIB_DIR=%{ada_objdir} \
%else
	-DENABLE_ada=OFF \
%endif
%if %{with d}
	-DENABLE_d=ON \
%else
	-DENABLE_d=OFF \
%endif
%if %{with java}
	-DCMAKE_Java_RUNTIME=%{java} \
	-DCMAKE_Java_COMPILER=%{javac} \
	-DCMAKE_Java_ARCHIVE=%{jar} \
	-DJAR_DIR=%{_javadir} \
	-DJAVAWRAPPER_DIR=%{_libdir} \
%else
	-DENABLE_java=OFF \
%endif
%if %{with lua}
	-DENABLE_lua=ON \
	-DLUA_VERSION=5.1 \
	-DREQUIRED_LUA_VERSION=5.1 \
%else
	-DENABLE_lua=OFF \
%endif
	-DENABLE_itcl=%{?with_itcl:ON}%{!?with_itcl:OFF} \
	-DENABLE_itk=%{?with_itcl:ON}%{!?with_itcl:OFF} \
%if %{with ocaml}
	-DENABLE_ocaml=ON \
	-DOCAML_INSTALL_DIR=%{_libdir}/ocaml \
%else
	-DENABLE_ocaml=OFF \
%endif
	-DENABLE_octave=%{?with_octave:ON}%{!?with_octave:OFF} \
	%{!?with_perl_pdl:-DENABLE_pdl=OFF} \
	%{!?with_pyqt:-DENABLE_pyqt5=OFF} \
	-DENABLE_tk=ON \
	-DPLPLOT_USE_QT5=ON \
	-DFORTRAN_MOD_DIR=%{_includedir}/plplot \
	%{cmake_on_off shapelib HAVE_SHAPELIB} \
	-DOCTAVE_INCLUDE_PATH=%{_includedir}/octave \
	-DOCTAVE_OCT_DIR=%{octave_oct_sitedir} \
	-DOCTAVE_M_DIR=%{octave_m_sitedir} \
	-DPL_FREETYPE_FONT_PATH=/usr/share/fonts/TTF \
	%{?with_cgm:-DPLD_cgm=ON} \
	-DPLD_ntk=ON \
	-DPLD_pdf=ON \
	%{?with_plmeta:-DPLD_plmeta=ON} \
	-DPLD_pstex=ON \
	-DSIPBUILD_OPTIONS:LIST="--qmake;%{_qt5_qmake}" \
	-DUSE_INCRTCL_VERSION_4=ON \
	-DUSE_RPATH=OFF \
%if %{with itcl}
	-DPLPLOT_ITCL_VERSION="$(rpm -q itcl --qf '%%{VERSION}')" \
	-DPLPLOT_ITK_VERSION="$(rpm -q itk --qf '%%{VERSION}')" \
	-DIWIDGETS_VERSIONS_LIST="$(rpm -q iwidgets --qf '%%{VERSION}');$(rpm -q itk --qf '%%{VERSION}');$(rpm -q itcl --qf '%%{VERSION}')" \
%endif
	-DwxWidgets_CONFIG_EXECUTABLE=/usr/bin/wx-gtk3-unicode-config \
	-DwxWidgets_USE_UNICODE=ON

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%{__mv} $RPM_BUILD_ROOT%{_datadir}/plplot%{version}/examples \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__rm} -rf installed-docs
%{__mv} $RPM_BUILD_ROOT%{_docdir}/plplot installed-docs

%py3_comp $RPM_BUILD_ROOT%{py3_sitedir}
%py3_ocomp $RPM_BUILD_ROOT%{py3_sitedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	c++ -p /sbin/ldconfig
%postun	c++ -p /sbin/ldconfig

%post	fortran -p /sbin/ldconfig
%postun	fortran -p /sbin/ldconfig

%post	ada -p /sbin/ldconfig
%postun	ada -p /sbin/ldconfig

%post	tcl -p /sbin/ldconfig
%postun	tcl -p /sbin/ldconfig

%post	qt5 -p /sbin/ldconfig
%postun	qt5 -p /sbin/ldconfig

%post	wxwidgets -p /sbin/ldconfig
%postun	wxwidgets -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ABOUT AUTHORS ChangeLog.release Copyright FAQ NEWS PROBLEMS README README.release SERVICE ToDo
%doc installed-docs/README.{csa,nn,drivers}
%if %{with plmeta}
%attr(755,root,root) %{_bindir}/plm2gif
%attr(755,root,root) %{_bindir}/plpr
%attr(755,root,root) %{_bindir}/plrender
%endif
%attr(755,root,root) %{_bindir}/pltek
%attr(755,root,root) %{_bindir}/pstex2eps
%attr(755,root,root) %{_libdir}/libcsirocsa.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcsirocsa.so.0
%attr(755,root,root) %{_libdir}/libcsironn.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcsironn.so.0
%if %{with cgm}
%attr(755,root,root) %{_libdir}/libnistcd.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libnistcd.so.0
%endif
%attr(755,root,root) %{_libdir}/libqsastime.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libqsastime.so.0
%attr(755,root,root) %{_libdir}/libplplot.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libplplot.so.17
%if %{with plmeta}
%{_mandir}/man1/plm2gif.1*
%{_mandir}/man1/plpr.1*
%{_mandir}/man1/plrender.1*
%endif
%{_mandir}/man1/pltek.1*
%{_mandir}/man1/pstex2eps.1*
%dir %{_libdir}/plplot%{version}
%dir %{_libdir}/plplot%{version}/drivers
%if %{with cgm}
%attr(755,root,root) %{_libdir}/plplot%{version}/drivers/cgm.so
%{_libdir}/plplot%{version}/drivers/cgm.driver_info
%endif
%attr(755,root,root) %{_libdir}/plplot%{version}/drivers/mem.so
%{_libdir}/plplot%{version}/drivers/mem.driver_info
%attr(755,root,root) %{_libdir}/plplot%{version}/drivers/null.so
%{_libdir}/plplot%{version}/drivers/null.driver_info
%if %{with plmeta}
%attr(755,root,root) %{_libdir}/plplot%{version}/drivers/plmeta.so
%{_libdir}/plplot%{version}/drivers/plmeta.driver_info
%endif
%attr(755,root,root) %{_libdir}/plplot%{version}/drivers/ps.so
%{_libdir}/plplot%{version}/drivers/ps.driver_info
%attr(755,root,root) %{_libdir}/plplot%{version}/drivers/pstex.so
%{_libdir}/plplot%{version}/drivers/pstex.driver_info
%attr(755,root,root) %{_libdir}/plplot%{version}/drivers/svg.so
%{_libdir}/plplot%{version}/drivers/svg.driver_info
%attr(755,root,root) %{_libdir}/plplot%{version}/drivers/xfig.so
%{_libdir}/plplot%{version}/drivers/xfig.driver_info
%dir %{_datadir}/plplot%{version}
%{_datadir}/plplot%{version}/*.pal
%{_datadir}/plplot%{version}/*.fnt

%files driver-cairo
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/plplot%{version}/drivers/cairo.so
%{_libdir}/plplot%{version}/drivers/cairo.driver_info

%files driver-ntk
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/plplot%{version}/drivers/ntk.so
%{_libdir}/plplot%{version}/drivers/ntk.driver_info

%files driver-pdf
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/plplot%{version}/drivers/pdf.so
%{_libdir}/plplot%{version}/drivers/pdf.driver_info

%files driver-psttf
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/plplot%{version}/drivers/psttf.so
%{_libdir}/plplot%{version}/drivers/psttf.driver_info

%files driver-tk
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/plplot%{version}/drivers/tk.so
%{_libdir}/plplot%{version}/drivers/tk.driver_info
%attr(755,root,root) %{_libdir}/plplot%{version}/drivers/tkwin.so
%{_libdir}/plplot%{version}/drivers/tkwin.driver_info

%files driver-qt5
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/plplot%{version}/drivers/qt.so
%{_libdir}/plplot%{version}/drivers/qt.driver_info

%files driver-wxwidgets
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/plplot%{version}/drivers/wxwidgets.so
%{_libdir}/plplot%{version}/drivers/wxwidgets.driver_info

%files driver-xwin
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/plplot%{version}/drivers/xwin.so
%{_libdir}/plplot%{version}/drivers/xwin.driver_info

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcsirocsa.so
%attr(755,root,root) %{_libdir}/libcsironn.so
%if %{with cgm}
%attr(755,root,root) %{_libdir}/libnistcd.so
%endif
%attr(755,root,root) %{_libdir}/libplplot.so
%attr(755,root,root) %{_libdir}/libqsastime.so
%dir %{_includedir}/plplot
%if %{with cgm}
%{_includedir}/plplot/cd.h
%{_includedir}/plplot/defines.h
%endif
%{_includedir}/plplot/csa.h
%{_includedir}/plplot/csadll.h
%{_includedir}/plplot/disptab.h
%{_includedir}/plplot/drivers.h
%{_includedir}/plplot/nn.h
%{_includedir}/plplot/nndll.h
%{_includedir}/plplot/pdf.h
%{_includedir}/plplot/plConfig.h
%{_includedir}/plplot/plDevs.h
%{_includedir}/plplot/pldebug.h
%{_includedir}/plplot/pldll.h
%{_includedir}/plplot/plevent.h
%{_includedir}/plplot/plplot.h
%{_includedir}/plplot/plplotP.h
%{_includedir}/plplot/plstrm.h
%{_includedir}/plplot/qsastime.h
%{_includedir}/plplot/qsastimedll.h
# xwin driver (uses X11 headers)
%{_includedir}/plplot/plxwd.h
%{_pkgconfigdir}/plplot.pc
%{_libdir}/cmake/plplot
%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/c
%{_examplesdir}/%{name}-%{version}/cmake
%{_examplesdir}/%{name}-%{version}/CMakeLists.txt
%{_examplesdir}/%{name}-%{version}/Chloe.pgm
%{_examplesdir}/%{name}-%{version}/Makefile
%{_examplesdir}/%{name}-%{version}/README.Chloe
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/plplot-test.sh
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/plplot-test-interactive.sh
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/test_c.sh
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/test_c_interactive.sh
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/test_diff.sh
%{_examplesdir}/%{name}-%{version}/plplot_test
%if %{with plmeta}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/test_plrender.sh
%endif
%if %{with perl_pdl}
# perl examples use PDL::Graphics::PLplot module found in perl-PDL
%{_examplesdir}/%{name}-%{version}/perl
%endif

%files c++
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libplplotcxx.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libplplotcxx.so.15

%files c++-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libplplotcxx.so
%{_includedir}/plplot/plstream.h
%{_pkgconfigdir}/plplot-c++.pc
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/test_cxx.sh
%{_examplesdir}/%{name}-%{version}/c++

%if %{with d}
%files d-devel
%defattr(644,root,root,755)
%{_libdir}/libplplotdmd.a
%{_includedir}/plplot/plplot.d
%{_pkgconfigdir}/plplot-d.pc
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/test_d.sh
%{_examplesdir}/%{name}-%{version}/d
%endif

%files fortran
%defattr(644,root,root,755)
%doc bindings/fortran/README_array_sizes
%attr(755,root,root) %{_libdir}/libplplotfortran.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libplplotfortran.so.0

%files fortran-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libplplotfortran.so
%{_libdir}/libplfortrandemolib.a
%{_includedir}/plplot/plfortrandemolib.mod
%{_includedir}/plplot/plplot_double.mod
%{_includedir}/plplot/plplot_graphics.mod
%{_includedir}/plplot/plplot.mod
%{_includedir}/plplot/plplot_private_exposed.mod
%{_includedir}/plplot/plplot_private_utilities.mod
%{_includedir}/plplot/plplot_single.mod
%{_includedir}/plplot/plplot_types.mod
%{_pkgconfigdir}/plplot-fortran.pc
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/test_fortran.sh
%{_examplesdir}/%{name}-%{version}/fortran

%if %{with ada}
%files ada
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libplplotada.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libplplotada.so.4

%files ada-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libplplotada.so
%{ada_objdir}/plplot_*.ali
%{ada_incdir}/plplot*.ad*
%{_pkgconfigdir}/plplot-ada.pc
%{_examplesdir}/%{name}-%{version}/ada
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/test_ada.sh
%endif

%if %{with java}
%files java
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libplplotjavac_wrap.so
%{_javadir}/plplot.jar

%files java-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/test_java.sh
%{_examplesdir}/%{name}-%{version}/java
%endif

%files tcl
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pltcl
%attr(755,root,root) %{_bindir}/plserver
%attr(755,root,root) %{_libdir}/libplplottcltk.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libplplottcltk.so.14
%attr(755,root,root) %{_libdir}/libtclmatrix.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtclmatrix.so.10
%attr(755,root,root) %{_libdir}/libplplottcltk_Main.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libplplottcltk_Main.so.1
%{_datadir}/plplot%{version}/*.tcl
%{_datadir}/plplot%{version}/tcl
%{_mandir}/man1/pltcl.1*
%{_mandir}/man1/plserver.1*

%files tcl-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libplplottcltk.so
%attr(755,root,root) %{_libdir}/libtclmatrix.so
%attr(755,root,root) %{_libdir}/libplplottcltk_Main.so
%{_includedir}/plplot/pltcl.h
%{_includedir}/plplot/pltk.h
%{_includedir}/plplot/tclMatrix.h
%{_pkgconfigdir}/plplot-tcl.pc
%{_pkgconfigdir}/plplot-tcl_Main.pc
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/test_tcl.sh
%{_examplesdir}/%{name}-%{version}/tcl
%{_examplesdir}/%{name}-%{version}/tk

%files qt5
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libplplotqt.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libplplotqt.so.2

%files qt5-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libplplotqt.so
%{_includedir}/plplot/qt.h
%{_pkgconfigdir}/plplot-qt.pc

%files wxwidgets
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/wxPLViewer
%attr(755,root,root) %{_libdir}/libplplotwxwidgets.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libplplotwxwidgets.so.1

%files wxwidgets-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libplplotwxwidgets.so
%{_includedir}/plplot/wxPLplot*.h
%{_pkgconfigdir}/plplot-wxwidgets.pc

%if %{with octave}
%files octave
%defattr(644,root,root,755)
%doc bindings/octave/{BUGS,FGA,README,ToDo,USAGE}
%attr(755,root,root) %{octave_oct_sitedir}/plplot_octave.oct
%{octave_m_sitedir}/*.m
%{_datadir}/plplot_octave
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/test_octave_interactive.sh

%files octave-examples
%defattr(644,root,root,755)
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/test_octave.sh
%{_examplesdir}/%{name}-%{version}/octave
%endif

%if %{with lua}
%files -n lua-plplot
%defattr(644,root,root,755)
%dir %{_libdir}/lua/5.1/plplot
%attr(755,root,root) %{_libdir}/lua/5.1/plplot/plplotluac.so
%{_examplesdir}/%{name}-%{version}/lua
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/test_lua.sh
%endif

%if %{with ocaml}
%files -n ocaml-plplot
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dllplplot_stubs.so

%files -n ocaml-plplot-devel
%dir %{_libdir}/ocaml/plplot
%{_libdir}/ocaml/plplot/META
%{_libdir}/ocaml/plplot/libplplot_stubs.a
%{_libdir}/ocaml/plplot/plplot.cma
%{_libdir}/ocaml/plplot/plplot.cmi
%{_libdir}/ocaml/plplot/plplot.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/plplot/plplot.a
%{_libdir}/ocaml/plplot/plplot.cmx
%{_libdir}/ocaml/plplot/plplot.cmxa
%endif
%{_pkgconfigdir}/plplot-ocaml.pc
%{_examplesdir}/%{name}-%{version}/ocaml
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/test_ocaml.sh

%if %{with ocaml_cairo}
%files -n ocaml-plcairo
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dllplcairo_stubs.so

%files -n ocaml-plcairo-devel
%dir %{_libdir}/ocaml/plcairo
%{_libdir}/ocaml/plcairo/META
%{_libdir}/ocaml/plcairo/libplcairo_stubs.a
%{_libdir}/ocaml/plcairo/plcairo.cma
%{_libdir}/ocaml/plcairo/plcairo.cmi
%{_libdir}/ocaml/plcairo/plcairo.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/plcairo/plcairo.a
%{_libdir}/ocaml/plcairo/plcairo.cmxa
%endif
%endif
%endif

%files -n python3-plplot
%defattr(644,root,root,755)
%attr(755,root,root) %{py3_sitedir}/_Pltk_init.so
%attr(755,root,root) %{py3_sitedir}/_plplotc.so
%{py3_sitedir}/__pycache__/Plframe.cpython-*.py[co]
%{py3_sitedir}/__pycache__/Pltk_init.cpython-*.py[co]
%{py3_sitedir}/__pycache__/plplotc.cpython-*.py[co]
%{py3_sitedir}/__pycache__/plplot.cpython-*.py[co]
%{py3_sitedir}/__pycache__/TclSup.cpython-*.py[co]
%{py3_sitedir}/Plframe.py
%{py3_sitedir}/Pltk_init.py
%{py3_sitedir}/plplotc.py
%{py3_sitedir}/plplot.py
%{py3_sitedir}/TclSup.py

%if %{with pyqt}
%files -n python3-plplot-qt5
%defattr(644,root,root,755)
%attr(755,root,root) %{py3_sitedir}/plplot_pyqt5.so
%endif

%files -n python3-plplot-examples
%defattr(644,root,root,755)
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/test_python.sh
%{_examplesdir}/%{name}-%{version}/python
