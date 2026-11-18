#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define	pdir	Class
%define	pnam	Std
Summary:	Class::Std - Support for creating standard "inside-out" classes
Name:		perl-Class-Std
Version:	0.013
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	82bcc56d9769edce671b0bd0e183ec3a
URL:		http://search.cpan.org/dist/Class-Std/
BuildRequires:	perl-modules >= 1:5.8.8
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides tools that help to implement the "inside out
object" class structure in a convenient and standard way.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Class/*.pm
%{_mandir}/man3/*
