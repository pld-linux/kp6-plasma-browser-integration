#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeplasmaver	6.1.3
%define		qtver		5.15.2
%define		kpname		plasma-browser-integration

Summary:	KDE Plasma Browser Integration
Name:		kp6-%{kpname}
Version:	6.1.3
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	a5db2253d5e0a8b24d1d263e588fb3a3
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6DBus-devel
BuildRequires:	Qt6Gui-devel
BuildRequires:	Qt6Widgets-devel
BuildRequires:	cmake >= 3.16.0
BuildRequires:	gettext-devel
BuildRequires:	kf6-extra-cmake-modules
BuildRequires:	kp6-plasma-activities-devel
BuildRequires:	kf6-kauth-devel
BuildRequires:	kf6-kcodecs-devel
BuildRequires:	kf6-kcompletion-devel
BuildRequires:	kf6-kconfigwidgets-devel
BuildRequires:	kf6-kcoreaddons-devel
BuildRequires:	kf6-kcrash-devel
BuildRequires:	kf6-kdbusaddons-devel
BuildRequires:	kf6-kfilemetadata-devel
BuildRequires:	kf6-ki18n-devel
BuildRequires:	kf6-kio-devel
BuildRequires:	kf6-kitemviews-devel
BuildRequires:	kf6-kjobwidgets-devel
BuildRequires:	kf6-knotifications-devel
BuildRequires:	kf6-kpackage-devel
BuildRequires:	kf6-krunner-devel
BuildRequires:	kf6-kservice-devel
BuildRequires:	kf6-kwidgetsaddons-devel
BuildRequires:	kf6-kwindowsystem-devel
BuildRequires:	kf6-kxmlgui-devel
BuildRequires:	kf6-purpose-devel
BuildRequires:	kf6-solid-devel
BuildRequires:	kp6-plasma-workspace-devel >= %{kdeplasmaver}
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	xz
Obsoletes:	kp5-%{kpname} < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt6dir		%{_libdir}/qt6

%description
KDE Plasma Browser Integration.

%prep
%setup -q -n %{kpname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir}
%ninja_build -C build

%if %{with tests}
ctest
%endif

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kpname}.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/chromium
%dir %{_sysconfdir}/chromium/native-messaging-hosts
%{_sysconfdir}/chromium/native-messaging-hosts/org.kde.plasma.browser_integration.json
%dir %{_sysconfdir}/opt/chrome
%dir %{_sysconfdir}/opt/chrome/native-messaging-hosts
%{_sysconfdir}/opt/chrome/native-messaging-hosts/org.kde.plasma.browser_integration.json
%attr(755,root,root) %{_bindir}/plasma-browser-integration-host
%dir %{_prefix}/lib/mozilla
%dir %{_prefix}/lib/mozilla/native-messaging-hosts
%{_prefix}/lib/mozilla/native-messaging-hosts/org.kde.plasma.browser_integration.json
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kded/browserintegrationreminder.so
%dir %{_sysconfdir}/opt/edge
%dir %{_sysconfdir}/opt/edge/native-messaging-hosts
%{_sysconfdir}/opt/edge/native-messaging-hosts/org.kde.plasma.browser_integration.json
%{_datadir}/krunner/dbusplugins/plasma-runner-browserhistory.desktop
%{_datadir}/krunner/dbusplugins/plasma-runner-browsertabs.desktop
%{_desktopdir}/org.kde.plasma.browser_integration.host.desktop
