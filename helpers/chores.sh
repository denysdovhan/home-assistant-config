#!/bin/bash

# Prepare git
git config user.name "Denys Dovhan"
git config user.email "denysdovhan@gmail.com"

# Update content
python3 helpers/update_content.py README.md
python3 helpers/update_content.py custom_components/README.md
python3 helpers/update_content.py docs/config/index.md
python3 helpers/update_content.py docs/config/custom-extensions.md
python3 helpers/commit_updates.py
