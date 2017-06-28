Name:		mcperf
Version:	0.1.1
Release:	1%{?dist}
Summary:	mcperf - a tool for measuring memcached server performance

Group:		System Environment/Libraries
License:	GNU
URL:		https://github.com/twitter/twemperf
Source0:	mcperf-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
mcperf is a tool for measuring memcached server performance. mcperf is like
httperf, but for memcached protocol. It speaks memcached ASCII protocol and
is capable of generating connections and requests at a high rate.

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
%make_install


%clean
%{__rm} -rf %{buildroot}


%files
%doc LICENSE ChangeLog README.md
%attr(755,root,root) /usr/bin/mcperf


%changelog
* Wed Jun 28 2017 Mario Santos <mario.rf.santos@gmail.com> - 0.1.1
- First build
