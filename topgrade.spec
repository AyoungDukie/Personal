%global debug_package %{nil}

Name:    topgrade
Version: 7.1.0
Release: 1%{?dist}
Summary: Topgrade - Invoke the upgrade procedure of multiple package managers

Group:   System Environment/Shells
License: GPLv3
URL:     https://github.com/r-darwish/%{name}
Source0: https://github.com/r-darwish/%{name}/releases/download/v%{version}/%{name}-v%{version}-x86_64-unknown-linux-gnu.tar.gz
BuildRequires: cargo

%description
Keeping your system up to date mostly involves invoking more than a single package manager. This usually results in big shell one-liners saved in your shell history. Topgrade tries to solve this problem by detecting which tools you use and run their appropriate package managers. 

%prep
%setup -q -c

%build
curl -LJO %{URL}/blob/v{%version}/README.md
curl -LJO %{URL}/blob/v{%version}/LICENSE

%install
install -Dm 0755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
* Mon Aug 16 2021 James Flynn <ayoungdukie_copr@duk13.win> - 7.1.0-1
- Update to topgrade-7.1.0
* Mon May 10 2021 James Flynn <ayoungdukie_copr@duk13.win> - 6.9.0-1
- Update to 6.9.0
* Sun May 2 2021 James Flynn <ayoungdukie_copr@duk13.win> - 6.8.0-1
- Update to 6.8.0, rebase on source binaries
* Mon Mar 8 2021 James Flynn <ayoungdukie_copr@duk13.win> - 6.7.0-1
- Initial with topgrade 6.7.0
