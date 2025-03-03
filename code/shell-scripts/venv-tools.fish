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


function venv
    if test (count $argv) -eq 0
        set venv_target (basename (pwd))
    else
        set venv_target $argv[1]
    end
    if test (count $argv) -ge 3
        set extra_args $argv[3..(count $argv)]
    else
        set extra_args ""
    end

    if not test -d ~/venvs
        mkdir ~/venvs
    end
    echo "New venv target=$venv_target" 

    if test -d ~/venvs/$venv_target
        echo "Folder '~/venvs/$venv_target' exists, choose a different name for new venv"
        return 1
    else
        if type -q uv
            if test (count $argv) -eq 2
                uv venv --seed --python $argv[2] $extra_args ~/venvs/$venv_target
            else
                uv venv --seed ~/venvs/$venv_target
            end
        else
            if test (count $argv) -eq 2
                echo "Cant use specific python version without uv"
                return 1
            end
            python -m venv ~/venvs/$venv_target
        end
        echo "Created virtual enviornment $venv_target"
    end
end

function venvs
    for dr in ~/venvs/*
        echo (string split / $dr)[-1] "| python" (cat $dr/pyvenv.cfg | grep version)
    end
end
