---
title: "Software design and architecture"
lecture: "08-design"
weight: 8
---


## Communicating design / architecture

### Diagrams

{{< tutorial diagrams "For a small tutorial on how to make different diagrams, see" >}}

One of the better models I have encountered for displaying software architecture (or design) is the
[C4 model](https://c4model.com/). Below is a video by its creator describing the model:

Visualising software architecture with the C4 model - Simon Brown, Agile on the Beach 2019
{{< youtube x2-rSnhpw0g >}}

There are also a number of other diagrams that are useful for communicating the design and
function of your software:

- Functional diagrams
- State diagrams
- [Sequence diagrams](https://en.wikipedia.org/wiki/Sequence_diagram)

### Code

Documentation can do a great deal to communicate design and architecture, especially package and
module level docstrings, or a design page of a separate documentation. You can also signal a lot
with just good naming conventions of modules and sub packages, for example this structure:

```
src/package/
├── __init__.py
├── server.py
├── client.py
├── plotting.py
├── cli.py
```

Directly tells me that there is a server and a client and that this functionality is (hopefully)
mostly contained to these separate modules. I can also see that I can probably use this as a
stand-alone library in addition to the CLI since these have been separated. 
I also know that there is a dedicated plotting module which indicates that plotting is
not littered throughout the code, but rather isolated to this file. Consider instead this structure: 

```
src/package/
├── __init__.py
├── functions.py
├── processes.py
```

How would I know where to look to find certain functionality?

## Design by example

It is easy to think that the design of the architecture is a given because whatever architecture is
chosen will solve the problem, and that the focus should be on code-level design decisions.

However, there may be many architectures that fulfill the requirements! And if you do now know of
them, you do not even have a choice. So below are a listing of projects that contain interesting
designs and architectures which can hopefully help broaden your horizons. 

### My projects

So the easiest for me to point to are my own projects as I know exactly how they are designed!

#### `sorts`

Space Object Radar Tracking Simulator (SORTS) is a collection of modules designed for research
purposes concerning the tracking and detection of objects in space. Its ultimate goal is to simulate
the tracking and discovery of objects in space using radar systems in a very general fashion. This
library is currently in its 4th refactoring because we discovered a lot while writing it the last 3
times! So this is a good example of a larger library style package written by researchers that did
not really know everything when we started. The largest problem that caused the current refactoring
was that the library was TOO general, causing it to be hard to debug and hard to optimize.

- [GitHub repository](https://github.com/danielk333/sorts)


### `hardtarget`

General package for hard target processing of radar data in the `digital_rf` format using matched
filtering. This is a typical example of a general purpose tool for data pipeline construction.

- [GitHub repository](https://github.com/danielk333/hardtarget)

#### `rain`

ReseArch Infrastructure Network (RAIN) is a Python package that allows users to exchange messages
between each other. This package was created with the purpose of sending status information between
research infrastructure in the Arctic regions of the Nordics. This is a very different type of
package compared to what researchers generally work with. It is small and simple but it was not
trivial for us, i.e. not software engineers, to put it togehter. We are currently trying to fix the
last issues and then use it to enable automatic control of several instruments in real time.

- [GitHub repository](https://github.com/danielk333/rain)


#### `pyorb`

Python implementation of the definition of Kepler orbits and related transformations, nothing more,
nothing less. An example of a really simple package to do a simple and well defined thing well.

- [GitHub repository](https://github.com/danielk333/pyorb)


#### `runningman`

Runtime Manager, i.e. a running-man(ager), for setting up a set of service like processes that are
asynchronously managed by triggers and fed data trough queues. This is again a very different type
of package since it is basically a runtime for instrumentation. I am using this to setup the meteor
camera stations to record the video, do automatic detection, archive the results, do calibration,
ect. In real-time.

- [GitHub repository](https://github.com/danielk333/runningman)

#### `dasst`

Dynamical Astronomy Statistical Simulations Toolbox, or DASST (pronounce as "dust") for short. A
toolbox for all things small body dynamics simulations that has a statistical component to them.
Mainly focused on meteoroid streams. This is basically 90% unfinished, its an idea I had like 8
years ago. Have not had time to finish it. But i did add one thing which i discovered i needed a
lot: meteor orbit-determination. This turns out was a good move because this is now used by several
radar meteor pipelines around the world. Ill get to the cool parts of the package at some point.

> [!Varning] Work in progress

- [GitHub repository](https://github.com/danielk333/dasst)

#### `metecho`

Radar Meteor Head Echo Analysis package - metecho. Package for processing radar data measuring
meteor head echoes. Mainly focused on fitting meteoroid models to the processed data and performing
the additional tasks needed such as calibration and error estimation. This is a good example of bad
decisions coming back to haunt me. When i started my PhD I decided to keep the code in MATLAB rather
then directly rewriting, now here I am and need to rewrite it anyway and now it is like 5 times more
MATLAB code. Since my work pertins to meteor head echo studies, I am going to do that a lot. Hence I
want reusable software and hence I am now doing that rewrite. 

> [!Varning] Work in progress - porting from MATLAB

- [GitHub repository](https://github.com/danielk333/metecho)

#### `ablate`

A collection of ablation models implemented or wrapped in Python to use for research, mostly
directed towards meteoroids and meteor research. This is an example of re-implementing models from
the literature that do not exist as open source packages that can then be used in research. Not all
packages have to invent some new method, this package has already proven very useful for validation
and analysis reasons.

- [GitHub repository](https://github.com/danielk333/ablate)

#### `rebound-player`

This is a software to reconstruct simulations created in
[Rebound](https://rebound.readthedocs.io/en/latest/) to be replayed in real-time using OpenGL
rendering. Again a very different type of software where the focus IS on visualization rather than
the algorithms, but this again turned into a question of novel algorithms because visualizing
millions of particles in video frame rates is not trivial.

> [!Varning]
> Work in progress

- [IRF Gitlab repository](https://gitlab.irf.se/danielk/rebound-player)


### Python wrapped libraries and functions

#### `scipy`

[scipy](https://github.com/scipy/scipy) is one of the quintessential scientist python package. The
entire structure is scipy is fascinating for many reasons. Not only can one deep-dive into how
algorithms and special functions are actually calculated (like e.g. what approximations the
exponential integral uses) but also how the package is built and distributed. Scipy contains _a lot_
of foreign code, current the statistics are:

- Python 60.6%
- C 16.9%
- C++ 8.9%
- Fortran 8.7%
- Cython 4.3%
- Meson 0.5%
- Other 0.1%

One thing I learned from looking at this package was how to completely switch out `setuptools` for
[Mason](https://mesonbuild.com/) for building the package (and some of the utilities that [already
exist](https://mesonbuild.com/meson-python/tutorials/introduction.html)).

#### `rebound`

[rebound](https://github.com/hannorein/rebound) is "An open-source multi-purpose N-body code". The
integrator itself is written in C but it is mostly used trough the Python interface that they have
developed. I would say that `rebound` is an example of a extremely successful research software.

### Making API calls in Python

### `rebound`

Rebound implements a convenience function where one can simply state the name of the object and it
will get the state of that object from [Horizons](https://ssd.jpl.nasa.gov/horizons/), this implementation makes an API call using the
Python [requests](https://github.com/psf/requests) package and is contained in [this
file](https://github.com/hannorein/rebound/blob/main/rebound/horizons.py) in the repository.

### `spacetrack`

The [spacetrack](https://github.com/python-astrodynamics/spacetrack) package provides a convenient
way to download data about resident space objects directly from the database usually published on
[space-track.org](https://www.space-track.org/).


### `hardtarget`

In our `hardtarget` package mentioned above we also provide a option to download data, in this case
EISCAT radar data from the EISCAT portal page, using either `requests` or `wget` as a subprocess.
The relevant implementation of this can be found in the [download.py file](https://github.com/danielk333/hardtarget/blob/main/src/hardtarget/radars/eiscat/download.py)

### More

If any reader has suggestions for more repositories or projects to look for inspiration in, please
contact me with the recommendation and I will check it out and probably add it here!

## Design and architecture experience

The best way to gain experience is to actually design a lot of software. _Shocking, right_! There
are a few hobby projects I think are very good for learning design, such as something involving
networks, a compiler or interpreter, or a game. However, the best projects, I have found at least,
are the ones I really want to do.

For example, I have always been fascinated by the technology behind compilers: its amazing that it
actually works! So that's why it was both very fun and educational when I wrote one for the
[Brainf*** language](https://en.wikipedia.org/wiki/Brainfuck).

Similarly, I wanted to keep better track of my configurations and rather than using a ready made
system I decided to design my own since it was a type of problem I had never tackled before and I
had no problem motivating myself to work on it in my free time (and I have much better
configurations of my machines now!).

But if you need some inspiration, this blog post called [Challenging projects every programmer
should try](https://austinhenley.com/blog/challengingprojects.html) details some suggestions. And as
is usual on the internet, there is a reaction video to go with it:

ThePrimeTime - Projects Every Programmer Should Try
{{< youtube yeatOU5vVsA >}}


## Factors to consider when designing

The below description are taken from [Kullbrandt, Kenneth - The Efficiency of Good Software
Practices](https://urn.kb.se/resolve?urn=urn:nbn:se:ltu:diva-90443).

### Compatibility

Compatibility is a measurement for requirements on both software and hardware, operating system,
etc. A low compatibility represents difficulties running the software on another platform due to
restrictions mentioned above, while a high compatibility would make this process easy.

### Extensibility

Extensibility is a measurement for how hard it is to add new code to an existing project. Low
extensibility would represent a lot of effort to add features to an existing project, while a
project with high extensibility would generally take less time.

### Modularity

Modularity is how much a project can be broken down into smaller pieces for implementation and
maintenance, allowing complex software to be easier to maintain. Low modularity would represent code
that would be hard to use in different contexts, or functions that are used for only one specific
case, while high modularity would represent code that can be used in different parts of the project
without having to change it.

### Fault-tolerance/Robustness

Fault-tolerance/Robustness is the resistance to corrupt data or user input. A robust program will
not crash or pose a risk to other software given bad inputs. A program with low
fault-tolerance/robustness would crash or cause memory leaks given bad input, while a program with
high fault-tolerance/robustness would either gracefully exit or be able to continue without crashing
while still producing the right results.

### Maintainability

Maintainability is a measurement of how hard a project is to maintain. Many factors calculate into
this, but generally it scales negatively with project size, external dependencies, code readability.
A project with low maintainability would require a larger overhead to maintain, with extra time
needed to work on it in general. A project with high maintainability would require less work to be
able to produce the same results due to less overhead.

### Reusability

Reusability is an aspect in software engineering to focus on using existing assets where usable
instead of creating new ones. It builds on creating on finding a large common ground and extending
it instead of creating a unique version for each. A program with low reusability would have more
unique code in it, with each being used few times,while a program with high reusability would have
more functions that are used repeatedly throughout the program.

### Security

Security is the aspect of protecting the program and end-user from malicious and accidental attacks.
It can be summarized as the program continuing to function normally during malicious attacks. It is
related to robustness as well, but with a larger focus on protecting the user instead of the
program. A program with low security might pose a risk to other computers in the same network, or
might completely compromise the host. Conversely, a program with high security will sanitize and
verify input such that these problems wouldn't occur.

### Usability

Usability is a subjective measurement of how hard it is for the end-user to interact with the
program and the experience of using the program. A program with low usability might be slow,
unintuitive, and generally user unfriendly. A program with high usability might have special designs
for user interface and experience with focus for the needs of the user base.

### Performance

Performance is a measurement of how quickly a program runs, how much memory it uses, file sizes, and
more. A computer with low performance might be sluggish, take long time to execute, or might use a
lot of memory for the task. A computer with high performance might be parallelized well for the
given task, be able to compute demanding tasks in real-time, and have better memory management.

### Portability 

Portability is how hard it is to change the requirements of project while sustaining the same
functionality. Another way to view it would be how difficult it is to transfer the program between
two different systems. Low portability might occur as a program that only works on a single system
or requires large amounts of work to work with other systems. High portability might manifest as
being able to run natively on most systems with little overhead.

### Scalability

Scalability is the ability of a program to perform when working with a different scale of hardware.
It is directly related to performance, but also includes additional factors such as how it performs
over networks or running on multiple nodes. Low scalability might be a program that has the same
performance no matter the amount of nodes it runs on. In contrast, high scalability might have a
high parallelization efficiency, allowing the performance to scale nearly linearly with the increase
of computing power.


## Data oriented-design

For our professions, this is the recommended approach. Know your data and you shall know how to find
performance. In the handout on [Solving problems](handouts/solving-problems) one of the sections
covers data oriented-design, if you did not have a look then I suggest you do so now!

To further highlight why understanding your data and how you represent it matters I wanted to
contrast linked lists vs vectors. [Linked lists](https://en.wikipedia.org/wiki/Linked_list) are the
standard example of a data structure that should allow for easy deletes and inserts since you just
shuffle a few pointers around versus a vector of contiguous memory where you have to basically move
part of the list every time. However, it turns out that mostly this is not the case: vectors are
pretty much always better.

I could not find the original video by Bjarne Stroustrup but I did find this reaction video, it
explains nicely why how you arrange your data matters so much for performance and the above issue
with linked lists:

ThePrimeTime - Why You Should AVOID Linked Lists
{{< youtube cvZArAipOjo >}}


## Homework

### Code review

Do a group review of the practical task from the other groups, take some notes on design and
contrast with your own design decisions.

### Present your software

Choose a piece of software you have written, it could be something from your work or something you
developed during this course, such as the simple calculator or the numerical integrator. 

Prepare a flowchart, according to the C4 model, outlining the design and present the design during the next lesson.

