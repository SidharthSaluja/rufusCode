# Git Repository Information

## Project Description
This program allows you to print specific facts about a local git repository. It takes in one argument:
- git_dir: directory in which to assess git status

The program prints the following things:
- active branch (boolean)
- whether repository files have been modified (boolean)
- whether the current head commit was authored in the last week (boolean)
- whether the current head commit was authored by Rufus (boolean)

## Usage
```
python3 rufus.py
```
It will prompt you to enter the directory in which to assess git status.

## Requirements
- Python 3.x
- GitPython library

You can install the GitPython library by running the following command:
```
pip install gitpython
```

## Notes
Make sure the repository you are trying to access is a git repository and it is initialized.
