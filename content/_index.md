---
title: Introduction
---

## Course details

Credits
: 7.5 ECTS
: Workload ranges from 3-6 weeks full time work depending on your current programming skills.
: Currently, only PhD students can earn course credits from this course.

Grading
: The grades for this course are `Pass` and `Fail`. 
: The grading is based 50% on the completion of homework tasks and 50% on completion and quality of the group work practicals.
: Around 80% completion is required for a pass.

Lectures
: Hybrid on zoom and recorded
: 90 minutes including practical moments

Practicals
: Done in groups
: Larger tasks started during a half day hackathon

## Software development for researchers

The last 50 years have seen a staggering increase in the use of computers and available computer power. 

{{< columns "45% 45%" "1em">}}

![Supercomputer performance since the 1990s](computer-performance.png#expandable.light "Supercomputer performance from www.top500.org.")

<--->

The graph to the left shows the growth of supercomputers performance since the 1990s. The logarithmic y-axis shows performance in Floating Point Pperations Per Second (FLOPS). The green markers are the combined performance of the 500 largest supercomputers, the orange the fastest supercomputer and the blue the 500'th fastest. 

{{< /columns >}}

This availability of computational resources together with a similar inverse trend for storage and price per byte has ushered in a golden age of scientific computing.

However this also means that most researchers today will have to produce computer code at some point in their career. Whether it be scripting or library development. The most basic tasks today require programming such as code to run other code and libraries, code to parse and analyze data from other code, code to visualize data for publication, code to compile statistics, or code to record data from instruments. 

Often code starts of small and transient, with an idea and an experiment. Then when proven useful, it grows and persists in time. Years later the scope, needs, uses, and circumstances are completely different than when it started. 

Well designed and maintained code can change the course of an entire scientific discipline, accelerating the research of hundreds of scientists world-wide. At the same time, re-inventing the wheel can exhaust and waste the time of equally many PhD candidates and scientists if software is not made available or the software sharing paradigm is not embraced. Being able to know when to re-write something, when to use someone elses library or code, when to contribute to their code, or when to fork, and _how_ to do these things can make the difference between months and years worth of productivity. 

**This course aims to teach the tools and skills needed to navigate the modern software oriented world of scientific research.**

## Prerequisites

To take full use of this course the participant should:

1. Have working knowledge of a programming language, preferably [Python](https://www.python.org/) as that is the language in which the course is given. However, if one has high level knowledge of another language, the course can be completed in that language or it is usually relatively easy to learn Python with the pre-existing knowledge.

2. Have experience using the terminal and running software on ones machine. Preferably a Unix based system as most instructions will refer to Linux.

## Learning goals

The goal is that by the end of the course the participant should be able to:

- Design a software system
- Implement the design using programming
- Solve, or be able to learn how to solve, problems using programming and tools
- Write readable and maintainable software
- Read and understand others software
- Collaborate with others in software development
- Implement strategies and tools for efficient development and for producing reliable software
- Be able to competently discuss software development with researchers and professional software developers

## Course philosophy

I firmly believe that programming and software development is a practical skill, not a theoretical one. Much like you would not tell a pole vaulter to just read a few books and watch some guides and then go compete, we should *not* tell that to people who wants to improve their programming either. 

To get good at programming and software development you have to:
- Write code, write a lot of code
- Read other peoples code
- Have other read your code
- Throw away code, and write it again
- Talk to others about code and writing code
- Get coached on writing code
- Learn the connection between code and hardware
- Read about others opinions and experience on writing code
- Read research and theory on software

This course tries to strike a balance between the above with a focus on actually doing something practical and getting feedback and giving feedback on that work.

## Replication crisis

A major motivation for such an extensive approach to software development is to ensure maintainable and reproducible code which upholds proper research ethics.

Consider the case of laboratory work, the first thing we get comfortable with is to keep a lab-protocol during an experiment of what nob was turned to what setting, or how much of a compound was mixed with another. This ensures that the experiment is reproducible, a cornerstone of the scientific method. Of course we should uphold software to the same rigor when we do numerical experiments and advanced calculations. 

Imagine reading a math proof where suddenly the author just states “well, this next part of the proof is in my desk. But, its mine and not nicely typed out so I rather not share it, just take my word for it that it looks right when i read it.”. Most would reject that proof as being completely untrustworthy! 

When the code is not described accurately enough in a paper, the code is not publicly available, and/or the code is so obscure that it cannot be used by any independent research group: independent reproducibility and verification is impossible (see [Replication crisis](https://en.wikipedia.org/wiki/Replication_crisis)). And even if the algorithms / equations are described correctly in the published paper so that replication of method is possible, this is no guarantee that replication of results is possible since the code could still be faulty. This concept applies to both data science and simulations. 
