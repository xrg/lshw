%define git_repo lshw
%define git_head HEAD

%define realversion B.0%{version}

Summary: A hardware lister
Name:		lshw
Version:	%git_get_ver
Release:	%mkrel %git_get_rel2
Source:		%git_bs_source %{name}-%{version}.tar.gz
Source1:	%{name}-gitrpm.version
Source2:	%{name}-changelog.gitrpm.txt
License: GPLv2
Group: System/Kernel and hardware
Url: http://ezix.sourceforge.net/software/lshw.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: ldetect-lst >= 0.1.282
BuildRequires: sqlite3-devel

%description
lshw (Hardware Lister) is a tool to provide detailed information 
on the hardware configuration of the machine.

%package gui
Summary: HardWare LiSter (GUI version)
Group:  System/Kernel and hardware
Requires: %{name}
Requires: gtk2
BuildRequires: gtk2-devel
%description gui
This package provides a graphical user interface to lshw

%prep
%git_get_source
%setup -q
# Ugly since 2.07 default rights are messed
find -type f | xargs chmod 644
find -type d | xargs chmod 755

%build
make
make gui

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall DESTDIR=$RPM_BUILD_ROOT
make PREFIX=%_prefix SBINDIR=%_sbindir MANDIR=%_mandir DESTDIR=$RPM_BUILD_ROOT install-gui

# packaged as part of ldetect-lst
rm -f $RPM_BUILD_ROOT%{_datadir}/lshw/{oui.txt,*.ids}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%{_sbindir}/lshw
%dir %{_datadir}/lshw
%{_datadir}/lshw/*.txt
%attr(644,root,root) %{_mandir}/man1/lshw.*

%files gui
%defattr(-,root,root)
%doc COPYING
%{_sbindir}/gtk-lshw
%{_datadir}/lshw/artwork
%{_datadir}/lshw/ui




