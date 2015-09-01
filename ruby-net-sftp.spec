#
# Conditional build:
%bcond_with	tests		# build without tests
%bcond_without	doc			# don't build ri/rdoc

%define pkgname net-sftp
Summary:	Ruby SFTP library
Summary(pl.UTF-8):	Biblioteka SFTP dla języka Ruby
Name:		ruby-%{pkgname}
Version:	2.1.2
Release:	2
License:	MIT
Group:		Development/Libraries
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	c49f16fae9cea91123b06d903267205b
URL:		https://github.com/net-ssh/net-sftp
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildRequires:	ruby-modules
%if %{with tests}
BuildRequires:	ruby-mocha
BuildRequires:	ruby-test-unit
%endif
Requires:	ruby-net-ssh >= 2.6.5
Obsoletes:	ruby-Net-SFTP
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::SFTP is to SFTP as Net::FTP is to FTP and Net::HTTP is to HTTP.
Perform non-interactive SFTP processing, purely from Ruby!

%description -l pl.UTF-8
Net::SFTP ma się do SFTP tak, jak Net::FTP do FTP i Net::HTTP do HTTP.
Umożliwia nieinteraktywne przetwarzanie SFTP w czystym Rubym.

%package rdoc
Summary:	HTML documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie HTML dla %{pkgname}
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
HTML documentation for %{pkgname}.

%description rdoc -l pl.UTF-8
Dokumentacja w formacie HTML dla %{pkgname}.

%package ri
Summary:	ri documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie ri dla %{pkgname}
Group:		Documentation
Requires:	ruby

%description ri
ri documentation for %{pkgname}.

%description ri -l pl.UTF-8
Dokumentacji w formacie ri dla %{pkgname}.

%prep
%setup -q -n %{pkgname}-%{version}

%build
# write .gemspec
%__gem_helper spec

%if %{with doc}
rdoc --inline-source --op rdoc lib
rdoc --ri --op ri lib
rm -r ri/Net/SSH
rm -r ri/Net/cdesc-Net.ri
rm ri/*.rid
rm ri/cache.ri
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%if %{with doc}
install -d $RPM_BUILD_ROOT{%{ruby_ridir},%{ruby_rdocdir}/%{name}-%{version}}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc/* $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_vendorlibdir}/net/sftp.rb
%{ruby_vendorlibdir}/net/sftp
%{ruby_specdir}/%{pkgname}-%{version}.gemspec

%if %{with doc}
%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}

%files ri
%defattr(644,root,root,755)
%{ruby_ridir}/Net/SFTP
%endif
