# How to install confgit

## Clone repository

`cd` into a directory where you want to install confgit.

```txt
git clone https://github.com/yagarea/confgit/
```

## Install dependencies

```txt
cd confgit
pip install -r requirements.txt
```

## Make alias

Making an alias makes usage much easier. I highly recommend it.

### fish

```fish
function confgit
	python /absolute/path/to/confgit/main.py $argv
end

funcsave confgit
```

### bash

Add the following line to your `~/.bashrc` file:

```bash
alias confgit="python absolute/path/to/main.py"
```

Then run `source ~/.bashrc` to load the new alias.
