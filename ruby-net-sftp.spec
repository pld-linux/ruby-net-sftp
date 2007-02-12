Summary:	Ruby SFTP library
Summary(pl.UTF-8):   Biblioteka SFTP dla języka Ruby
Name:		ruby-Net-SFTP
Version:	1.1.0
Release:	1
License:	GPL
Group:		Development/Libraries
Source0:	http://rubyforge.org/frs/download.php/7929/net-sftp-%{version}.tar.bz2
# Source0-md5:	bd87febdab5d4613319f68a4edd6feab
URL:		http://net-ssh.rubyforge.org/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
Requires:	ruby-Net-SSH
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::SFTP is to SFTP as Net::FTP is to FTP and Net::HTTP is to HTTP.
Perform non-interactive SFTP processing, purely from Ruby!

%description -l pl.UTF-8
Net::SFTP ma się do SFTP tak, jak Net::FTP do FTP i Net::HTTP do HTTP.
Umożliwia nieinteraktywne przetwarzanie SFTP w czystym Rubym.

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
