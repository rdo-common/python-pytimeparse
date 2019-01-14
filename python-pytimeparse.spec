%global pypi_name pytimeparse

Name:           python-pytimeparse
Version:        1.1.5
Release:        14%{?dist}
Summary:        Python time expression parse library
License:        MIT
URL:            https://github.com/wroberts/pytimeparse
Source0:        https://pypi.python.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%package -n python3-%{pypi_name}

Summary:        Python time expression parse library
%{?python_provide:%python_provide python3-pytimeparse}

BuildRequires:    python3-setuptools
BuildRequires:    python3-devel

%description -n python3-%{pypi_name}
A small Python library to parse various kinds of time expressions


%description
A small Python library to parse various kinds of time expressions

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%py3_build

# Find all *.py files with the exact line '#!/usr/bin/env python' and for each
# such file replace the line with nothing (if it's the 1st line).
grep -ilrx build -e '#!/usr/bin/env python' --include '*.py'| xargs sed -i '1s\^#!/usr/bin/env python$\\'

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst
%{python3_sitelib}/*


%changelog
* Mon Jan 14 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.5-14
- Subpackage python2-pytimeparse has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.5-12
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.1.5-11
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

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

