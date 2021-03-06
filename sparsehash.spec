# disable -debuginfo subpackage
%global debug_package %{nil}

Name:           sparsehash
Version:        1.12
Release:        1%{?dist}
Summary:        Extremely memory-efficient C++ hash_map implementation

Group:          Development/Libraries
License:        BSD
URL:            http://code.google.com/p/sparsehash
Source0:        http://sparsehash.googlecode.com/files/sparsehash-%{version}.tar.gz

%description
The Google SparseHash project contains several C++ template hash-map
implementations with different performance characteristics, including
an implementation that optimizes for space and one that optimizes for
speed.

# all files are in -devel package
%package        devel
Summary:        Extremely memory-efficient C++ hash_map implementation
Group:          Development/Libraries

%description    devel
The Google SparseHash project contains several C++ template hash-map
implementations with different performance characteristics, including
an implementation that optimizes for space and one that optimizes for
speed.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

# Remove unneeded files
rm $RPM_BUILD_ROOT%{_defaultdocdir}/sparsehash-%{version}/INSTALL
rm $RPM_BUILD_ROOT%{_defaultdocdir}/sparsehash-%{version}/README_windows.txt

%check
make check

%files devel
%doc %{_defaultdocdir}/sparsehash-%{version}/
%{_includedir}/google/
%{_libdir}/pkgconfig/libsparsehash.pc

%changelog
* Wed Feb 27 2013 Raven <admin@sysadmins.el.kg> - 1.12-2
- Initial building for el6

* Sat Jan 21 2012 Kalev Lember <kalevlember@gmail.com> - 1.12-1
- Update to 1.12
- Corrected the download URL

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 24 2011 Kalev Lember <kalev@smartlink.ee> - 1.11-1
- Update to 1.11
- Cleaned up the spec file for modern rpmbuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 22 2011 Kalev Lember <kalev@smartlink.ee> - 1.10-1
- Update to 1.10

* Fri Dec 17 2010 Kalev Lember <kalev@smartlink.ee> - 1.9-1
- Update to 1.9
- Added libsparsehash.pc pkgconfig file
- The -devel subpackage is no longer noarch as the new .pc file
  needs to go in arch-specific _libdir

* Thu Aug 05 2010 Kalev Lember <kalev@smartlink.ee> - 1.8.1-1
- Update to 1.8.1

* Sat Jul 03 2010 Kalev Lember <kalev@smartlink.ee> - 1.7-3
- Marked -devel as noarch, thanks to Chen Lei (#609728)

* Sat Jul 03 2010 Kalev Lember <kalev@smartlink.ee> - 1.7-2
- Move all files to -devel (#609728)

* Thu Jul 01 2010 Kalev Lember <kalev@smartlink.ee> - 1.7-1
- Initial RPM release
