%define upstream_name	 File-Next
%define upstream_version 1.12

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

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


