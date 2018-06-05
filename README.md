# jupyter-shoebot

Jupyter kernel for running [Shoebot](https://github.com/shoebot/shoebot) scripts

## Installation

First, you need to have Jupyter installed, as well as the development version
of Shoebot. Using `virtualenvwrapper` for this is heavily recommended.

```bash
pip install jupyter jupyter-pip
# clone the Shoebot repository and enter it
cd shoebot
python setup.py install
```

After ensuring both packages are available, install the extension.

```bash
# clone the jupyter-shoebot repository and enter it
cd jupyter-shoebot
python setup.py install
```

And finally, run

```bash
jupyter kernelspec install --user shoebot_kernel
```

## Usage

After running Jupyter with `jupyter notebook`, go to the `Kernel` menu, select `Change kernel` and select `Shoebot`.

**Warning:** Right now, notebooks must be created on the repository root or the kernel won't launch properly. We'll fix this ASAP!

## Acknowledgements

This plugin's workings and install script are based on [cairo-jupyter](https://github.com/fomightez/cairo-jupyter)'s, and its structure was heavily inspired by the [Jupyter bash kernel](https://github.com/takluyver/bash_kernel).
