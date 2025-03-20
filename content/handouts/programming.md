---
title: "Programming"
lecture: "02-programming"
weight: 2
---

## Learning Python

Below is a collection of resources for learning to program in Python!

### CodeRefinery

[CodeRefinery](https://coderefinery.org/) is a project within the Nordic e-Infrastructure Collaboration ([NeIC](https://neic.no/)) and aims to train researchers in research software development.

They have some excellent [material](https://coderefinery.org/lessons/) on many topics, including basic Python:

[Basic Python](https://coderefinery.github.io/data-visualization-python/python-basics/)
: A quick syntax primer for Python.

[Python for Scientific Computing](https://aaltoscicomp.github.io/python-for-scicomp/)
: Discusses how Python can be utilized in scientific computing.

[Reproducible research using Python](https://coderefinery.github.io/reproducible-python-ml/)
: hands-on course on software engineering for reproducible research using Python with a ML example.

[Python Progression](https://coderefinery.github.io/python-progression/)
: Short intermediate-level workshop that covers how to write Python with a focus on reproducibility and re-usability.

[Jupyter notebooks](https://coderefinery.github.io/jupyter/)
: Covers the user interface of JupyterLab, how Jupyter notebooks work, and what some common and powerful use cases are.

Many of the lessons are also recorded and uploaded to the [CodeRefinery youtube channel](https://www.youtube.com/@coderefinery3414/videos).

### Software-carpentry

Software carpentry has some really good [lesson material](https://software-carpentry.org/lessons/) on many aspects of software development, including some beginners Python material:

[Basic Python](https://swcarpentry.github.io/python-novice-inflammation/)
: A starter lesson on programming with Python.

[Python plotting](https://swcarpentry.github.io/python-novice-gapminder/)
: A starter lesson on plotting and programming in Python.

### freeCodeCamp

[freeCodeCamp](https://www.freecodecamp.org/) is a non-profit organisation with lots of material, especially on their youtube channel. The below video is a good starting tutorial for Python.

{{< youtube eWRfhZUzrAc >}}

### Advent of Code

> [Advent of code](https://adventofcode.com/) is an Advent calendar of small programming puzzles for a variety of skill levels that can be solved in any programming language you like.

Advent of code, made by Eric Wastl, is a really nice way to get some algorithmic task with input data and a automatic check on the output data if your solution is correct. I have used it several times when trying out new programming languages such as Rust.

You can find all previous advents of code [here](https://adventofcode.com/events) where the problems are stated and there are also solutions available if you get stuck! 

### python.org

The official Python docs also has many tutorials e.g. [python.org tutorial](https://docs.python.org/3/tutorial/index.html).


## History of programming languages

Even though the below talk is oriented towards Functional programming it is actually a really good lecture on history of programming languages and what has made many of them so popular. It also makes has some good points on what is important to developers.

Richard Feldman - Why Isn't Functional Programming the Norm?
{{< youtube QyJZzq0v7Z4 >}}


## Concepts

There are several concepts within software development that are good to understand or at least have heard about, below I cover some of the important ones.

### Polymorphism

[https://en.wikipedia.org/wiki/Polymorphism_(computer_science)](Polymorphism) is generally when a single operation or interface works with many different types. The below is a overview of what this implies:

OOP Channel - What is Polymorphism
{{< youtube 68uXfDlfYSE >}}

### Functional programming

[Functional programming](https://en.wikipedia.org/wiki/Functional_programming) is almost exactly what it sounds like: its programming with only functions that have no side-effects or state. Functional programming has some _very_ compelling properties and arguments as to why it should be a preferred paradigm. However, most of the things that we need to do in our daily work contain things that are inherently not functional (i.e. side-effects and state). Many believe functional programming is extremely hard to understand but I would argue it is a fantastic tool to have in ones toolbox and is not that hard to grasp, especially for us within research.

CodeAesthetic - Dear Functional Bros
{{< youtube nuML9SmdbJ4 >}}

### Object-oriented programming

[Object-oriented programming](https://en.wikipedia.org/wiki/Object-oriented_programming) (OOP) is not a well defined concept. Most people who are not professional programmers I have talked to think it is "just use classes and inheritance for everything". While that is often the case, it is not required. The "quality" (readability, performance, etc.) of code that uses classes is completely dependant on how the problem was solved, there will almost always be some state and there will almost always be some side-effects in code, and one can still write good code while using objects. Again I think it is a very good tool to have in ones toolbox and often it is quite intuitive to structure programs by building your own objects.

### Procedural programming

[Procedural programming](https://en.wikipedia.org/wiki/Procedural_programming) is by far my favorite programming paradigm. I would define it as using a set of procedures in a clear sequence that is simple to follow and where control flow is clearly visible and code is modular even without classes. This is not strictly what the broader definition of procedural programming is, which is just using procedures to modify state and possibly have side-effects, but this is generally what it means to tend towards procedural programming. Below is a talk about the return of procedural programming, the middle part can be skipped if you watched the other talk by Richard Feldman on functional programming as it contains some of the same information:

Richard Feldman - The Return of Procedural Programming
{{< youtube vQPHtAxOZZw >}}

## The correct language for the job

Every language has its strengths and weaknesses. Below are some fun "hot takes" on a few languages to highlight the pros and cons of a few.

[Python](https://www.python.org/)
: High level interpreted language which is amazingly simple to learn and rapid to develop in, pretty much everything you can think of is available in Python.
: If used incorrectly will be very slow and error prone, does not allow the low level access you need for optimization.

[Rust](https://www.rust-lang.org/)
: Low level compiled language with an amazing type system and ownership model that can guarantee memory-safety and thread-safety.
: Very hard to learn and forces you into certain development models which might not be what you want for research software.

[C](https://gcc.gnu.org/c99status.html)
: The most common goto (pun intended) low level compiled language, pretty much all parts of our modern computers runs on C, the language itself is very simple and one can almost map its statements directly into the resulting assembly, thereby making almost any optimization you can think of possible (and if that's not enough - you can of course just inline assembly).
: Its so low level that you need to write heaps of code that looks useless to the untrained eye just to not blow everything up later on, error handling is horrendous, doing any high level infrastructure can be a pain, forget rapid prototyping when you have to write literally everything from scratch, there is no modularity and no packaging system, and compilation is far from trivial if you have external dependencies.

If you want to get [nerd-sniped](https://xkcd.com/356/) for a few minutes, check out this blog post called [C Isn't A Programming Language Anymore](https://faultlore.com/blah/c-isnt-a-language/) that discusses some of the consequences of C becoming so prevalent that its become the lingua franca of programming.

[JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Language_overview)
: Interpreted language has become one of the core technologies of the World Wide Web. Pretty much all websites use JavaScript of some kind to have client-side behavior. Its incredibly easy to learn and prototype in and there is a ton of packages and infrastructure around it. Because its wide use it also has a gigantic user community.
: JavaScript is a jumbled mess of a language and has probably been used outside of its reasonable scope more often than any other language out there. JavaScript frameworks are hell on Earth and micro-libraries easily turn into [Dependency hell](https://en.wikipedia.org/wiki/Dependency_hell) that also [make systems very fragile](https://en.wikipedia.org/wiki/Npm_left-pad_incident) and vulnerable. Its horrendous performance (JavaScript is single-threaded) is only saved by web-browsers throwing literally thousands of developers at [JavaScript engines](https://v8.dev/).

[C++](https://isocpp.org/)
: C++ started as C with object-oriented features, its a compiled (to a native binary) language with manual memory management. Many features were added over the years with subtle intricacies, so it is common to use only some subset of features for a project. C++ is commonly used in system programming, game development, and high-performance applications and it is _increadibly_ powerful because pretty much anything you would like to do is going to be supported.
: However, C++ is so diverse and so broad that a code-base can make horrible choices easily. Reading two different project might as well be like reading two different languages because of this width of features.

[Java](https://docs.oracle.com/javase/8/docs/technotes/guides/language/)
: Java is a (VERY) object-oriented, strongly typed, and garbage collected language. It is compiled to runs on a Java Virtual Machine (JVM) so it is not native in that sense. In the last couple of years features that allow functional programming have been added. It is commonly used in enterprise applications, android apps and has an entire family of other languages running on JVM like Kotlin and Scala. Java has a massive framework around it because it has been so used by enterprises.
: However, I think Java is one of the most ridiculed languages (next to JavaScript ironically enough) because of its extreme tendency to abstraction at every point. It has brought us things like the `SimpleBeanFactoryAwareAspectInstanceFactory` class and the `AbstractInterruptibleBatchPreparedStatementSetter`, good luck figuring out what it is actually supposed to do or how it does whatever that is.

For a really funny deep dive into some of the madness of interpreted languages such as JavaScript and Ruby have a look at [Wat](https://www.destroyallsoftware.com/talks/wat).

Some languages I am currently learning and keeping my eyes on are:

[Odin](https://odin-lang.org/)
: Odin is a general-purpose programming language with distinct typing built for high performance, modern systems and data-oriented programming. 

[Zig](https://ziglang.org/)
: Zig is a general-purpose programming language and tool-chain for maintaining robust, optimal and reusable software. Very similar syntax to C.

Both have some very good things going for them, where the more I learn about the features of Zig, the more excited I become to learn it. Currently, I use C for implementations that need to be optimized. But I'm slowly drifting towards wanting to exchange that for something else.

Other languages that are on my radar are:

- [Julia](https://julialang.org/)
- [Go](https://go.dev/)
- [Lua](https://www.lua.org/)
- [Chapel](https://chapel-lang.org/)

> [!Viktigt]
> The takeaway is: don't get attached to one language! They all have their pros and cons. Learning to use a hammer does not make everything a nail. Try to pair a high-level language with a low-level language to cover as many bases as possible. My usual approach is "Write infrastructure in Python that orchestrates the calling of compiled low level languages that actually do the work".


## Homework assignments

Tutorial
: If you have not programmed in Python before - choose some of the learning material above and work through it. Save the code you wrote while learning and note down which material you worked through. 

Scripts, modules and packages
: Create a small Python package following the [packaging tutorial](https://packaging.python.org/en/latest/tutorials/packaging-projects/).
: Install your package into your virtual environment (look up editable install with `-e`).
: Create 2 functions in two separate [modules](https://docs.python.org/3/tutorial/modules.html) inside your package. One function should reverse a list and the other should take two lists as input, reverse the first list and then interleave every other argument of two lists outputting a single new list. You should import the list-reveral function from the other module ([hint: intra-package-references](https://docs.python.org/3/tutorial/modules.html#intra-package-references)).
: Create a scripts in a different location than were the package is that uses this function from the package to interleave the following two strings: `'VOG!lo olH'` and `'el,Wrd ROY'`. 

Python `with` keyword and file handling
: Implement a function in your package that uses the following: [with](https://docs.python.org/3/reference/compound_stmts.html#with), [encode](https://docs.python.org/3/library/stdtypes.html#str.encode), and [decode](https://docs.python.org/3/library/stdtypes.html#bytes.decode) to save an input string in a binary file. Also implement a function to load a string from a binary file.

Plotting
: Install [matplotlib](https://matplotlib.org/) into your environment.
: Implement one of the [examples](https://matplotlib.org/stable/gallery/index).
: Run the code and get the plot to show. 
: Add it to your package and add `matplotlib` as a dependency

> [!Tips]
> Depending on how your system is setup you might need to install `pyqt5` or `pyqt6` in your local environment to show plots. 
