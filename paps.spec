Name:           paps
Version:        0.6.8
Release:        45
License:        LGPLv2+
Summary:        Plain Text to PostScript converter
URL:            http://paps.sourceforge.net/
Source0:        http://downloads.sourceforge.net/paps/paps-%{version}.tar.gz
BuildRequires:  pango-devel automake autoconf libtool doxygen cups-devel
Requires:       cups-filesystem fontpackages-filesystem
Provides:       paps-libs = %{version}-%{release}
Obsoletes:      paps-libs
Patch0000:      paps-0.6.8-shared.patch
Patch0001:      paps-0.6.8-wordwrap.patch
Patch0002:      paps-langinfo.patch
Patch0003:      paps-0.6.6-lcnumeric.patch
Patch0004:      paps-exitcode.patch
Patch9001:      paps-fix_manpage_inconsistency_issues.patch
Patch9002:      paps-applied_to_work_paps_as_cups_filter.patch
Patch9003:      paps-cpi_scale_calculation.patch
Patch9004:      paps-fix_dsc_compliant_issues.patch
Patch9005:      paps-fix_autoconf_error.patch
Patch9006:      paps-fix_cpi_setting_not_used_issues.patch
Patch9007:      paps-fix_infinite_loop_in_split_text.patch
Patch9008:      paps-fix_tab_print_issues.patch
Patch9009:      paps-fix_non_weak_symbol_issues.patch
Patch9010:      paps-use_correct_fsf_address.patch
Patch9011:      paps-add_ft_header_file.patch
Patch9012:      paps-add_support_for_a3_paper.patch
Patch9013:      paps-add_gobject_glib_lib_for_build.patch

%description
paps is a PostScript converter from plain text file using Pango.

%package        devel
Summary:        Development files for paps
Requires:       paps = %{version}-%{release}

%description    devel
paps is a PostScript converter from plain text file using Pango.

This package contains the development files that is necessary to develop
applications using paps API.

%package        help
Summary:        Documentation for paps

%description    help
Documentation for paps

%prep
%autosetup -n   paps-%{version} -p1
libtoolize -f -c
autoreconf -f -i

%build
%configure --disable-static
%{make_build}

%install
%{make_install}
%delete_la
install -d $RPM_BUILD_ROOT%{_cups_serverbin}/filter
ln -s %{_bindir}/paps %{buildroot}%{_cups_serverbin}/filter/texttopaps
install -d $RPM_BUILD_ROOT%{_datadir}/cups/mime
install -d $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc AUTHORS COPYING.LIB README TODO
%{_bindir}/paps
%{_libdir}/libpaps.so.*
%{_cups_serverbin}/filter/texttopaps

%files devel
%doc COPYING.LIB
%{_includedir}/libpaps.h
%{_libdir}/libpaps.so

%files help
%{_mandir}/man1/paps.1*

%changelog
* Tue Feb 18 2020 Ling Yang <lingyang2@huawei.com> - 0.6.8-45
- Package init
