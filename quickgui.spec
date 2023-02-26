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
patchelf  .build/linux/x64/release/bundle/lib/libwindow_size_plugin.so  --set-rpath "\$ORIGIN"
patchelf  .build/linux/x64/release/bundle/lib/liburl_launcher_linux_plugin.so  --set-rpath "\$ORIGIN"

%install
# preallocate folders
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_datadir}/tmp
# place assets
%define bpath $(pwd)
mv ./assets/resources/%{name}.desktop ./assets/%{name}.desktop
install -Dpm 0644 ./assets/%{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
mv ./assets/resources/* %{buildroot}%{_datadir}/pixmaps/
cp -pr ./build/linux/x64/release/bundle/ %{buildroot}%{_datadir}/tmp
rm -rf ./build
rm -rf ./lib
rm -rf ./linux
cd %{buildroot}%{_bindir}/..
mkdir ./%{name}
%define flpath $(pwd)/%{name}
install -Dm 0755 %{buildroot}%{_datadir}/tmp/bundle/%{name} %{flpath}/%{name}
mv %{buildroot}%{_datadir}/tmp/bundle/* ./%{name}
#ln -s %{flpath}/%{name} %{buildroot}%{_bindir}/tmp/%{name}
cd %{bpath}
#install -Dm 0755 %{buildroot}%{_bindir}/tmp/%{name} %{buildroot}%{_bindir}/%{name}
rm -rf %{buildroot}%{_datadir}/tmp


%post
if [ $1 == 1 ];then
    sudo ln -s %{flpath}/%{name} %{_bindir}/%{name} 
fi

%postun
if [ $1 == 0 ];then
    sudo rm %{_bindir}/%{name}
fi 

%files
%defattr(-,root,root,-)
%doc README.md
#%{_bindir}/%{name}
%{flpath}/%{name}
%{flpath}/lib/*
%{flpath}/data/*
%{flpath}/data/flutter_assets/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/*

%changelog
* Sun Feb 26 2023 James Flynn <ayoungdukie_copr@duk13.win> - 1.2.8-1
- Initial with quickgui-1.2.8
