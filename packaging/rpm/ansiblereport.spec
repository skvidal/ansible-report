Name:       ansiblereport
Version:	0.1
Release:	1%{?dist}
Summary:	Reporting tool for Ansible

Group:		Development/Libraries
License:	GPLv3
URL:		https://github.com/sfromm/ansible-report
#Source0:	https://github.com/sfromm/ansible-report/archive/release%{version}.tar.gz
Source0:	ansiblereport-%{version}.tar.gz

BuildArch:  noarch
BuildRequires:	python-devel
Requires:   python-alembic
Requires:   python-dateutil
Requires:   ansible
%if ( 0%{?rhel} && 0%{?rhel} == 6 )
BuildRequires:  python-sqlalchemy0.7
Requires:	python-sqlalchemy0.7
%else
BuildRequires:  python-sqlalchemy > 0.5
Requires:   python-sqlalchemy > 0.5
%endif

%description
A utility to record events in a database via ansible callbacks and then 
report on them at a later date.

%prep
%setup -q

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{python_sitelib}/ansiblereport*
%{_bindir}/ansible-report
%{_datadir}/ansible_plugins/callback_plugins/ansiblereport-logger.py
%{_datadir}/ansible-report/plugins/*.py
%doc README.md COPYING

%changelog
* Thu May 2 2013 Stephen Fromm <sfromm gmail com> - 0.1-0
- Initial version
