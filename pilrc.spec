%define name pilrc
%define version 3.2
%define release %mkrel 4

Summary: Takes a resource script file and generates one or more binary resource
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
URL: http://pilrc.sourceforge.net/
Source: %{name}-%{version}.tar.bz2
Group: Development/Other
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
BuildRequires: gtk-devel

%description
PilRC is an application that takes a resource script file and generates one or
more binary resource files that are to be used when developing for the Palm 
Computing Platform. PilRCUI gives you a preview of your resource file. 


%prep
%setup -q

%build

cd unix
%configure2_5x --enable-pilrcui 

%make

%install
rm -rf $RPM_BUILD_ROOT

cd unix/
cp -r ../ppmquant .

%makeinstall

cd ..
chmod 0755 doc/images
chmod 0644 LICENSE.txt README.txt doc/*.html doc/images/*

%clean
rm -rf $RPM_BUILD_ROOT 

%files
%defattr (-,root,root)
%doc LICENSE.txt README.txt doc/*.html doc/images
%{_bindir}/*
%_datadir/%name/*


