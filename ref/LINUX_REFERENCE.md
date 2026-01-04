Unix Quick Reference
====================

These are all of the Unix commands we use in the course.

| Token | Meaning
|:------|:-------------------------------------------
| ^A    | go to the start of the command line
| ^C    | send interrupt signal
| ^D    | send enf of transmission signal
| ^E    | go to the end of the command line
| tab   | complete names of commands and files
| `.`   | your current directory
| `..`  | your parent directory
| `~`   | your home directory (also $HOME)
| `*`   | wildcard - matches everything
| `\|`  | pipe output from one command to another
| `>`   | redirect stdout to file
| `<`   | send a file as stdin


| Command   | Example          | Intent
|:----------|:-----------------|:----------------------------------------------
| `cat`     | `cat > f`        | create file f and wait for stdin (see ^D)
|           | `cat f`          | stream contents of file f to stdout
|           | `cat a b > c`    | concatenate files a and b into c
| `cd`      | `cd d`           | change to relative directory d
|           | `cd ..`          | go up one directory (parent)
|           | `cd /d`          | change to absolute directory d
| `cp`      | `cp f1 f2`       | make a copy of file f1 called f2
| `cut`     | `cut -f 1 f`     | cut field 1 from file f
| `date`    | `date -I`        | report the date in ISO 8601 format
|           | `date "+%m/%d"`  | report month and date
| `diff`    | `diff a b`       | find differences in file a and b
| `find`    | `find .`         | reports file information recursively
| `git`     | `git add f`      | start tracking file f
|           | `git commit -m`  | finished edits, ready to upload
|           | `git push`       | put changes into repository
|           | `git pull`       | retrieve latest documents from repository
|           | `git status`     | check on status of repository
| `grep`    | `grep "p" f`     | print lines with the letter p in file f
|           | `grep "^p" f`    | print lines that begin with p
|           | `grep "p$" f`    | print lines that end with p
| `gzip`    | `gzip f`         | compress file f
|           | `gzip -k f`      | compress file f and keep the original
| `gunzip`  | `gunzip f.gz`    | uncompress file f.gz
|           | `gunzip -k f.gz` | uncompress file.gz and keep original
|           | `gunzip -c f.gz` | stream contents of f.gz to stdout
| `head`    | `head f`         | display the first 10 lines of file f
|           | `head -2 f`      | display the first 2 lines of file f
| `history` | `history`        | display the recent commands you typed
| `less`    | `less f`         | page or search through a file
| `ls`      | `ls`             | list current directory
|           | `ls -F`          | list with file type symbols appended
|           | `ls -l`          | list with file details
|           | `ls -la`         | also show invisible files
|           | `ls -lta`        | sort by time instead of name
| `mkdir`   | `mkdir d`        | make a directory named d
| `mv`      | `mv foo bar`     | rename file foo as bar
|           | `mv foo ..`      | move file foo to parent directory
| `nano`    | `nano`           | use the nano text file editor
|           | `nano foo`       | start nano and edit/create file foo
| `pwd`     | `pwd`            | print working directory
| `rm`      | `rm f1 f2`       | remove files f1 and f2
|           | `rm -r d`        | remove directory d and all files beneath
|           | `rm -rf /`       | destroy your computer
| `rmdir`   | `rmdir d`        | remove directory d
| `sum`     | `sum f`          | calculate a checksum for file f
| `sort`    | `sort f`         | sort file f alphabetically by first column
|           | `sort -n f`      | sort file f numerically by first column
|           | `sort -nk2 f`    | sort file f numerically by column 2
| `tail`    | `tail f`         | display the last 10 lines of file f
|           | `tail -f f`      | as above and keep displaying if streaming
| `time`    | `time x`         | report CPU and elapsed time for command x
| `uname`   | `uname -a`       | reports the name of your flavor of unix
| `touch`   | `touch f`        | create/update file
| `wc`      | `wc f`           | count lines, words, and characters in file f
| `zless`   | `zless f.gz`     | like`less` for compressed files
