%global debug_package %{nil}

%define vtag 20230712-072601-f4abf8fd

Name:    wezterm
Version: %(echo "$(tr '-' '.' <<< %{vtag})")
Release: 1%{?dist}
Summary: WezTerm - a GPU-accelerated cross-platform terminal emulator and multiplexer written by @wez and implemented in Rust
Group:   System Environment/Shells
License: MIT
URL:     https://github.com/wez/%{name}
Source0: https://github.com/wez/%{name}/releases/download/%{vtag}/%{name}-%{vtag}.Ubuntu20.04.tar.xz
BuildRequires: desktop-file-utils
Requires: openssl
%description
A GPU-accelerated cross-platform terminal emulator and multiplexer written by @wez and implemented in Rust
%prep
%setup -q -c
%build
# pull fresh License and README Files
curl -LJO %{URL}/blob/v%{vtag}/LICENSE.md
curl -LJO %{URL}/blob/v%{vtag}/README.md
%install
# Prepare asset files
mkdir -p %{buildroot}/etc/profile.d
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_metainfodir}
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/128x128/apps
cd %{name}
ls
mv ./usr/share/icons/hicolor/128x128/apps/org.wezfurlong.wezterm.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/org.wezfurlong.wezterm.png
mv ./usr/share/metainfo/org.wezfurlong.wezterm.appdata.xml %{buildroot}%{_metainfodir}/org.wezfurlong.wezterm.appdata.xml
# install binaries, desktop file
install -Dpm 0644 ./etc/profile.d/wezterm.sh %{buildroot}/etc/profile.d/wezterm.sh
install -Dpm 0644 ./usr/share/applications/org.wezfurlong.wezterm.desktop %{buildroot}%{_datadir}/applications/org.wezfurlong.wezterm.desktop
install -Dm 0755 ./usr/bin/%{name} %{buildroot}%{_bindir}/%{name}
install -Dm 0755 ./usr/bin/%{name}-gui %{buildroot}%{_bindir}/%{name}-gui
install -Dm 0755 ./usr/bin/%{name}-mux-server %{buildroot}%{_bindir}/%{name}-mux-server
install -Dm 0755 ./usr/bin/strip-ansi-escapes %{buildroot}%{_bindir}/strip-ansi-escapes
%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.wezfurlong.wezterm.desktop
%files
%defattr(-,root,root,-)
%license LICENSE.md
%doc README.md
%dir %{_datadir}
%{_datadir}/applications/org.wezfurlong.wezterm.desktop
%{_datadir}/icons/hicolor/128x128/apps/org.wezfurlong.wezterm.png
%{_metainfodir}/org.wezfurlong.wezterm.appdata.xml
/etc/profile.d/wezterm.sh
%{_bindir}/%{name}
%{_bindir}/%{name}-gui
%{_bindir}/%{name}-mux-server
%{_bindir}/strip-ansi-escapes

%changelog
* Sun Aug 6 2023 James Flynn <ayoungdukie_copr@duk13.win> - 20230712.072601.f4abf8fd-1
- Update to wezterm 20230712-072601-f4abf8fd 
* Sun Aug 6 2023 James Flynn <ayoungdukie_copr@duk13.win> - 20230408.112425.69ae8472-1
- Update to wezterm 20230408-112425-69ae8472 
* Sun Aug 6 2023 James Flynn <ayoungdukie_copr@duk13.win> - 20230326.111934.3666303c-1
- Update to wezterm 20230326-111934-3666303c 
* Sun Aug 6 2023 James Flynn <ayoungdukie_copr@duk13.win> - 20230320.124340.559cb7b0-1
- Update to wezterm 20230320-124340-559cb7b0 
* Sat Dec 31 2022 James Flynn <ayoungdukie_copr@duk13.win> - 20221119.145034.49b9839f-1
- Update to wezterm 20221119-145034-49b9839f
* Tue Sep 6 2022 James Flynn <ayoungdukie_copr@duk13.win> - 20220905.102802.7d4b8249-1
- Update to wezterm 20220905-102802-7d4b8249 
* Mon Aug 8 2022 James Flynn <ayoungdukie_copr@duk13.win> - 20220807.113146.c2fee766-1
- Update to wezterm 20220807-113146-c2fee766
* Sun Jun 26 2022 James Flynn <ayoungdukie_copr@duk13.win> - 20220624.141144.bd1b7c5d-1
- Update to wezterm 20220624-141144-bd1b7c5d
* Tue Apr 12 2022 James Flynn <ayoungdukie_copr@duk13.win> - 20220408.101518.b908e2dd-1
- Update to wezterm 20220408-101518-b908e2dd
* Sun Mar 20 2022 James Flynn <ayoungdukie_copr@duk13.win> - 20220319.142410.0fcdea07-1
- Update to wezterm 20220319-142410-0fcdea07
* Sat Jan 1 2022 James Flynn <ayoungdukie_copr@duk13.win> - 20220101.133340.7edc5b5a-1
- Update to wezterm 20220101-133340-7edc5b5a
* Mon Dec 6 2021 James Flynn <ayoungdukie_copr@duk13.win> - 20211205.192649.672c1cc1-1
- Update to wezterm 20211205-192649-672c1cc1
* Mon Dec 6 2021 James Flynn <ayoungdukie_copr@duk13.win> - 20210814.124438.54e29167-2
- Switch source for build to latest LTS version.
* Mon Aug 16 2021 James Flynn <ayoungdukie_copr@duk13.win> - 20210814.124438.54e29167-1
- Update to wezterm 20210814-124438-54e29167
* Tue May 4 2021 James Flynn <ayoungdukie_copr@duk13.win> - 20210502.154244.3f7122cb-1
- Updated with wezterm 20210405-110924-a5bb5be8 and rebased on source binaries
* Sat May 1 2021 James Flynn <ayoungdukie_copr@duk13.win> - 20210405.110924.a5bb5be8-1
- Updated with wezterm 20210405-110924-a5bb5be8 and rebased on source binaries
* Thu Apr 1 2021 James Flynn <ayoungdukie_copr@duk13.win> - 20210314.114017.04b7cedd-1
- Initial with wezterm 20210314-114017-04b7cedd
