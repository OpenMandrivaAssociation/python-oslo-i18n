Name: python-oslo-i18n
Version: 5.0.1
Release: 1
Source0: https://files.pythonhosted.org/packages/source/o/oslo.i18n/oslo.i18n-%{version}.tar.gz
Summary: Python internationalization library
URL: https://pypi.org/project/oslo.i18n/
License: Apache
Group: System/Libraries
BuildArch: noarch
BuildRequires: python python-setuptools

%description
The oslo.i18n library contain utilities for working with internationalization
(i18n) features, especially translation for text strings in an application or
library.

%prep
%autosetup -p1 -n oslo.i18n-%{version}

%build
python setup.py build

%install
PYTHONDONTWRITEBYTECODE= python setup.py install --root=%{buildroot}

%files
%{py_puresitedir}/oslo_i18n
%{py_puresitedir}/*.egg-info
