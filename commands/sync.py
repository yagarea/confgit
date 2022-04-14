import os
import json
from util.log_util import *
from util.sys_util import *


def sync(config):
    cg_print("Start syncing")
    registered_files = get_all_registered_files(config)
    registered_files_dif = []
    for rf in registered_files:
        if not have_same_content(rf, path_in_repo(rf, config)):
            registered_files_dif.append(rf)
    if len(registered_files_dif) == 0:
        cg_print("There are no changes in complementary files of registered files")
        end()
    for rf in registered_files_dif:
        cg_print(f"\t{rf}")
    cg_print("Do you want to sync content of all these files with theirs complementary files ? [Y/N]")
    answer = str(input()).lower()
    if answer == "y":
        for rf in registered_files_dif:
            cg_print(f"Syncing {path_relative_home(rf)}")
            write_file_to_other_file(path_in_repo(rf, config), rf)
    end()