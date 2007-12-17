%define module	File-Next
%define name	perl-%{module}
%define version 1.00
%define	release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	File-finding iterator
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source:		%{module}-%{version}.tar.bz2
BuildArch:	noarch

%description
File::Next is a lightweight, taint-safe file-finding module. It's lightweight
and has no non-core prerequisites.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test 

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/File
%{_mandir}/*/*



