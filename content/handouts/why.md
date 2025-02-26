---
title: "Motivation"
lecture: "01-why"
weight: 1
---

## Links to lecture material

- [Lars Wirzenius, "40 years of programming"](https://liw.fi/40/)
- [Monya Baker, "1,500 scientists lift the lid on reproducibility"](https://www.nature.com/articles/533452a)
- [AI is Creating a Generation of Illiterate Programmers](https://nmn.gl/blog/ai-illiterate-programmers)
- [Quake III Arena Fast inverse square root](https://en.wikipedia.org/wiki/Fast_inverse_square_root)
- [Some of the software I have written](https://danielk.developer.irf.se/software/)


## Homework assignments

Scripts, modules and packages
: Create a small python package following the [packaging tutorial](https://packaging.python.org/en/latest/tutorials/packaging-projects/).
: Install your package into your virtual environment.
: Create 2 functions in two separate [modules](https://docs.python.org/3/tutorial/modules.html) inside your package. One function should reverse a list and the other should take two lists as input, reverse the first list and then interleave every other argument of two lists outputting a single new list. You should import the list-reveral function from the other module ([hint: intra-package-references](https://docs.python.org/3/tutorial/modules.html#intra-package-references)).
: Create a scripts in a different location than were the package is that uses this function from the package to interleave the following two strings: `'VOG!lo olH'` and `'el,Wrd ROY'`. 

Python basic syntax
: Implement a function in your package that uses the following: [f-strings](https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals), [with](https://docs.python.org/3/reference/compound_stmts.html#with), and [encode](https://docs.python.org/3/library/stdtypes.html#str.encode) / [decode](https://docs.python.org/3/library/stdtypes.html#bytes.decode) to save an input string in a binary file. Also implement a function to load a string from a binary file.

Plotting
: Install [matplotlib](https://matplotlib.org/) into your environment.
: Implement one of the [examples](https://matplotlib.org/stable/gallery/index).
: Run the code and get the plot to show. 


> [!Tips]
> Depending on how your system is setup you might need to install `pyqt5` or `pyqt6` in your local environment to show plots. 
