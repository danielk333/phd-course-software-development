---
title: "Solving problems"
lecture: "04-solving-problems"
weight: 4
---

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

CodeAesthetic - Dependency Injection, The Best Pattern
{{< youtube J1f5b4vcxCQ >}}

CppCon 2014: Mike Acton "Data-Oriented Design and C++"
{{< youtube rX0ItVEVjHc >}}
