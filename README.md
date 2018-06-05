# jupyter-shoebot

Jupyter kernel for running [Shoebot](https://github.com/shoebot/shoebot) scripts

## Installation

First, you need to have Jupyter installed, as well as the development version
of Shoebot. Using `virtualenvwrapper` for this is heavily recommended.

```bash
# create the virtualenv
mkvirtualenv jupytershoebot
# install jupyter dependencies
pip install jupyter jupyter-pip
# clone the Shoebot repository, enter it and install
git clone https://github.com/shoebot/shoebot
cd shoebot
python setup.py install
```

After ensuring both packages are available, install the extension.

```bash
# clone the jupyter-shoebot repository, enter it and install
git clone https://github.com/shoebot/jupyter-shoebot
cd jupyter-shoebot
python setup.py install
```

And finally, while still on the `jupyter-shoebot/` directory, run

```bash
jupyter kernelspec install shoebot_kernel --sys-prefix
```

## Usage

After running Jupyter with `jupyter notebook`, go to the `Kernel` menu, select `Change kernel` and select `Shoebot`.

## Acknowledgements

This plugin's workings and install script are based on [cairo-jupyter](https://github.com/fomightez/cairo-jupyter)'s, and its structure was heavily inspired by the [Jupyter bash kernel](https://github.com/takluyver/bash_kernel).
