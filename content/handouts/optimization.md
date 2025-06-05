---
title: "Optimization"
lecture: "13-optimization"
weight: 13
---

## Assembly, CPU instructions and computer architecture

For the audience that takes this course it will be quite unlikely that you will ever have to
actually read or write assembly. However, it can be important to understand that it exists, what it
does, and how it works. For example, understanding that a square root is many many more instructions
in the CPU than a multiplication can maybe help you write your algorithms in such a way that they
are naturally fast. 

Below are some good videos that go trough these concepts.


Computer Timescales Mapped onto Human Timescales - Computerphile
{{< youtube PpaQrzoDW2I >}}

How CPU Memory & Caches Work - Computerphile
{{< youtube SAk-6gVkio0 >}}

How Branch Prediction Works in CPUs - Computerphile
{{< youtube nczJ58WvtYo >}}

Theo - I finally know how CPUs work (w/ Casey Muratori)
{{< youtube jC_z1vL1OCI >}}

Actually, the entire [playlist with Matt Godbolt on
Computerphile](https://www.youtube.com/playlist?list=PLzH6n4zXuckpwdGMHgRH5N9xNHzVGCxwf) is
fantastic and I can really recommend watching trough it at some point. And yes, that is *the*
legendary Godbolt that created [Compiler Explorer](https://godbolt.org/).


If you want to try writing some assembly yourself just to experiment, I have played around with
[fasm](https://flatassembler.net/) before which you can install a compiler for.

Additionally, while trying to figure out if my compiler actually managed to properly optimize my
code and while reading the output assembly I used these resources:

- [University of Virginia Computer Science - x86 Assembly Guide](https://www.cs.virginia.edu/~evans/cs216/guides/x86.html)
- [Agner Fog. Technical University of Denmark - Software optimization resources](https://www.agner.org/optimize/?e=0#0)
- [Agner Fog. Technical University of Denmark - Optimizing subroutines in assembly language](https://www.agner.org/optimize/optimizing_assembly.pdf)

## Comments to lecture

During the lecture we noticed the "page faults" statistic from `perf`. As we discussed, we assumed
it is quite close to cache misses (see [CPU cache](https://en.wikipedia.org/wiki/CPU_cache)).
However, it turns out the answer is both yes and no, looking at definition of a [page
fault](https://en.wikipedia.org/wiki/Page_fault), it is actually due to the much more complicated
layout of modern CPU's which now has a memory management unit (MMU). So far I have not found good
documentation that details the relation between page faults and cache misses but it seems that in
most cases, a page fault is triggered by a cache miss, see [this stackoverflow
post](https://stackoverflow.com/a/50328447). 


## Optimization

Casey Muratori is a well known proponent of writing performant code by default and he has a wealth
of knowledge on the subject. So if you want to get into optimization I can recommend having a listen
to the series of lectures he has created on the subject, or at least the first episode that is
linked below which is about his take on the subject.

Molly Rocket - Refterm Lecture Part 1 - Philosophies of Optimization
{{< youtube pgoetgxecw8 >}}

In one of the previous lectures I linked a video about optimizing hash maps. In case you did not
watch it that time, I would recommend giving it a go for this lecture as now with this context
in mind it might make a lot of sense!

strager - Faster than Rust and C++: the PERFECT hash table
{{< youtube DMQ_HcNSOAI >}}

Lastly, below are two very entertaining stores about optimization that I can recommend watching/listening
to.

First is the story of [hatetris](https://qntm.org/hatetris) on the episode [CORECURSIVE #109: HATETRIS - Obsession, Friendship, and World Records](https://corecursive.com/hatetris-with-david-and-felipe/). Hatetris is a version of Tetris where you always get the worst piece, and how people beat world records by both algorithmic advances but also optimization.

I like math, and sometimes I do some "recreational math" and watch videos about math. One evening I found a video about a hilarious story of community optimization. The problem itself is about finding five-letter words with twenty-five unique letters.

Stand-up Maths - Someone improved my code by 40,832,277,770%
{{< youtube c33AZBnRHks >}}


## Algorithms

In the lecture I mentioned the visualization of sorting algorithms and data representations used by chess engine algorithms, so below I have linked those videos!

Timo Bingmann - 15 Sorting Algorithms in 6 Minutes
{{< youtube kPRA0W1kECg >}}


Coding with Tom - I Coded a Chess Engine in 7 Languages to test Performance!
{{< youtube cFNBIYwht8o >}}

## Testing language speed

Lastly I would like to highlight how bad most "language speed tests" are. They are almost never
representations of the real world applications and sometimes just plain bad. Below is a longer
discussion about why one of these tests that has made the rounds on the internet is not good.

ThePrimeTime - It's Really Just That Bad
{{< youtube EH12jHkQFQk >}}
