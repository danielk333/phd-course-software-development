---
title: "Your tools and environment"
lecture: "03-tools"
weight: 3
---

## Minimal setups

A cut down version of my current NeoVim setup which is still quite minimal can be found [here](https://gitlab.irf.se/danielk/starting-nvim#).

## Managing "dotfiles"

As the amount of tools you depend on increases and the number of computers go > 1 (e.g. when you want to change to a new machine), you probably want a nice way to manage your configuration files or so called [dotfiles](https://wiki.archlinux.org/title/Dotfiles). 

First of all you probably want to keep your dotfiles in a git repository so that they are version controlled and backed up. To do this you will need to somehow link them from this git repository to their location on your computer where they act as the configuration. This is what tools like [GNU Stow](https://www.gnu.org/software/stow/manual/stow.html) does. It manages a repository of dotfiles and creates symbolic links to their intended locations. This makes getting started on a new system trivial!

Dreams of Autonomy - Stow has forever changed the way I manage my dotfiles
{{< youtube y6XCebnB9gs >}}

As a hobby project I have built [my own dotfiles manager](https://github.com/danielk333/dotfiles-installer) that essentially does the same thing but with additional options to have diverging dotfiles between systems and installation of extra things. Doing these type of projects allow me to try things that I usually do not get exposed to and this has helped me a lot. My next thing to do is add in this hobby project is a terminal UI using [urwid](https://urwid.org/) to learn how `urwid` works since it could be useful in making TUIs for interacting with some of my analysis pipelines, but I don't want to try it on something that complicated until I understand what it is and how it works and if it would be useful.

## Editors

### vim-motions

A good article about the power of vim-motions, regardless of which editor you use, is 
[vim is not about speed](https://levelup.gitconnected.com/vim-is-not-about-speed-88968ae4283c).

A good starting tutorial on vim-motions can be found here:

{{< youtube lWTzqPfy1gE >}}

And I like this video series on advanced motions:

{{< youtube qZO9A5F6BZs >}}

### VsCode

Currently my [Code-OSS](https://github.com/microsoft/vscode) uses these extension

```bash
danielk@IRF033-danielk ~> code --list-extensions
bungcip.better-toml
danielgavin.ols
gruntfuggly.todo-tree
james-yu.latex-workshop
llvm-vs-code-extensions.vscode-clangd
ms-python.black-formatter
ms-python.debugpy
ms-python.flake8
ms-python.python
redhat.vscode-yaml
streetsidesoftware.code-spell-checker
streetsidesoftware.code-spell-checker-swedish
twxs.cmake
usernamehw.errorlens
waderyan.gitblame
```

I really like `ErrorLens` together with the `ms-python` suite as it gives me direct feedback on bad formatting, bugs, and syntax errors. `todo-tree` is really helpful in navigating across large projects that use the `# TODO:` style syntax. I also recommend the [VsCode-NeoVim](https://open-vsx.org/extension/asvetliakov/vscode-neovim) extension to start learning vim-motions: that's how I got started at one point.

There are a TON of tutorials on VsCode due to its popularity so I wont link any here.

### Sublime Text

Below are a few good starting points for beginning to master Sublime text posted on a Youtube channel dedicated to Sublime Text.

{{< youtube wUsKBuTZ0dw >}}

{{< youtube VuyDseaaJl8 >}}

### NeoVim

Below is an example starting setup of `nvim` with most of the bells and whistles that you would want:

{{< youtube w7i4amO_zaE >}}

[This blogpost](https://www.josean.com/posts/neovim-linting-and-formatting) also provides a nice tutorial on how to setup several aspects of NeoVim manually without using a distribution.

Some other useful things to know about `nvim` that you might not just discover while learning the editor are:

- `lcd %:h` - Local `cd` to folder (`:h`) of current file (`%`)
- `gf` - goto file under cursor, the `<cfile>` "variable" does the same in command mode, so e.g. `:e <cfile>` would edit that.
- `:mksession!session.vim` will make save the current session to the file `session.vim`, the `!` causes overwrite if it exists
- `:save {file}` will save the current buffer under the new name `{file}` and change the buffer to point to that file
- **More things will be added here as time passes!**


## Homework assignments

Debug a python program
: Take one of programs that you wrote in a homework task and step trough the code with either 1) pdb, 2) pudb, 3) spyder/VsCode/other built in debugger, 4) a general DAP interface.

Inventory of tools
: Write down what you generally use in terms of tooling while developing but also write a separate list of what you would like to have, now that you have seen a sample during the lecture.

Watch / read / listen to material about your tools
: Choose some material that goes trough the usage of your tools. Be it from the suggestions above or something that you found by your self on the internet. Write down what you consumed and maybe some of the most important points you learned and share it with the class: it might help others!

Find duplicate files
: Download [this](code/python-scripts/create_files.py) python file, read it first (as you always should!!), then run it to create a folder called "a_few_files" with different files in it.
: Your task is to find out which files in this folder are duplicates, i.e. their content is the same.
: You should be able to time the execution of your script externally using `time find_duplicates.py`. 
