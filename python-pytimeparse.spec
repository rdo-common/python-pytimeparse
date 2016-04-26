%global pypi_name pytimeparse

Name:           python-pytimeparse
Version:        1.1.5
Release:        4%{?dist}
Summary:        Python time expression parse library
License:        MIT
URL:            https://github.com/wroberts/pytimeparse
Source0:        https://pypi.python.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:    python3-setuptools
BuildRequires:    python3-devel

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

%files
%doc README.rst
%{python3_sitelib}/*


%changelog
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

