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

## Documentation building

There are a few tools that build documentation specifically for Python projects. However, really to build documentation all you need is a good static website generator! A few examples are

- [mkdocs](https://www.mkdocs.org/)
- [hugo](https://gohugo.io/)
- [jekyll](https://jekyllrb.com/)
- [pelican](https://getpelican.com/)
- [sphinx](https://www.sphinx-doc.org/en/master/)

For a more complete list, see e.g. [myles/awesome-static-generators](https://github.com/myles/awesome-static-generators).

There are also tools to simply convert structured text to HTML, such as [pandoc](https://pandoc.org/), that can be used for essentially the same purpose, but you would have to set up multi-file and templates yourself.

Notably sphinx has specialized tools for making Python documentation, but currently it can get very complicated very fast. Hence my current recommendation is `mkdocs` as its very simple to setup and configure and uses markdown by default.

## docstrings

Having standardized docstring styles is probably a good idea as you will be encouraged to be consistent and you can use community tools for e.g. parsing and rendering your docstrings.

Some standard docstring formats are:

- [numpydoc](https://numpydoc.readthedocs.io/en/latest/install.html) (recommended)
- [sphinx.autodoc](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html)
- [google](https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings)

## Rules and guidelines

There are several styles and guidlines for writing code, on all levels that were mentioned in the lecture. The most known one within Python is [PEP 8](https://peps.python.org/pep-0008/). PEP stands for Python Enhancement Proposals and this particular proposal was originally made in 2001. PEP 8 together with proposals such as [the one for docstrings](https://peps.python.org/pep-0257/) make up the rules which most linters follow. Other static code analyzers such as [mypy](https://mypy-lang.org/) turn styles into rules, e.g. here that type hints (according to [PEP 484](https://peps.python.org/pep-0484/)) must be adhered to.

However, there are other sets of rules that might be good to read trough just to get an idea of how enforcing these rules can change the code you produce. One such document I can recommended reading trough is the [NASA The Power of Ten – Rules for Developing Safety Critical Code](https://spinroot.com/gerard/pdf/P10.pdf).

## Resources for making readable projects

- [Semantic Versioning](https://semver.org/) - how to handle *your* versions
- [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) - "This project aims to be a better changelog convention."
- [Git tags](https://git-scm.com/book/en/v2/Git-Basics-Tagging) - How to tag in git

## Complexity

Another static code analyzer for python is [radon](https://radon.readthedocs.io/en/latest/). It measures

> raw metrics: SLOC, comment lines, blank lines, &c.
> Cyclomatic Complexity (i.e. McCabe’s Complexity)
> Halstead metrics (all of them)
> the Maintainability Index (a Visual Studio metric)

One of the metric mentioned above is [Cyclomatic complexity](https://en.wikipedia.org/wiki/Cyclomatic_complexity). This concept basically means how many linearly independent paths you can take trough the code you executed. This is something that might pop up if you have an LSP that measures it and it usually means that you have a _lot_ of branching and code-calling going on in your code. Sometimes this is just a necessary evil, but often it can be reduced to make the calling structure of your code simpler.

## Examples

Writing good examples is a bit of an art and an exercise in knowing who your user base is. I would recommended some simple guidelines to start with:

- Solve a problem in your example
- Make it non-trivial so that the reader gains understanding of the code
- Make it simple enough that its easy to comprehend
- Make it easy to run and modify so one can play around with it
- Make sure your examples are up to date

I remember reading a post on the The Developer Advocacy Handbook called [Write excellent code examples](https://developer-advocacy.com/write-excellent-code-examples) a while back and it might spark some ideas for you as well.

## Homework assignments

Make documentation for your code
: Make a `docs` folder inside your course repository and build a small wiki-page of your notes.
: Compile the docs to html using [mkdocs](https://www.mkdocs.org/).

Write docstrings
: Write a docstrings for your last homework. Both module level and function level.

Advanced documentation
: If you want a more complicated example, use the [mkdocstrings](https://mkdocstrings.github.io/) package to compile an API page of the package you made earlier in the course.
: If you don't already have a favourite format, use [numpydoc](https://numpydoc.readthedocs.io/en/latest/format.html). You can also try the [material theme](https://squidfunk.github.io/mkdocs-material/).

### Recommended watching

CodeAesthetic - Naming Things in Code
{{< youtube -J3wNP6u5YU >}}

CodeAesthetic - Don't Write Comments
{{< youtube Bf7vDBBOBUA >}}
