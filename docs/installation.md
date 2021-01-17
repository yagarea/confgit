# How to install confgit

### Clone repository
At first you need to download configit code. You can a achieve it by running this in 
your command line:
```
git clone https://github.com/yagarea/confgit/
```

### Install dependencies
You can install all dependencies by running:
```
pip install -r requirements.txt
```

### Make alias
By making alias you make usage much easier. I highly recommend it.
If you are using fish. Copy and paste this to your command line:
```
function confgit
	/absolute/way/to/confgit $argv
end
```
Replace `/absolute/way/to/` with output of `pwd`. Than hit enter and run command 
`funcsave`.

And if you are using bash:
```
$ alias confgit="python absolute/way/to/confgit"
```

