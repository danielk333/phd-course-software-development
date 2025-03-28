---
title: "Development environment"
lecture: "00-hello"
weight: 0
---

## Handouts

This handout collects much relevant information about what to consider when setting up ones development environment, such as choice of editor and Python environment management. For first time Python users or beginner codes it is recommended to simply follow the tutorials linked below. For more experienced users, and later in this course, the below handout may serve as a starting point for upgrading your environment and how you interact with it.

## Skill tree

{{< tutorial skill_tree "Get an achievement list to track milestones on your journey! See" >}}

## First time Python user?

{{< tutorial python "For a short Python environment tutorial, see" >}}

Code Refinery also has some great tutorials on [setting up a starting environment](https://coderefinery.github.io/installation/), including installing and setting up [git](https://git-scm.com/) and [github
](https://github.com/), editors such as VSCode and vim, and [anaconda](https://www.anaconda.com/). Although for this course, I do not recommended anaconda for beginners as we aim to directly work with environments as a starting point and anaconda might be something you choose to use later on. 

Code Refinery together with Aalto Scientific Computing also has some crash courses on using the shell, which is required for this course:

{{< youtube xbTTDLA3txI >}}


## Don't know which editor to choose?

{{< tutorial editor "For a short guide on choosing an editor, see" >}}

## What is a "Development environment"

A development environment is simply the set of programs and patterns that you use to

1. write code
2. run code
3. debug code
4. (deploy code)

As many of us who started programming as kids, my first "development environment" was [notepad](https://en.wikipedia.org/wiki/Windows_Notepad), [cmd](https://en.wikipedia.org/wiki/Cmd.exe) and the then new and cool [mingw32](https://en.wikipedia.org/wiki/MinGW).

In essenece you do not need a lot to have a development environment. Back then `notepad` let me edit the code, `mingw32` and `cmd.exe` allowed me to compile and run it. Debugging occurred by reading compilation and runtime errors (bad as they were in those days) and by littering the code with "im here now!" print statements. Deploying was literally the same as running the code locally so I had that covered too.

> [!Viktigt]
> The most important thing is that your environment does not get in the way of your development. If you need to bend over backwards and spend time wrangling your system just to run and manage the code: rethink your environment. 


## Python environment

One of the most common pitfalls with Python is managing multiple projects with different dependencies across different versions, and maintaining these over time.

This is why there are a whole host of tools that have been developed to do this for you. A few popular alternatives are:

- [venv](https://docs.python.org/3/library/venv.html)
- [pyenv](https://github.com/pyenv/pyenv)
- [uv](https://github.com/astral-sh/uv)
- [anaconda](https://www.anaconda.com/)
- [miniconda](https://docs.anaconda.com/miniconda/)
- [poetry](https://python-poetry.org/)
- [pipenv](https://pipenv.pypa.io/en/latest/)
- [hatch](https://github.com/pypa/hatch)
- [pdm](https://pdm-project.org/en/latest/)

In addition to these, many editors today have built in environment management. Some popular options are:

- [spyder](https://www.spyder-ide.org/)
- [vscode](https://code.visualstudio.com/docs/setup/linux)
- [vscodium](https://vscodium.com/)
- [pycharm](https://www.jetbrains.com/pycharm/)

During this course I recommend choosing two things:

1. A system for downloading and compiling Python versions
2. A way to create Python virtual environments

> [!Viktigt]
> Never mess with the system Python installation - if you don't know what you are doing, you will break your computer. Use environments that can be painlessly deleted when broken.

If you already have a preferred way to work with Python, go with that and learn how to create and manage virtual environments. During the course I expect you to be able to create a new empty environment with whatever Python version we require. 

If you are completely new to the whole environment thing I like to keep things simple: use Python's built in [venv](https://docs.python.org/3/library/venv.html) command to create environments.

Using this command, you can create an environment with Python equal to the system Python version by running the `venv` command:

```bash
python -m venv /path/to/new/virtual/environment
```

The Python that runs the command dictates the version. Lets say you have `python3.11` and `python3.7` installed. You can then make two different virtual environments with two different version by

```bash
python3.11 -m venv env3.11
python3.7 -m venv env3.7
```

Then you can activate this environment as per [the documentation](https://docs.python.org/3/library/venv.html).

Once you have a Python environment created with `venv` you can install packages into this environment using [pip](https://packaging.python.org/en/latest/tutorials/installing-packages/). `pip` by default looks for packages on the central Python repository called [PyPI](https://pypi.org/).
Which means that running

```bash
pip install numpy
```

will fetch and install [this](https://pypi.org/project/numpy/) package into the virtual environment. You can inspect what was installed by looking into `<venv>/lib/python3.13/site-packages`. If provided with a local path `pip` will also install from a locally available package source. You can even directly install from a version control repository, such as git, by using the [pip VCS format](https://pip.pypa.io/en/latest/topics/vcs-support/#vcs-support).

To manage Python versions, I recommend using [uv](https://docs.astral.sh/uv/) (or [pyenv](https://github.com/pyenv/pyenv) if you cant get `uv` to work) to download and manage Python versions. This tool is easy and stores the binaries locally in your home folder. This way you are not contaminating anything else and can easily just delete all the data if you want to start over. For example on my main machine I have:

```bash
danielk@IRF033-danielk ~> ls -l .local/share/uv/python/
Permissions Size User    Date Modified Name
drwxr-xr-x     - danielk 3 mar 16.29  📁 cpython-3.10.16-linux-x86_64-gnu/
drwxr-xr-x     - danielk 3 mar 17.17  📁 cpython-3.13.2-linux-x86_64-gnu/
drwxr-xr-x     - danielk 3 mar 17.03  📁 cpython-3.7.9-linux-x86_64-gnu/
drwxr-xr-x     - danielk 3 mar 17.03  📁 cpython-3.9.21-linux-x86_64-gnu/
```

While it is not strictly required during the course to have a way to install different Python versions, depending on the group-work problems might arise if you cannot internally settle on a single version. 

Another option for running different Python versions is by using containers. This can be done using [docker](https://www.docker.com/) or [podman](https://podman.io/). Here I would recommend `podman` as it is the open source alternative. 

For example to run a Python 3.12 container I can do the following to download

```bash
danielk@IRF033-danielk ~> podman pull python:3.12
Trying to pull docker.io/library/python:3.12...
```

and run it:

```bash
danielk@IRF033-danielk ~> podman run -ti python:3.12 /bin/bash
root@e75f5e9469bf:/# python --version
Python 3.12.9
root@e75f5e9469bf:/# python
Python 3.12.9 (main, Feb 25 2025, 05:22:35) [GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import pathlib
>>> 
```

There are many good tutorials on how to work with containers when developing code, e.g. this [docker blog-post](https://www.docker.com/blog/containerized-python-development-part-1/).


> [!Notera]
> This website is built automatically on changes to the git-repository inside of a `registry.gitlab.com/pages/hugo/hugo_extended:0.139.3` container using the [Gitlab CI](https://docs.gitlab.com/ci/) system!

## Working with `venv`

As it is really annoying to type `source /really/long/path/to/activate.fish` all the time it is recommended to remove some of that friction by creating a few shell-scripts or aliases. 

It can be as simple as putting the following function in your `.bashrc`

```bash
activate() {
    source "$HOME/venvs/$1/bin/activate"
}
```

which assumes that all your environments are stored under `$HOME/venvs/`. Then you can simply type `activate that-project`. 

The below snippets of bash and [fish shell](https://fishshell.com/) scripts are the ones I personally use together with `pyenv` to provide the following functions:

- `lazyvenv`
- `activate`
- `venv`
- `venvdel`
- `venvs`

These create new environments in `$HOME/venvs/` with `venv` and can delete them with `venvdel`. But my favorite command is `lazyvenv` which just looks at the name of the current folder and tries to activate a virtual environment with that name, and if it cant find one it creates it. 

This is very similar to how `uv` works if one lets it manage all aspects of your virtual environment.

{{< details summary="Example fish shell script function for working with python venv" >}}
{{< include-code "fish" "code/shell-scripts/venv-tools.fish" "">}}
{{< /details >}}

{{< details summary="Example bash shell script function for working with python venv" >}}
{{< include-code "bash" "code/shell-scripts/venv-tools.sh" "">}}
{{< /details >}}

However, if you choose to e.g. use `uv` completely you will never even activate your environment: `uv` will manage that for you. Similarly with many other environment managers you do not directly interact with the environment.

> [!Notera]
> This is just an example of how one can work with environments in a minimalistic way. Sometimes more complexity is good and sometimes less complexity is better. Often less complex systems are more robust but require you to learn the basics. Either way, rolling your own environments will teach you how they work and that might save heaps of time later, even if you transition into a management system that does it for you.

## Editor

We already mentioned some popular editors that have a lot of functionality baked into them and are often called Integrated Development Environments (IDEs). However, most of this course will not focus on making us experts at using IDEs but making us experts at software development. For that we simply need to write and edit code efficiently.

A few popular editors are:

- [vim](https://www.vim.org/)
- [nvim](https://neovim.io/)
- [emacs](https://www.gnu.org/software/emacs/)
- [sublime text](https://www.sublimetext.com/)
- [kate](https://kate-editor.org/)
- [geany](https://www.geany.org/)
- [spyder](https://www.spyder-ide.org/)
- [vscode](https://code.visualstudio.com/docs/setup/linux)
- [vscodium](https://vscodium.com/)
- [pycharm](https://www.jetbrains.com/pycharm/)
- [notepad++](https://notepad-plus-plus.org/)

At minimum I recommend having an editor that has the following features:

- Syntax highlighting
- [Language Server Protocol (LSP)](https://en.wikipedia.org/wiki/Language_Server_Protocol) integration or some sort of symbol finding system ( e.g. [ctags](https://github.com/universal-ctags/ctags) )
- Text searching and go-to functionality
- File-browsing or file-searching

Having these features will make life a lot simpler and speed up development by quite a lot. 

Personally - I use `VSCode` and `nvim`. I mostly still have `VSCode` until I fully learn how to use [vim-motions](https://www.ssp.sh/brain/vim-language-and-motions/) efficiently. In my journey I have went trough pretty much the entire list of editors and IDEs above, I started out simple, sought out complexity, and now I'm back inside a terminal just coding again. 

A pretty cool interactive vim tutorial is available on [openvim](http://www.openvim.com).

## Homework assignments

Install git
: If [git](https://git-scm.com/) is not installed on your system (try `git --version`), install it (remember to always favor your package manager) and create a new repository for homework solutions.
: If you want - upload the repo on [codeberg](https://codeberg.org/), [github](https://github.com/), or [gitlab](https://gitlab.irf.se/).

Virtual environments
: Choose a method to manage virtual environments and implement it, write a cheat sheet for creating, entering, exiting and deleting environments.

Editor mastery
: Go trough the shortcuts that your chosen editors has, create a short cheat sheet for the shortcuts that you think are the most useful! 
: Some suggestions are "Goto definition", "Fuzzy find [file/symbol]", "Goto line", "Goto symbol"
