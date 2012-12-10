%define	name	chkfontpath
%define	version	1.10.1
%define	release	%mkrel 7

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



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.10.1-7mdv2011.0
+ Revision: 617034
- the mass rebuild of 2010.0 packages

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 1.10.1-6mdv2010.0
+ Revision: 424833
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.10.1-5mdv2009.0
+ Revision: 243881
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.10.1-3mdv2008.1
+ Revision: 136304
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Sep 14 2007 Adam Williamson <awilliamson@mandriva.org> 1.10.1-3mdv2008.0
+ Revision: 85437
- rebuild for 2008
- drop file dependency on /sbin/pidof, which is indirectly required by basesystem anyway
- Fedora license policy


* Fri Mar 02 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1.10.1-1mdv2007.0
+ Revision: 131216
- new release: 1.10.1
- removed dev-null patch (applied upstream)
- bunzipped remaining patch

* Fri Nov 03 2006 Pablo Saratxaga <pablo@mandriva.com> 1.10.0-3mdv2007.1
+ Revision: 76296
- corrected system call to kill to properly direct stderr to /dev/null
- changed group to System/X11
- Import chkfontpath

* Sat Dec 31 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 1.10.0-2mdk
- Rebuild

* Fri Nov 12 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.10.0-1mdk
- 1.10.0

