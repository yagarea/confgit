#!/usr/bin/env python3

from commands.util.sys_util import *
from commands.util.fs_util import *
from commands.util.args_util import *
from commands.init import *
from commands.sync import *
from commands.update import *
from commands.backup import *
from commands.include import *
from commands.exclude import *

def main():

    if contains_confgit_command(): # if user has specified confgit command

        args = vars(parse_confgit_args())

        if args['debug']:
            debug_mode = True

        print_debug(args)

        if args['command'] == 'init':
            init(args['init_path'], args['CONFIG_PATH'])

        config = load_config(args['CONFIG_PATH'])
        print_debug(config)

        if args['command'] == 'include':
            for i in args['paths']:
                include(i, config, args['CONFIG_PATH'])

        if args['command'] == 'exclude':
            for i in args['paths']:
                exclude(i, config, args["CONFIG_PATH"])

        if args['command'] == 'sync':
            sync(config)

        if args['command'] == 'update':
            update(config)

        if args['command'] == 'backup':
            backup(config, args['backup_path'])

    else: # if user has not specified confgit command
        #! doesn't check if it's a valid git command, could be problem later - g3ner1c
        config, git_command = parse_git_args()
        print_debug(git_command)
        cd(config["repo_dir"])
        send_to_git(git_command)

main()
