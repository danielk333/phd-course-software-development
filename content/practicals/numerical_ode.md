---
title: "Numerical integration"
weight: 1
---

## A first-order linear system of ODEs integrator

As we are all working on research it seems fitting to start off by implementing a numerical method for integrating coupled first order ordinary differential equations (ODEs)!

The goal is to write a program that can integrate arbitrary coupled first order ODEs using a selected method.

### Requirements

The program should:

- Have a command line interface
- Provide a way to specify the initial condition of the integration and the integration settings
- Have the possibility to use several different methods
- Have the ability to save the results to file
- Have the ability to plot the output files


### Development

The team should split responsibilities between each member. Plan out then work first, i.e. do a software design, and then get to coding.

- Use git to collaborate
- Design on a high level
- Define interfaces for each other
- Allow the design to change over time
- Implement the code into a python package 

### Methods 

The program should implement two different methods:

- [The Euler method](https://en.wikipedia.org/wiki/Euler_method)
- [The implicit Euler method](https://en.wikipedia.org/wiki/Backward_Euler_method)

### Tips

#### Data format

To save data to file many file formats are possible:

- [numpy](https://numpy.org/doc/stable/reference/generated/numpy.save.html)
- [h5py](https://www.h5py.org/)
- [csv](https://numpy.org/doc/stable/reference/generated/numpy.savetxt.html)

#### CLI

It is recommended to use the python built-in [argparse](https://docs.python.org/3/library/argparse.html) package.

Also look into [entry points](https://setuptools.pypa.io/en/latest/userguide/entry_point.html) of your code.

#### Configuration

For configuration there are several options

- All trough the CLI
- [cfg files - configparser](https://docs.python.org/3/library/configparser.html)
- [toml files - tomllib](https://docs.python.org/3/library/tomllib.html)
- [yaml files - pyyaml](https://pyyaml.org/)
- custom format

Probably cfg or toml files are the best choice here.

#### Plot

Obvious choice here is [matplotlib](https://matplotlib.org/). But there are other options, explore as you see fit!

#### Implementation

For inspiration you can look at [Numerical Recipes in C](http://s3.amazonaws.com/nrbook.com/book_C210.html). Luckily it does not detail Euler methods but rather starts at Runge-Kutta.

#### OS-agnostic

There are many ways to make code independent of the operating system. E.g. for paths the recommended method is to use [pathlib](https://docs.python.org/3/library/pathlib.html) for all path manipulation.


## Task

Once the program works, integrate the equations of motion (or the canonical equations) for the following Hamiltonian, 

$$
H = \frac{p_\theta^2}{2 m l^2} - m l^2 \omega^2 \cos{\theta}.
$$

These are, 

$$
\frac{\mathrm{d}\theta}{\mathrm{d}t} = \frac{\partial H}{\partial p_\theta} = \frac{p_\theta}{m l^2}
$$
$$
\frac{\mathrm{d}p_\theta}{\mathrm{d}t} = - \frac{\partial H}{\partial \theta} = - m l^2 \omega^2 \sin{\theta}
$$

I.e. a set of two coupled first order ordinary differential equations.

Integrate the system with both Euler methods: what are the results? Which one is better?
