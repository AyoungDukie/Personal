%global debug_package %{nil}

Name:    wezterm
Version: 20210314.114017.04b7cedd
Release: 1%{?dist}
Summary: WezTerm - a GPU-accelerated cross-platform terminal emulator and multiplexer written by @wez and implemented in Rust

%define version $(echo "$(tr '.' '-' <<< %{version})")

Group:   System Environment/Shells
License: MIT
URL:     https://github.com/wez/wezterm
Source0: https://github.com/wez/wezterm/archive/%{version}/topgrade-v%{version}.tar.gz
BuildRequires: rust,cargo,make,gcc,gcc-c++,fontconfig-devel,openssl-devel,perl-interpreter,python3,libxcb-devel,libxkbcommon-devel,libxkbcommon-x11-devel,wayland-devel,mesa-libegl-devel,xcb-util-keysyms-devel,xcb-util-image-devel,xcb-util-wm-devel,rpm-build,redhat-lsb-core
Requires: dbus,fontconfig,libx11,libxkbcommon-x11,wayland,xcb-util-keysyms,xcb-util-wm

%description
A GPU-accelerated cross-platform terminal emulator and multiplexer written by @wez and implemented in Rust

%prep

%setup -q -n %{name}-%{version}

%build
mkdir -p ./_build/src/github.com/wez
ln -s $(pwd) ./_build/src/github.com/wez/%{name}
cargo build --release
#make generate

%install
install -Dm 0755 ./target/release/%{name} %{buildroot}%{_bindir}/%{name}

%files
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
* Mon Mar 16 2021 James Flynn <ayoungdukie_copr@duk13.win> - %{version}-1
- Initial with wezterm %{version}
