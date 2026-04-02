%define module oslo_i18n

Name: python-oslo-i18n
Version: 6.7.2
Release: 1
Summary: Python internationalization library
License: Apache
Group: System/Libraries
URL: https://pypi.org/project/oslo.i18n/
Source0: https://files.pythonhosted.org/packages/source/o/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pbr)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
The oslo.i18n library contain utilities for working with internationalization
(i18n) features, especially translation for text strings in an application or
library.

%files
%{py_puresitedir}/%{module}
%{py_puresitedir}/%{module}-%{version}.dist-info
