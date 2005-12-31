Summary:	Ruby SFTP library
Summary(pl):	Biblioteka SFTP dla jêzyka Ruby
Name:		ruby-Net-SFTP
Version:	0.9.0
Release:	2
License:	GPL
Group:		Development/Libraries
Source0:	http://rubyforge.org/frs/download.php/2561/net-sftp-%{version}.tar.bz2
# Source0-md5:	09d8df913c7a0c650e4d3952b4cb3c65
URL:		http://net-ssh.rubyforge.org/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
Requires:	ruby-Net-SSH
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::SFTP is to SFTP as Net::FTP is to FTP and Net::HTTP is to HTTP.
Perform non-interactive SFTP processing, purely from Ruby!

%description -l pl
Net::SFTP ma siê do SFTP tak, jak Net::FTP do FTP i Net::HTTP do HTTP.
Umo¿liwia nieinteraktywne przetwarzanie SFTP w czystym Rubym.

%prep
%setup -q -n net-sftp-%{version}

%build
ruby setup.rb config \
	--site-ruby=%{ruby_rubylibdir} \
	--so-dir=%{ruby_archdir}

ruby setup.rb setup
rdoc --inline-source --op rdoc lib
rdoc --ri --op ri lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_rubylibdir}/*
%{ruby_ridir}/*
