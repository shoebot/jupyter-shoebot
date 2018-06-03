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

## Acknowledgements

This plugin's structure was heavily inspired by the [Jupyter bash kernel](https://github.com/takluyver/bash_kernel).
