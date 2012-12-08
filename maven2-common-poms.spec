# Copyright (c) 2000-2006, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

%define parent maven2
%define subname common-poms

Name:              %{parent}-%{subname}
Version:           1.0
Release:           %mkrel 5.1.9
Epoch:             0
Summary:           Common poms for maven2
License:           Apache License
Group:             Development/Java
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:               http://jpackage.org/

# No source location for these. They are ascii files generated from maven
# repositories, and are not in cvs/svn.
Source0:           %{name}-src.tar.gz
Source1:           %{name}-jpp-depmap.xml
Source2:           %{name}-docs.tar.gz


BuildArch:         noarch
BuildRequires:     java-rpmbuild >= 0:1.7.2
Requires:          jpackage-utils >= 0:1.7.2

%description
This package is a collection of poms required by various maven2-dependent 
packages.

%prep
%setup -q -n %{name}

tar xzf %{SOURCE2}

%build

%install
rm -rf $RPM_BUILD_ROOT

# Map
install -dm 755 $RPM_BUILD_ROOT%{_mavendepmapdir}
cp %{SOURCE1} $RPM_BUILD_ROOT%{_mavendepmapdir}/maven2-versionless-depmap.xml

install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/maven2
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/default_poms
install -pm 644 *.pom $RPM_BUILD_ROOT%{_datadir}/maven2/default_poms

install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/maven2
ln -s %{_datadir}/maven2/default_poms $RPM_BUILD_ROOT%{_javadir}/maven2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc APACHE_LICENSE.TXT JSCH_LICENSE.TXT FEDORA.README
%config(noreplace) %{_mavendepmapdir}/maven2-versionless-depmap.xml
%{_javadir}/maven2
%{_datadir}/maven2


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0:1.0-5.1.8mdv2011.0
+ Revision: 666393
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0:1.0-5.1.7mdv2011.0
+ Revision: 606631
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0:1.0-5.1.6mdv2010.1
+ Revision: 523289
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0:1.0-5.1.5mdv2010.0
+ Revision: 426078
- rebuild

* Tue Feb 19 2008 Alexander Kurtakov <akurtakov@mandriva.org> 0:1.0-5.1.4mdv2008.1
+ Revision: 172968
- sync with jpp

  + Thierry Vignaud <tv@mandriva.org>
    - fix no-buildroot-tag

* Wed Jan 09 2008 Alexander Kurtakov <akurtakov@mandriva.org> 0:1.0-5.1.3mdv2008.1
+ Revision: 147306
- add surefire-root pom

* Wed Jan 09 2008 Alexander Kurtakov <akurtakov@mandriva.org> 0:1.0-5.1.2mdv2008.1
+ Revision: 146965
- bump release
- fix conflict with bcel

* Tue Jan 08 2008 Alexander Kurtakov <akurtakov@mandriva.org> 0:1.0-5.1.1mdv2008.1
+ Revision: 146642
- new version (fc symc)

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Dec 16 2007 Anssi Hannula <anssi@mandriva.org> 0:1.0-4.2.2mdv2008.1
+ Revision: 120977
- buildrequire java-rpmbuild, i.e. build with icedtea on x86(_64)

* Sun Jul 01 2007 David Walluck <walluck@mandriva.org> 0:1.0-4.2.1mdv2008.0
+ Revision: 46254
- Import maven2-common-poms



* Thu Mar 15 2007 Deepak Bhole <dbhole@redhat.com> 1.0-4jpp.2
- Updated depmap to make javax-servlet be tomcat-2.4-servlet-api

* Mon Feb 12 2007 Deepak Bhole <dbhole@redhat.com> 0:1.0-4jpp.1
- Fix spec per Fedora guidelines.

* Fri Oct 13 2006 Deepak Bhole <dbhole@redhat.com> 1.0-3jpp
- Changed file names to comply with the new maven2 rpm.

* Fri Sep 18 2006 Deepak Bhole <dbhole@redhat.com> - 0:1.0-2jpp
- Moved common poms from maven2 rpm into this one.

* Tue Jun 13 2006 Deepak Bhole <dbhole@redhat.com> - 0:1.0-1jpp
- Initial build
