import os
import json
from util.log_util import *
from util.sys_util import *


def include(file_to_include, config, config_path):
    if file_to_include == "" or file_to_include is None:
        print_error("You have to specify file for include")
        end(1)
    if not path.exists(file_to_include):
        print_error(f"File or directory {file_to_include} does not exists")
        end(1)
    if config["include"] is None:
        config["include"] = []
    if path_relative_home(file_to_include) in config["include"]:
        cg_print(f"{file_to_include} is already included")
        end()
    if config["exclude"] is not None and path_relative_home(file_to_include) in config["exclude"]:
        cg_print(f"{file_to_include} is explicitly excluded. Such a config does not make sense.")
        cg_print("Didn't you want to include the parent directory and exclude some of its contents?")
        end()
    config["include"].append(path_relative_home(file_to_include))
    save_config(config, config_path)
    cg_print(f"{file_to_include} has been successfully included in to confgit repository")
    end()