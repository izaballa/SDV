# Requirements

## Eclipse zenoh-python
This library provides a Python binding based on the main Zenoh implementation written in Rust.

### How to install it
The Eclipse zenoh-python library is available on [Pypi.org](https://pypi.org/project/eclipse-zenoh/). Install the latest available version using ```pip```:
```bash
pip3 install eclipse-zenoh
```

⚠️ En mi caso para Python 3.12 y pip 24.0 en Ubuntu la release 24.04 tengo el siguiente error:
```bash
User@Ubuntu:~$ pip3 install eclipse-zenoh
error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try apt install
    python3-xyz, where xyz is the package you are trying to
    install.
    
    If you wish to install a non-Debian-packaged Python package,
    create a virtual environment using python3 -m venv path/to/venv.
    Then use path/to/venv/bin/python and path/to/venv/bin/pip. Make
    sure you have python3-full installed.
    
    If you wish to install a non-Debian packaged Python application,
    it may be easiest to use pipx install xyz, which will manage a
    virtual environment for you. Make sure you have pipx installed.
    
    See /usr/share/doc/python3.12/README.venv for more information.
```
This error can be overridden, at the risk of breaking your Python installation or operating system, by passing ```--break-system-packages```.
