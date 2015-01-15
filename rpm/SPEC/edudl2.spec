Name:		edudl2%(echo ${UDL2_ENV_NAME:=""})
Version:	%(echo ${RPM_VERSION:="X.X"})
Release:	%(echo ${BUILD_NUMBER:="X"})%{?dist}
Summary:	Edware's Universal Data Loader
Group:		ETL pipeline
License:	Proprietary software
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
Vendor: Amplify Insight Edware Team <edwaredev@wgen.net>
Url: https://github.wgenhq.net/Ed-Ware-SBAC/edware

BuildRequires:	python3
BuildRequires:	python3-libs
AutoReqProv: no

%define _unpackaged_files_terminate_build 0

%description
EdWare UDL2
commit: %(echo ${GIT_COMMIT:="UNKNOWN"})


%prep
rm -rf virtualenv/udl2
rm -rf %{buildroot}
mkdir -p %{buildroot}/opt/edware
cp -r ${WORKSPACE}/edudl2 %{buildroot}/opt/edware
mkdir -p %{buildroot}/opt/edware/conf
mkdir -p %{buildroot}/etc/rc.d/init.d
cp ${WORKSPACE}/edudl2/config/linux/opt/edware/conf/celeryd-udl2.conf %{buildroot}/opt/edware/conf/
cp ${WORKSPACE}/edudl2/config/linux/etc/rc.d/init.d/celeryd-udl2 %{buildroot}/etc/rc.d/init.d/
cp ${WORKSPACE}/edudl2/config/linux/etc/rc.d/init.d/edudl2-trigger %{buildroot}/etc/rc.d/init.d/
cp ${WORKSPACE}/edudl2/config/linux/etc/rc.d/init.d/edudl2-file-grabber %{buildroot}/etc/rc.d/init.d/
cp ${WORKSPACE}/config/generate_ini.py %{buildroot}/opt/edware/conf/
cp ${WORKSPACE}/config/udl2_conf.yaml %{buildroot}/opt/edware/conf/
cp ${WORKSPACE}/config/settings.yaml %{buildroot}/opt/edware/conf/

%build
export LANG=en_US.UTF-8
virtualenv-3.3 --distribute virtualenv/udl2
source virtualenv/udl2/bin/activate

cd ${WORKSPACE}/config
python setup.py clean --all
python setup.py install
cd -
cd ${WORKSPACE}/edcore
python setup.py clean --all
python setup.py install
cd -
cd ${WORKSPACE}/edschema
python setup.py clean --all
python setup.py install
cd -
cd ${WORKSPACE}/edauth
python setup.py clean --all
python setup.py install
cd -
cd ${WORKSPACE}/edapi
python setup.py clean --all
python setup.py install
cd -
cd ${WORKSPACE}/edworker
python setup.py clean --all
python setup.py install
cd -
cd ${WORKSPACE}/edudl2
python setup.py clean --all
python setup.py install
cd -
cd ${WORKSPACE}/smarter_common
python setup.py clean --all
python setup.py install
cd -

deactivate
find virtualenv/udl2/bin -type f -exec sed -i 's/\/var\/lib\/jenkins\/rpmbuild\/BUILD/\/opt/g' {} \;

%install
mkdir -p %{buildroot}/opt/virtualenv
cp -r virtualenv/udl2 %{buildroot}/opt/virtualenv
prelink -u %{buildroot}/opt/virtualenv/udl2/bin/python3

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,-)
/opt/edware/conf/celeryd-udl2.conf
/opt/edware/conf/generate_ini.py
/opt/edware/conf/udl2_conf.yaml
/opt/edware/conf/settings.yaml
/opt/edware/edudl2/scripts/driver.py
/opt/virtualenv/udl2/include/*
/opt/virtualenv/udl2/lib/*
/opt/virtualenv/udl2/lib64
/opt/virtualenv/udl2/bin/activate
/opt/virtualenv/udl2/bin/activate.csh
/opt/virtualenv/udl2/bin/activate.fish
/opt/virtualenv/udl2/bin/activate_this.py
%attr(755,root,root) /opt/virtualenv/udl2/bin/easy_install
%attr(755,root,root) /opt/virtualenv/udl2/bin/easy_install-3.3
#%attr(755,root,root) /opt/virtualenv/udl2/bin/initialize_udl2_database.sh
#%attr(755,root,root) /opt/virtualenv/udl2/bin/teardown_udl2_database.sh
#%attr(755,root,root) /opt/virtualenv/udl2/bin/initialize_udl2_system.sh
#%attr(755,root,root) /opt/virtualenv/udl2/bin/initialize_udl2_database_user.sh
#%attr(755,root,root) /opt/virtualenv/udl2/bin/initialize_udl2_directories.sh
#%attr(755,root,root) /opt/virtualenv/udl2/bin/initialize_udl2_database_user.sh
#%attr(755,root,root) /opt/virtualenv/udl2/bin/start_rabbitmq.sh
#%attr(755,root,root) /opt/virtualenv/udl2/bin/driver.py
#%attr(755,root,root) /opt/virtualenv/udl2/bin/add_tenant.sh
#%attr(755,root,root) /opt/virtualenv/udl2/bin/start_rabbitmq.py
%attr(755,root,root) /opt/virtualenv/udl2/bin/pip
%attr(755,root,root) /opt/virtualenv/udl2/bin/pip-3.3
%attr(755,root,root) /opt/virtualenv/udl2/bin/python3.3
%attr(755,root,root) /opt/virtualenv/udl2/bin/celery
%attr(755,root,root) /opt/virtualenv/udl2/bin/celerybeat
%attr(755,root,root) /opt/virtualenv/udl2/bin/celeryctl
%attr(755,root,root) /opt/virtualenv/udl2/bin/celeryd
%attr(755,root,root) /opt/virtualenv/udl2/bin/celeryd-multi
%attr(755,root,root) /opt/virtualenv/udl2/bin/celeryev
%attr(755,root,root) /opt/virtualenv/udl2/bin/python
%attr(755,root,root) /opt/virtualenv/udl2/bin/python3
%attr(755,root,root) /etc/rc.d/init.d/celeryd-udl2
%attr(755,root,root) /etc/rc.d/init.d/edudl2-trigger
%attr(755,root,root) /etc/rc.d/init.d/edudl2-file-grabber

%pre
# check if udl2 group exists and create if not
egrep -i "^udl:" /etc/group > /dev/null 2>&1
if [ $? -ne 0 ]; then
   groupadd udl2 -f -g 501
fi

# check if udl2 user exists and create if not
id udl2 > /dev/null 2>&1
if [ $? -ne 0 ]; then
   # add udl2 user with id 501 and group udl2
   useradd udl2 -g udl2 -u 501
fi

%post
UDL2_ROOT=/opt/edware
if [ ! -d $UDL2_ROOT/keys ]; then
    mkdir -p $UDL2_ROOT/keys
    chown -R udl2.udl2 $UDL2_ROOT/keys
fi
if [ -d $UDL2_ROOT/conf ]; then
    chown -R udl2.udl2 $UDL2_ROOT/conf
fi
if [ ! -d /var/log/celery-udl2 ]; then
    mkdir -p /var/log/celery-udl2
    chown udl2.udl2 /var/log/celery-udl2
fi
if [ ! -d /var/log/edudl2-trigger ]; then
    mkdir -p /var/log/edudl2-trigger
    chown udl2.udl2 /var/log/edudl2-trigger
fi
if [ ! -d /var/log/edudl2-file-grabber ]; then
    mkdir -p /var/log/edudl2-file-grabber
    chown udl2.udl2 /var/log/edudl2-file-grabber
fi
if [ ! -d /var/run/celery-udl2 ]; then
    mkdir -p /var/run/celery-udl2
    chown udl2.udl2 /var/run/celery-udl2
fi
if [ ! -d /var/run/edudl2-trigger ]; then
    mkdir -p /var/run/edudl2-trigger
    chown udl2.udl2 /var/run/edudl2-trigger
fi
if [ ! -d /var/run/edudl2-file-grabber ]; then
    mkdir -p /var/run/edudl2-file-grabber
    chown udl2.udl2 /var/run/edudl2-file-grabber
fi
chkconfig --add celeryd-udl2
chkconfig --add edudl2-trigger
chkconfig --add edudl2-file-grabber
chkconfig --level 2345 celeryd-udl2 off
chkconfig --level 2345 edudl2-trigger off
chkconfig --level 2345 edudl2-file-grabber off

%preun
chkconfig --del celeryd-udl2
chkconfig --del edudl2-trigger
chkconfig --del edudl2-file-grabber

%postun


%changelog
