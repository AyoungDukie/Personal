%global debug_package %{nil}

Name:    elvish
Version: 0.15.0
Release: 1%{?dist}
Summary: Elvish - A friendly and expressive Unix shell

Group:   System Environment/Shells
License: BSD 2-Clause
URL:     https://github.com/elves/elvish
Source0: https://github.com/elves/elvish/archive/v%{version}/elvish-v%{version}.tar.gz
BuildRequires: git,golang-bin,golang-x-tools-stringer

# I would like to thank the Fedora Chinese Community (FZUG) and their work on the spec file (https://github.com/FZUG/repo/blob/master/rpms/elvish/elvish.spec)
# which formed the basis of this file. More info can be found at http://zh.fedoracommunity.org/repo/

%description
Elvish aims to explore the potentials of the Unix shell. It is a work in progress; things will change without warning. 

%prep
%setup -q -n %{name}-%{version}

%build
mkdir -p ./_build/src/github.com/elves
ln -s $(pwd) ./_build/src/github.com/elves/elvish
export GOPATH=$(pwd)/_build:%{gopath}
go build -o elvish
#make generate

%install
install -Dm 0755 elvish %{buildroot}%{_bindir}/elvish

%files
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
%{_bindir}/elvish

%changelog
* Mon Mar 8 2021 James Flynn <ayoungdukie_copr@duk13.win> - 0.15.0-1
- Initial with elvish-0.15.0
