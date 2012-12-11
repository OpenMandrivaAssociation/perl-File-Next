%define upstream_name	 File-Next
%define upstream_version 1.06

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	File-finding iterator
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/File/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
File::Next is a lightweight, taint-safe file-finding module. It's lightweight
and has no non-core prerequisites.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test 

%install
%makeinstall_std

%files
%doc Changes
%{perl_vendorlib}/File
%{_mandir}/*/*

%changelog
* Tue Aug 11 2009 Jérôme Quelin <jquelin@mandriva.org> 1.60.0-1mdv2010.0
+ Revision: 415004
- update to 1.06

* Tue Aug 04 2009 Jérôme Quelin <jquelin@mandriva.org> 1.40.0-1mdv2010.0
+ Revision: 408833
- update to 1.04

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.20.0-1mdv2010.0
+ Revision: 403176
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.02-3mdv2009.0
+ Revision: 256983
- rebuild

* Tue Jan 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.02-1mdv2008.1
+ Revision: 152919
- new version
- update to new version 1.02

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Jul 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.00-1mdv2008.0
+ Revision: 46526
- update to new version 1.00


* Mon Mar 12 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.40-1mdv2007.1
+ Revision: 141685
- new version

* Tue Mar 06 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.38-1mdv2007.1
+ Revision: 133685
- new version

* Thu Dec 14 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.32-1mdv2007.1
+ Revision: 96807
- new version

* Thu Oct 19 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.28-1mdv2007.1
+ Revision: 66430
- Import perl-File-Next

