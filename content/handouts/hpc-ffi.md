---
title: "Parallelization and foreign function interfaces"
lecture: "12-hpc-ffi"
weight: 12
---

## Code examples

### MPI

Dependencies

- Arch: `pacman -S base-devel openmpi`
- Ubuntu: `apt install build-essential openmpi-bin openmpi-common libopenmpi-dev`

Then install [mpi4py](https://mpi4py.readthedocs.io/en/stable/) with `pip install mpi4py`. If the
installation process fails, probably you are lacking some basic build dependency, have a look at the
docs to see what is missing.

{{< details summary="The typical hello world example - but in parallel!" >}}
{{< include-code "python" "code/python-scripts/mpi_hello.py" "">}}
{{< /details >}}

{{< details summary="A more involved example with actual communication and processing logic" >}}
{{< include-code "python" "code/python-scripts/mpi_example.py" "">}}
{{< /details >}}

### Threading

{{< details summary="A threading/multiprocessing example highlighting the Global interpreter lock" >}}
{{< include-code "python" "code/python-scripts/gil_example.py" "">}}
{{< /details >}}

### Ctypes

{{< details summary="A more involved example with actual communication and processing logic" >}}
{{< include-code "python" "code/python-scripts/mpi_example.py" "">}}
{{< /details >}}


### Ctypes

{{< details summary="A more involved example with actual communication and processing logic" >}}
{{< include-code "python" "code/python-scripts/mpi_example.py" "">}}
{{< /details >}}


## Extensions in other languages

The most common way to build extensions to your Python package in other languages is trough a
[setuptools Extension](https://setuptools.pypa.io/en/stable/userguide/ext_modules.html). This system
can e.g. compile C code as a part of the installation and building process of your package. However
there are other methods, such as using [meson](https://mesonbuild.com/index.html).

There are also systems for automatically creating interfaces such as [pybind11](https://github.com/pybind/pybind11) or the numpy [f2py](https://numpy.org/doc/stable/f2py/).

## Increasing performance

The [The Computer Language Benchmarks Game](https://benchmarksgame-team.pages.debian.net/benchmarksgame/index.html) is a quite fun website that micro-benchmarks languages. Remember, this is of course no-where near a real metric for if a language is more performant than another (for that you need a real domain-specific example with actual throughput), but it does show some things about its basic functionality and its compiler/interpreter.


## High-performance computing system tools

### Languages

So far I have only found one programming language that is specifically designed to be used for
parallel or high-performance computing. That language is [Chapel](https://chapel-lang.org/). So far
it seems very interesting and I'm keeping my eye on it!

Hewlett Packard Enterprise - Chapel: Making parallel computing as easy as Py(thon), from laptops to supercomputers
{{< youtube 7Qk8T7_bevo >}}

Also, Chapel does support
[interoperability](https://chapel-lang.org/docs/language/spec/interoperability.html) with other
languages trough C, which means you could probably interface to a chapel program trough `ctypes`
from Python and similarly parallelize your existing C code by calling the functions from a shared
library in chapel.

One example of using Chapel to implement HPC calculations is
[arkouda](https://github.com/Bears-R-Us/arkouda), a Python package for executing data processing on
a cluster where the cluster server is written in Chapel.


### Schedulers

- [apache YARN](https://hadoop.apache.org/docs/current/hadoop-yarn/hadoop-yarn-site/YARN.html)
- [slurm](https://slurm.schedmd.com/documentation.html)

### Data systems

- [dCache](https://github.com/dCache/dcache)
- [apache hdfs](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/HdfsDesign.html)
- [lustre](https://www.lustre.org/)
- [daos](https://daos.io/)
- [BeeGFS](https://www.beegfs.io/c/)

### Map-reduce systems

- [apache spark](https://spark.apache.org/docs/latest/api/python/index.html)

### More stuff

There are more links to HPC tooling at [awesome-high-performance-computing](https://github.com/trevor-vincent/awesome-high-performance-computing).


## Application binary interface

An [application binary interface](https://en.wikipedia.org/wiki/Application_binary_interface) is a
interface for accessing in-process machine code, e.g. calling a function from a compiled binary from
a process.

The blog post mentioned in the lecture can be found
[here](https://faultlore.com/blah/c-isnt-a-language/). Again, if you are not much for reading, there
is a reaction video for the post.

ThePrimeTime - C Is Not A Language Anymore
{{< youtube gqKyP2hXFoA >}}


## Homework

### Parallelization

Parallelize some piece of software you have written, either during the course or elsewhere. The
important part is that this software should theoretically benefit from parallelization (you don't
have to fit your portion coefficients if you know most of the program you can trivially parallelize). You
will then show the code before and after so that we can discuss it, as well as show benchmarks of before and after.

### Python as glue

Choose some small function from a software you have written, either during the course or elsewhere. The function should be doing mostly "Python things", not just be one line of numpy. Then implement this function in C or another low level language of your choice and create an extension for your code. You should be able to call the function via your Python code without using something like `subprocess`, rather it should use `ctypes` or something like the `Python.h` and `f2py` approach. Benchmark the performance before and after. We will review the compiled low level code and the Python code before and after.
