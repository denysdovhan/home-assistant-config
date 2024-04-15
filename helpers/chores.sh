#!/bin/bash

# Prepare git
git config user.name "Denys Dovhan"
git config user.email "denysdovhan@gmail.com"

python3 helpers/update_readme.py
python3 helpers/commit_updates.py
