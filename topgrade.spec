%global debug_package %{nil}

Name:    topgrade
Version: 16.3.0
Release: 1%{?dist}
Summary: Topgrade - Invoke the upgrade procedure of multiple package managers

Group:   System Environment/Shells
License: GPLv3
URL:     https://github.com/topgrade-rs/%{name}
Source0: https://github.com/topgrade-rs/%{name}/releases/download/v%{version}/%{name}-v%{version}-x86_64-unknown-linux-gnu.tar.gz
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
* Mon Nov 17 2025 James Flynn <ayoungdukie_copr@duk13.win> - 16.3.0-1
- Update to topgrade-16.3.0
* Mon Nov 17 2025 James Flynn <ayoungdukie_copr@duk13.win> - 16.2.1-1
- Update to topgrade-16.2.1
* Mon Nov 17 2025 James Flynn <ayoungdukie_copr@duk13.win> - 16.2.0-1
- Update to topgrade-16.2.0
* Thu Nov 6 2025 James Flynn <ayoungdukie_copr@duk13.win> - 16.1.2-1
- Update to topgrade-16.1.2
* Thu Nov 6 2025 James Flynn <ayoungdukie_copr@duk13.win> - 16.1.1-1
- Update to topgrade-16.1.1
* Thu Nov 6 2025 James Flynn <ayoungdukie_copr@duk13.win> - 16.1.0-1
- Update to topgrade-16.1.0
* Fri Oct 31 2025 James Flynn <ayoungdukie_copr@duk13.win> - 16.0.4-1
- Update to topgrade-16.0.4
* Wed Apr 30 2025 James Flynn <ayoungdukie_copr@duk13.win> - 16.0.3-1
- Update to topgrade-16.0.3
* Wed Apr 30 2025 James Flynn <ayoungdukie_copr@duk13.win> - 16.0.2-1
- Update to topgrade-16.0.2
* Wed Apr 30 2025 James Flynn <ayoungdukie_copr@duk13.win> - 16.0.1-1
- Update to topgrade-16.0.1
* Wed Apr 30 2025 James Flynn <ayoungdukie_copr@duk13.win> - 16.0.0-1
- Update to topgrade-16.0.0
* Mon Jul 8 2024 James Flynn <ayoungdukie_copr@duk13.win> - 15.0.0-1
- Update to topgrade-15.0.0
* Mon Jul 8 2024 James Flynn <ayoungdukie_copr@duk13.win> - 14.0.1-1
- Update to topgrade-14.0.1
* Mon Jul 8 2024 James Flynn <ayoungdukie_copr@duk13.win> - 14.0.0-1
- Update to topgrade-14.0.0
* Sun Jul 7 2024 James Flynn <ayoungdukie_copr@duk13.win> - 13.0.0-1
- Update to topgrade-13.0.0
* Sun Jul 7 2024 James Flynn <ayoungdukie_copr@duk13.win> - 12.0.2-1
- Update to topgrade-12.0.2
* Sun Jul 7 2024 James Flynn <ayoungdukie_copr@duk13.win> - 12.0.1-1
- Update to topgrade-12.0.1
* Tue Jun 27 2023 James Flynn <ayoungdukie_copr@duk13.win> - 12.0.0-1
- Update to topgrade-12.0.0
* Tue Jun 27 2023 James Flynn <ayoungdukie_copr@duk13.win> - 11.0.2-1
- Catchup update to topgrade-11.0.2
* Tue Jun 27 2023 James Flynn <ayoungdukie_copr@duk13.win> - 11.0.1-1
- Catchup update to topgrade-11.0.1
* Tue Jun 27 2023 James Flynn <ayoungdukie_copr@duk13.win> - 11.0.0-1
- Catchup update to topgrade-11.0.0
* Sat Apr 1 2023 James Flynn <ayoungdukie_copr@duk13.win> - 10.3.3-1
- Catchup update to topgrade-10.3.3
* Sat Apr 1 2023 James Flynn <ayoungdukie_copr@duk13.win> - 10.3.2-1
- Catchup update to topgrade-10.3.2
* Sat Apr 1 2023 James Flynn <ayoungdukie_copr@duk13.win> - 10.3.1-1
- Catchup update to topgrade-10.3.1
* Sat Apr 1 2023 James Flynn <ayoungdukie_copr@duk13.win> - 10.3.0-1
- Catchup update to topgrade-10.3.0
* Sat Apr 1 2023 James Flynn <ayoungdukie_copr@duk13.win> - 10.2.6-1
- Catchup update to topgrade-10.2.6
* Sat Dec 31 2022 James Flynn <ayoungdukie_copr@duk13.win> - 10.2.4-1
- Catchup update to topgrade-10.2.4
* Sun Jun 26 2022 James Flynn <ayoungdukie_copr@duk13.win> - 10.0.1-1
- Update to topgrade-10.0.1, via community fork prepared by topgrade-rs
* Sun Jun 26 2022 James Flynn <ayoungdukie_copr@duk13.win> - 9.0.1-1
- Update to topgrade-9.0.1
* Wed May 18 2022 James Flynn <ayoungdukie_copr@duk13.win> - 9.0.0-1
- Update to topgrade-9.0.0
* Tue Apr 12 2022 James Flynn <ayoungdukie_copr@duk13.win> - 8.3.1-1
- Update to topgrade-8.3.1
* Wed Mar 30 2022 James Flynn <ayoungdukie_copr@duk13.win> - 8.3.0-1
- Update to topgrade-8.3.0
* Mon Jan 24 2022 James Flynn <ayoungdukie_copr@duk13.win> - 8.2.0-1
- Update to topgrade-8.2.0
* Thu Dec 16 2021 James Flynn <ayoungdukie_copr@duk13.win> - 8.1.2-1
- Update to topgrade-8.1.2
* Mon Dec 13 2021 James Flynn <ayoungdukie_copr@duk13.win> - 8.1.1-1
- Update to topgrade-8.1.1
* Mon Aug 16 2021 James Flynn <ayoungdukie_copr@duk13.win> - 8.0.3-1
- Update to topgrade-8.0.3
* Mon Aug 16 2021 James Flynn <ayoungdukie_copr@duk13.win> - 7.1.0-1
- Update to topgrade-7.1.0
* Mon May 10 2021 James Flynn <ayoungdukie_copr@duk13.win> - 6.9.0-1
- Update to 6.9.0
* Sun May 2 2021 James Flynn <ayoungdukie_copr@duk13.win> - 6.8.0-1
- Update to 6.8.0, rebase on source binaries
* Mon Mar 8 2021 James Flynn <ayoungdukie_copr@duk13.win> - 6.7.0-1
- Initial with topgrade 6.7.0
