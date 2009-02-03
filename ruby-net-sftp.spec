Summary:	Ruby SFTP library
Summary(pl.UTF-8):	Biblioteka SFTP dla języka Ruby
Name:		ruby-Net-SFTP
Version:	2.0.2
Release:	1
License:	GPL
Group:		Development/Libraries
Source0:	http://rubyforge.org/frs/download.php/51131/net-sftp-2.0.2.tar.gz
# Source0-md5:	2951825da7e2daed64c5db975ece2945
URL:		http://net-ssh.rubyforge.org/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
Requires:	ruby-Net-SSH >= 2.0
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
rm ri/*.rid

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_rubylibdir}/*
%{ruby_ridir}/Net/SFTP
