from commands.util.sys_util import *
from commands.util.fs_util import *
from commands.init import *
from commands.sync import *
from commands.update import *
from commands.backup import *
from commands.include import *
from commands.exclude import *

def main():

    if contains_confgit_command():

        args = vars(get_arguments())
        print_debug(args)

        if args["debug"]:
            debug_mode = True

        if "help" in args.keys():
            print(help_message)

        if "init_path" in args.keys():
            init(args["init_path"], args["CONFIG_PATH"])

        config = load_config(args["CONFIG_PATH"])
        print_debug(config)

        if "file_to_include" in args.keys():
            include(args["file_to_include"], config, args["CONFIG_PATH"])

        if "file_to_exclude" in args.keys():
            exclude(args["file_to_exclude"], config, args["CONFIG_PATH"])

        if "update" in args.keys():
            update(config)

        if "sync" in args.keys():
            sync(config)

        if "backup_name" in args.keys():
            backup(config, args["backup_name"])

    else:
        config, git_command = parse_git_args()
        print_debug(git_command)
        set_cwd_to(config["repo_dir"])
        send_to_git(git_command)

main()