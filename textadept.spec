%global debug_package %{nil}

Name:           textadept
Version:        11.3
Release:        1%{?dist}
Summary:        Textadept is a fast, minimalist, and remarkably extensible cross-platform text editor.

License:        MIT
URL:            https://orbitalquark.github.io/textadept/
Source0:        https://github.com/orbitalquark/%{name}/releases/download/%{name}_%{version}/%{name}_%{version}.linux.tgz

BuildRequires:  gcc-c++
BuildRequires:  libstdc++
BuildRequires:  gtk2-devel
BuildRequires:  ncurses-devel
BuildRequires:  wget   

%description
Textadept is a fast, minimalist, and remarkably extensible cross-platform text editor for programmers. Written in a combination of C and Lua and relentlessly optimized for speed and minimalism over the years, Textadept is an ideal editor for programmers who want endless extensibility without sacrificing speed or succumbing to code bloat and featuritis.

%prep
%setup -q -n %{name}-d40c3fab6fb4

%build
make deps -C src
make -C src
make curses -C src

%install
install -d $RPM_BUILD_ROOT/opt/%{name}
cp -r core doc modules scripts themes $RPM_BUILD_ROOT/opt/%{name}
cp -r src/scintilla/lexlua $RPM_BUILD_ROOT/opt/%{name}/lexers
cp init.lua $RPM_BUILD_ROOT/opt/%{name}
install -D -m 0755 %{name} $RPM_BUILD_ROOT/opt/%{name}/%{name}
install -D -m 0755 %{name}-curses $RPM_BUILD_ROOT/opt/%{name}/%{name}-curses
install -d $RPM_BUILD_ROOT%{_bindir}
ln -s /opt/%{name}/%{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
ln -s /opt/%{name}/%{name}-curses $RPM_BUILD_ROOT%{_bindir}/%{name}-curses
install -D -m 0644 src/%{name}.desktop $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
install -D -m 0644 src/%{name}-curses.desktop $RPM_BUILD_ROOT%{_datadir}/applications/%{name}-curses.desktop
rm $RPM_BUILD_ROOT/opt/%{name}/core/images/ta_32x32.ico
rm $RPM_BUILD_ROOT/opt/%{name}/core/images/textadept.icns
rm $RPM_BUILD_ROOT/opt/%{name}/core/images/textadept.ico
install -d $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps
ln -s /opt/%{name}/core/images/ta_16x16.png \
      $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/textadept.png
install -d $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
ln -s /opt/%{name}/core/images/ta_32x32.png \
      $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/textadept.png
install -d $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
ln -s /opt/%{name}/core/images/ta_48x48.png \
      $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/textadept.png
install -d $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
ln -s /opt/%{name}/core/images/ta_64x64.png \
      $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps/textadept.png
install -d $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
ln -s /opt/%{name}/core/images/ta_128x128.png \
      $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps/textadept.png
install -d $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/256x256/apps
ln -s /opt/%{name}/core/images/ta_256x256.png \
      $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/256x256/apps/textadept.png
install -d $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps
ln -s /opt/%{name}/core/images/textadept.svg \
      $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps/textadept.svg

%files
%doc CHANGELOG.md FAQ.md MEDIA.md README.md TECHNOLOGY.md THANKS.md doc/*
%license LICENSE
/opt/%{name}
%{_bindir}/%{name}
%{_bindir}/%{name}-curses
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-curses.desktop
%{_datadir}/icons/hicolor/16x16/apps/textadept.png
%{_datadir}/icons/hicolor/32x32/apps/textadept.png
%{_datadir}/icons/hicolor/48x48/apps/textadept.png
%{_datadir}/icons/hicolor/64x64/apps/textadept.png
%{_datadir}/icons/hicolor/128x128/apps/textadept.png
%{_datadir}/icons/hicolor/256x256/apps/textadept.png
%{_datadir}/icons/hicolor/scalable/apps/textadept.svg

%changelog
* Fri Mar 20 2020 Aku3 <akuzeru3 at gmail.com> - 10.8
- First release
