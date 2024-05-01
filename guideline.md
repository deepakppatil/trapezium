# Trapezium

Project summary to be added.

## Spirit/Principles for Java

To be added

## Spirit/Principles for python

- https://en.wikipedia.org/wiki/DevOps
- setUp/tearDown: https://m.subbu.org/code-the-infra-8c67a869cb89
- reproducible workflow: http://bost.ocks.org/mike/make
- versioning: https://semver.org
- virtualenv: https://virtualenv.pypi.io
- dependencies are fetched, not managed in version control
  - pip: https://pip.pypa.io/en/stable/
- platform independence, use os
- Python
  - develop modules for reuse, scripts are the last step
  - logging, not print statements
    - command line functions as [click](http://click.pocoo.org/5/) functions
    - no print statements
  - everything is callable
  - tests, tests, tests
  - PEP8: http://www.python.org/dev/peps/pep-0008/ , specifically:
    - 4 spaces, NOT tabs
    - UNIX line endings, NOT DOS
    - 4 spaces, NOT tabs
    - did we mention 4 spaces, NOT tabs?
    - always absolute imports
    - always run code through flake8 before committing:
```bash
    pip install flake8
    flake8 foo.py
```

## Overview of Structure

```
trapezium/
|__ python/
|____ doji/  # the actual package 
|    |__ __init__.py  # always set `__version__` to x.y.z 
|    |__  # more code goes here
|    |__ tests/
|    |   |__ data/  # test data files (if none, you don't need this directory)
|    |   |__ run_tests.py  # unittest style testing, see https://docs.python.org/3/library/unittest.html
|____ .gitignore  # Python-based files to ignore
|____ README.md  # Description in [Markdown](https://en.wikipedia.org/wiki/Markdown) format
|____ MANIFEST.in  # if there are non-python files that should be included in the distribution (see https://docs.python.org/3/distutils/sourcedist.html#specifying-the-files-to-distribute)
|____ requirements.txt  # dependencies, see https://pip.pypa.io/en/latest/user_guide/#requirements-files
|____ requirements-dev.txt  # developer-centric dependencies (testing, packaging, etc.)
|____ setup.py  # setup script, set UPPERCASE variables scripts should be set as list
|__ README.md  # Description in [Markdown](https://en.wikipedia.org/wiki/Markdown) format
|__ LICENSE 
|__ .gitignore  # Project-level files to ignore 

```

## Common workflows

Always work in a virtualenv for python project to protect clashing python environment on the system

```bash

virtualenv -p python3 trapezium/python
cd trapezium/python
. bin/activate
git clone https://github.com/deepakppatil/trapezium.git
cd trapezium/python
# run tests
cd tests && python run_tests.py
# create a distribution
python3 setup.py sdist  # result is in dist/doji-x.y.z.tar.gz

```