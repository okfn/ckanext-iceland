from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='ckanext-iceland',
    version=version,
    description="",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Sam Smith',
    author_email='sam.smith@okfn.org',
    url='https://github.com/okfn/ckanext-iceland',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.iceland'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        iceland=ckanext.iceland.plugin:IcelandPlugin
    ''',
)
