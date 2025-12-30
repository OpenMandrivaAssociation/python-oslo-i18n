Name: python-oslo-i18n
Version: 6.7.1
Release: 1
Source0: https://files.pythonhosted.org/packages/source/o/oslo_i18n/oslo_i18n-%{version}.tar.gz
Summary: Python internationalization library
URL: https://pypi.org/project/oslo.i18n/
License: Apache
Group: System/Libraries
BuildArch: noarch
BuildSystem: python
BuildRequires: python%{pyver}dist(setuptools)
BuildRequires: python%{pyver}dist(pip)
BuildRequires: python%{pyver}dist(wheel)
BuildRequires: python%{pyver}dist(pbr)

%description
The oslo.i18n library contain utilities for working with internationalization
(i18n) features, especially translation for text strings in an application or
library.

%files
%{py_puresitedir}/oslo_i18n
%{py_puresitedir}/oslo_i18n-%{version}.dist-info
