---
title: "Solving problems"
lecture: "04-solving-problems"
weight: 4
---


## Some common patterns

### Dependency injection

[Dependency injection wikipedia entry](https://en.wikipedia.org/wiki/Dependency_injection)

CodeAesthetic - Dependency Injection, The Best Pattern
{{< youtube J1f5b4vcxCQ >}}

### Composition over inheritance

A very useful concept or pattern is [composition over inheritance](https://en.wikipedia.org/wiki/Composition_over_inheritance) which solves many of the problems of Object Oriented programming. More on these programming paradigms later.

CodeAesthetic - The Flaws of Inheritance
{{< youtube hxGOiiR9ZKg >}}

### Adapter

ArjanCodes - Let's Take The Adapter Design Pattern To The Next Level 
{{< youtube fsB8_79zI_A >}}

### Interface

TODO

### Strategy pattern

TODO

### Vectorisation

Usually when we talk about "vectorisation" we mean one of two different things:

#### CPU instruction vectorisation

Specific processors can have a special instruction set for doing [Single instruction, multiple data (SIMD)](https://en.wikipedia.org/wiki/Single_instruction,_multiple_data) operations. 

#### Translating your problem into tensor/matrix/vector operations

TODO

Doing this has special significance in Python as doing sequential loops in Python is very slow due to the nature of interpreted languages. So if we can translate our work into tensor/vector/matrix operations we can offload all looping to `numpy` and hence C. This allows both for automatic parallelisation across cores but also for accessing the speed of C/FORTRAN in Python.

### Online-algorithm

todo

### Map-Reduce

todo 

spark

more later in the advanced lecture

### Visitor

todo

### Honorable mentions

NeetCode - 8 Design Patterns EVERY Developer Should Know
{{< youtube tAuRQs_d9F8 >}}
(While I don't agree that everyone should know all of these and be able to apply them, e.g. the singleton is rare in research software - we just use globals usually, its still a good idea to have heard about them!)

## 

design patterns




##

[protocols in python](https://typing.python.org/en/latest/spec/protocol.html#protocols)

A two explanations of the Strategy pattern 

https://www.youtube.com/watch?v=sZDJJeDNe_M
https://www.youtube.com/watch?v=hVLb3-OE3pM

## Rules and guidelines

https://spinroot.com/gerard/pdf/P10.pdf

## Cost of dependencies

https://bvisness.me/microlibraries/

## Building your own tools

The opening gif was created using this script

{{< details summary="Python script to create an orbit git" >}}
{{< include-code "python" "code/python-scripts/make-orbit-gif.py" "">}}
{{< /details >}}


## Homework assignments

### Logistic map

The task is to implement a function that can repeatedly apply the [logistic map](https://en.wikipedia.org/wiki/Logistic_map) for a specified number of iterations, with a given starting value and a given value of `r`. The function should return all the values for each step of the repeated application of the map. 

Using this implementation, create a large set of starting values in terms of random `x0` between [0, 1] and a regular grid of `r` between [0, 4]. Iterate these values 50 times trough the logistic map.

The goal is to re-produce a arbitrary frame (or frame 50 in this case) of this animation:

![Feigenbaum Tree animation](https://upload.wikimedia.org/wikipedia/commons/0/09/Feigenbaum_Tree.gif)

You should see [Bifurcation](https://en.wikipedia.org/wiki/Bifurcation_theory) occurring, showing that the dynamical system created by repeated applications of the Logistic Map is in fact chaotic for certain values of the functions parameters. The path to chaos is in this case a infinite production of stable regions, also called a period-doubling bifurcation cascade.

### Recommended watching

CppCon 2014: Mike Acton "Data-Oriented Design and C++"
{{< youtube rX0ItVEVjHc >}}
