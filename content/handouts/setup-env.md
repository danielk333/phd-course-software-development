---
title: "Development environment"
lecture: "00-hello"
weight: 0
---

## TL;DR

Install an editor you like.

Use `venv` to create new environments.

```bash
python -m venv /path/to/new/virtual/environment
```

Activate them with `source <venv>/bin/activate`. Then use `pip` to install packages. Use `python your_stuff.py` to run code.

Optionally: install [pyenv](https://github.com/pyenv/pyenv) to manage python versions.

## What is a "Development environment"

A development environment is simply the set of programs and patterns that you use to

1. write code
2. run code
3. debug code
4. (deploy code)

As many of us who started programming as kids, my first "development environment" was [notepad](https://en.wikipedia.org/wiki/Windows_Notepad) (yes notepad is >40 years old), [cmd](https://en.wikipedia.org/wiki/Cmd.exe) and the then new and cool [mingw32](https://en.wikipedia.org/wiki/MinGW).

In essenece you do not need a lot to have a development environment. Back then `notepad` let me edit the code, `mingw32` and `cmd.exe` allowed me to compile and run it. Debugging occurred by reading compilation and runtime errors (bad as they were in those days) and by littering the code with "im here now!" print statements. Deploying was literally the same as running the code locally so I had that covered too.

> [!Viktigt]
> The most important thing is that your environment does not get in the way of your development. If you need to bend over backwards and spend time wrangling your system just to run and manage the code: rethink your environment. 


## Python environment

One of the most common pitfalls with python is managing multiple projects with different dependencies across different versions, and maintaining these over time.

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

1. A system for downloading and compiling python versions
2. A way to create python virtual environments

> [!Viktigt]
> Never mess with the system python installation - if you don't know what you are doing, you will break your computer. Use enviornments that can be painlessly deleted when broken.

If you already have a preferred way to work with python, go with that and learn how to create and manage virtual environments. During the course I expect you to be able to create a new empty environment with whatever python version we require. 

If you are complexly new to the whole environment thing I like to keep things simple: use pythons built in [venv](https://docs.python.org/3/library/venv.html) command to create environments.

Using this command, you simply choose which python binary should be main python version of the environment by running the `venv` command with that version:

```bash
python -m venv /path/to/new/virtual/environment
```

Lets say you have `python3.11` and `python3.7` installed. You can then make two different virtual environments with two different version by

```bash
python3.11 -m venv env3.11
python3.7 -m venv env3.7
```

To activate the environment (this makes sure `pip`, `python` and your `$PATH` points to the correct places) use the correct command according to your shell:

{{% tabs %}}

{{% tab "POSIX" %}}

| Shell    | Command                           |
|----------|-----------------------------------|
| bash/zsh | `source <venv>/bin/activate`      |
| fish     | `source <venv>/bin/activate.fish` |
| csh/tcsh | `source <venv>/bin/activate.csh`  |
| pwsh     | `<venv>\Scripts\Activate.ps1`     |


{{% /tab %}}

{{% tab "Windows" %}}

| Shell      | Command                       |
|------------|-------------------------------|
| cmd.exe    | `<venv>\Scripts\activate.bat` |
| PowerShell | `<venv>\Scripts\Activate.ps1` |


{{% /tab %}}

{{% /tabs %}}

Then to get out of the environment simply type `deactivate`.

To test what the activation does, first activate the environment, then type `which python` and `pip --version`. Then `deactivate` and try again. You will see that the paths have changed and probably `pip` is not even an available command any more.

Once you have a python enviornment created with `venv` you can install packages into this enviornment using [pip](https://packaging.python.org/en/latest/tutorials/installing-packages/). `pip` by default looks for packages on the central python repository called [PyPI](https://pypi.org/).

Which means that running

```bash
pip install numpy
```

will fetch and install [this](https://pypi.org/project/numpy/) package into the virtual environment. You can inspect what was installed by looking into `<venv>/lib/python3.13/site-packages`.

To manage python versions, I recommend using [pyenv](https://github.com/pyenv/pyenv) to download and compile different python versions. This tool is easy and stores the binaries locally in your home folder . This way you are not contaminating anything else and can easily just delete all the data if you want to start over. For example on my main machine I have:

```bash
danielk@IRF033-danielk ~> ll .pyenv/versions
Permissions Size User    Date Modified Name
drwxr-xr-x     - danielk  9 dec  2024 📁 3.6.15
drwxr-xr-x     - danielk 15 jun  2023 📁 3.7.16
drwxr-xr-x     - danielk 14 jun  2023 📁 3.8.10
drwxr-xr-x     - danielk 14 sep  2022 📁 3.9.13
drwxr-xr-x     - danielk  6 dec  2023 📁 3.10.13
drwxr-xr-x     - danielk 30 jul  2024 📁 3.11.9
drwxr-xr-x     - danielk 17 jan  2024 📁 3.12.0
drwxr-xr-x     - danielk 25 mar  2024 📁 3.12.2
```

While it is not strictly required during the course to have a way to install different python versions, depending on the group-work problems might arise if you cannot internally settle on a single version. 

## Installing python

{{% tabs %}}

{{% tab "MacOS" %}}

On MacOS *TODO*

See [Using Python on macOS](https://docs.python.org/3/using/mac.html) for more information.

{{% /tab %}}

{{% tab "Linux" %}}

Congratulations! You are already done.

{{% /tab %}}

{{% tab "Windows" %}}

To minimize the amount of pain while developing on Windows I recommend using the [Windows Subsystem for Linux](https://learn.microsoft.com/en-us/windows/wsl/install). Following the instructions there you can pretty much install any Linux you would like, such as [Arch](https://wsldl-pg.github.io/ArchW-docs/How-to-Setup/) or [Ubuntu](https://ubuntu.com/desktop/wsl). 

You can then either edit the files directly inside the Linux using e.g. [vim](https://www.vim.org/) or [nvim](https://neovim.io/) or you can open the files in Windows using your preferred editor. You can also couple your [VSCode to WSL](https://code.visualstudio.com/docs/remote/wsl) and edit and develop this way. This is probably the preferred option if you absolutely need to use Windows and already know VSCode and do not want to learn `vim`.

{{% /tab %}}

{{% /tabs %}}

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
- `venvup`
- `venvs`

These create new enviornments in `$HOME/venvs/` with `venv` and can delete them with `venvdel`. But my favorite command is `lazyvenv` which just looks at the name of the current folder and tries to activate a virtual environment with that name, and if it cant find one it creates it.

{{< details summary="Example fish shell script function for working with python venv" >}}
{{< include-code "fish" "code/shell-scripts/venv-tools.fish" "">}}
{{< /details >}}

{{< details summary="Example bash shell script function for working with python venv" >}}
{{< include-code "bash" "code/shell-scripts/venv-tools.sh" "">}}
{{< /details >}}

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
- [Language Server Protocol (LSP)](https://en.wikipedia.org/wiki/Language_Server_Protocol) integration
- Searching and goto
- File-browser

Having these features will make life a lot simpler and speed up development by quite a lot. 

Having said that, for this course I recommend:

1. If you already have an editor you like and know - go with that
2. If you want to setup something exactly like you want it, want to be as efficient as possible with editing, and you are ok with spending lots of time achieving that, use/learn [nvim](https://neovim.io/). One advantage of `nvim` is that it is a terminal editor which means: no fancy GUI to worry about, this can be used on any machine you SSH into. A similar bare-bones editor but with a GUI instead which can be customized to the gills is [sublime text](https://www.sublimetext.com/). 
3. If you just want something that just works out of the box where you can install extensions that take care of LSP's and everything: go with [vscode](https://code.visualstudio.com/docs/setup/linux) or [vscodium](https://vscodium.com/).
4. If you want all the bells and IDE-whistles with python debuggers and environment handling: go with [spyder](https://www.spyder-ide.org/) or [pycharm](https://www.jetbrains.com/pycharm/).

Personally - I use `VSCode` and `nvim`. I mostly still have `VSCode` until I fully learn how to use [vim-motions](https://www.ssp.sh/brain/vim-language-and-motions/) efficiently. In my journey I have went trough pretty much the entire list of editors and IDEs above, I started out simple, sought out complexity, and now I'm back inside a terminal just coding again. 

## Homework assignments

If you have not used python before, go trough a few tutorials, e.g. [python.org tutorial](https://docs.python.org/3/tutorial/index.html), and complete a few coding excersizes e.g. from [exercism](https://exercism.org/tracks/python/exercises) or [adventofcode](https://adventofcode.com/) in addition to the below in order to catch up.


Scripts, modules and packages
: Create a small python package following the [packaging tutorial](https://packaging.python.org/en/latest/tutorials/packaging-projects/).
: Install your package into your virtual environment.
: Create 2 functions in two separate [modules](https://docs.python.org/3/tutorial/modules.html) inside your package. One function should reverse a list and the other should take two lists as input, reverse the first list and then interleave every other argument of two lists outputting a single new list. You should import the list-reveral function from the other module ([hint: intra-package-references](https://docs.python.org/3/tutorial/modules.html#intra-package-references)).
: Create a scripts in a different location than were the package is that uses this function from the package to interleave the following two strings: `'VOG!lo olH'` and `'el,Wrd ROY'`. 

Python basic syntax
: Implement a function in your package that uses the following: [f-strings](https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals), [with](https://docs.python.org/3/reference/compound_stmts.html#with), and [encode](https://docs.python.org/3/library/stdtypes.html#str.encode) / [decode](https://docs.python.org/3/library/stdtypes.html#bytes.decode) to save or load an input string in a binary file.

Plotting
: Install [matplotlib](https://matplotlib.org/) into your environment.
: Implement one of the [examples](https://matplotlib.org/stable/gallery/index).
: Run the code and get the plot to show. 


> [!Tips]
> Depending on how your system is setup you might need to install `pyqt5` or `pyqt6` in your local environment to show plots. 
