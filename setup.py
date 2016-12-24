from sys import argv
from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst')) as f:
    long_description = f.read()

packages = ['myassert']

# Only include pytest runner in setup requires if needed
needs_pytest = {'pytest', 'test'}.intersection(argv)
pytest_runner = ['pytest-runner'] if needs_pytest else []

setup(
    name='my-assert',
    version='0.0.3',
    description='Simple assertion library with verbose error messages',
    long_description=long_description,
    url='https://github.com/thaffenden/myassert',
    author='Tristan Haffenden',
    author_email="tristanehaffenden@gmail.com",
    packages=packages,
    setup_requires=[pytest_runner],
    tests_require=['pytest'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
    ]
)
