%define upstream_name	 File-Next
%define upstream_version 1.18

Name:		perl-%{upstream_name}
Version:	1.18
Release:	3

Summary:	File-finding iterator
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/petdance/file-next/tree/master
Source0:	https://cpan.metacpan.org/authors/id/P/PE/PETDANCE/File-Next-1.18.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
File::Next is a lightweight, taint-safe file-finding module. It's lightweight
and has no non-core prerequisites.

%prep
%setup -q -n File-Next-1.18

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
%make_install

%files
%doc Changes
%{perl_vendorlib}/File
%{_mandir}/*/*
