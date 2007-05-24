Summary:	A fast metadata parser for yum
Name:		yum-metadata-parser
Version:	1.1.1
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://linux.duke.edu/projects/yum/download/yum-metadata-parser/%{name}-%{version}.tar.gz
# Source0-md5:	19a7bb09aa644be9093d73b5baa71cc3
URL:		http://linux.duke.edu/projects/yum/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.228
Requires(post,preun):	/sbin/chkconfig
Requires:	python >= 2.5
Requires:	python-libxml2
Requires:	python-sqlite1
Requires:	rc-scripts
Requires:	yum
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fast metadata parser for yum implemented in C.

%prep
%setup -q

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install -O1 --root=%{buildroot}

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS ChangeLog
%{py_sitedir}/*.py*
%attr(755,root,root) %{py_sitedir}/*.so
