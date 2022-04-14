import os
import json
from .util.log_util import *
from .util.sys_util import *


def update(config):
    cg_print("Start updating")
    files_to_include = get_all_registered_files(config)
    files_to_include_dif = []
    for fti in files_to_include:
        if not have_same_content(fti, path_in_repo(fti, config)):
            files_to_include_dif.append(fti)
    if len(files_to_include_dif) == 0:
        cg_print("There are no changes in origins of registered files")
        end()
    cg_print(f"Including {len(files_to_include_dif)} files")
    for fti in files_to_include_dif:
        cg_print(f"Updating {path_relative_home(fti)}")
        write_file_to_other_file(fti, path_in_repo(fti, config))
    cg_print("Successfully updated")
    end()