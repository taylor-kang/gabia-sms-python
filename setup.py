from __future__ import with_statement

import setuptools


VERSION = '0.1'


def readme():
    try:
        with open('README.rst') as f:
            return f.read()
    except IOError:
        return ''


INSTALL_REQUIRES = [
    'Flask>=1.0.2',
]

TESTS_REQUIRE = [
    'pytest>=3.0.0',
    'pytest-cov',
    'tox',
    'mock',
]


setuptools.setup(
    name='gabia-sms-python',
    version=1.0,
    description='Send SMS messages to mobile devices through GABIA SMS api.',
    long_description=readme(),
    author='Taehee Kang',
    author_email='taehee.taylor.kang@gmail.com',
    url='https://github.com/', #
    download_url='https://github.com//master.zip', #
    packages=(setuptools.find_packages()),
    install_requires=INSTALL_REQUIRES,
    tests_require=TESTS_REQUIRE,
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.7',
    ],
)
