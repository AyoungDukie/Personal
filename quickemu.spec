%global debug_package %{nil}

%define repoauth quickemu-project

Name:    quickemu
Version: 4.9.2
Release: 2%{?dist}
Summary: quickemu - Quickly create and run optimised Windows, macOS and Linux desktop virtual machines.

Group:   System Environment/Shells
License: MIT
URL:     https://github.com/%{repoauth}/%{name}
Source0: https://github.com/%{repoauth}/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires: git
Requires: qemu,bash,coreutils,edk2-tools,grep,jq,lsb,procps,python3,genisoimage,usbutils,util-linux,sed,spice-gtk-tools,swtpm,wget,xdg-user-dirs,xrandr,unzip
Recommends: aria2,zsync
%description
Quickly create and run highly optimised desktop virtual machines for Linux, macOS and Windows; with just two commands. You decide what operating system you want to run and Quickemu will figure out the best way to do it for you.

%prep

%setup -q -n %{name}-%{version}

%build
mkdir -p ./_build/src/github.com/%{repoauth}
ln -s $(pwd) ./_build/src/github.com/%{repoauth}/%{name}


%install
# Prepare asset files
mkdir -p %{buildroot}%{_bindir}
install -Dm 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dm 0755 quickget %{buildroot}%{_bindir}/quickget
install -Dm 0755 macrecovery %{buildroot}%{_bindir}/macrecovery
install -Dm 0755 windowskey %{buildroot}%{_bindir}/windowskey

%files
%defattr(-,root,root,-)
%doc README.md
%doc  ./docs/%{name}.1
%doc  ./docs/%{name}.1.md
%doc  ./docs/quickget.1
%doc  ./docs/quickget.1.md
%doc  ./docs/%{name}_conf.1
%doc  ./docs/%{name}_conf.1.md
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/quickget
%{_bindir}/macrecovery
%{_bindir}/windowskey

%changelog
* Wed Jan 3 2024 James Flynn <ayoungdukie_copr@duk13.win> - 4.9.2-2
- Add zsync reccomendation (e.g. from RPMSphere)
* Mon Jan 1 2024 James Flynn <ayoungdukie_copr@duk13.win> - 4.9.2-1
- Update to quickemu-4.9.2
* Mon Jan 1 2024 James Flynn <ayoungdukie_copr@duk13.win> - 4.9.1-1
- Update to quickemu-4.9.1
* Mon Jan 1 2024 James Flynn <ayoungdukie_copr@duk13.win> - 4.9-1
- Update to quickemu-4.9
* Mon Jan 1 2024 James Flynn <ayoungdukie_copr@duk13.win> - 4.8-1
- Update to quickemu-4.8
* Sun Apr 30 2023 James Flynn <ayoungdukie_copr@duk13.win> - 4.7-1
- Update to quickemu-4.7
* Sun Feb 19 2023 James Flynn <ayoungdukie_copr@duk13.win> - 4.6-1
- Initial with quickemu-4.6
