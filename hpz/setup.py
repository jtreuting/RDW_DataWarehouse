import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pyramid == 1.4',
    'pyramid_debugtoolbar==1.0.8',
    'pyramid_beaker==0.8',
    'waitress==0.8.7',
    'SQLAlchemy == 0.8.3',
    'py-postgresql == 1.1.0',
    'zope.sqlalchemy==0.7.3',
    'Jinja2==2.7.2',
    'config',
    'edschema',
    'edauth',
    'edcore',
    'edidentity']

setup(name='hpz',
      version='0.1',
      description='hpz',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Pyramid",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application", ],
      author='',
      author_email='',
      url='',
      keywords='web pyramid pylons',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite='nose.collector',
      entry_points="""\
      [paste.app_factory]
      main = hpz:main
      """,
      )