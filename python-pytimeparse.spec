%{!?__python2:        %global __python2 /usr/bin/python2}
%{!?python2_sitelib:  %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%global pypi_name pytimeparse

Name:           python-pytimeparse
Version:	1.1.5
Release:	1%{?dist}
Summary:        Python time expression parse library
License:	MIT
URL:		https://github.com/wroberts/pytimeparse
Source0:	https://pypi.python.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:	python-setuptools
BuildRequires:  python2-devel

%description
A small Python library to parse various kinds of time expressions

%prep
%setup -q -n %{pypi_name}-%{version}

%build

%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%files
%{python2_sitelib}/pytimeparse
%{python2_sitelib}/pytimeparse*.egg-info
%doc README.rst


%changelog
* Tue Aug 04 2015 Pradeep Kilambi <pkilambi@redhat.com> - 1.1.5-1
- new version build

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 05 2015 Pradeep Kilambi <pkilambi@redhat.com> 1.1.4
- initial package release


