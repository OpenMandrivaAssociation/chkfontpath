%define	name	chkfontpath
%define	version	1.10.1
%define	release	%mkrel 3

Summary:	Simple interface for editing the font path for the X font server
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPLv2+
Group:		System/X11
BuildRequires:	popt-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source0:	%{name}-%{version}.tar.gz
Patch0:		chkfontpath-1.7-unscaled.patch
Requires:	xfs

%description 
This is a simple terminal mode program for configuring the directories
in the X font server's path. It is mostly intended to be used
'internally' by RPM when packages with fonts are added or removed, but
it may be useful as a stand-alone utility in some instances.

%prep
%setup -q
%patch0 -p1 -b .old

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
perl -pi -e "s!/usr/man!%{_mandir}!g" Makefile man/Makefile
%makeinstall INSTROOT=$RPM_BUILD_ROOT BINDIR=%{_sbindir} MANDIR=%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_sbindir}/chkfontpath
%{_mandir}/man8/chkfontpath.8*

