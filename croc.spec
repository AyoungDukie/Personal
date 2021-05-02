%global debug_package %{nil}

Name:    croc
Version: 9.1.1
Release: 1%{?dist}
Summary: croc - secure and easy data transfer

Group:   System Environment/Shells
License: MIT
URL:     https://github.com/schollz/%{name}
Source0: https://github.com/schollz/%{name}/releases/download/v%{version}/%{name}_%{version}_Linux-64bit.tar.gz

%description
croc is a tool that allows any two computers to simply and securely transfer files and folders

%prep

%setup -q -n %{name}-%{version}

%build
# set up file locations
mkdir -p ./_build/src/github.com/schollz/%{name}
ls
ln -s $(pwd) ./_build/src/github.com/schollz/%{name}
# Download fresh tarball and extract
# curl -LJO "https://github.com/schollz/%{name}/releases/download/v%{version}/%{name}_%{version}_Linux-64bit.tar.gz"
# tar -xvzf %{name}_%{version}_Linux-64bit.tar.gz -C ./_build/src/github.com/schollz/%{name}

%install
# setup final installation
mkdir -p %{buildroot}%{_bindir}
# Install Files
# cp -a ./_build/src/github.com/schollz/%{name}/. .
install -Dm 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dm 0755 bash_autocomplete %{buildroot}%{_bindir}/%{name}
install -Dm 0755 zsh_autocomplete %{buildroot}%{_bindir}/%{name}

%files
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
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
