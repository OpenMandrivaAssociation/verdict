%define major 1
%define libname %mklibname verdict
%define devname %mklibname verdict -d

Name: verdict
Version: 1.4.2
Release: 1
Source0: https://github.com/sandialabs/verdict/archive/%{version}/%{name}-%{version}.tar.gz
Summary: Library for computing quality functions of 2 and 3-dimensional regions
URL: https://github.com/sandialabs/verdict
License: MIT
Group: System/Libraries
BuildRequires: pkgconfig(gtest)
BuildRequires: cmake
BuildRequires: ninja

%description
Library for computing quality functions of 2 and 3-dimensional regions

%package -n %{libname}
Summary: Library for computing quality functions of 2 and 3-dimensional regions
Group: System/Libraries

%description -n %{libname}
Library for computing quality functions of 2 and 3-dimensional regions

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}, a library for computing
quality functions of 2 and 3-dimensional regions

%prep
%autosetup -p1
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%doc %{_docdir}/verdict/
