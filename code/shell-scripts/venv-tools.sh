# user_confirm function
user_confirm() {
    local prompt="$1 [y/N] "
    while true; do
        read -p "$prompt" confirm
        case "$confirm" in
            Y|y) return 0 ;;
            ''|N|n) return 1 ;;
        esac
    done
}

# venvdel function
venvdel() {
    local venvpath="$HOME/venvs/$1"
    if user_confirm "Do you want to delete '$venvpath'?"; then
        echo "Removing '$venvpath' ...."
        rm -rfv "$venvpath"
    fi
}

# activate function
activate() {
    source "$HOME/venvs/$1/bin/activate"
}

# lazyvenv function
lazyvenv() {
    local name
    name=$(basename "$(pwd)")
    if [[ -d "$HOME/venvs/$name" ]]; then
        activate "$name"
    else
        echo "No venv found: creating venv"
        venv
        if [[ -d "$HOME/venvs/$name" ]]; then
            activate "$name"
        fi
    fi
}

# venv_up function
venvup() {
    local venv_target pypath
    if [[ $# -eq 0 ]]; then
        venv_target=$(basename "$(pwd)")
    else
        venv_target="$1"
    fi

    if [[ $# -eq 2 ]]; then
        pypath="$HOME/.pyenv/versions/$2/bin/python"
    else
        pypath=$(which python)
    fi

    "$pypath" -m venv --upgrade "$HOME/venvs/$venv_target"
}

# venv function
venv() {
    local venv_target pypath
    if [[ $# -eq 0 ]]; then
        venv_target=$(basename "$(pwd)")
    else
        venv_target="$1"
    fi

    if [[ $# -eq 2 ]]; then
        pypath="$HOME/.pyenv/versions/$2/bin/python"
    else
        pypath=$(which python)
    fi

    echo "New venv target=$venv_target"
    if [[ ! -d "$HOME/venvs" ]]; then
        mkdir "$HOME/venvs"
    fi
    if [[ -d "$HOME/venvs/$venv_target" ]]; then
        echo "Folder '~/venvs/$venv_target' exists, choose a different name for new venv"
    else
        "$pypath" -m venv "$HOME/venvs/$venv_target"
        echo "Created virtualenv $venv_target"
    fi
}

# venvs function
venvs() {
    for dr in "$HOME/venvs"/*; do
        echo "$(basename ${dr}) | python $(grep version ${dr}/pyvenv.cfg)"
    done
}
