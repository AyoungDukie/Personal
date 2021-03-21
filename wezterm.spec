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

%pre
cp ./assets/wezterm.desktop ./org.wezfurlong.wezterm.desktop

%install
install -Dm 0755 ./target/release/%{name} %{buildroot}%{_bindir}/%{name}
install -Dm 0755 ./target/release/%{name}-gui %{buildroot}%{_bindir}/%{name}
install -Dm 0755 ./target/release/%{name}-mux-server %{buildroot}%{_bindir}/%{name}
install -Dm 0755 ./target/release/strip-ansi-escapes %{buildroot}%{_bindir}/%{name}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications org.wezfurlong.wezterm.desktop

%files
%defattr(-,root,root,-)
%doc README.md
%license LICENSE.md
%{_bindir}/%{name}

%changelog
* Sun Mar 21 2021 James Flynn <ayoungdukie_copr@duk13.win> - %{version}-1
- Initial with wezterm 20210314-114017-04b7cedd
