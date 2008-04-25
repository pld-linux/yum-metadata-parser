Summary:	A fast metadata parser for yum
Summary(pl.UTF-8):	Szybki analizator metadanych dla yuma
Name:		yum-metadata-parser
Version:	1.1.2
Release:	2
License:	GPL
Group:		Applications/System
Source0:	http://linux.duke.edu/projects/yum/download/yum-metadata-parser/%{name}-%{version}.tar.gz
# Source0-md5:	13df226ef004ea78eebc59022720b536
URL:		http://linux.duke.edu/projects/yum/
BuildRequires:	glib2-devel
BuildRequires:	libxml2-devel
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpmbuild(macros) >= 1.228
BuildRequires:	rpm-pythonprov
BuildRequires:	sqlite3-devel
Requires:	python >= 1:2.5
Requires:	python-modules-sqlite >= 1:2.5.1-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fast metadata parser for yum implemented in C.

%description -l pl.UTF-8
Szybki analizator metadanych dla yuma zaimplementowany w C.

%prep
%setup -q

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install -O1 --root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS ChangeLog
%{py_sitedir}/*.py*
%{py_sitedir}/*.egg-info
%attr(755,root,root) %{py_sitedir}/*.so
