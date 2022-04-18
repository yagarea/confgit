from .util.log_util import *
from .util.sys_util import *


def exclude(file_to_exclude, config, config_path):

    if file_to_exclude == "" or file_to_exclude is None:
        print_error("No file or directory specified")
        end(1)

    if not path.exists(file_to_exclude):
        print_error(f"File or directory {file_to_exclude} does not exists")
        end(1)
    
    if config["exclude"] is None:
        config["exclude"] = []
    
    if file_to_exclude in config["exclude"]:
        cg_print(f"{file_to_exclude} is already excluded")
        end()
    
    if config["exclude"] is not None and path_relative_home(file_to_exclude) in config["include"]: # fixed typo 'include' -> 'exclude' - g3ner1c

        cg_print(f"{file_to_exclude} is explicitly included. Such a config does not make sense.")
        cg_print("Didn't you want to include the parent directory and exclude some of its contents?")
        end()

    config["exclude"].append(path_relative_home(file_to_exclude))
    save_config(config, config_path)
    cg_print(f"{file_to_exclude} has been successfully excluded from confgit repository")
    end()