from .util.log_util import *
from .util.sys_util import *


def update(config): # made update more consistent with sync - g3ner1c

    cg_print("Starting update...")
    registered_files = get_all_registered_files(config)
    registered_files_diff = [] # file paths with changes

    for rf in registered_files:
        if not have_same_content(rf, path_in_repo(rf, config)):
            registered_files_diff.append(rf)

    if len(registered_files_diff) == 0:
        cg_print("There are no changes in origins of registered files")
        end()

    for rf in registered_files_diff:
        cg_print(f"\t{path_in_repo(rf, config)}")

    cg_print("Do you want to update these files with their origins? [Y/n]")
    answer = str(input()).lower()
    if answer == "y" or answer == "":
        for rf in registered_files_diff:
            cg_print(f"Updating {path_relative_home(rf)}")
            write_file_to_other_file(rf, path_in_repo(rf, config))
        cg_print(f"Successfully updated {len(registered_files_diff)} files")
    end()