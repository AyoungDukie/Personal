%global debug_package %{nil}

%define repoauth quickemu-project

Name:    quickemu
Version: 4.9.6
Release: 1%{?dist}
Summary: quickemu - Quickly create and run optimised Windows, macOS and Linux desktop virtual machines.

Group:   System Environment/Shells
License: MIT
URL:     https://github.com/%{repoauth}/%{name}
Source0: https://github.com/%{repoauth}/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires: git
Requires: qemu,bash,coreutils,edk2-tools,grep,jq,lsb,procps,python3,genisoimage,usbutils,util-linux,sed,spice-gtk-tools,swtpm,wget,xdg-user-dirs,xrandr,unzip,pciutils
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
install -Dm 0755 quickreport %{buildroot}%{_bindir}/quickreport
install -Dm 0755 chunkcheck %{buildroot}%{_bindir}/chunkcheck
install -Dm 0755 windowskey %{buildroot}%{_bindir}/windowskey

%preun
if %{_bindir}/macrecovery; then
  rm -f %{_bindir}/macrecovery
fi

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
%{_bindir}/quickreport
%{_bindir}/chunkcheck
%{_bindir}/windowskey

%changelog
* Sun Jul 7 2024 James Flynn <ayoungdukie_copr@duk13.win> - 4.9.6-1
- Update to quickemu-4.9.6
* Sun Jul 7 2024 James Flynn <ayoungdukie_copr@duk13.win> - 4.9.5-1
- Update to quickemu-4.9.5
* Sun Jul 7 2024 James Flynn <ayoungdukie_copr@duk13.win> - 4.9.4-2
- Update to quickemu-4.9.4 fix binary naming issue
* Sun Jul 7 2024 James Flynn <ayoungdukie_copr@duk13.win> - 4.9.3-2
- Update to quickemu-4.9.3 fix binary naming issue
* Sun Jul 7 2024 James Flynn <ayoungdukie_copr@duk13.win> - 4.9.4-1
- Update to quickemu-4.9.4 
* Sun Jul 7 2024 James Flynn <ayoungdukie_copr@duk13.win> - 4.9.3-1
- Update to quickemu-4.9.3 (+quickreport, +chunkcheck, -macrecovery)
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
