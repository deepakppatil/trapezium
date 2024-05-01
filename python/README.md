# ⚡ Trapezium
<hr>

## Overview

Pattern recognition

## Installation

The easiest way to install doji is via the Python [pip](https://pip.pypa.io)
utility:

```bash
pip3 install doji
```

### Requirements - [Setup](DEVSETUP.md)
- Python 3
- [virtualenv](https://virtualenv.pypa.io)

### Dependencies
Dependencies are listed in [requirements.txt](requirements.txt). Dependencies
are automatically installed during doji installation.

### Installing doji

```bash
# clone source code
git clone https://github.com/deepakpatil/trapezium.git

# setup virtualenv
cd trapezium/python

# create dev-env under the parent folder
python3 -m venv dev-env
#activate virtial environment
source dev-env/bin/activate

# Install all packages in one go
pip install -r requirements-dev.txt

# Build and install
python3 setup.py build
python3 setup.py install
```

## Running

```bash
cp doji-config.env local.env
vi local.env # update environment variables accordingly

doji --version
```

### Using the API

```python
# Python API examples go here
```
<hr>

## Development

### Running Tests

```bash
# install dev requirements
pip3 install -r requirements-dev.txt

# run tests like this:
python3 doji/tests/run_tests.py

# or this:
python3 setup.py test

# measure code coverage
coverage run --source=doji -m unittest doji.tests.run_tests
coverage report -m
```

## Release

```bash
rm -fr build dist *.egg-info
python3 setup.py sdist bdist_wheel --universal
twine upload dist/*
```

### Code Conventions

* [PEP8](https://www.python.org/dev/peps/pep-0008)

### Bugs and Issues

All bugs, enhancements and issues are managed on [GitHub](https://github.com/deepakpatil/trapezium/issues).

<hr>

## Contact

* Deepak Patil
