%global debug_package %{nil}

Name:    wezterm
Version: 20210314.114017.04b7cedd
Release: 1%{?dist}
Summary: WezTerm - a GPU-accelerated cross-platform terminal emulator and multiplexer written by @wez and implemented in Rust

# %define vtag $(echo "$(tr '.' '-' <<< %{version})")
%define vtag %(echo "$( sed 's/.*= //' <<< "appVersion = 20210314-114017-04b7cedd" )")
# %define dltag %(echo "$( sed 's/.*= //' <<< "appVersion = 20210314_114017_04b7cedd" )")
# %define Version %{vtag}

Group:   System Environment/Shells
License: MIT
URL:     https://github.com/wez/wezterm
Source0: https://github.com/wez/wezterm/archive/%{vtag}/wezterm-%{vtag}.tar.gz
BuildRequires: freetype,rust,cargo,fontconfig-devel,openssl-devel,perl-interpreter,perl-core,libxcb-devel,libxkbcommon-devel,libxkbcommon-x11-devel,wayland-devel,mesa-libEGL-devel,xcb-util-keysyms-devel,xcb-util-image-devel,xcb-util-wm-devel,redhat-lsb-core
Requires: openssl

%description
A GPU-accelerated cross-platform terminal emulator and multiplexer written by @wez and implemented in Rust

%prep

%setup -q -n %{name}-%{vtag}

%build
mkdir -p ./_build/src/github.com/wez
ln -s $(pwd) ./_build/src/github.com/wez/%{name}
cargo build --release
# make generate

%install
install -Dm 0755 ./target/release/%{name} %{buildroot}%{_bindir}/%{name}
# dnf install -y %{source0}

%files
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
* Sat Mar 20 2021 James Flynn <ayoungdukie_copr@duk13.win> - 20210314-114017-04b7cedd-1
- Initial with wezterm 20210314-114017-04b7cedd
