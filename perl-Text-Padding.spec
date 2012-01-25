%define	module	Text-Padding

Name:		perl-%{module}
Version:	1.110170
Release:	1
Summary:	Simple way of formatting a text
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source0:	http://www.cpan.org/modules/by-module/Text/%{module}-%{version}.tar.gz

BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Moose)
BuildRequires:	perl(MooseX::Has::Sugar)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Text::Truncate)
BuildRequires:	perl(Module::Build)
BuildArch:	noarch

%description
This module provides a simple way to align a text on the left, right or
center. If left & right are easy to achieve (see 'sprintf()'), i found no
cpan module that achieved a simple text centering. Well, of course, the
Perl6::Form manpage provides it, but it's incredibly slow during startup /
destroy time. And the Text::Reform manpage was segfaulting during destroy
time.

Hence this module, which aims to provide only those 3 methods.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Build.PL installdirs=vendor

./Build

%check
./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc README Changes LICENSE META.yml META.json
%{_mandir}/man3/*
%{perl_vendorlib}/*
