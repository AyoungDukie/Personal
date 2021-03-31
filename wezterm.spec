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
# locate files for install
mkdir -p %{buildroot}/etc/profile.d
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_metainfodir}
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/128x128/apps
# prepare desktop and icon files
%define mybuild $(pwd)
cp %{mybuild}/assets/icon/terminal.png %{buildroot}/%{_datadir}/icons/hicolor/128x128/apps/org.wezfurlong.wezterm.png
cp %{mybuild}/assets/wezterm.desktop ./org.wezfurlong.wezterm.desktop
# place apddata nd integration files
cp %{mybuild}/assets/wezterm.appdata.xml %{buildroot}%{_metainfodir}/org.wezfurlong.wezterm.appdata.xml
cp %{mybuild}/assets/shell-integration/wezterm.sh %{buildroot}/etc/profile.d/wezterm.sh
# place additional binary afiles
cp %{mybuild}/target/release/%{name}-gui ./%{name}-gui
cp %{mybuild}/target/release/%{name}-mux-server ./%{name}-mux-server
cp %{mybuild}/target/release/strip-ansi-escapes ./strip-ansi-escapes

%install
install -Dpm 0644 org.wezfurlong.wezterm.desktop %{buildroot}%{_datadir}/applications/org.wezfurlong.wezterm.desktop
install -Dm 0755 ./target/release/%{name} %{buildroot}%{_bindir}/%{name}
install -Dm 0755 %{name}-gui %{buildroot}%{_bindir}/%{name}-gui
install -Dm 0755 %{name}-mux-server %{buildroot}%{_bindir}/%{name}-mux-server
install -Dm 0755 strip-ansi-escapes %{buildroot}%{_bindir}/strip-ansi-escapes

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.wezfurlong.wezterm.desktop

%files
%defattr(0644,root,root)
%license LICENSE.md
%doc README.md
%dir {_datadir}
%{_datadir}/applications/org.wezfurlong.wezterm.desktop
%{_datadir}/icons/hicolor/128x128/apps/org.wezfurlong.wezterm.png
%{_metainfodir}/org.wezfurlong.wezterm.appdata.xml
/etc/profild.d/wezterm.sh
%{_bindir}/%{name}
%{_bindir}/%{name}-gui
%{_bindir}/%{name}-mux-server
%{_bindir}/strip-ansi-escapes

%changelog
* Tue Mar 30 2021 James Flynn <ayoungdukie_copr@duk13.win> - %{version}-1
- Initial with wezterm 20210314-114017-04b7cedd
