import argparse
import datetime
from os import getcwd

from .fs_util import *

def parse_confgit_args():

    parser = argparse.ArgumentParser(
        description="Git overhead for version control of your config files",
        epilog="use 'confgit <command> -h' for help on specific commands",
        prog="confgit")

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
        help='confgit commands:')


    #* global arguments shared in every command
    common_args = argparse.ArgumentParser(add_help=False)
    common_args.add_argument( #! remove later - g3ner1c
        "-c", "--config",
        action="store",
        nargs="?",
        type=str,
        default="~/.config/confgit.yml",
        dest="CONFIG_PATH",
        metavar="config-path",
        help="load alternative config")

    common_args.add_argument(
        '--debug',
        action='store_true',
        default=False,
        dest='debug',
        help="enable debug mode")


    #* init
    init_parser = subparsers.add_parser(
        'init',
        help="initialize confgit repository",
        parents=[common_args])

    init_parser.add_argument(
        'init_path',
        action='store',
        nargs='?',
        type=str,
        default=str(getcwd()) + '/',
        metavar='<directory>',
        help="path of directory where you want to init confgit repository (default: './')")

    init_parser.add_argument(
        '--no-git',
        action='store_true',
        default=False,
        help="initialize confgit repository without git version control",
        dest='no_git')


    #* sync
    sync_parser = subparsers.add_parser(
        'sync',
        help="pushes confgit repository to file origin(s)",
        parents=[common_args])

    sync_parser.add_argument(
        '-f', '--force',
        action='store_true',
        default=False,
        dest='force',
        help="forces push to origin even if there are conflicts")


    #* update
    update_parser = subparsers.add_parser(
        'update',
        help="pulls changes to confgit repository from file origin(s)",
        parents=[common_args])
    
    update_parser.add_argument(
        '-f', '--force',
        action='store_true',
        default=False,
        dest='force',
        help="forces pull to origin even if there are conflicts")
    

    #* include
    include_parser = subparsers.add_parser(
        'include',
        help="add files or directories to the confgit index",
        parents=[common_args])
    
    include_parser.add_argument(
        'paths',
        action='store',
        nargs='*',
        type=str,
        metavar='<paths>',
        help="files or directories to include in to the confgit index")


    #* exclude
    exclude_parser = subparsers.add_parser(
        'exclude',
        help="remove files or directories from the confgit index",
        parents=[common_args])
    
    exclude_parser.add_argument(
        'paths',
        action='store',
        nargs='*',
        type=str,
        metavar='<paths>',
        help="files or directories to exclude in to the confgit index")

    
    #* backup
    backup_parser = subparsers.add_parser(
        'backup',
        help="create a zip archive of the confgit repository (excluding .git)",
        parents=[common_args])

    backup_parser.add_argument(
        'backup_path',
        action='store',
        nargs='?',
        type=str,
        default=f"confgit-backup-{str(datetime.datetime.now()).replace(' ', '-')}.zip",
        metavar='<path>',
        help="path of backup file (default: './confgit-backup-<date>.zip')")


    args = parser.parse_args()

    #! ###### debug mode jank, sort out later - g3ner1c

    debug_mode = args.debug

    print_debug(args)
    print(args)

    #! ######

    args.CONFIG_PATH = absolute_path(args.CONFIG_PATH)

    return args

parse_confgit_args()