%global debug_package %{nil}

%define repoauth AyoungDukie

Name:    quickgui
Version: 1.2.8
Release: 1%{?dist}
Summary: quickgui - A Flutter frontend for quickget and quickemu.

Group:   System Environment/Shells
License: MIT
URL:     https://github.com/%{repoauth}/%{name}
Source0: https://github.com/%{repoauth}/%{name}/archive/v%{version}/%{name}-v%{version}.tar.gz
BuildRequires: git,gcc,clang,cmake,gtk3-devel,ninja-build,pkg-config,xz-devel
Requires: quickemu
%description
A Flutter frontend for quickget and quickemu.

%prep

%setup -q -n %{name}-%{version}

%build
# Set up Flutter environment
mkdir flutterEnv
cd flutterEnv
git clone https://github.com/flutter/flutter.git -b stable
export PATH="$PATH:$(pwd)/flutter/bin"
flutter config --enable-linux-desktop
flutter config --no-enable-android
flutter config --no-enable-web
cd ..
# Build Binaries
mkdir -p ./_build/src/github.com/%{repoauth}
ln -s $(pwd) ./_build/src/github.com/%{repoauth}/%{name}
flutter build linux --release

%install
# preallocate folders
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_bindir}/../%{name}

# place assets
mv ./assets/resources/quickgui.desktop %{_datadir}/applications/quickgui.desktop
mv ./assets/resources/* %{buildroot}%{_datadir}/pixmaps/
cp -pr ./build/linux/x64/release/bundle/ %{buildroot}%{_bindir}/../%{name}
ln -s %{buildroot}%{_bindir}/../%{name}/%{name} %{buildroot}%{_bindir}/%{name}
install -Dm 0755 %{buildroot}%{_bindir}/../%{name}/%{name} %{buildroot}%{_bindir}/../%{name}/%{name}
install -Dm 0755 %{buildroot}%{_bindir}/%{name} %{buildroot}%{_bindir}/%{name}

%files
%defattr(-,root,root,-)
%doc README.md
%{_bindir}/%{name}
%{_bindir}/../%{name}/%{name}
%{_bindir}/../%{name}/lib/*
%{_bindir}/../%{name}/data/*
%{_bindir}/../%{name}/data/flutter_assets/*
%{_datadir}/applications/quickgui.desktop
%{_datadir}/pixmaps/*

%changelog
* Sat Feb 18 2023 James Flynn <ayoungdukie_copr@duk13.win> - 1.2.8-1
- Initial with quickgui-1.2.8
