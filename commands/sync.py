from .util.log_util import *
from .util.sys_util import *


def sync(config):

    cg_print("Starting sync...")
    registered_files = get_all_registered_files(config)
    registered_files_diff = [] # file paths with changes

    for rf in registered_files:
        if not have_same_content(rf, path_in_repo(rf, config)):
            registered_files_diff.append(rf)
    
    if len(registered_files_diff) == 0:
        cg_print("There are no changes in complementary files of registered files")
        end()
    
    for rf in registered_files_diff:
        cg_print(f"\t{rf}")
    
    cg_print("Do you want to sync these files with their complementary files? [Y/n]")
    answer = str(input()).lower()
    if answer == "y" or answer == "": # added default yes - g3ner1c
        for rf in registered_files_diff:
            cg_print(f"Syncing {path_relative_home(rf)}")
            write_file_to_other_file(path_in_repo(rf, config), rf)
        cg_print(f"Successfully synced {len(registered_files_diff)} files")
    end()