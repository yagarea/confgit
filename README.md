# Confgit
Git overhead for version control of your config files

## Usage

### Confgit internal commands
 
#### positional arguments:
- **init**                - Init confgit repository 
- **sync**                - Sync origins of files from confgit repository
- **update**              - Update files in config repository from their origin
- **backup**              - Create zip file with backup of all files in confgit repository
- **include**             - Include file or directory in to confgit repository
- **exclude**             - Exclude file or directory in to confgit repository 
  
#### optional arguments:
- **-h**, **--help**                                - show this help message and exit 
- **-c** _CONFIG_PATH_, **--config** _CONFIG_PATH_  - load alternative config

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

