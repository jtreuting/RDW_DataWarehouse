import os

from setuptools import setup, find_packages
import shutil
from distutils.core import run_setup

here = os.path.abspath(os.path.dirname(__file__))

dependencies = [
    'edapi',
    'edschema',
    'edauth']


for dependency in dependencies:
    pkg_path = os.path.abspath(here + "/../" + dependency + "/")
    os.chdir(pkg_path)
    run_setup("setup.py")
    os.chdir(here)
run_setup("setup.py")

from generate_ini import generate_ini
print(generate_ini('dev', 'development.ini'))
