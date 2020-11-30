from colorama import Fore, Back, Style
import datetime
import argparse
from os import path, getcwd, walk, chdir, popen
import yaml

DEFAULT_CONFIG_PATH = "~/.config/confgit.yml"


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
    parser.add_argument(
        "-s", "--sync",
        action="store_true",
        help="update original config files from their git copies")
    parser.add_argument(
        "-u", "--update",
        action="store_true",
        help="update repo config files from original copies")
    parser.add_argument(
        "-b", "--backup",
        type=str,
        action="store",
        nargs="?",
        dest="BACKUP",
        const=f"confgit-backup-{str(datetime.datetime.now()).replace(' ', '-')}.zip",
        default=False,
        help="create zip file with config backup")
    parser.add_argument(
        "-i", "--include",
        type=str,
        action="store",
        nargs="?",
        const="",
        default=False,
        dest="FILE_TO_INCLUDE",
        help="include file or directory in to confgit repository")
    parser.add_argument(
        "-e", "--exclude",
        type=str,
        action="store",
        dest="EXLUDED_FILE",
        help="exclude file or directory from confgit repository")
    parser.add_argument(
        "--init",
        type=str,
        action="store",
        nargs="?",
        const=str(getcwd()),
        default=False,
        dest="INIT",
        help="init confgit repository")

    arguments = parser.parse_args()
    arguments.CONFIG_PATH = path_absolute(arguments.CONFIG_PATH)
    return arguments


def cg_print(msg):
    print(f"{Back.GREEN + Fore.BLACK}CG:{Style.RESET_ALL} {msg}")


def print_error(msg):
    cg_print(f"{Fore.RED}ERROR:{Style.RESET_ALL} {msg}")


def print_warning(msg):
    cg_print(f"{Fore.LIGHTRED_EX}WARN:{Style.RESET_ALL} {msg}")

############################################################################


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
    except yaml.YAMLError as exc:
        print_error(f"Yaml parse of {config_file_path} failed")
        exit(1)
    except IOError as exc:
        print_error(f"File {config_file_path} does not exists")
        exit(1)


def save_config(config, config_file_path):
    with open(config_file_path, "w") as f:
        yaml.dump(config, f, default_flow_style=False)
