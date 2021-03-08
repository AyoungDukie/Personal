%global debug_package %{nil}

Name:    topgrade
Version: 6.7.0
Release: 1%{?dist}
Summary: Topgrade - Invoke the upgrade procedure of multiple package managers

Group:   System Environment/Shells
License: GPLv3
URL:     https://github.com/r-darwish/topgrade
Source0: https://github.com/r-darwish/topgrade/archive/v%{version}/topgrade-v%{version}.tar.gz
BuildRequires: rust
BuildRequires: cargo

%description
Keeping your system up to date mostly involves invoking more than a single package manager. This usually results in big shell one-liners saved in your shell history. Topgrade tries to solve this problem by detecting which tools you use and run their appropriate package managers. 

%prep
%setup -q -n %{name}-%{version}

%build
mkdir -p ./_build/src/github.com/r-darwish
ln -s $(pwd) ./_build/src/github.com/r-darwish/%{name}
cargo run %{name}
#make generate

%install
install -Dm 0755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
* Mon Mar 8 2021 James Flynn <ayoungdukie_copr@duk13.win> - 6.7.0-1
- Initial with topgrade 6.7.0
