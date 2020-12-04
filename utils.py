from colorama import Fore, Back, Style
import datetime
import argparse
from os import path, getcwd, walk, chdir, popen
from sys import exit, argv
import yaml
import re

DEFAULT_CONFIG_PATH = "~/.config/confgit.yml"

###########################################################################
# Parsing Arguments


def get_arguments():
    parser = argparse.ArgumentParser(
        prog="confgit",
        description="Git overhead for version control of your config files",
        formatter_class=argparse.RawTextHelpFormatter, )

    parser.add_argument(
        "-c", "--config",
        type=str,
        default=DEFAULT_CONFIG_PATH,
        dest="CONFIG_PATH",
        help="load alternative config")

    subparsers = parser.add_subparsers(help="Confgit commands:")

    subparsers.add_parser("init", help="Init confgit repository").add_argument(
        "init_path",
        type=str,
        action="store",
        nargs="*",
        metavar="test_init",
        default=str(getcwd()) + "/",
        help="path of directory where you want to init confgit repository")
    subparsers.add_parser("sync", help="Sync origins of files from confgit repository").add_argument(
        "sync",
        action="store_true",
        help="update original config files from their git copies")
    subparsers.add_parser("update", help="Update files in config repository from their origin").add_argument(
        "update",
        action="store_true",
        help="")
    subparsers.add_parser("backup", help="Create zip file with backup of all files in confgit repository").add_argument(
        "backup_name",
        type=str,
        action="store",
        nargs="?",
        const=f"confgit-backup-{str(datetime.datetime.now()).replace(' ', '-')}.zip",
        default=False,
        help="create zip file with config backup")
    subparsers.add_parser("include", help="Include file or directory in to confgit repository").add_argument(
        "file_to_include",
        type=str,
        action="store",
        nargs="?",
        const="",
        default=False,
        help="include file or directory in to confgit repository")
    subparsers.add_parser("exclude", help="Exclude file or directory in to confgit repository").add_argument(
        "exclude",
        type=str,
        action="store",
        help="exclude file or directory from confgit repository")

    arguments = parser.parse_args()
    arguments.CONFIG_PATH = path_absolute(arguments.CONFIG_PATH)
    return arguments


def contains_confgit_command():
    for c in ["init", "include", "exclude", "sync", "update", "backup"]:
        if c in argv:
            return True
    return False


def parse_git_args():
    args_string = " ".join(argv[1:]).strip()
    config_path = DEFAULT_CONFIG_PATH
    config_path_regex = re.search(r"--config\s([^\s]*)", args_string, re.IGNORECASE)
    if config_path_regex:
        config_path = config_path_regex.group(1)
    return load_config(path_absolute(config_path)), args_string.replace("--config " + config_path, "")


############################################################################
# Printing and logging


def cg_print(msg):
    print(f"{Back.GREEN + Fore.BLACK}CG:{Style.RESET_ALL} {msg}")


def print_error(msg):
    cg_print(f"{Fore.RED}ERROR:{Style.RESET_ALL} {msg}")


def print_warning(msg):
    cg_print(f"{Fore.LIGHTRED_EX}WARN:{Style.RESET_ALL} {msg}")


def print_debug(msg):
    cg_print(f"{Back.WHITE}{Fore.BLACK}DEBUG:{Style.RESET_ALL} {msg}")

############################################################################
# File system utilities


def path_relative_home(raw_path):
    output = path.abspath(raw_path)
    return output.replace(str(path.expanduser("~")), "~")


def path_absolute(raw_path):
    return path.abspath(path.expanduser(path.expandvars(raw_path)))


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


###########################################################################
# System calls

def execute_command(command):
    return popen(command).read().strip()


def send_to_git(git_command):
    output = execute_command(f"git {git_command}")
    cg_print(f"{Fore.BLUE}GIT:{Style.RESET_ALL}")
    for o in output.split("\n"):
        print(f"\t{o}")


def end(exit_code=0):
    exit(exit_code)
