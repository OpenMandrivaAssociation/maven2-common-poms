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

Summary:	Common poms for maven2
Name:		%{parent}-%{subname}
Version:	1.0
Release:	11
License:	Apache License
Group:		Development/Java
Url:		http://jpackage.org/
# No source location for these. They are ascii files generated from maven
# repositories, and are not in cvs/svn.
Source0:	%{name}-src.tar.gz
Source1:	%{name}-jpp-depmap.xml
Source2:	%{name}-docs.tar.gz
BuildArch:	noarch
BuildRequires:	java-rpmbuild >= 0:1.7.2
Requires:	jpackage-utils >= 0:1.7.2

%description
This package is a collection of poms required by various maven2-dependent 
packages.

%prep
%setup -qn %{name}
tar xzf %{SOURCE2}

%build

%install
# Map
install -dm 755 %{buildroot}%{_mavendepmapdir}
cp %{SOURCE1} %{buildroot}%{_mavendepmapdir}/maven2-versionless-depmap.xml

install -d -m 755 %{buildroot}%{_javadir}/maven2
install -d -m 755 %{buildroot}%{_datadir}/maven2/default_poms
install -pm 644 *.pom %{buildroot}%{_datadir}/maven2/default_poms

install -d -m 755 %{buildroot}%{_javadir}/maven2
ln -s %{_datadir}/maven2/default_poms %{buildroot}%{_javadir}/maven2

%files
%doc APACHE_LICENSE.TXT JSCH_LICENSE.TXT FEDORA.README
%config(noreplace) %{_mavendepmapdir}/maven2-versionless-depmap.xml
%{_javadir}/maven2
%{_datadir}/maven2

