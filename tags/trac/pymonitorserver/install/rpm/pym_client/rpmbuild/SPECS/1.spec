Name:	pym_client	
Version:	1.0
Release:	1
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
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/pym_client
install -m 755 %{SOURCE0} $RPM_BUILD_ROOT/pym_client

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%post
cd /pym_client > /dev/null 2>&1;
tar zxvf pym_client-1.0.tar.gz  > /dev/null 2>&1;
cp pym_client-1.0/init.d/* /etc/init.d/ > /dev/null 2>&1;
cp pym_client-1.0/sbin/* /usr/bin/ > /dev/null 2>&1;
mkdir /etc/monitor/ > /dev/null 2>&1;
mkdir /var/log/monitor/ > /dev/null 2>&1;
cp pym_client-1.0/conf/* /etc/monitor/ > /dev/null 2>&1;

mkdir /var/run/pym_client > /dev/null 2>&1; mkdir /var/lock/pym_client > /dev/null 2>&1;
	


%preun

rm -fr /var/run/pym_client; rm -fr /var/lock/pym_client; rm -f /etc/init.d/pym_client; rm -f /usr/sbin/pym_client; rm -fr /etc/monitor/pym_client.cfg;rm -rf /var/log/monitor/;

%files
%defattr(-,root,root,-)
%dir /pym_client/*
%doc



%changelog

