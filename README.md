# handbrake-devel
This is a development repository of mutimedia/handbrake for FreeBSD ports.

## How to use

This repository is a part of FreeBSD ports,
should be put in `/usr/ports/multimedia/handbrake-devel`.
You should clone this repository as follows.

```
$ cd /usr/ports/multimedia
$ git clone git@github.com:yuichiro-naito/handbrake-devel.git
$ cd handbrake-devel
$ make install
```

handbrake-devel conflicts with handbrake port.

## How to make a patch to FreeBSD ports tree

WE MUST CHANGE MAKEFILE AS FOLLOWING,
BEFORE MAKE A UPDATE PATCH TO PORTS TREE.

1. change PORTNAME to 'handbrake'.
2. delete CONFLICTS.
3. delete GH_TAGNAME.
4. update `files/version.txt`.
5. update distinfo.

Copy all files to `ports/multimedia/handbrake` except `README.md` and `CHANGES`.
Check which files are added and/or deleted.
Mark added files by svn add.
Mark deleted files by svn del.
Make a patch by svn diff.
