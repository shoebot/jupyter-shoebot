# -*- coding: utf-8 -*-
from setuptools import setup

try:
    from jupyterpip import cmdclass
except Exception:
    import pip
    import importlib
    pip.main(['install', 'jupyter-pip'])
    cmdclass = importlib.import_module('jupyterpip').cmdclass

setup(
    name='jupyter-shoebot',
    packages=['shoebot_kernel'],
    # ... more setup.py stuff here ...
    install_requires=["jupyter-pip", "shoebot"],
    cmdclass=cmdclass('shoebot_kernel'),
)

