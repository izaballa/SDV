# Requirements

## Eclipse zenoh-python
This library provides a Python binding based on the main Zenoh implementation written in Rust.

### How to install it
The Eclipse zenoh-python library is available on [Pypi.org](https://pypi.org/project/eclipse-zenoh/). Install the latest available version using ```pip```:
```bash
pip install eclipse-zenoh
```
⚠️ zenoh-python is developped in Rust. On Pypi.org provide binary wheels for the most common platforms (Linux x86_64, i686, ARMs, MacOS universal2 and Windows amd64). But also a source distribution package for other platforms. However, for ```pip``` to be able to build this source distribution, there are some prerequisites:
- ```pip``` version 19.3.1 minimum (for full support of PEP 517). If necessary upgrade it with command: ```sudo pip install --upgrade pip```.
- Have a Rust toolchain installed (instructions at [rustup.rs](https://rustup.rs/)). Unix command: ```curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh```.

### Supported Python versions and platforms
This library has been tested with Python 3.8, 3.9, 3.10, 3.11 and 3.12 .

## Problems
⚠️ For Python 3.12 and ```pip``` 24.0 in Ubuntu release 24.04 the following error occurs:
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
