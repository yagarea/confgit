import os
import json
from util.log_util import *
from util.sys_util import *


#! not to be confused with __init__.py

def init(repo_dir='.', config_path='.confgit.json'):

    os.chdir(os.path.realpath(repo_dir))

    if not os.path.isfile(config_path):
        with open(config_path, "w") as new_config:
            new_config.write( # im using json instead of yaml because json has a built-in module - g3ner1c
                "{\n" +
                f"    repo_dir: {os.path.normpath(os.getcwd())}\n" +
                "    include: {\n" +
                "    },\n" +
                "    exclude: {\n" +
                "    }\n"
            )
        cg_print(f"New config file generated: {config_path}")
    else:
        print_warning(f"Config file {config_path} already exists")
    execute_command("git init")
    end()