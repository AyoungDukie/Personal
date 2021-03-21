%global debug_package %{nil}

Name:    croc
Version: 8.6.11
Release: 1%{?dist}
Summary: croc - secure and easy data transfer

Group:   System Environment/Shells
License: MIT
URL:     https://github.com/schollz/croc
Source0: https://github.com/elves/elvish/archive/v%{version}/elvish-v%{version}.tar.gz
BuildRequires: golang-bin

# I would like to thank the Fedora Chinese Community (FZUG) and their work on the spec file (https://github.com/FZUG/repo/blob/master/rpms/elvish/elvish.spec)
# which formed the basis of this file. More info can be found at http://zh.fedoracommunity.org/repo/

%description
croc is a tool that allows any two computers to simply and securely transfer files and folders

%prep
%setup -q -n %{name}-%{version}

%build
mkdir -p ./_build/src/github.com/schollz
ln -s $(pwd) ./_build/src/github.com/schollz/%{name}
export GOPATH=$(pwd)/_build:%{gopath}
#go build -o %{name}
GO111MODULE=on go get -v github.com/schollz/croc/v8

%install
install -Dm 0755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
* Sun Mar 21 2021 James Flynn <ayoungdukie_copr@duk13.win> - 8.6.11-1
- Initial with croc-8.6.11
