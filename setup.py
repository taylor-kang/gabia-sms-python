from __future__ import with_statement

from setuptools import setup


VERSION = '1.0.0'


def readme():
    try:
        with open('README.rst') as f:
            return f.read().strip()
    except IOError:
        return ''


INSTALL_REQUIRES = [
    'Django>=1.11',
]

setup(
    name='gabia-sms-Django',
    version=VERSION,
    description='Send SMS messages to mobile devices through GABIA SMS api.',
    long_description=readme(),
    author='Hyunwoo Shim',
    author_email='hyunwoo.shim@laziness.xyz',
    url='https://github.com/hwshim0810/gabia-sms-Django',
    download_url='https://github.com/hwshim0810/gabia-sms-Django/archive/master.zip',
    packages=('gabia_sms',),
    install_requires=INSTALL_REQUIRES,
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: Apache License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
