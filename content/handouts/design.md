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

There are also a number of other diagrams that are super useful for communicating the design and
function of your software:

- Functional flow diagrams
- Control flow diagrams
- Data flow diagrams
- State diagrams
- Sequence diagrams

**TODO: add links to good descriptions of the above diagrams**

### Code

Documentation can do a great deal to communicate design and architecture, especially package and
module level docstrings or a design page of a separate documentation page. You can also signal a lot
with just good naming conventions of module and sub packages, for example this structure:

```
src/pyant/
├── __init__.py
├── beam.py
├── beams
│   ├── __init__.py
│   ├── beams.py
│   ├── eiscat_3d.py
│   ├── eiscat_uhf.py
│   ├── mu.py
├── coordinates.py
├── models
│   ├── __init__.py
│   ├── airy.py
│   ├── cassegrain.py
├── plotting.py
```

Directly tells me that the model is separate from the real world instance, as I know that `cassegrain` is
a general model for radiation patterns while `eiscat_uhf` is a radar that exists in the eal world.
I also know that there is a dedicated plotting module which indicates that plotting is
not littered throughout the code but isolated to this file. 

Similarly, if the software is supposed to contain a server somewhere, I would expect to find a file or package somewhere called `server` or something similar. If instead it was just baked into the same file the CLI and this was called something generic like `functions`, how would I know where to look other than starting to grep trough files or randomly following LSP definitions.

## Design by example

*TODO: add a bunch of repositories to look trough for good design choices*

## Design and architecture experience

The best way to gain experience is to actually design a lot of software. _Shocking, right_! There
are a few hobby projects I think are very good for learning design, such as something involving
networks, a compiler or interpreter, or a game. However, the best projects, I have found at least,
are the ones I really want to do.

For example, I have always been facinated by the technology behind compilers: its amazing that it
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

