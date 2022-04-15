# Confgit

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![PR info](https://img.shields.io/github/issues-pr/yagarea/confgit)](https://github.com/yagarea/confgit/pulls)
[![CodeFactor](https://www.codefactor.io/repository/github/yagarea/confgit/badge/master)](https://www.codefactor.io/repository/github/yagarea/confgit/overview/master)
[![Python 3.x](https://img.shields.io/badge/python-3.x-green.svg)](https://www.python.org/)
[![Closed issues](https://img.shields.io/github/issues-closed/yagarea/confgit)](https://github.com/yagarea/confgit/issues)
[![Repo starts](https://img.shields.io/github/stars/yagarea/confgit?style=social)](https://github.com/yagarea/confgit/stargazers)

Confgit is a Git overhead for version control of your config files. The main difference between confgit and any other config file version system is it's simplicity. It makes version control and migration of config files safe and easy.

## [Installation](./docs/installation.md)

## How does it work?

With confgit you do not have to learn anything new. You only need to set up a directory where confgit will copy all files you register. In result, you have all your config files centralized in one directory where you can edit and maintain your config files with git.

## Usage

### `init`

Initialize a git repository for your config files in current directory and generates config file in `~/.config/confgit.yml` if you do not specify other location using `--config` argument.

```txt
confgit init
```

```txt
confgit init --config /alternative/location/of/config/file/confgit.yml
```

### `sync`

Writes content of complementary files of registered files to their origins.

```txt
confgit sync
```

### `update`

Writes content of origins of registered files to their's complementary files.

```txt
confgit update
```

### `backup`

Creates a zip file with backup of all files in confgit repository.

```txt
confgit backup
```

You can specify the name of the backup file.

```txt
confgit backup my_backup_monday.zip
```

If the name of the backup does not end with `.zip` it will be automatically added.

### `include`

Registers a file or a directory into a confgit watch list.

```txt
confgit include nvim.init
```

Including directories will register all its files recursively.

```txt
confgit include ~/.config/
```

### `exclude`

Excludes a file or directory from the registered files.

```txt
confgit exclude zoom.conf
```

Excluding directories will exclude all its files recursively.

```txt
confgit exclude .config/rofi/
```

### _other_

Every other command will be called as git argument in directory with registered files.

`confgit pull` -> `git pull`

### Optional Arguments

- `-h`, `--help`                              - show this help message and exit
- `-c $config_path`, `--config $config_path`  - load alternative config
- `--debug`                                   - show additional information for debugging

### Git commands supported by confgit

clone, add, mv, restore, rm, sparse-checkout, bisect, diff, grep, log, show, status, branch, commit, merge, rebase, reset, switch, tag, fetch, pull, push

---
**Disclaimer:** Author does not have any responsibility for any damage or data loss caused by the usage of this software.
