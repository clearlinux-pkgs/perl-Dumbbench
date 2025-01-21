#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v20
# autospec commit: f35655a
#
Name     : perl-Dumbbench
Version  : 0.505
Release  : 36
URL      : https://cpan.metacpan.org/authors/id/B/BD/BDFOY/Dumbbench-0.505.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BD/BDFOY/Dumbbench-0.505.tar.gz
Summary  : 'More reliable benchmarking with the least amount of thinking'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Dumbbench-bin = %{version}-%{release}
Requires: perl-Dumbbench-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Capture::Tiny)
BuildRequires : perl(Class::XSAccessor)
BuildRequires : perl(Devel::CheckOS)
BuildRequires : perl(Number::WithError)
BuildRequires : perl(Params::Util)
BuildRequires : perl(Statistics::CaseResampling)
BuildRequires : perl(prefork)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
=pod
=encoding utf8
=for HTML <a href="https://www.github.com/briandfoy/dumbbench/actions?query=workflow%3Amacos"><img src="https://www.github.com/briandfoy/dumbbench/workflows/macos/badge.svg"></a>

%package bin
Summary: bin components for the perl-Dumbbench package.
Group: Binaries

%description bin
bin components for the perl-Dumbbench package.


%package dev
Summary: dev components for the perl-Dumbbench package.
Group: Development
Requires: perl-Dumbbench-bin = %{version}-%{release}
Provides: perl-Dumbbench-devel = %{version}-%{release}
Requires: perl-Dumbbench = %{version}-%{release}

%description dev
dev components for the perl-Dumbbench package.


%package perl
Summary: perl components for the perl-Dumbbench package.
Group: Default
Requires: perl-Dumbbench = %{version}-%{release}

%description perl
perl components for the perl-Dumbbench package.


%prep
%setup -q -n Dumbbench-0.505
cd %{_builddir}/Dumbbench-0.505
pushd ..
cp -a Dumbbench-0.505 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/dumbbench

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Benchmark::Dumb.3
/usr/share/man/man3/Dumbbench.3
/usr/share/man/man3/Dumbbench::Instance.3
/usr/share/man/man3/Dumbbench::Instance::Cmd.3
/usr/share/man/man3/Dumbbench::Instance::PerlEval.3
/usr/share/man/man3/Dumbbench::Instance::PerlSub.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
