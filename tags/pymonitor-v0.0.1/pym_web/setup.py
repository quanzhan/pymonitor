from setuptools import setup, find_packages

setup(
    name = "pymonitor",
    version = "0.1",
    author = 'xcluo',
    author_email = 'xcluo.mr@gmail.com',
    description = 'Monitor machine',

    packages = find_packages(),
    keywords = ('pymonitor', 'monitor', 'python'),
    ##cmdclass = cmdclasses,
    ##data_files = data_files,
    #scripts = ['scripts/pyssh.py'],
)
