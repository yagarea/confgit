import datetime
import argparse
from os import getcwd, popen
from sys import argv

import re

from .fs_util import *
from .args_util import *

# SYSTEM AND INPUT UTILITIES

DEFAULT_CONFIG_PATH = "~/.config/confgit.yml" #? proably going to remove later for less confusion to user - g3ner1c

###########################################################################
# Parsing Arguments


def contains_confgit_command(): #! kind of messy probably change later - g3ner1c
    for c in ["init", "include", "exclude", "sync", "update", "backup", "--help", "--debug"]:
        if c in argv:
            return True
    return False

# returns config path, git args
#! doesn't check if it's a valid git command, could be problem later - g3ner1c
def parse_git_args():

    args_string = " ".join(argv[1:]).strip()

    config_path = DEFAULT_CONFIG_PATH
    config_path_regex = re.search(r"--config\s([^\s]*)", args_string, re.IGNORECASE) # regex to capture config path

    if config_path_regex:
        config_path = config_path_regex.group(1)
    
    return load_config(absolute_path(config_path)), args_string.replace("--config " + config_path, "")

###########################################################################
# System calls


def execute_command(command):
    return popen(command).read().strip()


def send_to_git(git_command):
    output = execute_command(f"git {git_command}")
    print_debug(output)
    if output != "":
        cg_print(f"{Fore.BLUE}git:{Style.RESET_ALL}")
        for o in output.split("\n"):
            print(f"\t{o}")


def end(exit_code=0):
    exit(exit_code)


#############################################################################
# Help message

#! deprecated + gets overridden by argparse -h
help_message = """
CONFGIT HELP PAGE

Git overhead for version control of your config files

Confgit internal commands:  
    
    positional arguments:
      {init,sync,update,backup,include,exclude}
                            Confgit commands:
        init                Init confgit repository
        sync                Sync origins of files from confgit repository
        update              Update files in config repository from their origin
        backup              Create zip file with backup of all files in confgit repository
        include             Include file or directory in to confgit repository
        exclude             Exclude file or directory in to confgit repository
    
    optional arguments:
      -h, --help            show this help message and exit
      -c CONFIG_PATH, --config CONFIG_PATH
                            load alternative config
Git original commands supported by confgit:
    
    alternative way to start a working area 
       clone             Clone a repository into a new directory
    
    work on the current change (see also: git help everyday)
       add               Add file contents to the index
       mv                Move or rename a file, a directory, or a symlink
       restore           Restore working tree files
       rm                Remove files from the working tree and from the index
       sparse-checkout   Initialize and modify the sparse-checkout
    
    examine the history and state (see also: git help revisions)
       bisect            Use binary search to find the commit that introduced a bug
       diff              Show changes between commits, commit and working tree, etc
       grep              Print lines matching a pattern
       log               Show commit logs
       show              Show various types of objects
       status            Show the working tree status
    
    grow, mark and tweak your common history
       branch            List, create, or delete branches
       commit            Record changes to the repository
       merge             Join two or more development histories together
       rebase            Reapply commits on top of another base tip
       reset             Reset current HEAD to the specified state
       switch            Switch branches
       tag               Create, list, delete or verify a tag object signed with GPG
    
    collaborate (see also: git help workflows)
       fetch             Download objects and refs from another repository
       pull              Fetch from and integrate with another repository or a local branch
       push              Update remote refs along with associated objects
""".strip()
