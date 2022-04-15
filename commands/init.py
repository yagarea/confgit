import os
import json
from .util.log_util import *
from .util.sys_util import *


#! not to be confused with __init__.py

def init(repo_dir, config_path):
    set_cwd_to(repo_dir)
    if not path.isfile(config_path):
        with open(config_path, "w") as new_config:
            new_config.write(
                f"repo_dir: {path_relative_home(getcwd())}/\n" +
                "include: NULL\n" +
                "exclude: NULL"
            )
        cg_print(f"New config file generated: {config_path}")
    else:
        print_warning(f"Config file {config_path} already exists")
    execute_command("git init")
    end()