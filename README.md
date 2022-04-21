# confgit

[![Documentation Status](https://readthedocs.org/projects/confgit/badge/?version=latest)](https://confgit.readthedocs.io/en/latest/?badge=latest)
[![CodeFactor](https://www.codefactor.io/repository/github/yagarea/confgit/badge/master)](https://www.codefactor.io/repository/github/yagarea/confgit/overview/master)
[![Python 3.x](https://img.shields.io/badge/python-3.x-green.svg)](https://www.python.org/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![PR info](https://img.shields.io/github/issues-pr/yagarea/confgit)](https://github.com/yagarea/confgit/pulls)
[![Open issues](https://img.shields.io/github/issues/yagarea/confgit)](https://github.com/yagarea/confgit/issues)
[![Repo stars](https://img.shields.io/github/stars/yagarea/confgit?style=social)](https://github.com/yagarea/confgit/stargazers)

## [Documentation](https://confgit.readthedocs.io/)

Confgit is a Git overhead for version control of your config files. The main difference between confgit and any other config file version system is its simplicity. It makes version control and migration of config files safe and easy.

## How does it work?

With confgit, you do not have to learn anything new, you only need to set up a directory where confgit will copy all files you register. After setup, you will have all your config files centralized in one directory where you can edit and maintain your config files with Git.

## Features

- **Centralization:** Manage files across multiple directories in one directory
- **Version control:** Use Git with your config files without turning your entire filesystem into a Git repository
- **Import/Export:** Git allows you to easily push or clone your config files to and from a remote server to archive and share
  
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
