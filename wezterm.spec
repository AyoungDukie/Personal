%global debug_package %{nil}

Name:    wezterm
Version: 20210314.114017.04b7cedd
Release: 1%{?dist}
Summary: WezTerm - a GPU-accelerated cross-platform terminal emulator and multiplexer written by @wez and implemented in Rust

%define vtag %(echo "$(tr '.' '-' <<< %{version})")

Group:   System Environment/Shells
License: MIT
URL:     https://github.com/wez/wezterm
Source0: https://github.com/wez/wezterm/releases/download/%{vtag}/wezterm-%{vtag}-src.tar.gz
BuildRequires: git,desktop-file-utils,rust,cargo,fontconfig-devel,openssl-devel,perl-interpreter,perl-core,libxcb-devel,libxkbcommon-devel,libxkbcommon-x11-devel,wayland-devel,mesa-libEGL-devel,xcb-util-keysyms-devel,xcb-util-image-devel,xcb-util-wm-devel,redhat-lsb-core
Requires: openssl

%description
A GPU-accelerated cross-platform terminal emulator and multiplexer written by @wez and implemented in Rust

%prep
%setup -q -n %{name}-%{vtag}

%build
mkdir -p ./_build/src/github.com/wez
ln -s $(pwd) ./_build/src/github.com/wez/%{name}
cargo build --release
%define mybuild $(pwd)
# locate files for install
cp %{mybuild}/assets/icon/terminal.png ./org.wezfurlong.wezterm.png
cp %{mybuild}/assets/wezterm.desktop ./org.wezfurlong.wezterm.desktop
cp %{mybuild}/assets/wezterm.appdata.xml ./org.wezfurlong.wezterm.appdata.xml
cp %{mybuild}/assets/shell-integration/wezterm.sh ./wezterm.sh

%install
# place asset files
mkdir -p %{buildroot}/etc/profile.d
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_metainfodir}
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/128x128/apps
mv org.wezfurlong.wezterm.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/org.wezfurlong.wezterm.png
mv org.wezfurlong.wezterm.appdata.xml %{buildroot}%{_metainfodir}/org.wezfurlong.wezterm.appdata.xml
# install binaries, desktop file
install -Dpm 0644 wezterm.sh %{buildroot}/etc/profile.d/wezterm.sh
install -Dpm 0644 org.wezfurlong.wezterm.desktop %{buildroot}%{_datadir}/applications/org.wezfurlong.wezterm.desktop
install -Dm 0755 ./target/release/%{name} %{buildroot}%{_bindir}/%{name}
install -Dm 0755 ./target/release/%{name}-gui %{buildroot}%{_bindir}/%{name}-gui
install -Dm 0755 ./target/release/%{name}-mux-server %{buildroot}%{_bindir}/%{name}-mux-server
install -Dm 0755 ./target/release/strip-ansi-escapes %{buildroot}%{_bindir}/strip-ansi-escapes

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.wezfurlong.wezterm.desktop

%files
%defattr(0644,root,root)
%license LICENSE.md
%doc README.md
%dir %{_datadir}
%dir /etc/profile.d
%{_datadir}/applications/org.wezfurlong.wezterm.desktop
%{_datadir}/icons/hicolor/128x128/apps/org.wezfurlong.wezterm.png
%{_metainfodir}/org.wezfurlong.wezterm.appdata.xml
/etc/profild.d/wezterm.sh
%{_bindir}/%{name}
%{_bindir}/%{name}-gui
%{_bindir}/%{name}-mux-server
%{_bindir}/strip-ansi-escapes

%changelog
* Thu Apr 1 2021 James Flynn <ayoungdukie_copr@duk13.win> - %{version}-1
- Initial with wezterm 20210314-114017-04b7cedd
