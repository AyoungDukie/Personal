%global debug_package %{nil}

%define repoauth quickemu-project

Name:    quickgui
Version: 1.2.8
Release: 1%{?dist}
Summary: quickgui - A Flutter frontend for quickget and quickemu.

Group:   System Environment/Shells
License: MIT
URL:     https://github.com/%{repoauth}/%{name}
Source0: https://github.com/%{repoauth}/%{name}/archive/v%{version}/%{name}-v%{version}.tar.gz
BuildRequires: git,snapd
%description
A Flutter frontend for quickget and quickemu.

%prep

%setup -q -n %{name}-%{version}

%build
su -c "ln -s /var/lib/snapd/snap /snap"
su -c "snap install flutter --classic"
su -c "snap alias flutter.dart dart"
flutter config --enable-linux-desktop
flutter config --no-enable-android
mkdir -p ./_build/src/github.com/schollz
ln -s $(pwd) ./_build/src/github.com/%{repoauth}/%{name}
flutter build linux --release

%install
install -Dm 0755 %{name} %{buildroot}%{_bindir}/%{name}/build/linux/x64/release/bundle/%{name}

%files
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
* Sat Feb 18 2023 James Flynn <ayoungdukie_copr@duk13.win> - 1.2.8-1
- Initial with quickgui-1.2.8
