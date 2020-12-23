# Confgit

---

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![PR info](https://img.shields.io/github/issues-pr/yagarea/confgit)
[![CodeFactor](https://www.codefactor.io/repository/github/yagarea/confgit/badge/master)](https://www.codefactor.io/repository/github/yagarea/confgit/overview/master)
[![Python 3.x](https://img.shields.io/badge/python-3.x-green.svg)](https://www.python.org/)
[![Closed issues](https://img.shields.io/github/issues-closed/yagarea/confgit)

Git overhead for version control of your config files. The main difference between confgit and any other config file 
version system is it's simplicity. It makes version control and migration of config files safe and easy.

## Usage

### Confgit internal commands
Argument in _[]_ are optional.

#### positional arguments:
- **init**                      - Init confgit repository and generate config file in "~/.config/confgit.yml" if you do not 
  specify other location using `--config` argument
- **sync**                      - Write content of complementary files of registered files to their origins
- **update**                    - Write content of origins of registered files to their's complementary files
- **backup** _[backup name]_    - Create zip file with backup of all files in confgit repository
- **include** _file to include_ - Registeres file or directory in to confgit repository
- **exclude** _file to exclude_ - Exclude file or directory from registered files 

#### optional arguments:
- **-h**, **--help**                                - show this help message and exit 
- **-c** _CONFIG_PATH_, **--config** _CONFIG_PATH_  - load alternative config
- **--debug**                                       - show additional information for debugging

### Git original commands supported by confgit

#### alternative way to start a working area 
 - **clone**             - Clone a repository into a new directory
    
#### work on the current change (see also: git help everyday)
- **add**               - Add file contents to the index
- **mv**                - Move or rename a file, a directory, or a symlink
- **restore**           - Restore working tree files
- **rm**                - Remove files from the working tree and from the index
- **sparse-checkout**   - Initialize and modify the sparse-checkout
    
#### examine the history and state (see also: git help revisions)
- **bisect**            - Use binary search to find the commit that introduced a bug
- **diff**              - Show changes between commits, commit and working tree, etc
- **grep**              - Print lines matching a pattern
- **log**               - Show commit logs
- **show**              - Show various types of objects
- **status**            - Show the working tree status 
  
#### grow, mark and tweak your common history
- **branch**            - List, create, or delete branches
- **commit**            - Record changes to the repository
- **merge**             - Join two or more development histories together
- **rebase**            - Reapply commits on top of another base tip
- **reset**             - Reset current HEAD to the specified state
- **switch**            - Switch branches
- **tag**               - Create, list, delete or verify a tag object signed with GPG

#### collaborate (see also: git help workflows)
- **fetch**             - Download objects and refs from another repository
- **pull**              - Fetch from and integrate with another repository or a local branch
- **push**              - Update remote refs along with associated objects

