Unix Quick Reference
====================

These are all of Unix commands we use in the course.


| Token | Meaning
|:------|:-------------------------------------------
| ^C    | send interrupt signal
| tab   | tab-complete names
| `.`   | your current directory (see pwd)
| `..`  | your parent directory
| `~`   | your home directory (also $HOME)
| `*`   | wildcard - matches everything
| `\|`  | pipe output from one command to another
| `>`   | redirect stdout to file
| `<`   | send a file as stdin


| Command   | Example       | Intent
|:----------|:--------------|:------------------------------------------------
| `cat`     | `cat > f`     | create file f and wait for keyboard (see ^D)
|           | `cat f`       | stream contents of file f to STDOUT
|           | `cat a b > c` | concatenate files a and b into c
| `cd`      | `cd d`        | change to relative directory d
|           | `cd ..`       | go up one directory
|           | `cd /d`       | change to absolute directory d
| `cp`      | `cp f1 f2`    | make a copy of file f1 called f2
| `cut`     | `cut -f 1 f`  | cut field 1 from file f
| `git`     | `git add f`   | start tracking file f
|           | `git commit`  | finished edits, ready to upload
|           | `git push`    | put changes into repository
|           | `git pull`    | retrieve latest documents from repository
|           | `git status`  | check on status of repository
| `grep`    | `grep p f`    | print lines with the letter p in file f
| `gzip`    | `gzip f`      | compress file f
| `gunzip`  | `gunzip f.gz` | uncompress file f.gz
| `head`    | `head f`      | display the first 10 lines of file f
|           | `head -2 f`   | display the first 2 lines of file f
| `history` | `history`     | display the recent commands you typed
| `less`    | `less f`      | page through a file
| `ls`      | `ls`          | list current directory
|           | `ls -l`       | list with file details
|           | `ls -la`      | also show invisible files
|           | `ls -lta`     | sort by time instead of name
|           | `ls -ltaF`    | also show file type symbols
| `mkdir`   | `mkdir d`     | make a directory named d
| `mv`      | `mv foo bar`  | rename file foo as bar
|           | `mv foo ..`   | move file foo to parent directory
| `nano`    | `nano`        | use the nano text file editor
| `pwd`     | `pwd`         | print working directory
| `rm`      | `rm f1 f2`    | remove files f1 and f2
|           | `rm -r d`     | remove directory d and all files beneath
|           | `rm -rf /`    | destroy your computer
| `rmdir`   | `rmdir d`     | remove directory d
| `sort`    | `sort f`      | sort file f alphabetically by first column
|           | `sort -n f`   | sort file f numerically by first column
|           | `sort -k 2 f` | sort file f alphabetically by column 2
| `tail`    | `tail f`      | display the last 10 lines of file f
|           | `tail -f f`   | as above and keep displaying if file is open
| `touch`   | `touch f`     | update file f modification time (create if needed)
| `wc`      | `wc f`        | count the lines, words, and characters in file f
| `zless`   | `zless f.gz`  | page through compressed file f.gz, see `less`


----------

These may show up in an the optional content

| Command   | Example       | Intent
|:----------|:--------------|:------------------------------------------------
| `chmod`   | `chmod 644 f` | change permissions for file f in octal format
|           | `chmod u+x f` | change permissions for f the hard way
| `df`      | `df -h .`     | display free space on file system
| `diff`    | `diff f1 f2`  | shows differese between files f1 and f2
| `du`      | `du -h ~`     | display the sizes of your files
| `echo`    | `echo hi`     | prints hi to stdout
| `echo`    | `echo $HOME`  | prints path to home directory
| `htop`    | `htop`        | monitor resources, a variant of top
| `ln`      | `ln -s f1 f2` | make f2 an alias of f1
| `more`    | `more f`      | page through file f (see less)
| `sum`     | `sum f`       | create a checksum for a file
| `tar`     | `tar -cf ...` | create a compressed tar-ball (-z to compress)
|           | `tar -xf ...` | decompress a tar-ball (-z if compressed)
| `time`    | `time ...`    | determine how much time a process takes
| `top`     | `top`         | display processes running on your system
