#!/usr/bin/env python3

from itertools import groupby
import subprocess
import json
import yaml
from pathlib import Path

README = Path("README.md")
AUTOMATIONS = Path("automations.yaml")
URL = "https://github.com/denysdovhan/home-assistant-config/blob/{commit_hash}/{fname}"

def git_latest_edit_hash(filename):
    """Get the git hash to save with data to ensure reproducibility."""
    git_output = subprocess.check_output(
        ["git", "rev-list", "-1", "main", str(filename)]
    )
    return git_output.decode("utf-8").replace("\n", "")

def slugify(s):
    return s.lower().strip().replace(" ", "-").encode("ascii", "ignore").decode("ascii")

def to_file(lines):
  return "".join(lines)

def get_emoji(group):
  emojis = {
      "Alarm": "🚨",
      "Alert": "🔔",
      "Climate": "🌡️",
      "Energy": "⚡️",
      "Presence": "🔘",
      "Light": "💡",
      "Media": "🎵",
      "Mode": "🚦",
      "System": "🖥️",
      "Vacuum": "🧹",
      "Water": "💦",
  }
  return emojis.get(group, "⚙️")

def read_file(fname):
  with open(fname) as file:
    return file.readlines()

def write_file(fname, content):
  with open(fname, 'w') as file:
    file.write(to_file(content))

def read_yaml(fname):
  with fname.open() as file:
    # return sorted(yaml.safe_load(file), key=lambda automation: automation['alias'])
    return yaml.safe_load(file);

def remove_text(content, start, end):
  do_append = True
  new = []
  for line in content:
      if end in line:
          do_append = not do_append
      if do_append:
          new.append(line)
      if start in line:
          do_append = not do_append
  return new

def modify_lines(to_insert, lines, tag):
  MARKDOWN_COMMENT = "<!-- {} -->"
  start_tag = MARKDOWN_COMMENT.format(f"start-{tag}")
  end_tag = MARKDOWN_COMMENT.format(f"end-{tag}")
  
  # Find indices of start and end comments
  start_index, end_index = None, None
  for i, line in enumerate(lines):
    if start_tag in line:
        start_index = i
    elif end_tag in line:
        end_index = i
        break

  if start_index is None or end_index is None:
    print("Start or end tag not found. Text not inserted.")
    return lines

  # Remove existing text between start and end comments
  lines[start_index + 1:end_index] = []
  # Insert empty line after start comment
  lines.insert(start_index + 1, '\n')

  # Insert new text between start and end comments
  insertion_index = start_index + 2
  lines[insertion_index:insertion_index] = [line + '\n' for line in to_insert]

  return lines

def get_alias(automation):
  return automation['alias']

def get_description(automation):
  return automation["description"]

def group_and_title(automation):
  return get_alias(automation).split(": ")

def get_group_name(group):
  return f"{get_emoji(group)} {group}"

def git_latest_edit_hash(fname):
    """Get the git hash to save with data to ensure reproducibility."""
    git_output = subprocess.check_output(
        ["git", "rev-list", "-1", "main", str(fname)]
    )
    return git_output.decode("utf-8").replace("\n", "")

def get_addons():
  try:
    output = subprocess.check_output(["ha", "addons", "--raw-json"])
    return json.loads(output.decode("utf-8"))["data"]["addons"]
  except FileNotFoundError:
    # the 'ha' program isn't available in the host image, I can only
    # run it from the 'SSH & Web Terminal' Add-on.
    return None

def get_line(fname, text):
  assert isinstance(text, str)
  with fname.open() as f:
    for num_line, line in enumerate(f):
      if text in line:
        return num_line

def permalink(fname, commit_hash):
  return URL.format(commit_hash=commit_hash, fname=fname)

def render_toc_entry(title):
   slug = slugify(title)
   return f"1. [{title}](#{slug})"

def render_group_heading(group):
  return "\n" + f"### {group}" + "\n"

def render_automation_amount(amount):
  return f"({amount} automation)"

def render_automation(fname, commit_hash, title, line, description):
  href = permalink(fname, commit_hash) + f"#L{line}"
  item = f"- [{title}]({href})"
  if description:
    return f"{item} – {description}"
  return item 

def render_automations_toc(grouped_automations):
  text = []
  total_automations = 0
  for group, automations in grouped_automations.items():
    group_name = get_group_name(group)
    group_entry = render_toc_entry(group_name)
    group_amount = f"({len(list(automations))} automation)"
    total_automations += len(automations)
    text.append(group_entry + " " + group_amount)
  text.append(f"\nTotal number of automations: **{total_automations}**️")
  return text

def render_automations_groups(grouped_automations):
  text = []
  commit_hash = git_latest_edit_hash(AUTOMATIONS)
  for group, automations in grouped_automations.items():
    group_name = get_group_name(group)
    text.append(render_group_heading(group_name))
    for automation in automations:
      group, title = group_and_title(automation)
      line = get_line(AUTOMATIONS, get_alias(automation))
      description = get_description(automation)
      text.append(render_automation(AUTOMATIONS, commit_hash, title, line, description))
  return text

def render_automations():
  raw_automation = read_yaml(AUTOMATIONS)
  sorted_automaions = sorted(raw_automation, key=lambda automation: automation['alias'])
  grouped_automations = groupby(sorted_automaions, key=lambda automation: group_and_title(automation)[0])
  automations = {key: list(group) for key, group in grouped_automations}
  return render_automations_toc(automations) + render_automations_groups(automations)

def render_addon(addon):
  name = addon["name"]
  version = addon["version"]
  url = addon["url"]
  description = addon["description"]
  return f"- [{name}]({url}) v{version} – {description}"

def render_addons():
  text = []
  addons = get_addons()
  if addons is None:  
    return None
  for addon in addons:
    text.append(render_addon(addon))
  return text

def main():
  old_readme = read_file(README)
  new_readme = old_readme.copy()

  addons = render_addons()
  automations = render_automations()

  new_readme = modify_lines(automations, new_readme, 'automations')

  if addons is not None:
    new_readme = modify_lines(addons, new_readme, 'addons')

  # Write only when changes applied
  if to_file(new_readme) != to_file(old_readme):
    write_file(README, new_readme)

if __name__ == "__main__":
  main()
