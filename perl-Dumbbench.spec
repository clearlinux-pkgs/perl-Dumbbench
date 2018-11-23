#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Dumbbench
Version  : 0.111
Release  : 6
URL      : https://cpan.metacpan.org/authors/id/B/BD/BDFOY/Dumbbench-0.111.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BD/BDFOY/Dumbbench-0.111.tar.gz
Summary  : 'More reliable benchmarking with the least amount of thinking'
Group    : Development/Tools
License  : Artistic-1.0-Perl Artistic-2.0
Requires: perl-Dumbbench-bin = %{version}-%{release}
Requires: perl-Dumbbench-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Capture::Tiny)
BuildRequires : perl(Class::XSAccessor)
BuildRequires : perl(Devel::CheckOS)
BuildRequires : perl(Number::WithError)
BuildRequires : perl(Params::Util)
BuildRequires : perl(Statistics::CaseResampling)
BuildRequires : perl(prefork)

%description
=pod
=encoding utf8
=for HTML <a href="https://travis-ci.org/briandfoy/dumbbench"><img src="https://travis-ci.org/briandfoy/dumbbench.svg?branch=master"></a>

%package bin
Summary: bin components for the perl-Dumbbench package.
Group: Binaries
Requires: perl-Dumbbench-license = %{version}-%{release}

%description bin
bin components for the perl-Dumbbench package.


%package dev
Summary: dev components for the perl-Dumbbench package.
Group: Development
Requires: perl-Dumbbench-bin = %{version}-%{release}
Provides: perl-Dumbbench-devel = %{version}-%{release}

%description dev
dev components for the perl-Dumbbench package.


%package license
Summary: license components for the perl-Dumbbench package.
Group: Default

%description license
license components for the perl-Dumbbench package.


%prep
%setup -q -n Dumbbench-0.111

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Dumbbench
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Dumbbench/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.0/Benchmark/Dumb.pm
/usr/lib/perl5/vendor_perl/5.28.0/Dumbbench.pm
/usr/lib/perl5/vendor_perl/5.28.0/Dumbbench/BoxPlot.pm
/usr/lib/perl5/vendor_perl/5.28.0/Dumbbench/CPUFrequencyPinner.pm
/usr/lib/perl5/vendor_perl/5.28.0/Dumbbench/Instance.pm
/usr/lib/perl5/vendor_perl/5.28.0/Dumbbench/Instance/Cmd.pm
/usr/lib/perl5/vendor_perl/5.28.0/Dumbbench/Instance/PerlEval.pm
/usr/lib/perl5/vendor_perl/5.28.0/Dumbbench/Instance/PerlSub.pm
/usr/lib/perl5/vendor_perl/5.28.0/Dumbbench/Result.pm
/usr/lib/perl5/vendor_perl/5.28.0/Dumbbench/Stats.pm

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

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Dumbbench/LICENSE
