from setuptools import setup, find_packages

requires = [
    'SQLAlchemy',
    'zope.component >= 4.0.2',
    'zope.interface >= 4.0.3']

tests_require = requires + [
    'sqlite3']

setup(name='edschema',
      version='0.0',
      description='Schema for EdWare',
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Pyramid",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application", ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='nose.collector',
      install_requires=requires,
      tests_require=tests_require,
      entry_points="""\
      """,
      )
