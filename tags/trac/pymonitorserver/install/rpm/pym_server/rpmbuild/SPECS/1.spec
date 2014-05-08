Name:	pym_server	
Version:	1.0
Release:	1
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
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/pym_server
install -m 755 %{SOURCE0} $RPM_BUILD_ROOT/pym_server

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%post
cd /pym_server > /dev/null 2>&1;
tar zxvf pym_server-1.0.tar.gz  > /dev/null 2>&1;
cp pym_server-1.0/init.d/* /etc/init.d/ > /dev/null 2>&1;
cp pym_server-1.0/sbin/* /usr/bin/ > /dev/null 2>&1;
mkdir /etc/monitor/ > /dev/null 2>&1;
mkdir /var/log/monitor/ > /dev/null 2>&1;
cp pym_server-1.0/conf/* /etc/monitor/ > /dev/null 2>&1;

for i in nodedatacollect  nodedataredis  pym_server  webredis; do mkdir /var/run/$i > /dev/null 2>&1; mkdir /var/lock/$i > /dev/null 2>&1; done
	


%preun

for i in nodedatacollect  nodedataredis  pym_server  webredis; do rm -fr /var/run/$i; rm -fr /var/lock/$i; rm -f /etc/init.d/$i; rm -f /usr/sbin/$i; rm -fr /etc/monitor/$i.cfg;done
rm -rf /var/log/monitor;rm -rf /etc/monitor/node.conf;

%files
%defattr(-,root,root,-)
%dir /pym_server/*
%doc



%changelog

