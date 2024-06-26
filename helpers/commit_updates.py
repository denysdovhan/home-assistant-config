#!/usr/bin/env python3

import subprocess

STATUS_CMD = "git status --porcelain"
README = "README.md"
CUSTOM_COMPONENTS_README = "custom_components/README.md"
DOCS = "docs"
HA_VERSION = ".HA_VERSION"

def main():
  output = subprocess.run(STATUS_CMD.split(), capture_output=True).stdout.decode()
  
  for line in output.split('\n'):
    path = line[3:]

    if path.startswith(DOCS):
      subprocess.run(["git", "add", path])
      subprocess.run(["git", "commit", "-m", f"docs: Update docs"])

    if path == README:
      subprocess.run(["git", "add", README])
      subprocess.run(["git", "commit", "-m", f"docs: Update README.md"])
    
    if path == CUSTOM_COMPONENTS_README:
      subprocess.run(["git", "add", CUSTOM_COMPONENTS_README])
      subprocess.run(["git", "commit", "-m", f"docs: Update README.md for custom_components"])

    if path == HA_VERSION:
      with open(HA_VERSION) as file:
        version = file.read().strip()
      subprocess.run(["git", "add", HA_VERSION])
      subprocess.run(["git", "commit", "-m", "--no-verify", f"chore: Update Home Assistant to {version}"])

if __name__ == "__main__":
  main()
