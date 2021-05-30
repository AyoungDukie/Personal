%global debug_package %{nil}

%define binType Linux-64bit

Name:    croc
Version: 9.1.4
Release: 1%{?dist}
Summary: croc - secure and easy data transfer

Group:   System Environment/Shells
License: MIT
URL:     https://github.com/schollz/%{name}
Source0: https://github.com/schollz/%{name}/releases/download/v%{version}/%{name}_%{version}_%{binType}.tar.gz

%description
croc is a tool that allows any two computers to simply and securely transfer files and folders

%prep

%setup -q -c

%build

%install
# get checksums
# curl -LJO %{URL}/blob/releases/download/v%{version}/%{name}_%{version}_checksums.txt

# setup final installation
mkdir -p %{buildroot}%{_bindir}
# Install Files
install -Dm 0644 %{name} %{buildroot}%{_bindir}/%{name}
install -Dm 0755 bash_autocomplete %{buildroot}%{_bindir}/%{name}
install -Dm 0755 zsh_autocomplete %{buildroot}%{_bindir}/%{name}

%files
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
* Thu May 13 2021 James Flynn <ayoungdukie_copr@duk13.win> - 9.1.4-1
- Update to croc-9.1.4
* Tue May 11 2021 James Flynn <ayoungdukie_copr@duk13.win> - 9.1.3-1
- Update to croc-9.1.3
* Mon May 10 2021 James Flynn <ayoungdukie_copr@duk13.win> - 9.1.2-1
- Update to croc-9.1.2
* Sat May 1 2021 James Flynn <ayoungdukie_copr@duk13.win> - 9.1.1-1
- Update to croc-9.1.1
* Tue Apr 20 2021 James Flynn <ayoungdukie_copr@duk13.win> - 9.1.0-1
- Update to croc-9.1.0
* Mon Apr 19 2021 James Flynn <ayoungdukie_copr@duk13.win> - 9.0.0-1
- Update to croc-9.0.0
* Fri Mar 26 2021 James Flynn <ayoungdukie_copr@duk13.win> - 8.6.12-1
- Update to croc-8.6.12
* Sun Mar 21 2021 James Flynn <ayoungdukie_copr@duk13.win> - 8.6.11-1
- Initial with croc-8.6.11
