---
title: "Programming"
lecture: "02-programming"
weight: 2
---

## Learning python

Below is a collection of resources for learning to program in python!

### CodeRefinery

[CodeRefinery](https://coderefinery.org/) is a project within the Nordic e-Infrastructure Collaboration ([NeIC](https://neic.no/)) and aims to train researchers in research software development.

They have some excellent [material](https://coderefinery.org/lessons/) on many topics, including basic python:

[Basic python](https://coderefinery.github.io/data-visualization-python/python-basics/)
: A quick syntax primer for python

[Python for Scientific Computin](https://aaltoscicomp.github.io/python-for-scicomp/)
: Discusses how Python can be utilized in scientific computing

[Reproducible research using Python](https://coderefinery.github.io/reproducible-python-ml/)
: hands-on course on software engineering for reproducible research using Python with a ML example.

[Python Progression](https://coderefinery.github.io/python-progression/)
: Short intermediate-level workshop that covers how to write Python with a focus on reproducibility and re-usability

[Jupyter notebooks](https://coderefinery.github.io/jupyter/)
: Covers the user interface of JupyterLab, how Jupyter notebooks work, and what some common and powerful use cases are

Many of the lessons are also recorded and uploaded to the [CodeRefinery youtube channel](https://www.youtube.com/@coderefinery3414/videos).

### Software-carpentry

Software carpentry has some really good [lesson material](https://software-carpentry.org/lessons/) on many aspects of software development, including some beginners python material:

[Basic Python](https://swcarpentry.github.io/python-novice-inflammation/)
: A starter lesson on programming with Python

[Python plotting](https://swcarpentry.github.io/python-novice-gapminder/)
: A starter lesson on plotting and programming in Python

### freeCodeCamp

[freeCodeCamp](https://www.freecodecamp.org/) is a non-profit organisation with lots of material, especially on their youtube channel. The below video is a good starting tutorial for Python

{{< youtube eWRfhZUzrAc >}}

### exercism

[Exercism](https://exercism.org/) is a not-for-profit organisation that has loads of code exciersices listed on their website. [Here](https://exercism.org/tracks/python/exercises) are all their listed python exercises.

### python.org

The official python docs also has many tutorials e.g. [python.org tutorial](https://docs.python.org/3/tutorial/index.html).


## The correct language for the job

Every language has its strengths and weaknesses. 

[Python](https://www.python.org/)
: High level interpreted language which is amazingly simple to learn and rapidly develop in, pretty much everything you can think of is available in python
: If used incorrectly will be very slow and error prone, does not allow the low level access you need for hardcore optimization

[Rust](https://www.rust-lang.org/)
: Low level compiled language with an amazing type system and ownership model that can guarantee memory-safety and thread-safety
: Very hard to learn and forces you into certain development models which might not be what you want for research software

[C](https://gcc.gnu.org/c99status.html)
: The most common goto (pun intended) low level compiled language, pretty much all parts of our modern computers runs on C, the language itself is very simple and one can almost map its statements directly into the resulting assembly, thereby making almost any optimization you can think of possible (and if thats not enough - you can of course just inline assembly)
: Its so low level that you need to write heaps of code that looks useless to the untrained eye just to not blow everything up later on, error handling is horrendous, doing any high level infrastructure can be a pain, forget rapid prototyping when you have to write literally everything from scratch, there is no modularity and no packaging system, and compilation is far from trivial

If you want to get [nerd-sniped](https://xkcd.com/356/) for a few minutes, check out this blog post called [C Isn't A Programming Language Anymore](https://faultlore.com/blah/c-isnt-a-language/) that discusses some of the consequences of C becoming so prevalent that its become the lingua franca of programming.

[JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Language_overview)
: Interpreted language has become one of the core technologies of the World Wide Web. Pretty much all websites uses JavaScript of some kind to have client-side behavior. Its incredibly easy to prototype in and there is a ton of packages and infrastructure around it.
: JavaScript is a jumbled mess of a language and has probably been used outside of its reasonable scope more often than any other language out there. Debugging can be infuriating and its horrendous performance is only saved by web-browsers throwing literally thousands of developers at [JavaScript engines](https://v8.dev/).

For a really funny deep dive into some of the madness of interpreted languages such as JavaScript and Ruby have a look at [Wat](https://www.destroyallsoftware.com/talks/wat).

Some languages I am currently learning and keeping my eyes on are

[Odin](https://odin-lang.org/)
: Odin is a general-purpose programming language with distinct typing built for high performance, modern systems and data-oriented programming. 

[Zig](https://ziglang.org/)
: Zig is a general-purpose programming language and toolchain for maintaining robust, optimal and reusable software.

Both have some very good things going for them, where the more I learn about the features of `zig` the more excited I become to learn it. Currently my language of choice for low-level implementations that allow for optimizations is still C. But I'm slowly difting towards wanting to exchange that for something else.

Other languages that are on my radar are 

- [Julia](https://julialang.org/)
- [Go](https://go.dev/)
- [Lua](https://www.lua.org/)
- [Chapel](https://chapel-lang.org/)
- [Rust](https://www.rust-lang.org/)

> [!Viktigt]
> The takeaway is: don't get attached to a language! They all have their pros and cons. Learning to use a hammer does not make everything a nail. Try to pair a high-level language with a low-level language to cover as many bases as possible. My usual approach is "Write infrastructure in python that orchestrates the calling of compiled low level languages who actually will do the work".


## Homework assignments

Tutorial
: If you have not programmed in python before - choose some of the learning material above and work trough it. Save the code you wrote while learning and note down which material you worked trough. 

Scripts, modules and packages
: Create a small python package following the [packaging tutorial](https://packaging.python.org/en/latest/tutorials/packaging-projects/).
: Install your package into your virtual environment.
: Create 2 functions in two separate [modules](https://docs.python.org/3/tutorial/modules.html) inside your package. One function should reverse a list and the other should take two lists as input, reverse the first list and then interleave every other argument of two lists outputting a single new list. You should import the list-reveral function from the other module ([hint: intra-package-references](https://docs.python.org/3/tutorial/modules.html#intra-package-references)).
: Create a scripts in a different location than were the package is that uses this function from the package to interleave the following two strings: `'VOG!lo olH'` and `'el,Wrd ROY'`. 

Python basic syntax
: Implement a function in your package that uses the following: [with](https://docs.python.org/3/reference/compound_stmts.html#with), [encode](https://docs.python.org/3/library/stdtypes.html#str.encode), and [decode](https://docs.python.org/3/library/stdtypes.html#bytes.decode) to save an input string in a binary file. Also implement a function to load a string from a binary file.

Plotting
: Install [matplotlib](https://matplotlib.org/) into your environment.
: Implement one of the [examples](https://matplotlib.org/stable/gallery/index).
: Run the code and get the plot to show. 
: Add it to your package and add `matplotlib` as a dependency

> [!Tips]
> Depending on how your system is setup you might need to install `pyqt5` or `pyqt6` in your local environment to show plots. 
