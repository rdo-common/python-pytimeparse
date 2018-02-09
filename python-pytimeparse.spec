%{!?python2_shortver: %global python2_shortver %(%{__python2} -c 'import sys; print(str(sys.version_info.major) + "." + str(sys.version_info.minor))')}
%{!?python3_shortver: %global python3_shortver %(%{__python3} -c 'import sys; print(str(sys.version_info.major) + "." + str(sys.version_info.minor))')}

%global pypi_name pytimeparse

%if 0%{?fedora} >= 24
%global with_python3 1
%endif


Name:           python-pytimeparse
Version:        1.1.5
Release:        10%{?dist}
Summary:        Python time expression parse library
License:        MIT
URL:            https://github.com/wroberts/pytimeparse
Source0:        https://pypi.python.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%package -n python2-%{pypi_name}
Summary:        Python time expression parse library
%{?python_provide:%python_provide python2-pytimeparse}

BuildRequires:    python-setuptools
BuildRequires:    python2-devel

%description -n python2-%{pypi_name}
A small Python library to parse various kinds of time expressions

%if 0%{?with_python3}
%package -n python3-%{pypi_name}

Summary:        Python time expression parse library
%{?python_provide:%python_provide python3-pytimeparse}

BuildRequires:    python3-setuptools
BuildRequires:    python3-devel

%description -n python3-%{pypi_name}
A small Python library to parse various kinds of time expressions

%endif

%description
A small Python library to parse various kinds of time expressions

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%py2_build

%if 0%{?with_python3}
%py3_build
%endif


# Find all *.py files with the exact line '#!/usr/bin/env python' and for each
# such file replace the line with nothing (if it's the 1st line).
grep -ilrx build -e '#!/usr/bin/env python' --include '*.py'| xargs sed -i '1s\^#!/usr/bin/env python$\\'

%install
%if 0%{?with_python3}
%py3_install
%endif

%{__python2} setup.py install --skip-build --root %{buildroot}

%files -n python2-%{pypi_name}
%doc README.rst
%{python2_sitelib}/*

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%doc README.rst
%{python3_sitelib}/*
%endif


%changelog
* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.1.5-7
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Jun 17 2016 Pradeep Kilambi <pkilambi@redhat.com> - 1.1.5-5
- Add support so we build both py2 and py3

* Fri Apr 08 2016 Dominika Krejci <dkrejci@redhat.com> - 1.1.5-4
- Remove unnecessary shebang lines

* Mon Feb 08 2016 Matej Dujava <mdujava@redhat.com> - 1.1.5-3
- Add python3

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Aug 04 2015 Pradeep Kilambi <pkilambi@redhat.com> - 1.1.5-1
- new version build

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 05 2015 Pradeep Kilambi <pkilambi@redhat.com> 1.1.4
- initial package release

