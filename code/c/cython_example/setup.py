from setuptools import setup
from Cython.Build import cythonize

sources = [
    "compiled_py_calc.py",
    "cy_calc.pyx",
]

setup(ext_modules=cythonize(sources))
