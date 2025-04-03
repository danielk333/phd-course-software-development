---
title: Python environment
---

## Installing python

{{% tabs %}}

{{% tab "MacOS" %}}

On MacOS python comes pre-installed but its usually a good idea to also have a system-package manager installed such as 

- [Homebrew](https://brew.sh/)
- [MacPorts](https://www.macports.org/)
- [Nix](https://nixos.org/)

See also [Using Python on macOS](https://docs.python.org/3/using/mac.html) for more information.

{{% /tab %}}

{{% tab "Linux" %}}

Congratulations! You are already done.

{{% /tab %}}

{{% tab "Windows" %}}

To minimize the amount of pain while developing on Windows I recommend using the [Windows Subsystem for Linux](https://learn.microsoft.com/en-us/windows/wsl/install). Following the instructions there you can pretty much install any Linux you would like, such as [Arch](https://wsldl-pg.github.io/ArchW-docs/How-to-Setup/) or [Ubuntu](https://ubuntu.com/desktop/wsl). 

You can then either edit the files directly inside the Linux using e.g. [vim](https://www.vim.org/) or [nvim](https://neovim.io/) or you can open the files in Windows using your preferred editor. You can also couple your [VSCode to WSL](https://code.visualstudio.com/docs/remote/wsl) and edit and develop this way. This is probably the preferred option if you absolutely need to use Windows and already know VSCode and do not want to learn `vim`.

{{% /tab %}}

{{% /tabs %}}

## Basic Python environment

1. Install an editor you like or use the one you already have.
2. Use `venv` to create new environments.

```bash
python -m venv /path/to/new/virtual/environment
```

3. To activate the environment (this makes sure `pip`, `python` and your `$PATH` points to the correct places) use the correct command according to your shell.

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

To test what the activation does, first activate the environment, then type `which python` and `pip --version`. Then `deactivate` and try again. You will see that the paths have changed and probably `pip` is not even an available command any more.

4. Then use `pip` to install packages.

```bash
pip install numpy
```

5. Use `python your_stuff.py` to run code.
6. Use `deactivate` to exit the environment.

### Multiple python version 

1. Install [uv](https://docs.astral.sh/uv/) to manage python versions.
2. Create a new environment with (where `X` is the desired python version, skip `--python` to use default).

```bash
uv venv --python 3.X --seed /path/to/new/virtual/environment
```

3. Activate like before.
4. Install new python versions with `uv python install 3.X`.

Read the `uv` docs for more info.
