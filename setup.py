import setuptools


setuptools.setup(name='saih-hidrosur',
                 version='0.1',
                 description='Library around SAIH Hidrosur data',
                 long_description=open('README.md').read().strip(),
                 author='Frank Villaro-Dixon',
                 author_email='frank@villaro-dixon.eu',
                 url='https://www.github.com/Frankkkkk/python-saih-hydrosur',
                 py_modules=['saihhidrosur'],
                 install_requires=['requests'],
                 license='MIT License',
                 keywords='hydrology saih hidrosur',
                 classifiers=[])
