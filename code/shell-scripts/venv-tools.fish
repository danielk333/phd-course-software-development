function user_confirm
    while true
        set -l prompt "$argv [y/N] "
        read -l -P $prompt confirm

        switch $confirm
        case Y y
            return 0
        case '' N n
            return 1
        end
    end
end

function venvdel
    set -l path "$HOME/venvs/$argv"
    if user_confirm "Do you want to delete '$path'?"
        echo "removing '$path' ...."
        rm -rfv "$path"
    end
end

function activate
    source ~/venvs/$argv/bin/activate.fish
end

function lazyvenv
    set -l name (basename (pwd))
    if test -d ~/venvs/$name
        activate $name
    else
        echo "No venv found: creating venv"
        venv
        if test -d ~/venvs/$name
            activate $name
        end
    end
end

function venvup
    if test (count $argv) -eq 0
        set venv_target (basename (pwd))
    else
        set venv_target $argv[1]
    end

    if test (count $argv) -eq 2
        set pypath ~/.pyenv/versions/$argv[2]/bin/python
    else
        set pypath (which python)
    end

    $pypath -m venv --upgrade ~/venvs/$venv_target
end



function venv
    if test (count $argv) -eq 0
        set venv_target (basename (pwd))
    else
        set venv_target $argv[1]
    end

    if test (count $argv) -eq 2
        set pypath ~/.pyenv/versions/$argv[2]/bin/python
    else
        set pypath (which python)
    end

    echo "New venv target=$venv_target" 
    if not test -d ~/venvs
        mkdir ~/venvs
    end
    if test -d ~/venvs/$venv_target
        echo "Folder '~/venvs/$venv_target' exists, choose a different name for new venv"
    else
        $pypath -m venv ~/venvs/$venv_target
        echo "Created virtualenv $venv_target"
    end
end

function venvs
    for dr in ~/venvs/*
        echo (string split / $dr)[-1] "| python" (cat $dr/pyvenv.cfg | grep version)
    end
end
