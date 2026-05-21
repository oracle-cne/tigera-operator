
%global debug_package %{nil}
%{!?registry: %global registry container-registry.oracle.com/olcne}
%global _buildhost      build-ol%{?oraclelinux}-%{?_arch}.oracle.com

%global app_name tigera-operator
%global app_version 1.40.11
%global oracle_release_version 1

Name:		%{app_name}-container-image
Version:	%{app_version}
Release:	%{oracle_release_version}%{?dist}
Summary:	Calico Operator
License:	Apache 2.0
URL:		https://github.com/tigera/operator
Source0:	%{name}-%{version}.tar.bz2
Vendor:		Oracle America

%description
Kubernetes operator manages the lifecycle of a Calico or Calico Enterprise installation on Kubernetes.


%prep
%setup -q -n %{name}-%{version}


%build
%global rpm_name %{app_name}-%{version}-%{release}.%{_build_arch}
dnf clean all
dnf install -y --downloadonly --downloaddir=${PWD}/rpms %{rpm_name}

%__rm .dockerignore
chmod +x ./olm/builds/build-image.sh
./olm/builds/build-image.sh \
    %{version} \
    _output \
    %{registry}


%install
mkdir -p %{buildroot}/usr/local/share/olcne
install -m 755 -d %{buildroot}/usr/local/share/olcne
echo "+++ INSTALLING DOCKER IMAGE tigera-operator.tar"
install -p -m 755 -t %{buildroot}/usr/local/share/olcne _output/oracle_docker/tigera-operator.tar


%files
%license LICENSE THIRD_PARTY_LICENSES.txt
/usr/local/share/olcne/tigera-operator.tar


%changelog
* Thu May 21 2026 Oracle Cloud Native Environment Authors <noreply@oracle.com> - %{version}-%{oracle_release_version}
- Added Oracle specific files for kubernetes operator
