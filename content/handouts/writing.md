---
title: "Writing code for Humans to read and Machines to run"
lecture: "05-writing"
weight: 5
---

## Coding principles

### Clean code

Like everything there are pros and cons also to "Clean code". I put this concept into quotes here because as far as I know the term was coined together with the publishing of a book by Robert C. Martin called "Clean Code: A Handbook of Agile Software Craftsmanship". This book has been mentioned a lot and was praised for its push towards more readable code, which I agree with, and principles such as SOLID and DRY (see below). But as with any set of rules, there should be exceptions and there are downsides. One of the major ones being performance, for a nice walk-trough of this issue  - see the below talk:

Molly Rocket - "Clean" Code, Horrible Performance
{{< youtube tD5NrevFtbU >}}

### SOLID

The [SOLID](https://en.wikipedia.org/wiki/SOLID) principles stand for:

- Single responsibility
- Open–closed
- Liskov substitution
- Interface segregation
- Dependency inversion

Awesome-coding - SOLID Principles Explained
{{< youtube V3TUEeB0kW0 >}}

### DRY

The [Don't repeat yourself](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself), or DRY, principle is exactly what it sounds like. It is better to extract repeated code into a function, procedure, or class instead of copy-pasting the same code into 20 places. It makes it easy to test that code, to edit that code, and to overview the function of that code. However, this principle should not be taken as a holy quest to abstract all code so that no code that is even remotely similar is ever repeated. Rather it should be kept in mind and applied in moderation where needed.

## Rules and guidelines

https://spinroot.com/gerard/pdf/P10.pdf

## Homework assignments

### Recommended watching

CodeAesthetic - Naming Things in Code
{{< youtube J3wNP6u5YU >}}

CodeAesthetic - Don't Write Comments
{{< youtube Bf7vDBBOBUA >}}
