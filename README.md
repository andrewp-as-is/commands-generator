<!--
https://pypi.org/project/readme-generator/
-->

[![](https://img.shields.io/badge/OS-Unix-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/v/commands-generator.svg?maxAge=3600)](https://pypi.org/project/commands-generator/)
[![](https://img.shields.io/npm/v/commands-generator.svg?maxAge=3600)](https://www.npmjs.com/package/commands-generator)
[![Travis](https://api.travis-ci.org/looking-for-a-job/commands-generator.svg?branch=master)](https://travis-ci.org/looking-for-a-job/commands-generator/)

#### Installation
```bash
$ [sudo] npm i -g commands-generator
```
```bash
$ [sudo] pip install commands-generator
```

#### Features
+   generate **shell commands from scripts**
+   **shell namespaces** - `namespace:command`. folder names as namespaces

#### How it works
scripts (shebang `#!` required):
```
namespace/script.py
namespace/subnamespace/script.sh
```

generated commands:
```
namespace:script
namespace:subnamespace:script
```

#### Config
`~/.bashrc`:

`export PATH=path/to/commands:$PATH`

#### CLI
```bash
usage: commands-generator scripts_dir commands_dir
```

#### Examples
generate `~/.local/share/bin` from `dotfiles/scripts`:

```
dotfiles/scripts/git/commit.sh
dotfiles/scripts/files/python/setup.cfg/create.sh
dotfiles/scripts/web/github.com/push.sh
```

```bash
$ cd path/to/dotfiles
$ commands-generator scripts ~/.local/share/bin
```

generated commands:
```
~/.local/share/bin/git:commit
~/.local/share/bin/files:python:setup.cfg:create
~/.local/share/bin/web:github.com:push
```

usage:
```
$ files:python:requirements.txt:create
$ git:commit
$ web:github.com:push
```

#### Related projects
+   [`classifiers-generator` - python classifiers generator](https://pypi.org/project/classifiers-generator/)
+   [`commands-generator` - shell commands generator](https://pypi.org/project/commands-generator/)
+   [`launchd-generator` - launchd.plist generator](https://pypi.org/project/launchd-generator/)
+   [`readme-badges` - `README.md` badges](https://pypi.org/project/readme-badges/)
+   [`readme-docstring` - generate README.md from python docstrings](https://pypi.org/project/readme-docstring/)
+   [`readme-generator` - `README.md` generator](https://pypi.org/project/readme-generator/)
+   [`setupcfg-generator` - `setup.cfg` generator](https://pypi.org/project/setupcfg-generator/)
+   [`travis-generator` - `.travis.yml` generator](https://pypi.org/project/travis-generator/)

<p align="center">
    <a href="https://pypi.org/project/readme-generator/">readme-generator</a>
</p>