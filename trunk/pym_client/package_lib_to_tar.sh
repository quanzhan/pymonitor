cd lib;
/usr/bin/python setup.py bdist_rpm;
rm -rfv build pym_client.egg-info;
mv dist/pym_client-2.0.1.tar.gz ./;
rm -rf dist;
echo "OK!";
