# How to setup an environment for python

<hr>

## Pre-requisite - python

Install Python3 using homebrew(assuming homebrew is already installed if [not refer](https://brew.sh) 
on MacOS python is already shipped

```bash
python3 --version # if this works skip the below step
brew install python3 
```
Install pyenv for managing python versions

```bash
brew install pyenv
```

Setuptools can be updated via pip, without having to reinstall brewed Python:

```bash
python3 -m pip install --upgrade setuptools
```

Similarly, pip can be used to upgrade itself via:

```bash
python3 -m pip install --upgrade pip
```

Now let's take a moment to install PyEnv. This library will help you switch between different versions of Python 
(in case you need to run Python 2.x for some reason, and in anticipation of Python 4.0 coming).

```bash
brew install pyenv
````

#### Create [Virtual Environment](https://docs.python.org/3/library/venv.html)

```bash
pip install virtualenv # Using pip to install virtual environment
```

To Create virtual environment now for project to protect the working environment

```bash
python3 -m venv <env-name>
```
To activate the foo
```bash
source <env-name>/bin/activate
```

To test the packages installed under your foo
```bash
pip list
```

Or to install use;
```bash
pip install <pkg-name>

```

In order to de-activate dev-env

```bash
deactivate
```