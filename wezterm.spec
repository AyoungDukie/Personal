%global debug_package %{nil}

Name:    wezterm
Version: 20210405.110924.a5bb5be8
Release: 1%{?dist}
Summary: WezTerm - a GPU-accelerated cross-platform terminal emulator and multiplexer written by @wez and implemented in Rust

%define vtag %(echo "$(tr '.' '-' <<< %{version})")

Group:   System Environment/Shells
License: MIT
URL:     https://github.com/wez/%{name}
Source0: https://github.com/wez/%{name}/releases/download/%{vtag}/%{name}-%{vtag}.Ubuntu16.04.tar.xz
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
* Sat May 1 2021 James Flynn <ayoungdukie_copr@duk13.win> - 20210405-110924-a5bb5be8-1
- Updated with wezterm 20210405-110924-a5bb5be8 and rebased on source binaries
* Thu Apr 1 2021 James Flynn <ayoungdukie_copr@duk13.win> - 20210314.114017.04b7cedd-1
- Initial with wezterm 20210314-114017-04b7cedd
