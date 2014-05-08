from setuptools import setup, find_packages 

from pym_client import __version__

setup(
    name = "pym_client",
    version = __version__,
    author = 'baoyiluo',
    author_email = 'baoyiluo@gmail.com',
    description = 'the data library of pym_client in monitor system.',

    packages = find_packages(),
    keywords = ('pym_client', 'lib'),
    ##cmdclass = cmdclasses,
    ##data_files = data_files,
    #scripts = ['scripts/pyssh.py'],
)
