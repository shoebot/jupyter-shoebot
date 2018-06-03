# jupyter-shoebot

Jupyter kernel for running Shoebot scripts

## Installation

First, you need to have Shoebot and Jupyter installed. Using
`virtualenvwrapper` for this is heavily recommended.

After ensuring both packages are available, run

```bash
jupyter kernelspec install --user shoebot_kernel
```

## Usage

After running Jupyter with `jupyter notebook`, go to the `Kernel` menu, select `Change kernel` and select `Shoebot`.

**Warning:** Right now, notebooks must be created on the repository root or the kernel won't launch properly. We'll fix this ASAP!

## Acknowledgements

This plugin's workings and install script are based on [cairo-jupyter](https://github.com/fomightez/cairo-jupyter)'s, and its structure was heavily inspired by the [Jupyter bash kernel](https://github.com/takluyver/bash_kernel).
