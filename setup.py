from __future__ import with_statement

import setuptools


VERSION = '1.0.4'


def readme():
    try:
        with open('README.rst') as f:
            return f.read()
    except IOError:
        return ''


TESTS_REQUIRE = [
    'pytest>=3.0.0',
    'pytest-cov',
    'tox',
    'mock',
]


setuptools.setup(
    name='gabia-sms-python',
    version='1.0.4',
    description='Send SMS messages to mobile devices through GABIA SMS api.',
    long_description=readme(),
    author='Taehee Kang',
    author_email='taehee.taylor.kang@gmail.com',
    url='https://github.com/taylor-kang/gabia-sms-python.git',
    download_url='https://github.com/taylor-kang/gabia-sms-python/archive/master.zip',
    packages=(setuptools.find_packages()),
    install_requires=[],
    tests_require=TESTS_REQUIRE,
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.7',
    ],
)
