Summary:	A fast metadata parser for yum
Summary(pl.UTF-8):	Szybki analizator metadanych dla yuma
Name:		yum-metadata-parser
Version:	1.1.4
Release:	3
License:	GPL
Group:		Applications/System
Source0:	http://yum.baseurl.org/download/yum-metadata-parser/%{name}-%{version}.tar.gz
# Source0-md5:	05289971e5cfde532631f2a99f6c58c7
URL:		http://yum.baseurl.org/
BuildRequires:	glib2-devel
BuildRequires:	libxml2-devel
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.228
BuildRequires:	sqlite3-devel
Requires:	python >= 1:2.5
Requires:	python-modules-sqlite >= 1:2.5.1-2
Conflicts:	yum < 3.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fast metadata parser for yum implemented in C.

%description -l pl.UTF-8
Szybki analizator metadanych dla yuma zaimplementowany w C.

%prep
%setup -q

%build
export CFLAGS="%{rpmcflags}"
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS ChangeLog
%{py_sitedir}/*.py[co]
%{py_sitedir}/*.egg-info
%attr(755,root,root) %{py_sitedir}/*.so
