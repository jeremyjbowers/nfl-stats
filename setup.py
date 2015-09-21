import os.path

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


setup(
    name='nfl-stats',
    version='0.0.5',
    author='Jeremy Bowers',
    author_email='jeremyjbowers@gmail.com',
    url='https://github.com/jeremyjbowers/nfl-stats',
    description='Python modules for parsing team, player and game stats from NFL.com.',
    long_description=read('README.rst'),
    packages=['pynfl'],
    license="Apache License 2.0",
    keywords='football NFL sports data statistics',
    install_requires=['beautifulsoup4==4.4.0','lxml==3.4.4','requests==2.7.0','wheel==0.24.0'],
    classifiers=['Development Status :: 3 - Alpha',
                 'Intended Audience :: Developers',
                 'Programming Language :: Python',
                 'Topic :: Software Development :: Libraries :: Python Modules']
)