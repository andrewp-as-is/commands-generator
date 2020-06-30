<!--
https://readme42.com
-->



[![](https://img.shields.io/badge/OS-Unix-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/v/commands-generator.svg?maxAge=3600)](https://pypi.org/project/commands-generator/)
[![](https://img.shields.io/npm/v/commands-generator.svg?maxAge=3600)](https://www.npmjs.com/package/commands-generator)[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/commands-generator/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/commands-generator/actions)

### Installation
```bash
$ [sudo] pip install commands-generator
```

```bash
$ [sudo] npm i -g commands-generator
```

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

#### Features
+   generate **shell commands from scripts**
+   **shell namespaces** - `namespace:command`. folder names as namespaces

#### Config
`~/.bashrc`:

`export PATH=path/to/commands:$PATH`

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

#### Related
+   [`classifiers-generator` - python classifiers generator](https://pypi.org/project/classifiers-generator/)
+   [`commands-generator` - shell commands generator](https://pypi.org/project/commands-generator/)
+   [`launchd-generator` - launchd.plist generator](https://pypi.org/project/launchd-generator/)
+   [`readme-generator` - `README.md` generator](https://pypi.org/project/readme-generator/)
+   [`setupcfg-generator` - `setup.cfg` generator](https://pypi.org/project/setupcfg-generator/)
+   [`travis-generator` - `.travis.yml` generator](https://pypi.org/project/travis-generator/)

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>