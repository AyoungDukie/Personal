%global debug_package %{nil}

Name:    croc
Version: 9.5.2
Release: 1%{?dist}
Summary: croc - secure and easy data transfer

Group:   System Environment/Shells
License: MIT
URL:     https://github.com/schollz/%{name}
Source0: https://github.com/schollz/%{name}/archive/v%{version}/%{name}-v%{version}.tar.gz
BuildRequires: git,golang-bin
%description
croc is a tool that allows any two computers to simply and securely transfer files and folders
%prep
%setup -q -n %{name}-%{version}
%build
mkdir -p ./_build/src/github.com/schollz
ln -s $(pwd) ./_build/src/github.com/schollz/%{name}
export GOPATH=$(pwd)/_build:%{gopath}
go build -o %{name}
%install
install -Dm 0755 %{name} %{buildroot}%{_bindir}/%{name}
%files
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
* Sat Mar 12 2022 James Flynn <ayoungdukie_copr@duk13.win> - 9.5.2-1
- Update to croc-9.5.2
* Tue Feb 8 2022 James Flynn <ayoungdukie_copr@duk13.win> - 9.5.1-1
- Update to croc-9.5.1
* Thu Nov 18 2021 James Flynn <ayoungdukie_copr@duk13.win> - 9.5.0-1
- Update to croc-9.5.0
* Mon Oct 11 2021 James Flynn <ayoungdukie_copr@duk13.win> - 9.4.2-1
- Update to croc-9.4.2
* Mon Aug 16 2021 James Flynn <ayoungdukie_copr@duk13.win> - 9.3.0-1
- Update to croc-9.3.0
* Mon Aug 16 2021 James Flynn <ayoungdukie_copr@duk13.win> - 9.2.1-1
- Update to croc-9.2.1
* Thu May 13 2021 James Flynn <ayoungdukie_copr@duk13.win> - 9.1.4-1
- Update to croc-9.1.4
* Fri Mar 26 2021 James Flynn <ayoungdukie_copr@duk13.win> - 8.6.12-1
- Update to croc-8.6.12
* Sun Mar 21 2021 James Flynn <ayoungdukie_copr@duk13.win> - 8.6.11-1
- Initial with croc-8.6.11
