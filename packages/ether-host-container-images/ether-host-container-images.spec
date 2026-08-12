Name: %{_cross_os}ether-host-container-images
Version: 0.0
Release: 1%{?dist}
Epoch: 1
Summary: Pre-baked Ether host container image tarballs and preload unit
License: Apache-2.0 OR MIT
URL: https://github.com/zomato/bottlerocket

Source10: ether-host-containers-preload.service
Source20: ether-admin.tar
Source21: ether-control.tar

Requires: %{_cross_os}containerd-2.1

%description
%{summary}. Ships OCI archive tarballs of the ether-admin and ether-control host
containers, along with a systemd oneshot unit that imports them into
host-containerd before host-containers.target activates. Lets Ether-based hosts
boot with zero external registry access.

%prep
# nothing to prep

%build
# nothing to build

%install
install -d %{buildroot}%{_cross_datadir}/ether/host-containers
install -p -m 0644 %{S:20} %{buildroot}%{_cross_datadir}/ether/host-containers/ether-admin.tar
install -p -m 0644 %{S:21} %{buildroot}%{_cross_datadir}/ether/host-containers/ether-control.tar

install -d %{buildroot}%{_cross_unitdir}
install -p -m 0644 %{S:10} %{buildroot}%{_cross_unitdir}/ether-host-containers-preload.service

%files
%{_cross_datadir}/ether/host-containers/ether-admin.tar
%{_cross_datadir}/ether/host-containers/ether-control.tar
%{_cross_unitdir}/ether-host-containers-preload.service

%changelog
