%global debug_package %{nil}

Name:    elvish
Version: 0.16.0
Release: 1%{?dist}
Summary: Elvish - A friendly and expressive Unix shell

Group:   System Environment/Shells
License: BSD 2-Clause
URL:     https://github.com/elves/%{name}
Source0: https://dl.elv.sh/linux-amd64/%{name}-v%{version}.tar.gz

# I would like to thank the Fedora Chinese Community (FZUG) and their work on the spec file (https://github.com/FZUG/repo/blob/master/rpms/elvish/elvish.spec)
# which formed the basis of this file. More info can be found at http://zh.fedoracommunity.org/repo/

%description
Elvish aims to explore the potentials of the Unix shell. It is a work in progress; things will change without warning. 

%prep

%setup -q -c

%build
#get files for install
curl -LJO %{URL}/blob/v{%version}/README.md
curl -LJO %{URL}/blob/v{%version}/LICENSE
mv %{name}-v%{version} %{name}

%install
install -Dm 0755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
* Tue Apr 12 2022 James Flynn <ayoungdukie_copr@duk13.win> - 0.16.0-1
- Rebase on source binaries
* Wed May 5 2021 James Flynn <ayoungdukie_copr@duk13.win> - 0.15.0-2
- Rebase on source binaries
* Mon Mar 8 2021 James Flynn <ayoungdukie_copr@duk13.win> - 0.15.0-1
- Initial with elvish-0.15.0
