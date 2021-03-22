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
BuildRequires: git,rust,cargo,fontconfig-devel,openssl-devel,perl-interpreter,perl-core,libxcb-devel,libxkbcommon-devel,libxkbcommon-x11-devel,wayland-devel,mesa-libEGL-devel,xcb-util-keysyms-devel,xcb-util-image-devel,xcb-util-wm-devel,redhat-lsb-core
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
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/usr/share/icons/hicolor/128x128/apps
mkdir -p %{buildroot}/usr/share/applications
# prepare desktop and icon files
cp ./assets/wezterm.appdata.xml ./org.wezfurlong.wezterm.appdata.xml
# place additional asset files
cp ./assets/icon/terminal.png %{buildroot}/usr/share/icons/hicolor/128x128/apps/org.wezfurlong.wezterm.png
cp ./assets/shell-integration/wezterm.sh %{buildroot}/etc/profile.d/wezterm.sh
# place .desktop and additional binary files
cp ./target/release/%{name}-gui %{buildroot}/usr/bin/%{name}-gui
cp ./target/release/%{name}-mux-server %{buildroot}/usr/bin/%{name}-mux-server
cp ./target/release/strip-ansi-escapes %{buildroot}/usr/bin/strip-ansi-escapes
cp ./assets/wezterm.desktop %{buildroot}/usr/share/applications/org.wezfurlong.wezterm.desktop

%install
install -Dm 0755 ./target/release/%{name} %{buildroot}%{_bindir}/%{name}


%files
/usr/bin/%{name}-gui
/usr/bin/%{name}-mux-server
/usr/bin/strip-ansi-escapes
/usr/share/applications/org.wezfurlong.wezterm.desktop
/etc/profild.d/wezterm.sh
/usr/share/icons/hicolor/128x128/apps/org.wezfurlong.wezterm.png
%{_metainfodir} org.wezfurlong.wezterm.appdata.xml
%defattr(-,root,root,-)
%doc README.md
%license LICENSE.md
%{_bindir}/%{name}

%changelog
* Sun Mar 21 2021 James Flynn <ayoungdukie_copr@duk13.win> - %{version}-1
- Initial with wezterm 20210314-114017-04b7cedd
