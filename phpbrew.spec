Summary:	Brew & manage PHP versions in pure PHP at HOME
Name:		phpbrew
Version:	1.19.7
Release:	0.2
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/phpbrew/phpbrew/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	4d9b568120ee457faac15d5537511889
URL:		http://phpbrew.github.io/phpbrew
# for phpbrew runtime
Requires:	/usr/bin/php
Requires:	php(json)
Requires:	php(phar)
# deps for building php
Requires:	bzip2-devel
Requires:	gcc
Requires:	libmcrypt-devel
Requires:	libxml2-devel
Requires:	libxslt-devel
Requires:	openssl-devel
Requires:	readline-devel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
phpbrew builds and installs multiple version php(s) in your $HOME
directory.

phpbrew also manage the environment variables, so you can use, switch
php version whenever you need.

What phpbrew can do for you:
- Configure options are simplified into variants, no worries about the
  path anymore!
- Build php with different variants like PDO, mysql, sqlite, debug
  ...etc.
- Compile apache php module and separate them by different versions.
- Build and install php(s) in your home directory, so you don't need
  root permission.
- Switch versions very easily and is integrated with bash/zsh shell.
- Automatic feature detection.
- Install & enable php extensions into current environment with ease.
- Install multiple php into system-wide environment.
- Path detection optimization for HomeBrew and MacPorts.

%prep
%setup -q

# modifying phar would break signature
#%{__sed} -i -e '1s,^#!.*php,#!/usr/bin/php,' %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -p phpbrew $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%banner %{name} -e -o <<'EOF'
You probably want to execute the following line to add phpbrew to your shell:

echo '. ~/.phpbrew/bashrc' >> ~/.bashrc

EOF

%files
%defattr(644,root,root,755)
%doc README.md CHANGES.md CONTRIBUTORS.md HACKING.md todo.md
%doc %lang(ja) README.ja.md
%attr(755,root,root) %{_bindir}/phpbrew
