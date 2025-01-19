#!/bin/bash
# This script adds an alias for gptcmd to ~/.zshrc using sudo

# Absolute path to the script you want to alias
main_py_path=$(cd "$(dirname "$0")/../src" && pwd)/main.py

# Check if main.py exists
if [ ! -f "$main_py_path" ]; then
    echo "Error: main.py not found at $main_py_path"
    exit 1
fi

# Define the alias command
alias_command="alias gptcmd='python3 $main_py_path'"

# Path to Zsh configuration file
zshrc_file="$HOME/.zshrc"

# Check if the alias already exists in ~/.zshrc
if grep -Fxq "$alias_command" "$zshrc_file"; then
    echo "Alias already exists in $zshrc_file"
else
    # Use sudo to add the alias to ~/.zshrc
    sudo bash -c "echo \"$alias_command\" >> \"$zshrc_file\""
    echo "Alias added to $zshrc_file"
fi

# Prompt the user to reload ~/.zshrc
source ~/.zshrc
