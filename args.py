import argparse

def parse_confgit_args():

    parser = argparse.ArgumentParser(description="use 'confgit <command> -h' for help on specific commands", prog="confgit")
    subparsers = parser.add_subparsers(dest="command", required=True, help='confgit commands:')

    #* init
    init_parser = subparsers.add_parser(
        'init',
        help="initialize confgit repository")

    init_parser.add_argument(
        '--no-git',
        help="initialize confgit repository without git version control",
        action='store_true',
        default=False)

    #* sync
    sync_parser = subparsers.add_parser(
        'sync',
        help="pushes confgit repository to file origin")

    sync_parser.add_argument(
        '-f',
        '--force',
        help="forces push to origin even if there are conflicts",
        action='store_true',
        default=False)

    #* update
    update_parser = subparsers.add_parser(
        'update',
        help="pulls changes to confgit repository from file origin")
    
    update_parser.add_argument(
        '-f',
        '--force',
        help="forces pull from origin even if there are conflicts",
        action='store_true',
        default=False)
    
    #* include
    include_parser = subparsers.add_parser(
        'include',
        help="add a file or directory to the confgit index")
    
    include_parser.add_argument(
        'paths',
        type=str,
        nargs='*',
        help="files or directories to include in to the confgit index")

    #* exclude
    exclude_parser = subparsers.add_parser(
        'exclude',
        help="remove a file or directory from the confgit index")
    
    exclude_parser.add_argument(
        'paths',
        type=str,
        nargs='*',
        help="files or directories to exclude from the confgit index")
    
    args = parser.parse_args()
    
    return args