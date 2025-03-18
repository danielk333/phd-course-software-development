---
title: "Solving problems"
lecture: "04-solving-problems"
weight: 4
---

## Cost of dependencies

We often talk about not re-inventing the wheel and solving a problem yourself can seem useless. However, we must also recognize that pulling in a dependency to solve a problem also carries a huge cost.

I recommend reading this blog post [Micro-libraries need to die already](https://bvisness.me/microlibraries/) about micro-libraries. If you would rather have a live-reading, there is one [here by ThePrimeagen](https://www.youtube.com/watch?v=IVmIEtwsaYk). 

Another good talk about pitfalls of dependencies is the below from the DevOps conference.

{{< youtube VNqmHJtItCs >}}

## Some common patterns

Below are some common patterns and ideas with respect to solving problems that I think are useful to know. Many of these patterns might look like they are doing the same thing. It looks like this because in many instances they *are*. For any particular problem the possible ways it can be solved spans a huge space. Hence these patterns will often overlap, not make sense in some situations and fall cleanly into line in others. Learning about these patterns does not mean that you should use them everywhere you can but rather that you now see more possible solutions to your problem and sometimes those fit better with what you are trying to accomplish.

### Dependency injection

[Dependency injection wikipedia entry](https://en.wikipedia.org/wiki/Dependency_injection)

CodeAesthetic - Dependency Injection, The Best Pattern
{{< youtube J1f5b4vcxCQ >}}

### Composition over inheritance

A very useful concept or pattern is [composition over inheritance](https://en.wikipedia.org/wiki/Composition_over_inheritance) which solves many of the problems of Object Oriented programming. More on these programming paradigms later.

CodeAesthetic - The Flaws of Inheritance
{{< youtube hxGOiiR9ZKg >}}

### Adapter

[Adapters](https://en.wikipedia.org/wiki/Adapter_pattern) are useful when you want to plug something external into your own internal logic and this is mostly the case where I have used this pattern. 

ArjanCodes - Let's Take The Adapter Design Pattern To The Next Level 
{{< youtube fsB8_79zI_A >}}

### Interface

There are many types of interfaces, the specific one I am thinking about here is using [protocols](https://typing.python.org/en/latest/spec/protocol.html#protocols) and [abstract base classes](https://docs.python.org/3/library/abc.html) in Python to specify how something should be implement / behave. I sometimes find the `@abstractmethod` decorator for the `ABC` class is quite useful for defining what is needed in case someone wants to extend my code since it will crash directly if not all methods are implemented. Similarly if I am looking for building a very large structure of interaction - I might use `Protocol` instead.

ArjanCodes - Protocol Or ABC In Python - When to Use Which One?
{{< youtube xvb5hGLoK0A >}}

Another way to think about interfaces is just specifying structure of data rather than code. In this case useful concepts are [dataclasses](https://docs.python.org/3/library/dataclasses.html), packing [structs](https://docs.python.org/3/library/struct.html), or using Googles [protobuf python bindings](https://protobuf.dev/getting-started/pythontutorial/).

### Strategy pattern

I have been using the [Strategy pattern](https://en.wikipedia.org/wiki/Strategy_pattern) for years without even knowing I was doing it: it was just the most modular and readable way to solve many problems I face. 

Isaac Harris-Holt - The Strategy Pattern Will Make Your Python Code CLEANER
{{< youtube hVLb3-OE3pM >}}


Bitlytic - Modular Upgrades Made Easy Using the Strategy Pattern
{{< youtube sZDJJeDNe_M >}}

### Data oriented design

Although [data oriented design](https://en.wikipedia.org/wiki/Data-oriented_design) is more of a software design philosophy rather than a solution pattern, it is really conducive to thinking about your individual small solutions in a efficient way, and may guide you in a good direction if no clear pattern is visible. The below talk is again at CppCon but the fundamental idea that you should let the data drive your code design rather than how **you** think about the data, is fundamental to performance. It also ties in to the other patterns listed below.

CppCon 2014 - Mike Acton "Data-Oriented Design and C++"
{{< youtube rX0ItVEVjHc >}}

### Vectorisation

Usually when we talk about "vectorisation" we mean one of two different things: SIMD instructions or using vectors in your algorithm.

#### Translating your problem into tensor/matrix/vector operations

Translating your problem into any vector-like structure and then doing operations on those vectors has special significance in Python as doing loops in Python is very slow due to the nature of interpreted languages. So if we can translate our work into tensor/matrix/vector operations we can offload all looping, processing, casting, etc. to `numpy` and hence C - no interpretation needed. This also allows for automatic parallelisation across cores, for accessing the speed of C/FORTRAN in Python, and for SIMD (see below) to be utilized fully.

The following is a fantastic introduction into vectorising with `numpy` and how to use [broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html) to be memory efficient while doing it - a must watch for us scientists!

PyCon UK - Vectorise all the things! How basic linear algebra can speed up your data science code: J Burchell
{{< youtube 9_mhjjlKjDo >}}


#### CPU instruction vectorisation - SIMD

Specific processors can have a special instruction set for doing [Single instruction, multiple data (SIMD)](https://en.wikipedia.org/wiki/Single_instruction,_multiple_data) operations.

Since we do not have access to direct assembler instructions in Python it does not really have a concept of SIMD instructions, however `numpy` does! And since a few versions back `numpy` actually provides a way to look at all the functions it implements see which are optimized: the [lib.introspect.opt_func_info](https://numpy.org/doc/stable/reference/generated/numpy.lib.introspect.opt_func_info.html) function. On my machine I see for example that almost all functions have [AVX-512](https://en.wikipedia.org/wiki/AVX-512) instruction set available versions, but that all are currently running the regular [AVX2](https://en.wikipedia.org/wiki/Advanced_Vector_Extensions) versions.

In C you can pull in `immintrin.h` and use e.g. the `__m256` data type which is a 256-bit vector containing 8 floats instead of using 8 different `float` data types. In the CPU these 8 floats will be operated on in parallel if compiled towards the correct architecture. More on low-level code inspection in later lectures.


### Online-algorithm

An [Online algorithm](https://en.wikipedia.org/wiki/Online_algorithm) is simply an implementation that can consume the input in sequence without having the entire data available at the start. The concept is incredibly powerful and can be used in everything from something as simple as [calculating standard deviations](https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance#Welford's_online_algorithm) to operating real time systems or handling your computers memory cache.

The [following lecture](https://www.youtube.com/watch?v=IyWOjd-oZ4o) is quite long but introduces the concept of online algorithms and other useful concepts such as cache misses and paging which are important when we look at optimisation, but this is already quite outside the scope of this course so watch at your own peril!

### Map-Reduce

The [Map-Reduce](https://en.wikipedia.org/wiki/MapReduce) concept is a way to implement an algorithm such that it is easy to deploy to a super computer cluster trough use of ready made frameworks such as [Hadoop](https://hadoop.apache.org/) and [Spark](https://spark.apache.org/). If a computation is implemented in terms of spark operations (using the Python package), the python code will generate an optimized set of instructions for the super computer cluster to perform on the data. This instruction set can then be submitted to the cluster for execution. Interestingly enough, many algorithms can be implemented in terms of maps and reduces, although this is not [guaranteed](https://en.wikipedia.org/wiki/MapReduce#Theoretical_background).

Computerphile - MapReduce
{{< youtube cvhKoniK5Uo >}}

Computerphile - Apache Spark 
{{< youtube tDVPcqGpEnM >}}

### Visitor

The [Visitor pattern](https://en.wikipedia.org/wiki/Visitor_pattern) is something that might be much more common in regular software development compared to developing research software, especially physics research. Nevertheless, it is a useful mental model to have for abstracting away the algorithm and operations from the structure of the data that is being processed and shines in things like parsing structured documents such as HTML or XML.

CppCon 2022 - Breaking Dependencies - The Visitor Design Pattern in Cpp - Klaus Iglberger 
{{< youtube PEcy1vYHb8A >}}
(The above talk is at CppCon so the code is C++ but the concepts are still very well presented. After pretty much 30 minutes the rest is C++ specific information and more advanced versions of the visitor pattern and can be skipped.)

### Honorable mentions

NeetCode - 8 Design Patterns EVERY Developer Should Know
{{< youtube tAuRQs_d9F8 >}}
(While I don't agree that everyone should know all of these and be able to apply them, e.g. the singleton is rare in research software - we just use globals usually, its still a good idea to have heard about them!)


## Building your own tools

The opening gif was created using this script:

{{< details summary="Python script to create an orbit git" >}}
{{< include-code "python" "code/python-scripts/make-orbit-gif.py" "">}}
{{< /details >}}

Since I work a lot with orbits - I made a tool that specifically converts orbits from Cartesian coordinates to Kepler elements in an efficient way with lots of helper functions to make working with that type of data easy. Since I divided it up into a package I can depend on that package and the functions in this package are *heavily* tested so I can thrust the results.

## Homework assignments

### Logistic map

The task is to implement a function that can repeatedly apply the [logistic map](https://en.wikipedia.org/wiki/Logistic_map) for a specified number of iterations, with a given starting value and a given value of `r`. The function should return all the values for each step of the repeated application of the map. 

Using this implementation, create a large set of starting values in terms of random `x0` between [0, 1] and a regular grid of `r` between [0, 4]. Iterate these values 50 times trough the logistic map.

The goal is to re-produce a arbitrary frame (or frame 50 in this case) of this animation:

![Feigenbaum Tree animation](https://upload.wikimedia.org/wikipedia/commons/0/09/Feigenbaum_Tree.gif)

You should see [Bifurcation](https://en.wikipedia.org/wiki/Bifurcation_theory) occurring, showing that the dynamical system created by repeated applications of the Logistic Map is in fact chaotic for certain values of the functions parameters. The path to chaos is in this case a infinite production of stable regions, also called a period-doubling bifurcation cascade.

### Recommended watching and reading

Ideally, during this course, it would be good if you watched the videos and read the articles linked above.
