rm -rf /root/rpmbuild;
mkdir -p /root/rpmbuild/{SPECS,SOURCES};
cat > /root/rpmbuild/SPECS/1.spec << _BAOYILUO_
Name:	pym_server	
Version:	2.0
Release:	1
Requires:       redis,python-redis,pyssh
Summary:this is a monitor server rpm!	

Group:	CSVT	
License:GPL	
URL:	http://www.csvt.net	
Source0: %{name}-%{version}.tar.gz	
BuildRoot:	/var/tmp/%{name}-buildroot

%description
Installs /etc/init.d/
Installs /usr/sbin/

%prep
%setup -q -n %{name}-%{version}

%build
echo Done!

%install
rm -rf \$RPM_BUILD_ROOT
mkdir -p \$RPM_BUILD_ROOT/pym_server
install -m 755 %{SOURCE0} \$RPM_BUILD_ROOT/pym_server

%clean
[ "\$RPM_BUILD_ROOT" != "/" ] && rm -rf \$RPM_BUILD_ROOT

%post
cd /pym_server > /dev/null 2>&1;
tar zxvf pym_server-2.0.tar.gz  > /dev/null 2>&1;
cp pym_server-2.0/init.d/* /etc/init.d/ > /dev/null 2>&1;
chmod 777 -R pym_server-2.0/sbin/* > /dev/null 2>&1;
cp pym_server-2.0/sbin/* /usr/sbin/ > /dev/null 2>&1;
mkdir /etc/pymonitor/ > /dev/null 2>&1;
mkdir /var/log/pymonitor/ > /dev/null 2>&1;
cp pym_server-2.0/conf/* /etc/pymonitor/ > /dev/null 2>&1;
rm -rf /pym_server > /dev/null 2>&1;

%preun

/etc/init.d/pym_server stop > /dev/null 2>&1;
rm -rf /var/log/pymonitor/pym_server.log;rm -rf /etc/pymonitor/pym_server.conf;
rm -rf /usr/sbin/pym_server;
rm -rf /etc/init.d/pym_server;
if [ ! \`ls /etc/pymonitor\` ]
then
rm -rf /etc/pymonitor;
fi

%files
%defattr(-,root,root,-)
%dir /pym_server/*
%doc



%changelog
_BAOYILUO_
dir=`pwd`;
mkdir -p /root/rpmbuild/SOURCES/pym_server-2.0;
cp -r ./conf /root/rpmbuild/SOURCES/pym_server-2.0;
mv ./sbin/pym_server ./sbin/pym_server.py;
/usr/bin/python -c "import compileall;compileall.compile_dir('./sbin')";
mv ./sbin/pym_server.pyc ./sbin/pym_server;
mv ./sbin/pym_server.py ./;
cp -r ./sbin /root/rpmbuild/SOURCES/pym_server-2.0;
mv ./pym_server.py ./sbin/pym_server;
cp -r ./init.d_compiled /root/rpmbuild/SOURCES/pym_server-2.0/init.d;
rm -rf `find /root/rpmbuild/SOURCES/pym_server-2.0 -name .svn`;
cd /root/rpmbuild/SOURCES/;
chmod -R 777 pym_server-2.0;
tar zcvf pym_server-2.0.tar.gz pym_server-2.0;
rpmbuild -ba /root/rpmbuild/SPECS/1.spec;
cd $dir;
mv /root/rpmbuild/RPMS/x86_64/pym_server-2.0-1.x86_64.rpm ./pym_server-2.0.1-el6.x86_64.rpm;
rm -rf /root/rpmbuild;
