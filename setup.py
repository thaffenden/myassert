from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst')) as f:
    long_description = f.read()

packages = ['myassert']

setup(
    name='my-assert',
    version='0.0.2',
    description='Simple assertion library with verbose error messages',
    long_description=long_description,
    url='https://github.com/thaffenden/myassert',
    author='Tristan Haffenden',
    author_email="tristanehaffenden@gmail.com",
    packages=packages,
)
