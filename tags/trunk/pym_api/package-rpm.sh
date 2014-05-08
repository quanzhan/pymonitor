# 前提是你要安装 rpm-build
python setup.py bdist_rpm
echo "----------------------------------------------"
sleep 1
mv -fv dist/pym_api-0.1-1.noarch.rpm .
rm -rfv build/ dist/ pym_api.egg-info/
echo 'ok'
