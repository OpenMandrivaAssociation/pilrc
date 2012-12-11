%define name pilrc
%define version 3.2
%define release %mkrel 6

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




%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 3.2-6mdv2010.0
+ Revision: 430735
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tvignaud@mandriva.com> 3.2-5mdv2009.0
+ Revision: 259064
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 3.2-4mdv2009.0
+ Revision: 246978
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 3.2-2mdv2008.1
+ Revision: 140731
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Mon Jan 15 2007 Lenny Cartier <lenny@mandriva.com> 3.2-2mdv2007.0
+ Revision: 109171
- Rebuild & url
- Import pilrc

