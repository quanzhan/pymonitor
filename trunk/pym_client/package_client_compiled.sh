rm -rf /root/rpmbuild;
mkdir -p /root/rpmbuild/{SPECS,SOURCES};
cat > /root/rpmbuild/SPECS/1.spec << _BAOYILUO_
Name:	pym_client	
Version:	2.0
Release:	1
Requires:       python-setuptools,pyssh
Summary:this is a monitor client rpm!	

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
mkdir -p \$RPM_BUILD_ROOT/pym_client
install -m 755 %{SOURCE0} \$RPM_BUILD_ROOT/pym_client

%clean
[ "\$RPM_BUILD_ROOT" != "/" ] && rm -rf \$RPM_BUILD_ROOT

%post
cd /pym_client > /dev/null 2>&1;
tar zxvf pym_client-2.0.tar.gz  > /dev/null 2>&1;
cp pym_client-2.0/init.d/* /etc/init.d/ > /dev/null 2>&1;
chmod 777 -R pym_client-1.0/sbin/* > /dev/null 2>&1;
cp pym_client-2.0/sbin/* /usr/sbin/ > /dev/null 2>&1;
mkdir /etc/pymonitor/ > /dev/null 2>&1;
mkdir /var/log/pymonitor/ > /dev/null 2>&1;
cp pym_client-2.0/conf/* /etc/pymonitor/ > /dev/null 2>&1;
cd pym_client-2.0 > /dev/null 2>&1;
tar zxvf pym_client-2.0.1.tar.gz > /dev/null 2>&1;
cd pym_client-2.0.1 > /dev/null 2>&1;
/usr/bin/python setup.py install --record /var/log/pymonitor/pym_client_lib.log > /dev/null 2>&1;
rm -rf /pym_client > /dev/null 2>&1;

	


%preun
cat  /var/log/pymonitor/pym_client_lib.log | xargs rm -rf;
rm -rf /var/log/pymonitor/pym_client_lib.log;
/etc/init.d/pym_client stop > /dev/null 2>&1;
rm -rf /etc/init.d/pym_client; rm -rf /usr/sbin/pym_client; rm -fr /etc/pymonitor/pym_client.conf;rm -rf /var/log/pymonitor/pym_client.log;
if [ ! \`ls /etc/pymonitor\` ]
then
rm -rf /etc/pymonitor;
fi

%files
%defattr(-,root,root,-)
%dir /pym_client/*
%doc



%changelog

_BAOYILUO_
dir=`pwd`;
mkdir -p /root/rpmbuild/SOURCES/pym_client-2.0;
cp -r ./conf /root/rpmbuild/SOURCES/pym_client-2.0;
cp -r ./init.d_compiled /root/rpmbuild/SOURCES/pym_client-2.0/init.d;
mv ./sbin/pym_client ./sbin/pym_client.py;
/usr/bin/python -c "import compileall;compileall.compile_dir('./sbin')";
mv ./sbin/pym_client.pyc ./sbin/pym_client;
mv ./sbin/pym_client.py ./;
cp -r ./sbin /root/rpmbuild/SOURCES/pym_client-2.0;
mv ./pym_client.py ./sbin/pym_client;
cp  ./lib/pym_client-2.0.1.tar.gz /root/rpmbuild/SOURCES/pym_client-2.0;
rm -rf `find /root/rpmbuild/SOURCES/pym_client-2.0 -name .svn`;
cd /root/rpmbuild/SOURCES/;
chmod -R 777 pym_client-2.0;
tar zcvf pym_client-2.0.tar.gz pym_client-2.0;
rpmbuild -ba /root/rpmbuild/SPECS/1.spec;
cd $dir;
mv /root/rpmbuild/RPMS/x86_64/pym_client-2.0-1.x86_64.rpm ./pym_client-2.0.1-el6.x86_64.rpm;
rm -rf /root/rpmbuild;
