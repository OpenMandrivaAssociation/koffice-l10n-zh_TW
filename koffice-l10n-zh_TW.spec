Name: koffice-l10n-zh_TW
Version: 2.1.1
Release: %mkrel 1
Summary: Language files for KOffice Traditional Chinese
Group: System/Internationalization
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License: GPLv2+
URL: http://www.koffice.org
BuildArch: noarch
Source: ftp://ftp.kde.org/pub/kde/stable/koffice-%version/src/koffice-l10n/%name-%version.tar.bz2
BuildRequires: gettext >= 0.15
BuildRequires: kdelibs4-devel
Requires: locales-zh_TW
Requires: koffice-core
Provides: koffice-l10n

%description 
Provides Traditional Chinese translations for KOffice.

%files 
%defattr(-,root,root,-)
%{_kde_datadir}/*/*/*

#------------------------------------------------------------------------------------------------

%prep
%setup -q -n %name-%version

%build
%cmake_kde4
%make

%install
rm -rf %buildroot
%makeinstall_std -C build

%clean
rm -rf %buildroot
