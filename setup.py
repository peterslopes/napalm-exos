"""setup.py file."""

#import uuid

from setuptools import setup, find_packages
#try: # for pip >= 10
#    from pip._internal.req import parse_requirements
#except ImportError: # for pip <= 9.0.3
#    from pip.req import parse_requirements

__author__ = 'Tim Raphael <raphael.timothy@gmail.com>'

#install_reqs = parse_requirements('requirements.txt', session=uuid.uuid1())
#reqs = [str(ir.requirement) for ir in install_reqs]

with open("requirements.txt", "r") as fs:
    reqs = [r for r in fs.read().splitlines() if (len(r) > 0 and not r.startswith("#"))]

with open("README.md", "r") as fs:
    long_description = fs.read()


setup(
    name="napalm-exos",
    version="0.1.1",
    packages=find_packages(),
    author="Tim Raphael",
    author_email="raphael.timothy@gmail.com",
    description="Network Automation and Programmability Abstraction Layer with Multivendor support",
    classifiers=[
        'Topic :: Utilities',
         'Programming Language :: Python',
         'Programming Language :: Python :: 2',
         'Programming Language :: Python :: 2.7',
         'Programming Language :: Python :: 3.6',
         'Programming Language :: Python :: 3.7',
         'Programming Language :: Python :: 3.8',        
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS',
    ],
    url="https://github.com/tardoe/napalm-exos",
    include_package_data=True,
    install_requires=reqs,
#    zip_safe=False,
)
