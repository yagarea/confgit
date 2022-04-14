import os
import json
import zipfile
from util.log_util import *
from util.sys_util import *


def backup(config, backup_name):
    repo_dir = config["repo_dir"]
    if backup_name[-4:] != ".zip":
        backup_name += ".zip"
    backup_zip_file = zipfile.ZipFile(backup_name, mode="w", compression=zipfile.ZIP_DEFLATED)
    cg_print("Creating backup:")

    for root, directories, files in walk(repo_dir):
        for i, filename in enumerate(files):
            if ".git" in root:
                continue
            print(f"\t\t{'├── ' if i < len(files) - 1 else '└── '}{filename}")
            backup_zip_file.write(path.join(root, filename), arcname=filename)
    backup_zip_file.close()
    cg_print(f"Backup saved as {backup_name}")