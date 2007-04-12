%define game_name secondlife
%define name %{game_name}-artwork
%define version 1.14.0.0
%define snapshot 0
%if %{snapshot}
%define release %mkrel 0.%{snapshot}.1
%define oname slviewer-artwork
%define distname %{oname}-%{snapshot}
%else
%define release %mkrel 1
%define oname slviewer-artwork
%define distname %{oname}-%{version}
%endif

Summary: Artwork for the Second Life 3-D virtual world
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://secondlife.com/developers/opensource/downloads/%{distname}.zip
License: GPL
Group: Games/Other
Url: http://secondlife.com/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Obsoletes: secondlife-static-data

%description
Second Life is a 3-D virtual world entirely built and owned by its residents.

This package contains artwork required by Second Life.

%prep
%setup -q -n linden

%build

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_gamesdatadir}
cp -a indra/newview %{buildroot}%{_gamesdatadir}/%{game_name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_gamesdatadir}/%{game_name}/app_settings/*
%{_gamesdatadir}/%{game_name}/skins/textures/*


