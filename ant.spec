# Copyright (c) 2000-2008, JPackage Project
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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

%bcond_with bootstrap

%if %with bootstrap
%define build_javadoc        0
%else
%define build_javadoc        1
%endif

%define _with_gcj_support 1

%define gcj_support %{?_with_gcj_support:1}%{!?_with_gcj_support:%{?_without_gcj_support:0}%{!?_without_gcj_support:%{?_gcj_support:%{_gcj_support}}%{!?_gcj_support:0}}}

%define with_manifest_only 0

%define ant_home %{_datadir}/ant
%define section  free

%define major_version 1.7
%define cvs_version 1.7.1

Name:           ant
Version:        1.7.1
Release:        13%{?dist}
Epoch:          0
Summary:        Ant build tool for java
Summary(it):    Tool per la compilazione di programmi java
Summary(fr):    Outil de compilation pour java
License:        ASL 2.0 and W3C
URL:            http://ant.apache.org/
Group:          Development/Tools
Source0:        http://archive.apache.org/dist/ant/source/apache-ant-%{cvs_version}-src.tar.bz2
Source2:        apache-ant-%{major_version}.ant.conf
Source1:        http://repo1.maven.org/maven2/org/apache/ant/ant/1.7.1/ant-1.7.1.pom
Source3:        http://repo1.maven.org/maven2/org/apache/ant/ant-launcher/1.7.1/ant-launcher-1.7.1.pom
Source4:        http://repo1.maven.org/maven2/org/apache/ant/ant-netrexx/1.7.1/ant-netrexx-1.7.1.pom
Source5:        http://repo1.maven.org/maven2/org/apache/ant/ant-starteam/1.7.1/ant-starteam-1.7.1.pom
Source6:        http://repo1.maven.org/maven2/org/apache/ant/ant-stylebook/1.7.1/ant-stylebook-1.7.1.pom
Source7:        http://repo1.maven.org/maven2/org/apache/ant/ant-weblogic/1.7.1/ant-weblogic-1.7.1.pom
Source8:        http://repo1.maven.org/maven2/org/apache/ant/ant-antlr/1.7.1/ant-antlr-1.7.1.pom
Source9:        http://repo1.maven.org/maven2/org/apache/ant/ant-apache-bsf/1.7.1/ant-apache-bsf-1.7.1.pom
Source10:       http://repo1.maven.org/maven2/org/apache/ant/ant-apache-resolver/1.7.1/ant-apache-resolver-1.7.1.pom
Source11:       http://repo1.maven.org/maven2/org/apache/ant/ant-commons-logging/1.7.1/ant-commons-logging-1.7.1.pom
Source12:       http://repo1.maven.org/maven2/org/apache/ant/ant-commons-net/1.7.1/ant-commons-net-1.7.1.pom
#Source13:       http://repo1.maven.org/maven2/org/apache/ant/ant-jai/1.7.1/ant-jai-1.7.1.pom
Source14:       http://repo1.maven.org/maven2/org/apache/ant/ant-apache-bcel/1.7.1/ant-apache-bcel-1.7.1.pom
Source15:       http://repo1.maven.org/maven2/org/apache/ant/ant-apache-log4j/1.7.1/ant-apache-log4j-1.7.1.pom
Source16:       http://repo1.maven.org/maven2/org/apache/ant/ant-apache-oro/1.7.1/ant-apache-oro-1.7.1.pom
Source17:       http://repo1.maven.org/maven2/org/apache/ant/ant-apache-regexp/1.7.1/ant-apache-regexp-1.7.1.pom
Source18:       http://repo1.maven.org/maven2/org/apache/ant/ant-javamail/1.7.1/ant-javamail-1.7.1.pom
Source19:       http://repo1.maven.org/maven2/org/apache/ant/ant-jdepend/1.7.1/ant-jdepend-1.7.1.pom
Source20:       http://repo1.maven.org/maven2/org/apache/ant/ant-jmf/1.7.1/ant-jmf-1.7.1.pom
Source21:       http://repo1.maven.org/maven2/org/apache/ant/ant-jsch/1.7.1/ant-jsch-1.7.1.pom
Source22:       http://repo1.maven.org/maven2/org/apache/ant/ant-junit/1.7.1/ant-junit-1.7.1.pom
Source23:       http://repo1.maven.org/maven2/org/apache/ant/ant-nodeps/1.7.1/ant-nodeps-1.7.1.pom
Source24:       http://repo1.maven.org/maven2/org/apache/ant/ant-swing/1.7.1/ant-swing-1.7.1.pom
Source25:       http://repo1.maven.org/maven2/org/apache/ant/ant-trax/1.7.1/ant-trax-1.7.1.pom
Source26:       http://repo1.maven.org/maven2/org/apache/ant/ant-parent/1.7.1/ant-parent-1.7.1.pom

# Fix some places where copies of classes are included in the wrong jarfiles
Patch1:         apache-ant-bz163689.patch
Patch2:         apache-ant-gnu-classpath.patch
Patch3:         apache-ant-no-test-jar.patch
Patch4:         apache-ant-class-path-in-manifest.patch
Patch5:         apache-ant-package-info-bz43114.patch

BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  java-devel >= 0:1.5.0
BuildRequires:  jaxp_transform_impl
%if %without bootstrap
BuildRequires:  ant
BuildRequires:  junit
BuildRequires:  xml-commons-jaxp-1.3-apis
BuildRequires:  xerces-j2
%endif

Requires:       jpackage-utils >= 0:1.7.5
Requires:       java-devel >= 0:1.5.0
%if %without bootstrap
Requires:       xerces-j2
Requires:       xml-commons-jaxp-1.3-apis
%endif

%if ! %{gcj_support}
BuildArch:      noarch
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
Obsoletes:      ant-optional < %{epoch}:%{version}-%{release}
Provides:       ant-optional = %{epoch}:%{version}-%{release}
Obsoletes:      ant-optional-full < %{epoch}:%{version}-%{release}
Provides:       ant-optional-full = %{epoch}:%{version}-%{release}
# Allow subpackages not in RHEL to be installed from JPackage
Provides:       %{name} = %{epoch}:%{version}-%{release}
# RHUG
Obsoletes:      ant-devel < %{epoch}:%{version}-%{release}
Provides:       ant-devel = %{epoch}:%{version}-%{release}
# Mandriva
Conflicts:      j2sdk-ant
# RHEL3 and FC2
Obsoletes:      %{name}-libs < %{epoch}:%{version}-%{release}
Provides:       %{name}-libs = %{epoch}:%{version}-%{release}
Obsoletes:      %{name}-core < %{epoch}:%{version}-%{release}
Provides:       %{name}-core = %{epoch}:%{version}-%{release}
%if %{gcj_support}
BuildRequires:          java-gcj-compat-devel
%endif

Requires(post):   jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5

%description
Ant is a platform-independent build tool for java. It's used by apache
jakarta and xml projects.

%description -l fr
Ant est un outil de compilation multi-plateformes pour java. Il est
utilisé par les projets apache-jakarta et apache-xml.

%description -l it
Ant e' un tool indipendente dalla piattaforma creato per faciltare la
compilazione di programmi java.
Allo stato attuale viene utilizzato dai progetti apache jakarta ed
apache xml.

%package jmf
Summary:        Optional jmf tasks for %{name}
Group:          Development/Tools
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-nodeps = %{epoch}:%{version}-%{release}
Provides:       ant-jmf = %{epoch}:%{version}-%{release}

%description jmf
Optional jmf tasks for %{name}.

%description jmf -l fr
Taches jmf optionelles pour %{name}.

%package nodeps
Summary:        Optional tasks for %{name}
Group:          Development/Tools
Requires:       %{name} = %{epoch}:%{version}-%{release}
Provides:       ant-nodeps = %{epoch}:%{version}-%{release}

%description nodeps
Optional tasks for %{name}.

%description nodeps -l fr
Taches optionelles pour %{name}.

%package swing
Summary:        Optional swing tasks for %{name}
Group:          Development/Tools
Requires:       %{name} = %{epoch}:%{version}-%{release}
Provides:       ant-swing = %{epoch}:%{version}-%{release}

%description swing
Optional swing tasks for %{name}.

%description swing -l fr
Taches swing optionelles pour %{name}.

%package trax
Summary:        Optional trax tasks for %{name}
Group:          Development/Tools
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       jaxp_transform_impl
Requires:       %{name}-nodeps = %{epoch}:%{version}-%{release}
Provides:       ant-trax = %{epoch}:%{version}-%{release}
# The ant-xalan jar has been merged into the ant-trax one
Obsoletes:      ant-xalan2 < %{epoch}:%{version}-%{release}
Provides:       ant-xalan2 = %{epoch}:%{version}-%{release}

%description trax
Optional trax tasks for %{name}.

%description trax -l fr
Taches trax optionelles pour %{name}.

%if %without bootstrap
%if %{with_manifest_only}
%package manifest-only
Summary:        Manifest-only jars for %{name}
Group:          Development/Tools
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-nodeps = %{epoch}:%{version}-%{release}
Provides:       %{name}-icontract = %{epoch}:%{version}-%{release}
Provides:       %{name}-netrexx = %{epoch}:%{version}-%{release}
Provides:       %{name}-starteam = %{epoch}:%{version}-%{release}
Provides:       %{name}-stylebook = %{epoch}:%{version}-%{release}
Provides:       %{name}-vaj = %{epoch}:%{version}-%{release}
Provides:       %{name}-weblogic = %{epoch}:%{version}-%{release}
Provides:       %{name}-xalan1 = %{epoch}:%{version}-%{release}
Provides:       %{name}-xslp = %{epoch}:%{version}-%{release}

%description  manifest-only
Manifest-only jars for %{name}.
%endif

%package antlr
Summary:        Optional antlr tasks for %{name}
Group:          Development/Tools
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-nodeps = %{epoch}:%{version}-%{release}
Requires:       antlr
BuildRequires:  antlr
Provides:       ant-antlr = %{epoch}:%{version}-%{release}

%description antlr
Optional antlr tasks for %{name}.

%description antlr -l fr
Taches antlr optionelles pour %{name}.

%package apache-bsf
Summary:        Optional apache bsf tasks for %{name}
Group:          Development/Tools
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-nodeps = %{epoch}:%{version}-%{release}
Requires:       bsf
BuildRequires:  bsf
Provides:       ant-apache-bsf = %{epoch}:%{version}-%{release}

%description apache-bsf
Optional apache bsf tasks for %{name}.

%description apache-bsf -l fr
Taches apache bsf optionelles pour %{name}.

%package apache-resolver
Summary:        Optional apache resolver tasks for %{name}
Group:          Development/Tools
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-nodeps = %{epoch}:%{version}-%{release}
Requires:       xml-commons-resolver
BuildRequires:  xml-commons-resolver
Provides:       ant-apache-resolver = %{epoch}:%{version}-%{release}

%description apache-resolver
Optional apache resolver tasks for %{name}.

%description apache-resolver -l fr
Taches apache resolver optionelles pour %{name}.

%package commons-logging
Summary:        Optional commons logging tasks for %{name}
Group:          Development/Tools
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-nodeps = %{epoch}:%{version}-%{release}
Requires:       jakarta-commons-logging
BuildRequires:  jakarta-commons-logging
Provides:       ant-commons-logging = %{epoch}:%{version}-%{release}

%description commons-logging
Optional commons logging tasks for %{name}.

%description commons-logging -l fr
Taches commons logging optionelles pour %{name}.

%package commons-net
Summary:        Optional commons net tasks for %{name}
Group:          Development/Tools
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-nodeps = %{epoch}:%{version}-%{release}
Requires:       jakarta-commons-net
BuildRequires:  jakarta-commons-net
Provides:       ant-commons-net = %{epoch}:%{version}-%{release}

%description commons-net
Optional commons net tasks for %{name}.

%description commons-net -l fr
Taches commons net optionelles pour %{name}.

# Disable because we don't ship the dependencies
%if 0
%package jai
Summary:        Optional jai tasks for %{name}
Group:          Development/Tools
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-nodeps = %{epoch}:%{version}-%{release}
Requires:       jai
BuildRequires:  jai
Provides:       ant-jai = %{epoch}:%{version}-%{release}

%description jai
Optional jai tasks for %{name}.

%description jai -l fr
Taches jai optionelles pour %{name}.
%endif

%package apache-bcel
Summary:        Optional apache bcel tasks for %{name}
Group:          Development/Tools
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-nodeps = %{epoch}:%{version}-%{release}
Requires:       bcel
BuildRequires:  bcel
Provides:       ant-apache-bcel = %{epoch}:%{version}-%{release}
Provides:       ant-jakarta-bcel = %{epoch}:%{version}-%{release}
Obsoletes:      ant-jakarta-bcel < %{epoch}:%{version}-%{release}

%description apache-bcel
Optional apache bcel tasks for %{name}.

%description apache-bcel -l fr
Taches apache bcel optionelles pour %{name}.

%package apache-log4j
Summary:        Optional apache log4j tasks for %{name}
Group:          Development/Tools
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-nodeps = %{epoch}:%{version}-%{release}
Requires:       log4j
BuildRequires:  log4j
Provides:       ant-apache-log4j = %{epoch}:%{version}-%{release}
Provides:       ant-jakarta-log4j = %{epoch}:%{version}-%{release}
Obsoletes:      ant-jakarta-log4j < %{epoch}:%{version}-%{release}

%description apache-log4j
Optional apache log4j tasks for %{name}.

%description apache-log4j -l fr
Taches apache log4j optionelles pour %{name}.

%package apache-oro
Summary:        Optional apache oro tasks for %{name}
Group:          Development/Tools
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-nodeps = %{epoch}:%{version}-%{release}
Requires:       oro
BuildRequires:  oro
Provides:       ant-apache-oro = %{epoch}:%{version}-%{release}
Provides:       ant-jakarta-oro = %{epoch}:%{version}-%{release}
Obsoletes:      ant-jakarta-oro < %{epoch}:%{version}-%{release}

%description apache-oro
Optional apache oro tasks for %{name}.

%description apache-oro -l fr
Taches apache oro optionelles pour %{name}.

%package apache-regexp
Summary:        Optional apache regexp tasks for %{name}
Group:          Development/Tools
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-nodeps = %{epoch}:%{version}-%{release}
Requires:       regexp
BuildRequires:  regexp
Provides:       ant-apache-regexp = %{epoch}:%{version}-%{release}
Provides:       ant-jakarta-regexp = %{epoch}:%{version}-%{release}
Obsoletes:      ant-jakarta-regexp < %{epoch}:%{version}-%{release}

%description apache-regexp
Optional apache regexp tasks for %{name}.

%description apache-regexp -l fr
Taches apache regexp optionelles pour %{name}.

%package javamail
Summary:        Optional javamail tasks for %{name}
Group:          Development/Tools
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-nodeps = %{epoch}:%{version}-%{release}
Requires:       javamail >= 0:1.2-5jpp
Requires:       jaf >= 0:1.0.1-5jpp
BuildRequires:  javamail >= 0:1.2-5jpp
BuildRequires:  jaf >= 0:1.0.1-5jpp
Provides:       ant-javamail = %{epoch}:%{version}-%{release}

%description javamail
Optional javamail tasks for %{name}.

%description javamail -l fr
Taches javamail optionelles pour %{name}.

%package jdepend
Summary:        Optional jdepend tasks for %{name}
Group:          Development/Tools
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-nodeps = %{epoch}:%{version}-%{release}
Requires:       jdepend
BuildRequires:  jdepend
Provides:       ant-jdepend = %{epoch}:%{version}-%{release}

%description jdepend
Optional jdepend tasks for %{name}.

%description jdepend -l fr
Taches jdepend optionelles pour %{name}.

%package jsch
Summary:        Optional jsch tasks for %{name}
Group:          Development/Tools
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-nodeps = %{epoch}:%{version}-%{release}
Requires:       jsch
BuildRequires:  jsch
Provides:       ant-jsch = %{epoch}:%{version}-%{release}

%description jsch
Optional jsch tasks for %{name}.

%description jsch -l fr
Taches jsch optionelles pour %{name}.

%package junit
Summary:        Optional junit tasks for %{name}
Group:          Development/Tools
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-nodeps = %{epoch}:%{version}-%{release}
Requires:       junit
Provides:       ant-junit = %{epoch}:%{version}-%{release}

%description junit
Optional junit tasks for %{name}.

%description junit -l fr
Taches junit optionelles pour %{name}.

%package scripts
Summary:        Additional scripts for %{name}
Group:          Development/Tools
AutoReqProv:    no
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{_bindir}/perl
Requires:       %{_bindir}/python

%description scripts
Additional Perl and Python scripts for %{name}.

%description scripts -l fr
Scripts additionels pour %{name}.

%package manual
Summary:        Manual for %{name}
Group:          Documentation

%description manual
Documentation for %{name}.

%description manual -l it
Documentazione di %{name}.

%description manual -l fr
Documentation pour %{name}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation

%description javadoc
Javadoc for %{name}.

%description javadoc -l fr
Javadoc pour %{name}.
%endif

# -----------------------------------------------------------------------------

%prep
%setup -q -n apache-ant-%{cvs_version}
#https://issues.apache.org/bugzilla/show_bug.cgi?id=47669
sed -i -e "s|IMAGE_FILE_TYPE|BINARY_FILE_TYPE|g" src/main/org/apache/tools/ant/taskdefs/optional/net/FTP.java
# Disable the style and xmlvalidate tasks on ppc64 and s390x (#163689).
%ifarch ppc64 s390x
%patch1 -p1
%endif

# Update ant to work with recent versions of GNU Classpath
%patch2 -p1

# When bootstrapping, we don't have junit
%patch3 -p1

# Fix class-path-in-manifest rpmlint warning
%patch4 -p0

%patch5 -p0

# clean jar files
find . -name "*.jar" | %{_bindir}/xargs -t rm

# Fix file-not-utf8 rpmlint warning
iconv KEYS -f iso-8859-1 -t utf-8 -o KEYS.utf8
mv KEYS.utf8 KEYS
iconv LICENSE -f iso-8859-1 -t utf-8 -o LICENSE.utf8
mv LICENSE.utf8 LICENSE

# Provides: exclude perl(oata), perl(examples)
cat <<__EOF__ > %{name}-perl.prov
#!/bin/sh
/usr/lib/rpm/perl.prov \$* | grep -v '^perl(oata)$' | grep -v '^perl(examples)$'
__EOF__
%define __perl_provides %{_builddir}/apache-ant-%{cvs_version}/%{name}-perl.prov
chmod +x %{__perl_provides}


# Requires: exclude bogus perl(the)
cat <<__EOF__ > %{name}-perl.req
#!/bin/sh
/usr/lib/rpm/perl.req \$* | grep -v '^perl(the)$'
__EOF__
%define __perl_requires %{_builddir}/apache-ant-%{cvs_version}/%{name}-perl.req
chmod +x %{__perl_requires}

# -----------------------------------------------------------------------------

%build
export OPT_JAR_LIST=:
%if %without bootstrap
export CLASSPATH=$(build-classpath xerces-j2 xml-commons-jaxp-1.3-apis antlr bcel jaf javamail/mailapi jdepend junit log4j oro regexp bsf commons-logging commons-net jsch xml-commons-resolver)
%{ant} jars
%if %{build_javadoc}
%{ant} javadocs
%endif
%else
export JAVA_HOME=%{java_home}
export CLASSPATH=$JAVA_HOME/lib/tools.jar
sh ./build.sh --noconfig jars
%endif

# -----------------------------------------------------------------------------

%install
rm -rf $RPM_BUILD_ROOT

# ANT_HOME and subdirs
mkdir -p $RPM_BUILD_ROOT%{ant_home}/{lib,etc}

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 build/lib/ant.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
install -m 644 build/lib/ant-bootstrap.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-bootstrap-%{version}.jar
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.apache.ant %{name} %{version} JPP %{name}
install -m 644 build/lib/ant-launcher.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-launcher-%{version}.jar
install -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-launcher.pom
%add_to_maven_depmap org.apache.ant %{name}-launcher %{version} JPP %{name}-launcher

install -m 644 build/lib/ant-jmf.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-jmf-%{version}.jar
install -m 644 %{SOURCE20} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-jmf.pom
%add_to_maven_depmap org.apache.ant %{name}-jmf %{version} JPP/%{name} %{name}-jmf
install -m 644 build/lib/ant-nodeps.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-nodeps-%{version}.jar
install -m 644 %{SOURCE23} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-nodeps.pom
%add_to_maven_depmap org.apache.ant %{name}-nodeps %{version} JPP/%{name} %{name}-nodeps
install -m 644 build/lib/ant-swing.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-swing-%{version}.jar
install -m 644 %{SOURCE24} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-swing.pom
%add_to_maven_depmap org.apache.ant %{name}-swing %{version} JPP/%{name} %{name}-swing
install -m 644 build/lib/ant-trax.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-trax-%{version}.jar
install -m 644 %{SOURCE25} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-trax.pom
%add_to_maven_depmap org.apache.ant %{name}-trax %{version} JPP/%{name} %{name}-trax

# optional jars
%if %without bootstrap
%if %{with_manifest_only}
install -m 644 build/lib/ant-icontract.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-icontract-%{version}.jar
install -m 644 build/lib/ant-netrexx.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-netrexx-%{version}.jar
install -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-netrexx.pom
%add_to_maven_depmap org.apache.ant %{name}-netrexx %{version} JPP/%{name} %{name}-netrexx
install -m 644 build/lib/ant-starteam.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-starteam-%{version}.jar
install -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-starteam.pom
%add_to_maven_depmap org.apache.ant %{name}-starteam %{version} JPP/%{name} %{name}-starteam
install -m 644 build/lib/ant-stylebook.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-stylebook-%{version}.jar
install -m 644 %{SOURCE6} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-stylebook.pom
%add_to_maven_depmap org.apache.ant %{name}-stylebook %{version} JPP/%{name} %{name}-stylebook
install -m 644 build/lib/ant-vaj.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-vaj-%{version}.jar
install -m 644 build/lib/ant-weblogic.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-weblogic-%{version}.jar
install -m 644 %{SOURCE7} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-weblogic.pom
%add_to_maven_depmap org.apache.ant %{name}-weblogic %{version} JPP/%{name} %{name}-weblogic
install -m 644 build/lib/ant-xalan1.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-xalan1-%{version}.jar
install -m 644 build/lib/ant-xslp.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-xslp-%{version}.jar
%endif
install -m 644 build/lib/ant-antlr.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-antlr-%{version}.jar
install -m 644 %{SOURCE8} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-antlr.pom
%add_to_maven_depmap org.apache.ant %{name}-antlr %{version} JPP/%{name} %{name}-antlr
install -m 644 build/lib/ant-apache-bsf.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-apache-bsf-%{version}.jar
install -m 644 %{SOURCE9} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-apache-bsf.pom
%add_to_maven_depmap org.apache.ant %{name}-apache-bsf %{version} JPP/%{name} %{name}-apache-bsf
install -m 644 build/lib/ant-apache-resolver.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-apache-resolver-%{version}.jar
install -m 644 %{SOURCE10} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-apache-resolver.pom
%add_to_maven_depmap org.apache.ant %{name}-apache-resolver %{version} JPP/%{name} %{name}-apache-resolver
install -m 644 build/lib/ant-commons-logging.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-commons-logging-%{version}.jar
install -m 644 %{SOURCE11} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-commons-logging.pom
%add_to_maven_depmap org.apache.ant %{name}-commons-logging %{version} JPP/%{name} %{name}-commons-logging
install -m 644 build/lib/ant-commons-net.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-commons-net-%{version}.jar
install -m 644 %{SOURCE12} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-commons-net.pom
%add_to_maven_depmap org.apache.ant %{name}-commons-net %{version} JPP/%{name} %{name}-commons-net
#install -m 644 build/lib/ant-jai.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-jai-%{version}.jar
#install -m 644 %{SOURCE13} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-jai.pom
#%add_to_maven_depmap org.apache.ant %{name}-jai %{version} JPP/%{name} %{name}-jai
install -m 644 build/lib/ant-apache-bcel.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-apache-bcel-%{version}.jar
install -m 644 %{SOURCE14} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-apache-bcel.pom
%add_to_maven_depmap org.apache.ant %{name}-apache-bcel %{version} JPP/%{name} %{name}-apache-bcel
install -m 644 build/lib/ant-apache-log4j.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-apache-log4j-%{version}.jar
install -m 644 %{SOURCE15} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-apache-log4j.pom
%add_to_maven_depmap org.apache.ant %{name}-apache-log4j %{version} JPP/%{name} %{name}-apache-log4j
install -m 644 build/lib/ant-apache-oro.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-apache-oro-%{version}.jar
install -m 644 %{SOURCE16} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-apache-oro.pom
%add_to_maven_depmap org.apache.ant %{name}-apache-oro %{version} JPP/%{name} %{name}-apache-oro
install -m 644 build/lib/ant-apache-regexp.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-apache-regexp-%{version}.jar
install -m 644 %{SOURCE17} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-apache-regexp.pom
%add_to_maven_depmap org.apache.ant %{name}-apache-regexp %{version} JPP/%{name} %{name}-apache-regexp
ln -sf %{name}-apache-bcel.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-jakarta-bcel.jar
ln -sf %{name}-apache-log4j.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-jakarta-log4j.jar
ln -sf %{name}-apache-oro.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-jakarta-oro.jar
ln -sf %{name}-apache-regexp.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-jakarta-regexp.jar
install -m 644 build/lib/ant-javamail.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-javamail-%{version}.jar
install -m 644 %{SOURCE18} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-javamail.pom
%add_to_maven_depmap org.apache.ant %{name}-javamail %{version} JPP/%{name} %{name}-javamail
install -m 644 build/lib/ant-jdepend.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-jdepend-%{version}.jar
install -m 644 %{SOURCE19} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-jdepend.pom
%add_to_maven_depmap org.apache.ant %{name}-jdepend %{version} JPP/%{name} %{name}-jdepend
install -m 644 build/lib/ant-jsch.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-jsch-%{version}.jar
install -m 644 %{SOURCE21} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-jsch.pom
%add_to_maven_depmap org.apache.ant %{name}-jsch %{version} JPP/%{name} %{name}-jsch
install -m 644 build/lib/ant-junit.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-junit-%{version}.jar
install -m 644 %{SOURCE22} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-junit.pom
%add_to_maven_depmap org.apache.ant %{name}-junit %{version} JPP/%{name} %{name}-junit
install -m 644 %{SOURCE26} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-parent.pom
%add_to_maven_depmap org.apache.ant %{name}-parent %{version} JPP %{name}-parent
%endif

# jar aliases
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do jarname=`echo $jar| sed "s|-%{version}||g"`; ln -sf ${jar} ${jarname}; ln -sf ../../java/${jarname} $RPM_BUILD_ROOT%{ant_home}/lib/${jarname}; done)
(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}.jar; do jarname=`echo $jar| sed "s|-%{version}||g"`; ln -sf ${jar} ${jarname}; ln -sf ../../java/%{name}/${jarname} $RPM_BUILD_ROOT%{ant_home}/lib/${jarname}; done)

# scripts: remove dos and os/2 scripts
rm -f src/script/*.bat
rm -f src/script/*.cmd

# XSLs
cp -p src/etc/*.xsl $RPM_BUILD_ROOT%{ant_home}/etc

# install everything else
mkdir -p $RPM_BUILD_ROOT%{_bindir}
%if %without bootstrap
cp -p src/script/* $RPM_BUILD_ROOT%{_bindir}
%else
cp -p src/script/ant{,Run} $RPM_BUILD_ROOT%{_bindir}
%endif

# default ant.conf
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.conf

# OPT_JAR_LIST fragments
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d
echo "ant/ant-jmf" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/jmf
echo "ant/ant-nodeps" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/nodeps
echo "ant/ant-swing" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/swing
echo "jaxp_transform_impl ant/ant-trax xalan-j2-serializer" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/trax
%if %without bootstrap
echo "antlr ant/ant-antlr" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/antlr
echo "bsf ant/ant-apache-bsf" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/apache-bsf
echo "xml-commons-resolver ant/ant-apache-resolver" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/apache-resolver
echo "jakarta-commons-logging ant/ant-commons-logging" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/commons-logging
echo "jakarta-commons-net ant/ant-commons-net" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/commons-net
#echo "jai ant/ant-jai" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/jai
echo "bcel ant/ant-apache-bcel" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/apache-bcel
echo "log4j ant/ant-apache-log4j" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/apache-log4j
echo "oro ant/ant-apache-oro" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/apache-oro
echo "regexp ant/ant-apache-regexp" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/apache-regexp
echo "javamail jaf ant/ant-javamail" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/javamail
echo "jdepend ant/ant-jdepend" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/jdepend
echo "jsch ant/ant-jsch" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/jsch
echo "junit ant/ant-junit" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/junit
%endif

%if %{build_javadoc}
# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/javadocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%endif

# fix link between manual and javadoc
(cd docs/manual; ln -sf %{_javadocdir}/%{name}-%{version} api)

%if %with bootstrap
find $RPM_BUILD_ROOT%{_datadir}/ant/etc -type f -name "*.xsl" \
                                                 -a ! -name ant-update.xsl \
                                                 -a ! -name changelog.xsl \
                                                 -a ! -name coverage-frames.xsl \
                                                 -a ! -name junit-frames-xalan1.xsl \
                                                 -a ! -name log.xsl \
                                                 -a ! -name mmetrics-frames.xsl \
                                                 -a ! -name tagdiff.xsl \
                                                 | xargs -t rm
%endif

# -----------------------------------------------------------------------------

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%clean
rm -rf $RPM_BUILD_ROOT

# -----------------------------------------------------------------------------

%post
%update_maven_depmap
%if %{gcj_support}
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%postun
%update_maven_depmap
%if %{gcj_support}
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%post jmf
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun jmf
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%post nodeps
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun nodeps
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%post swing
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun swing
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%post trax
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun trax
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %without bootstrap
%if %{gcj_support}
%post commons-net
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun commons-net
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

# We do not ship dependencies for these, so they are disabled.
%if 0
%if %{gcj_support}
%post jai
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun jai
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif
%endif

%if %{gcj_support}
%post antlr
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun antlr
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%post apache-bcel
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun apache-bcel
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%post apache-log4j
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun apache-log4j
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%post apache-regexp
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun apache-regexp
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%post apache-resolver
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun apache-resolver
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%post junit
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun junit
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%post apache-oro
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun apache-oro
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%post javamail
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun javamail
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%post commons-logging
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun commons-logging
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%post jdepend
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun jdepend
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%post jsch
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun jsch
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%post apache-bsf
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun apache-bsf
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif
%endif

%files
%defattr(0644,root,root,0755)
%doc KEYS LICENSE NOTICE README WHATSNEW
%config(noreplace) %{_sysconfdir}/%{name}.conf
%attr(0755,root,root) %{_bindir}/ant
%attr(0755,root,root) %{_bindir}/antRun
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}-launcher.jar
%{_javadir}/%{name}-launcher-%{version}.jar
%{_javadir}/%{name}-bootstrap.jar
%{_javadir}/%{name}-bootstrap-%{version}.jar
%dir %{_javadir}/%{name}
%dir %{ant_home}
%dir %{ant_home}/etc
%{ant_home}/etc/ant-update.xsl
%{ant_home}/etc/changelog.xsl
%{ant_home}/etc/log.xsl
%{ant_home}/etc/tagdiff.xsl
%{ant_home}/etc/junit-frames-xalan1.xsl
%if %without bootstrap
%{ant_home}/etc/common2master.xsl
%endif
%dir %{ant_home}/lib
%{ant_home}/lib/%{name}.jar
%{ant_home}/lib/%{name}-launcher.jar
%{ant_home}/lib/%{name}-bootstrap.jar
%dir %{_sysconfdir}/%{name}.d
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/ant-%{version}.jar.*
%attr(-,root,root) %{_libdir}/gcj/%{name}/ant-launcher-%{version}.jar.*
%endif

%files jmf
%defattr(0644,root,root,0755)
%{_javadir}/%{name}/%{name}-jmf.jar
%{_javadir}/%{name}/%{name}-jmf-%{version}.jar
%{ant_home}/lib/%{name}-jmf.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/jmf
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/ant-jmf-%{version}.jar.*
%endif

%files nodeps
%defattr(0644,root,root,0755)
%{_javadir}/%{name}/%{name}-nodeps.jar
%{_javadir}/%{name}/%{name}-nodeps-%{version}.jar
%{ant_home}/lib/%{name}-nodeps.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/nodeps
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/ant-nodeps-%{version}.jar.*
%endif

%files swing
%defattr(0644,root,root,0755)
%{_javadir}/%{name}/%{name}-swing.jar
%{_javadir}/%{name}/%{name}-swing-%{version}.jar
%{ant_home}/lib/%{name}-swing.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/swing
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/ant-swing-%{version}.jar.*
%endif

%files trax
%defattr(0644,root,root,0755)
%{_javadir}/%{name}/%{name}-trax.jar
%{_javadir}/%{name}/%{name}-trax-%{version}.jar
%{ant_home}/lib/%{name}-trax.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/trax
%{ant_home}/etc/mmetrics-frames.xsl
%{ant_home}/etc/coverage-frames.xsl
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/ant-trax-%{version}.jar.*
%endif

%if %without bootstrap
%if %{with_manifest_only}
%files manifest-only
%defattr(0644,root,root,0755)
%{_javadir}/%{name}/ant-icontract-%{version}.jar
%{_javadir}/%{name}/ant-icontract.jar
%{_javadir}/%{name}/ant-netrexx-%{version}.jar
%{_javadir}/%{name}/ant-netrexx.jar
%{_javadir}/%{name}/ant-starteam-%{version}.jar
%{_javadir}/%{name}/ant-starteam.jar
%{_javadir}/%{name}/ant-stylebook-%{version}.jar
%{_javadir}/%{name}/ant-stylebook.jar
%{_javadir}/%{name}/ant-vaj-%{version}.jar
%{_javadir}/%{name}/ant-vaj.jar
%{_javadir}/%{name}/ant-weblogic-%{version}.jar
%{_javadir}/%{name}/ant-weblogic.jar
%{_javadir}/%{name}/ant-xalan1-%{version}.jar
%{_javadir}/%{name}/ant-xalan1.jar
%{_javadir}/%{name}/ant-xslp-%{version}.jar
%{_javadir}/%{name}/ant-xslp.jar
%endif

%files antlr
%defattr(0644,root,root,0755)
%{_javadir}/%{name}/%{name}-antlr.jar
%{_javadir}/%{name}/%{name}-antlr-%{version}.jar
%{ant_home}/lib/%{name}-antlr.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/antlr
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/ant-antlr-%{version}.jar.*
%endif

%files apache-bsf
%defattr(0644,root,root,0755)
%{_javadir}/%{name}/%{name}-apache-bsf.jar
%{_javadir}/%{name}/%{name}-apache-bsf-%{version}.jar
%{ant_home}/lib/%{name}-apache-bsf.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/apache-bsf
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/ant-apache-bsf-%{version}.jar.*
%endif

%files apache-resolver
%defattr(0644,root,root,0755)
%{_javadir}/%{name}/%{name}-apache-resolver.jar
%{_javadir}/%{name}/%{name}-apache-resolver-%{version}.jar
%{ant_home}/lib/%{name}-apache-resolver.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/apache-resolver
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/ant-apache-resolver-%{version}.jar.*
%endif

%files commons-logging
%defattr(0644,root,root,0755)
%{_javadir}/%{name}/%{name}-commons-logging.jar
%{_javadir}/%{name}/%{name}-commons-logging-%{version}.jar
%{ant_home}/lib/%{name}-commons-logging.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/commons-logging
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/ant-commons-logging-%{version}.jar.*
%endif

%files commons-net
%defattr(0644,root,root,0755)
%{_javadir}/%{name}/%{name}-commons-net.jar
%{_javadir}/%{name}/%{name}-commons-net-%{version}.jar
%{ant_home}/lib/%{name}-commons-net.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/commons-net
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/ant-commons-net-%{version}.jar.*
%endif

# Disable as we dont ship the dependencies
%if 0
%files jai
%defattr(0644,root,root,0755)
%{_javadir}/%{name}/%{name}-jai.jar
%{_javadir}/%{name}/%{name}-jai-%{version}.jar
%{ant_home}/lib/%{name}-jai.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/jai
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/ant-jai-%{version}.jar.*
%endif
%endif

%files apache-bcel
%defattr(0644,root,root,0755)
%{_javadir}/%{name}/%{name}-apache-bcel.jar
%{_javadir}/%{name}/%{name}-apache-bcel-%{version}.jar
%{_javadir}/%{name}/%{name}-jakarta-bcel.jar
%{ant_home}/lib/%{name}-apache-bcel.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/apache-bcel
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/ant-apache-bcel-%{version}.jar.*
%endif

%files apache-log4j
%defattr(0644,root,root,0755)
%{_javadir}/%{name}/%{name}-apache-log4j.jar
%{_javadir}/%{name}/%{name}-apache-log4j-%{version}.jar
%{_javadir}/%{name}/%{name}-jakarta-log4j.jar
%{ant_home}/lib/%{name}-apache-log4j.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/apache-log4j
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/ant-apache-log4j-%{version}.jar.*
%endif

%files apache-oro
%defattr(0644,root,root,0755)
%{_javadir}/%{name}/%{name}-apache-oro.jar
%{_javadir}/%{name}/%{name}-apache-oro-%{version}.jar
%{_javadir}/%{name}/%{name}-jakarta-oro.jar
%{ant_home}/lib/%{name}-apache-oro.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/apache-oro
%{ant_home}/etc/maudit-frames.xsl
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/ant-apache-oro-%{version}.jar.*
%endif

%files apache-regexp
%defattr(0644,root,root,0755)
%{_javadir}/%{name}/%{name}-apache-regexp.jar
%{_javadir}/%{name}/%{name}-apache-regexp-%{version}.jar
%{_javadir}/%{name}/%{name}-jakarta-regexp.jar
%{ant_home}/lib/%{name}-apache-regexp.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/apache-regexp
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/ant-apache-regexp-%{version}.jar.*
%endif

%files javamail
%defattr(0644,root,root,0755)
%{_javadir}/%{name}/%{name}-javamail.jar
%{_javadir}/%{name}/%{name}-javamail-%{version}.jar
%{ant_home}/lib/%{name}-javamail.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/javamail
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/ant-javamail-%{version}.jar.*
%endif

%files jdepend
%defattr(0644,root,root,0755)
%{_javadir}/%{name}/%{name}-jdepend.jar
%{_javadir}/%{name}/%{name}-jdepend-%{version}.jar
%{ant_home}/lib/%{name}-jdepend.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/jdepend
%{ant_home}/etc/jdepend.xsl
%{ant_home}/etc/jdepend-frames.xsl
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/ant-jdepend-%{version}.jar.*
%endif

%files jsch
%defattr(0644,root,root,0755)
%{_javadir}/%{name}/%{name}-jsch.jar
%{_javadir}/%{name}/%{name}-jsch-%{version}.jar
%{ant_home}/lib/%{name}-jsch.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/jsch
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/ant-jsch-%{version}.jar.*
%endif

%files junit
%defattr(0644,root,root,0755)
%{_javadir}/%{name}/%{name}-junit.jar
%{_javadir}/%{name}/%{name}-junit-%{version}.jar
%{ant_home}/lib/%{name}-junit.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/junit
%{ant_home}/etc/junit-frames.xsl
%{ant_home}/etc/junit-noframes.xsl
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/ant-junit-%{version}.jar.*
%endif

%files scripts
%defattr(0755,root,root,0755)
%{_bindir}/*.pl
%{_bindir}/*.py*

%files manual
%defattr(0644,root,root,0755)
%doc docs/*

%if %{build_javadoc}
%files javadoc
%defattr(0644,root,root,0755)
%{_javadocdir}/%{name}-%{version}
%endif
%endif

# -----------------------------------------------------------------------------

%changelog
* Mon Apr 26 2010 Jeff Johnston <jjohnstn@redhat.com> - 0:1.7.1-13
- Resolves: #585941
- Added apache-ant-package-info-bz43114.patch

* Wed Feb 03 2010 Jeff Johnston <jjohnstn@redhat.com> - 0:1.7.1-12.4
- Fix license to include W3C

* Wed Feb 03 2010 Jeff Johnston <jjohnstn@redhat.com> - 0:1.7.1-12.3
- Fix source URL

* Wed Feb 03 2010 Jeff Johnston <jjohnstn@redhat.com> - 0:1.7.1-12.2
- Fix rpmlint warnings

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0:1.7.1-12.1
- Rebuilt for RHEL 6

* Thu Aug 13 2009 Alexander Kurtakov <akurtako@redhat.com> 0:1.7.1-12
- Fix compile with commons-net 2.0.

* Fri Aug  7 2009 Orion Poplawski <orion@cora.nwra.com> - 0:1.1.7-11
- Add links to jar files into %%{ant_home} (Bug #179759)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.7.1-10.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.7.1-9.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 01 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0:1.7.1-8.2
- Rebuild for Python 2.6

* Wed Oct  1 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0:1.7.1-7.2
- Exclude bogus perl(the) Requires
- Exclude bogus perl(oata), perl(examples) Provides

* Fri Sep 26 2008 Permaine Cheung <pcheung@redhat.com> 0:1.7.1-7.1
- Define with_gcj_support

* Tue Sep 23 2008 Permaine Cheung <pcheung@redhat.com> 0:1.7.1-7
- Update to 1.7.1
- Fix some rpmlint issues

* Tue Jul 15 2008 David Walluck <dwalluck@redhat.com> 0:1.7.1-7
- enable non-bootstrap

* Tue Jul 15 2008 David Walluck <dwalluck@redhat.com> 0:1.7.1-6
- add ant-bootstrap jar if bootstrap is enabled
- enable jmf, swing, trax if bootstrap is enabled
- BuildRequires: jaxp_transform_impl
- BuildRequires: junit for non-bootstrap

* Tue Jul 15 2008 David Walluck <dwalluck@redhat.com> 0:1.7.1-5
- enable ant-nodeps in bootstrap mode

* Tue Jul 15 2008 David Walluck <dwalluck@redhat.com> 0:1.7.1-4
- remove junit for bootstrap

* Tue Jul 15 2008 David Walluck <dwalluck@redhat.com> 0:1.7.1-3
- build as bootstrap

* Tue Jul 15 2008 David Walluck <dwalluck@redhat.com> 0:1.7.1-2
- set rpm_mode=false by default

* Thu Jul 10 2008 David Walluck <dwalluck@redhat.com> 0:1.7.1-1
- 1.7.1
- update maven pom files
- rediff apache-ant-jars.patch
- rediff apache-ant-bz163689.patch
- add apache-ant-gnu-classpath.patch
- set rpm_mode=true in conf since the ant script handles the rest

* Thu Jul 10 2008 David Walluck <dwalluck@redhat.com> 0:1.7.0-3
- add bootstrap mode
- replace some alternatives/virtual requires by explicit requires
- remove javadoc scriptlets
- fix GCJ support
- add workaround for xalan-j2 in %%{_sysconfdir}/%%{name}.d/trax
- version Obsoletes and add Provides
- remove Conflicts
- mark files in %%{_sysconfdir} as %%config(noreplace)

* Thu Jul 03 2007 Ralph Apel <r.apel at r-apel.de> - 0:1.7.0-2.jpp5
- Add poms and depmap frags
- (B)R jpackage-utils >= 0:1.7.5
- BR java-devel = 0:1.5.0
- R java >= 0:1.5.0

* Wed Jun 20 2007 Fernando Nasser <fnasser at redhat.com> - 0:1.7.0-1jpp
- Upgrade to the final 1.7.0

* Thu Sep 21 2006 Will Tatam <will.tatam@red61.com> - 0:1.7.0-0.Beta1.1jpp
- Upgraded to 1.7.0Beta1
- removed the apache-ant-1.6.5-jvm1.5-detect.patch as merged upstream

* Fri Aug 11 2006 Deepak Bhole <dbhole@redhat.com> - 0:1.6.5-2jpp
- Added conditional native compilation
- Added patch to fix jvm version detection
- Add missing requirements
- Synch with Fedora spec

* Wed Nov 09 2005 Fernando Nasser <fnasser at redhat.com> - 0:1.6.5-1jpp
- Upgrade to 1.6.5
- Incorporate the following changes:
  From Gary Benson <gbenson at redhat.com>:
- Allow subpackages not in Fedora to be installed from JPackage
- Add NOTICE file as per Apache License version 2.0
- Own /usr/share/java/ant
  From Vadim Nasardinov <vadimn@redhat.com>
- Removed apache-ant-1.6.2.patch.  Incorporated upstream.
  From David Walluck <david@jpackage.org>
- Add manifest-only package (mainly for eclipse)
- Add conflicts on j2sdk for Mandriva

* Mon Nov  8 2004 Gary Benson <gbenson at redhat.com> - 0:1.6.2-3jpp
- Build OPT_JAR_LIST from files in /etc/ant.d.

* Mon Sep 06 2004 Fernando Nasser <fnasser at redhat.com> - 0:1.6.2-2jpp
- Fix to backward compatibility symbolic links.

* Wed Aug 17 2004 Fernando Nasser <fnasser at redhat.com> - 0:1.6.2-1jpp
- Update to Ant 1.6.2

* Thu Aug 05 2004 Fernando Nasser <fnasser at redhat.com> - 0:1.6.1-2jpp
- Remove incorrect noreplace option for ant.conf; it can't be used anymore
  because the sub-packages update that file.
- Add patch to fix temp directory used for file containing large
  command strings (> 4k)

* Tue Jun 01 2004 Randy Watler <rwatler at finali.com> - 0:1.6.1-1jpp
- Extend subpackage builds to update ant.conf

* Tue Mar 23 2004 Randy Watler <rwatler at finali.com> - 0:1.6.1-1jpp
- Update to Ant 1.6.1
- Change ant launch script to source instead of patch
- Move optional components to ant subdirectory: %%{_javadir}/%%{name}
- Remove os/2 scripts and set JAVA_HOME for build

* Wed Feb 11 2004 Randy Watler <rwatler at finali.com> - 0:1.6.0-1jpp
- Update to Ant 1.6.0
- Break out optional/optional-full components
- Revise ant launch scripts and support ~/.ant/ant.conf configuration file
- Use --noconfig flag to bootstrap ant build and override existing jpp config
- Modify ant launcher to use ant.library.dir property to find extra jars
- Port changes made in ant launch script for 1.6.2 back into patches

* Wed Aug 13 2003 Paul Nasrat <pauln at truemesh.com> - 0:1.5.4-2jpp
- remove bogus NoSource entries

* Tue Aug 12 2003 Paul Nasrat <pauln at truemesh.com> - 0:1.5.4-1jpp
- Update to 1.5.4
- JavaCC task fixed using merged upstream patches from ant HEAD

* Mon May  5 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.5.3-2jpp
- Fix non-versioned javadoc symlinking.

* Tue Apr 22 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.5.3-1jpp
- Update to 1.5.3.
- Remove runtime java-devel dependency.
- Add Epochs in all Provides and Requires.
- Include non-versioned javadoc symlink.
- Build without dependencies that are partially or completely missing from
  JPackage 1.5 (oldbsf, xalan-j1, stylebook1.0b3).
- Add netcomponents to optional jar list in ant.conf.

* Tue Apr 01 2003 Nicolas Mailhot <Nicolas.Mailhot at JPackage.org> - 1.5.2-13jpp
- ant-optional is optional (silly me)
- jaxp_transform is optional , do not require it
- epoch, correct jpackage-utils requires...

* Fri Mar 21 2003 Nicolas Mailhot <Nicolas.Mailhot at JPackage.org> - 1.5.2-11jpp
- add an optional jar list as per Ville's suggestion

* Thu Mar 20 2003 Nicolas Mailhot <Nicolas.Mailhot at JPackage.org> - 1.5.2-10jpp
- hopefully fix CLASSSPATH_OVERRIDE behaviour

* Tue Mar 18 2003 Nicolas Mailhot <Nicolas.Mailhot at JPackage.org> - 1.5.2-7jpp
- for JPackage-utils 1.5

* Wed Mar 12 2003 Ville Skyttä <ville.skytta at iki.fi> - 1.5.2-5jpp
- Move ANT_HOME to /usr/share/ant.
- Don't special-case the lib dir for RPM layout any more, use ANT_HOME/lib.
- Install XSLs into ANT_HOME/etc.
- Call set_jvm by default in ant.conf.
- Provide ant-optional-clean (versioned) in ant-optional.
- Make ant-optional-full conflict with ant-optional-clean.
- Add version info to ant-optional provision in ant-optional-full.
- Built with Sun 1.4.1_02 javac (to get JDK 1.4 regex).

* Tue Mar 11 2003 Henri Gomez <hgomez@users.sourceforge.net> 1.5.2-4jp
- changed provided /etc/ant.conf so that if usejikes is allready provided
  it didn't set it. Which such modification if you want to disable
  ant to use jikes even if jikes is set in /etc/ant.conf you'll just have
  to do usejikes=false ant build.xml.

* Mon Mar 10 2003 Henri Gomez <hgomez@users.sourceforge.net> 1.5.2-3jp
- rebuilt with IBM SDK 1.3.1 since there was zip corruption when built
  with jikes 1.18 and IBM SDK 1.4.

* Wed Mar 05 2003 Henri Gomez <hgomez@users.sourceforge.net> 1.5.2-2jp
- updated URL and source location

* Wed Mar 05 2003 Henri Gomez <hgomez@users.sourceforge.net> 1.5.2-1jp
- 1.5.2
- remove JDK 1.4 related patchs which are now included in ant 1.5.2
- fix ant-optional-full pre/post install script (now remove correctly all
  ant optional jars)
- Built with jikes 1.18 and IBM SDK 1.4

* Sat Feb  1 2003 Ville Skyttä <ville.skytta at iki.fi> - 1.5.1-8jpp
- Symlink a transformer into ANT_LIB for smoother experience on Java 1.3.
- Requires jaxp_transform_impl.
- Don't remove optional.jar symlinks on optional-full upgrade.
- Include Sun's 1.4 JSSE and JCE jars in runtime path, see
  <http://nagoya.apache.org/bugzilla/show_bug.cgi?id=16242>.
- Use jpackage-utils for setting JAVA_HOME when building.
- Built with Sun 1.4.1_01 javac.

* Mon Jan 20 2003 David Walluck <david@anti-microsoft.org> 1.5.1-7jpp
- oldbsf

* Fri Dec 20 2002 Ville Skyttä <ville.skytta at iki.fi> - 1.5.1-6jpp
- Really get rid of automatic dependencies for the -scripts package.

* Wed Dec 18 2002 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.5.1-5jpp
- scripts subpackages
- file-based manual dependencies, as packages doesn't have the same name on RedHat and Mandrake

* Wed Dec 11 2002 Ville Skyttä <ville.skytta at iki.fi> - 1.5.1-4jpp
- Patched to allow easier use with Jikes and IBM's 1.4.0, see
  <http://nagoya.apache.org/bugzilla/show_bug.cgi?id=15289> for details.

* Mon Oct 07 2002 Henri Gomez <hgomez@users.sourceforge.net> 1.5.1-3jpp
- new post script for optional-full since rpm didn't works as
  expected and didn't set correct symlink for ant-optional.jar

* Thu Oct 03 2002 Henri Gomez <hgomez@users.sourceforge.net> 1.5.1-2jpp
- really used JDK 1.4.1 to get JDK 1.4.x Regexp

* Thu Oct 03 2002 Henri Gomez <hgomez@users.sourceforge.net> 1.5.1-1jpp
- ant 1.5.1

* Fri Jul 12 2002 Henri Gomez <hgomez@users.sourceforge.net> 1.5-5jpp
- ant script standard behaviour restored, ie ant/lib jars are taken
  before CLASSPATH. You should define CLASSPATH_OVERRIDE env var to have
  CLASSPATH before ant/lib jars
- applied ant script patch for cygwin (cygwin rpm users around ?)
- remove conflict in ant-optional-full, just put provides

* Fri Jul 12 2002 Henri Gomez <hgomez@users.sourceforge.net> 1.5-4jpp
- fix a problem in xerces-j2 build by changing the way CLASSPATH is constructed:
  first add jars found in CLASSPATH, then add xml-commons-apis, jaxp_parser_impl,
  ant, ant-optional and finish with jars found in ant/lib.
- jpackage-utils is no more required (but recommanded :)
- ant-optional-full provides ant-optional
- fix link between manual and api (javadoc)

* Thu Jul 11 2002 Henri Gomez <hgomez@users.sourceforge.net> 1.5-3jpp
- add missing symlink between optional-full.jar and optional.jar

* Wed Jul 10 2002 Ville Skyttä <ville.skytta at iki.fi> 1.5-2jpp
- Requires jaxp_parser_impl, no longer jaxp_parser2
  (jaxp_parser_impl already requires xml-commons-apis).
- Use sed instead of bash 2 extension when symlinking.

* Wed Jul 10 2002 Henri Gomez <hgomez@users.sourceforge.net> 1.5-1jpp
* ant 1.5

* Tue Jul 09 2002 Henri Gomez <hgomez@users.sourceforge.net> 1.5.Beta3-1jpp
- ant 1.5 beta 3
- added bcel as required

* Tue Jul 09 2002 Henri Gomez <hgomez@users.sourceforge.net> 1.4.1-14jpp
- added regexp to list of dependant packages

* Tue Jul 09 2002 Henri Gomez <hgomez@users.sourceforge.net> 1.4.1-13jpp
- added optional-full which include all ant tasks, even those without
  matching package
- added jdepend 2.2
- remove require oro, since ant could works without it
- ant lib is now in %%{_javadir}/%%{name}, put external jars here

* Tue May 07 2002 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.4.1-12jpp
- hardcoded distribution and vendor tag
- group tag again

* Thu May 2 2002 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.4.1-11jpp
- no more jikes specific support in launch script
- source user prefs before configuration in launch script
- distribution tag
- group tag
- provided original script as documentation

* Fri Apr 05 2002 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.4.1-10jpp
- used xalan-j1 instead of xalan-j2-compat

* Mon Mar 11 2002 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.4.1-9jpp
- jaxp_parser2 support

* Wed Feb 06 2002 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.4.1-8jpp
- netcomponents support

* Sun Jan 27 2002 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.4.1-7jpp
- adaptation to new stylebook1.0b3 package
- stylebook is a dependency of optional package
- removed redundant dependencies
- launch script correction

* Fri Jan 25 2002 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.4.1-6jpp
- cleaned manifest from class-path references
- section macro

* Thu Jan 17 2002 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.4.1-5jpp
- versioned dir for javadoc
- no dependencies for manual and javadoc packages
- stricter dependency for optional package
- additional sources in individual archives
- upgraded launch script
- no more javadoc cross-linking
- additional requirement for optional package: xml-commons-apis, xalan-j2, xalan-j2-compat, jaf, javamail, & log4j

* Sat Dec 1 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.4.1-4jpp
- removed conditional build
- removed redundant BuildRequires
- ant-optional.jar in ant-optional package
- javadoc into javadoc package
- new launch script using functions library

* Wed Nov 21 2001 Christian Zoffoli <czoffoli@littlepenguin.org> 1.4.1-3jpp
- readded Requires: oro junit stylebook-1.0b3 bsf rhino antlr to the main package
- corrected changelog release 1jpp-> 2jpp

* Tue Nov 20 2001 Christian Zoffoli <czoffoli@littlepenguin.org> 1.4.1-2jpp
- conditional build
- removed packager tag
- new jpp extension
- added xalan 2.2.D13 support
- added BuildRequires: xalan-j2 >= 2.2.D13
- removed Requires: oro junit stylebook-1.0b3 bsf rhino antlr

* Mon Oct 15 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.4.1-1jpp
- 1.4.1

* Sat Oct 6 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.4-4jpp
- used original tarball

* Sun Sep 30 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.4-3jpp
- more macros

* Wed Sep 26 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.4-2jpp
- first unified release
- dropped explicit xalan-j2 requirement, as stylebook-1.0b3 already requires it
- added missing xalan-j1 compatibility classes
- s/jPackage/JPackage

* Wed Sep 05 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.4-1mdk
- 1.4
- added xalan-j2 antlr bsf rhino to buildrequires and requires
- launch script cleanup

* Tue Jul 31 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.3-4mdk
- jaxp_parser symlink is now jaxp_parser.jar

* Thu Jul 26 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.3-3mdk
- used alternative jaxp_parser
- updated launch script

* Sat Jun 23 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.3-2mdk
- s/Copyright/License/
- truncated description to 72 columns in spec
- updated launch script

* Mon Jun 11 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.3-1mdk
- 1.3
- new versioning scheme
- compiled with oro, junit and stylebook support
- spec cleanup

* Sat Mar 10 2001 Guillaume Rousse <guillomovitch@users.sourceforge.net> 1.2-9mdk
- vendor tag
- packager tag

* Sat Feb 17 2001 Guillaume Rousse <g.rousse@linux-mandrake.com> 1.2-8mdk
- spec cleanup
- corrected changelog
- changed description

* Sun Feb 04 2001 Guillaume Rousse <g.rousse@linux-mandrake.com> 1.2-7mdk
- launch script improvments (Christian Zoffoli <czoffoli@linux-mandrake.com>)
- added french in spec
- more macros

* Fri Feb 02 2001 Guillaume Rousse <g.rousse@linux-mandrake.com> 1.2-6mdk
- corrected launch script

* Thu Feb 01 2001 Christian Zoffoli <czoffoli@linux-mandrake.com> 1.2-5mdk
- more macros
- added italian in spec

* Wed Jan 31 2001 Guillaume Rousse <g.rousse@linux-mandrake.com> 1.2-4mdk
- merged with Henri Gomez <hgomez@users.sourceforge.net> specs:
- changed name to ant
- changed javadir to /usr/share/java
- dropped jdk and jre requirement
- corrected require to jaxp
- added Jikes support
- used our own bash script
- dropped perl script
- dropped ant home directory

* Sun Jan 14 2001 Guillaume Rousse <g.rousse@linux-mandrake.com> 1.2-3mdk
- changed name to jakarta-ant
- changed group to Development/Java

* Wed Jan 04 2001 Guillaume Rousse <g.rousse@linux-mandrake.com> 1.2-2mdk
- new spec file
- discarded ugly non-free Sun jaxp library from sources, and used pretty open-source xerces instead

* Wed Dec 20 2000 Guillaume Rousse <g.rousse@linux-mandrake.com> 1.2-1mdk
- first Mandrake release
- used SRPMS from Henri Gomez <hgomez@users.sourceforge.net>
