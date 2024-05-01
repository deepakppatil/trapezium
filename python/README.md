# ⚡ Trapezium

Trapezium si a cutting-edge algorithmic trading software that revolutionizes the way you approach the financial markets. Our software is built on advanced pattern identification using technical analysis, empowering you to make informed and strategic trading decisions with confidence and precision.

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

### Pre-requisite

```bash
# clone source code
git clone https://github.com/deepakpatil/trapezium.git
cd trapezium/python

```

Setup virtualenv as dev-env(you can use any name) under the parent folder

```bash
python3 -m venv dev-env
#activate virtial environment
source dev-env/bin/activate
```

Now install all the packages required for dev using `-r @file-name`

For TA-lib we need to first install talib using homebrew on MacOS

```bash
brew install ta-lib
```

```bash
pip install -r requirements.txt # has all the packages
pip install -r requirements-dev.txt # extended packages only requried for development purpose
```



Build and install
```bash
python3 setup.py build
python3 setup.py install
```

<hr>

### Development

```bash
cp doji-config.env local.env
vi local.env # update environment variables accordingly

doji --version
```

#### Using the API

```python
# Python API examples go here
```

#### Running locally

Run tests like this:

```bash
python3 doji/tests/run_tests.py

# or this:
python3 setup.py test

# measure code coverage
coverage run --source=doji -m unittest doji.tests.run_tests
coverage report -m
```

You can also use jupyter notebooks as well. Install jupyter using `pip` currently its already installed as part of requirements-dev.txt, to start jupyter;

```bash
jupyter lab
```

<hr>

## Release

```bash
rm -fr build dist *.egg-info
python3 setup.py sdist bdist_wheel --universal
twine upload dist/*
```

<hr>

### Code Conventions

* [PEP8](https://www.python.org/dev/peps/pep-0008)

### Bugs and Issues

All bugs, enhancements and issues are managed on [GitHub](https://github.com/deepakppatil/trapezium/issues).

<hr>

## Contact

* Deepak Patil
