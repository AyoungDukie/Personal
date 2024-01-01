%global debug_package %{nil}

%define repoauth TuxVinyards

Name:    qqX
Version: 1.4.01
Release: 1%{?dist}
Summary: qqX - Safe & Powerful text based Quickemu Virtual Machine Manager

Group:   Utilities/Virtual Machines
License: GPLv3
URL:     https://github.com/%{repoauth}/%{name}
Source0: https://github.com/%{repoauth}/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildRequires: desktop-file-utils
Requires: quickemu

%description
Quickemu Quickget X terminal project - qqX offers an alternative menu system that has lots of power and functions. More even than quickemu. It has an easy installation. No additional software or dependancies are required. Quickemu works on the command line and traditionally has had a simple menu interface called quickgui.

%prep
%setup -q -c

%build
mkdir -p ./_build/src/github.com/%{repoauth}
ln -s $(pwd) ./_build/src/github.com/%{repoauth}/%{name}
curl -LJO %{URL}/blob/{%version}/README.md

%install
# Prepare asset files
mkdir -p %{buildroot}%{_bindir}/qqX.system
cp -r ./qqX.system/*  %{_bindir}/qqX.system/*
install -Dm 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dm 0755 %{name}_settings %{buildroot}%{_bindir}/%{name}_settings
install -Dm 0755 %{name}_setup_and_install %{buildroot}%{_bindir}/%{name}_setup_and_install

%post
%{_bindir}/%{name}_setup_and_install

%files
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
%doc LICENSE.Addendum.txt
%{_bindir}/%{name}
%{_bindir}/%{name}_settings
%{_bindir}/%{name}_setup_and_install
%{_bindir}/qqX.system/*

%changelog
* Sun Dec 31 2023 James Flynn <ayoungdukie_copr@duk13.win> - 1.4.01-1
- Initial with qqX 1.4.01
