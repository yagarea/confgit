from os import path, walk, chdir, makedirs
from sys import exit
import yaml

from log_util import *


def path_relative_home(raw_path):
    if raw_path[0] == "~":
        return raw_path
    output = path.abspath(raw_path)
    return output.replace(str(path.expanduser("~")), "~")


def path_absolute(raw_path):
    return path.abspath(path.expanduser(path.expandvars(raw_path)))


def path_in_repo(raw_path, config):
    return path_absolute(raw_path).replace(str(path.expanduser("~")), config["repo_dir"])


def load_config(config_file_path):
    try:
        with open(config_file_path, 'r') as stream:
            raw_config = yaml.safe_load(stream)
            raw_config["repo_dir"] = path_absolute(raw_config["repo_dir"])
            if raw_config["include"] is not None:
                parsed = []
                for i in raw_config["include"]:
                    parsed.append(path_relative_home(i))
                raw_config["include"] = parsed
            if raw_config["exclude"] is not None:
                parsed = []
                for e in raw_config["exclude"]:
                    parsed.append(path_relative_home(e))
                raw_config["exclude"] = parsed
            return raw_config
    except yaml.YAMLError:
        print_error(f"Yaml parse of {config_file_path} failed")
        exit(1)
    except IOError:
        print_error(f"File {config_file_path} does not exists")
        exit(1)


def save_config(config, config_file_path):
    with open(config_file_path, "w") as f:
        yaml.dump(config, f, default_flow_style=False)


def set_cwd_to(dir_path):
    chdir(path.realpath(dir_path))


def mine_files(path_to_mine):
    path_to_mine = path_absolute(path_to_mine)
    if path.isfile(path_to_mine):
        return [path_to_mine]
    list_of_files = []
    for root, directories, files in walk(path_to_mine):
        for filename in files:
            list_of_files.append(path_absolute(path.join(root, filename)))
    return list_of_files


def write_file_to_other_file(source_path, destination_path: str):
    makedirs(path.dirname(destination_path), exist_ok=True)
    with open(source_path, "r") as source:
        with open(destination_path, "w") as destination:
            destination.write(source.read())