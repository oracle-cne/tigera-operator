

%global debug_package %{nil}
%global git_short_ver $(git rev-parse --short HEAD)
%global build_dir src/github.com/projectcalico/calicoctl
%global _buildhost      build-ol%{?oraclelinux}-%{?_arch}.oracle.com
%{!?registry_url: %global registry_url container-registry.oracle.com/olcne}

%global app_name tigera-operator
%global app_version 1.38.13
%global oracle_release_version 1

Name:           %{app_name}
Version:        %{app_version}
Release:        %{oracle_release_version}%{?dist}
Summary:        Calico Operator
License:        Apache 2.0
Url:            https://github.com/tigera/operator
Source:         %{name}-%{version}.tar.bz2
Vendor:         Oracle America
BuildRequires:  git
BuildRequires:  podman
BuildRequires:  podman-docker
BuildRequires:  make
BuildRequires:  golang

%description
Kubernetes operator which manages the lifecycle of a Calico or Calico Enterprise installation on Kubernetes


%prep
%setup -n %{name}-%{version}


%build
GOPATH=$(pwd)
mkdir -p ${GOPATH}/bin

go build -trimpath=false -v \
         -o ${GOPATH}/bin/operator \
         -ldflags "-X main.VERSION=v%{version}" \
         cmd/main.go

%install
install -D -m 755 bin/operator %{buildroot}%{_bindir}/operator


%files
%license LICENSE THIRD_PARTY_LICENSES.txt
%attr(755,root,root) %{_bindir}/operator


%changelog
* Thu Mar 19 2026 Oracle Cloud Native Environment Authors <noreply@oracle.com> - %{version}-%{oracle_release_version}
- Added Oracle specific files for kubernetes operator
