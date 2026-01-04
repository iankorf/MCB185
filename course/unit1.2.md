Unit 1.2: Unix Basics
=====================

## Unix/Linux ##

Most professional bioinformatics is done in a Unix/Linux environment. You don't
have to love Unix/Linux, but you do have to be proficient at it.

### Unix ###

Unix is an operating system, Like Mac or Windows, but much older. It uses a
command line interface (CLI) where you type at the keyboard to make things
happen. On a computer running Mac or Windows, you typically use a mouse to make
things happen. For example, if you wanted to move a picture called "oops.jpg"
from your Downloads folder into the trash, you could click the icon of the
picture and drag it to the trash can. Alternatively, you might right-click the
icon, and choose "Delete" from the menu that pops up. On a Unix computer, you
would type the following command and then hit the Enter or Return key.

```
rm oops.jpg
```

Dragging a file to a trash can is a lot more intuitive than typing commands, so
why do you have to learn Unix? Because when it comes to doing repetitive tasks,
it's much easier to automate them in Unix. Imagine you had 100 PDFs in your
Downloads folder along with a bunch of other files. identifying, clicking and
dragging each PDF to you Favorites folder is a lot of clicking and dragging.
However, in Unix, it's something as simple as this:

```
mv *.pdf ~/Favorites
```

### Linux ###

Linux is a lot newer than Unix. It is designed to work just like Unix. The main
difference is that Unix is a commercial product and Linux is completely free.
It can be confusing that Linux is branded with different names like Debian,
Fedora, LinuxLite, Mint, and Ubuntu. They are all similar to each other and all
similar to Unix (which also has several different flavors). In addition, there
are also other Unix-like things that aren't truly Linux or Unix but behave
similarly. In this course, the terms Unix and Linux are used interchangeably.

### CLI and Terminal ###

99% of bioinformatics is done in a Unix Command Line Interface (CLI). If you
have any aspirations of becoming a bioinformatics programmer or a modern
biologist, you need to become comfortable with the CLI.

A "terminal" is an application (program) that allows you to type commands and
see the text outputs of those commands.

In order to begin your journey as a bioinformatics programmer, you will need to
find/install a Terminal with a Unix-compatible CLI.

### Recommendations ###

+ Recommended
    + Mac
    + Windows + WSL
    + Windows + Cygwin
    + Windows + Virtual Machine
    + Install Linux on spare PC
+ Not Recommended
    + Chromebook
    + Git bash
    + Remote login

### Unix on Mac ###

If your computer is a Mac, you already have Unix installed, and your specific
flavor of Unix is called Darwin. You can get to the CLI with the _Terminal_
application. However, you might not have `git` and other developer tools
installed by default. To install these, type the following in your terminal and
follow the instructions:

```
xcode-select --install
```

By default, your home directory might not be shown in your sidebar. Add it by
clicking the home-shaped icon in Finder->Settings->Sidebar.

### Windows + WSL ###

Modern versions of Windows have Windows Subsystem for Linux (WSL). This allows
you to run Linux terminals from within Windows. To install Linux go to the
Microsoft Store. You don't have to buy anything, but that's where you find it.
There are several Linux distributions. Install Ubuntu.

### Windows + Cygwin ###

Cygwin is not an entire operating system but rather a terminal with Unix-like
commands. If you have an older Windows machine that doesn't support Windows 11,
use this. It works great for this course and for lots of Unix and Python tasks
in general. However, some external libraries (which we don't use in the course)
may be a pain to install.

1. Go to https://www.cygwin.com
2. Download and run the installer: `setup-x86_64.exe`
3. Choose the defaults with "Next" until you get to the Download Sites
4. Choose one of the sites, and if it is slow, stop and choose another
5. Install packages by double-clicking "Skip" -> version number
    + Interpreters - python39
    + Devel - git
    + Editors - nano
6. Choose "Next" and ultimately "Finish"

Launching the "Cygwin64 Terminal" brings up a typical CLI where you type
commands. Try typing `git` followed by the return key.

```
git
```

If this produces an error message, you didn't install Cygwin properly. Stop and
get help right now. Do not move on thinking you will get back to this later.

### Windows + Virtual Machine ###

A virtual machine (VM) is a _fictional_ computer running inside your normal
Windows operating system. The virtualization _host_ software (e.g. VirtualBox)
running on the Windows PC (host) tricks the new _guest_ operating system
(Linux) into thinking it is attached to its own motherboard, CPU, keyboard,
mouse, monitor, etc.

The upside of virtualization is that it's safe and inexpensive. It's hard to
destroy data on your computer and you don't have to buy any new hardware.
VirtualBox is free software that works very well. Other popular virtualization
products include VMware and Parallels. If you want commercial support, you may
like those.

The downside of a VM is that your virtual machines will take away some RAM,
CPU, and storage from your host OS. RAM is the most critical resource because
it isn't easily shared. If you have less than 8 GB of RAM in your computer, you
will probably not want to run a VM.

On the CPU side, your programs running in a VM will typically run 1-10% slower.
You will also have to dedicate about 20 GB of hard disk space. Even with the
downsides, VMs are a great way to run Linux on your PC.

One additional complication is that your BIOS might need to be modified to run
virtual machines. Some manufacturers ship their products with virtualization
disabled. This is easily changed in BIOS. Reboot and hold down the F10 key - or
sometimes it's F1, F2, F12, or DEL to enter BIOS. Navigate to CPU (sometimes
it's in security). Enable virtualization, save changes, and reboot. If this is
causing problems or is too confusing, see Cygwin above.

There are many distributions of Linux. The most obvious differences among them
is their default desktop Graphical User Interface (GUI). Some look like
old-school Windows while others look like Mac OS, and still others offer their
own unique look and feel. Here are some recommendations for setting up your VM.

+ Linux: Lubuntu
+ VM Memory: 2 GB (or 4 GB if your computer has more than 8 GB)
+ Disk: use default types, 20G is a good amount

If you want to be able to copy-paste between Windows and Linux or create a
shared folder that both can access, you need to "Install the Guest Additions
CD" and run its installation script.

+ Start up the Linux VM
+ Click on the "Devices" menu
+ Click on "Install the Guest Additions CD image..."
+ Click OK if you get a dialog box asking if you want to mount the CD
+ Open a Terminal application
+ Do the two commands below, replacing `username` with your user name

```
cd /media/username/VBOX_GAs*
sudo sh VBoxLinuxAdditions.run
```

+ Set up a shared clipboard if you want to copy-paste between host and VM
+ Set up a shared folder if you want Linux and Windows to share files

If you have any problems or questions, seek help from the instructor or TA.

### Install Linux ###

There are a variety of ways you can install Linux natively on your PC. You can
repartition your main SSD and dual boot, choosing Windows or Linux during
startup. You can install Linux on a spare SSD. You can even run Linux off a
flash drive, plugging it in whenever you want to run it. Any of these methods
will give you a 100% Linux-only environment that will take advantage of all of
the CPU and memory of your laptop/desktop. The main downside is that you may
accidentally destroy Windows during installation. Linux is a great way to
revive an older PC that no longer runs modern Windows.

### Linux on Chromebook ###

Chromebooks are some of the least expensive computers you can buy.
Conveniently, Linux is built right in. Select the clock in the lower right
corner and then go to Settings->Advanced->Developers.

Scroll down to "Linux development environment" and turn it on. It takes a few
minutes to install the first time and also between OS updates. To get to the
Linux CLI, use the Terminal application.

Chromebooks are not really recommended because it's not a popular platform for
professional bioinformatics work. However, they will work great for this
course.

### Git Bash on Windows ###

Git Bash is software intended for running git commands on Windows PCs using a
command line interface. It can be used for more tasks, such as Python
programming. Some programming languages are built-in (e.g. Perl) but Python is
not by default. Git Bash feels very similar to Cygwin but software installation
is slightly more complex.

### Raspberry Pi ###

The Raspberry Pi is an inexpensive ($50-100) single board computer (SBC) that
is about the size of a deck of cards. You can also get one built into a slim
keyboard. They use Linux as their OS. You just need to provide a mouse,
keyboard, and monitor. They work great as a learning platform, but can be
limiting later on as some useful bioinformatics software isn't pre-compiled for
the Pi. Raspberry Pi was the first cheap SBC, but you can buy them from several
companies now. However, for the same price, you can buy an old laptop, which
will work better.

### Remote Login ###

Another way to work with Linux is to use your computer as a portal to another
computer located somewhere on the Internet that provides a Linux CLI. This
might be part of a larger cloud computing service (e.g. Google, Amazon, etc.)
or a computer located at your school. The small downside here is that you'll
need a network connection.

------------------------------------------------------------------------------

## Terminal ##

The terminal is how you interact with the Unix/Linux command line interface
(CLI).

There are many terminal applications. Generally, it doesn't matter which one
you use. It's sort of like choosing between Firefox and Chrome: they look a
little different, but both let you browse the Internet. Find a terminal
application on your computer. Windows WSL users gve the 'Ubuntu' application.
Mac users have 'Terminal'. Cygwin users have 'Cygwin64 Terminal'. Linux users
have 'xterm', 'Qterm' or some other name with 'term' in it. Create a shortcut
in your dock/launchbar so you can access it quickly.

Every terminal has a command line interpreter called a shell. There are many
flavors of shell with names like `sh`, `bash`, `zsh`, `csh`, `ksh`, etc. The
shell interprets what you type on the command line. For example, when you type
`ls` followed by return, the shell interprets that to mean you want to run the
`ls` program. The shell is actually a programming language. The various flavors
of shell are like different dialects. We won't be using many features of shell
programming in this course, so the choice of shell doesn't really matter.

Each time you interact with the CLI, you give it a named _command_. Commands
are sometimes called _programs_ or _tools_. Each command does some useful
tasks. For example, the command `date` reports the current date. Each time you
see a block of text as shown below, this means to type the line and end with
the return key. Try that now in your terminal.

```
date
```

Most commands have additional behaviors that are invoked with "command line
options", which are sometimes called "arguments", "flags" or "parameters".
These options are often single dashes followed by single letters, like
`-I`, and sometimes double dashes with longer tokens, like `--iso-8601`. Many
Linux programs like `date` support both long and short options. Both of these
lines do the exact same thing. But not every version of Unix `date` has the
**exact** same command line options. For example, on Mac OS, `-I` works but
`--iso-8601` does not.

Note, in the following block of text, you're supposed to type `date -I` and
then hit the return/enter key. Then type the next line and hit return/enter.
It's two separate commands. And if you're on a Mac, the 2nd command will result
in an error.

```
date -I
date --iso-8601
```

To see which options are availble for a command, use the `man` command, which
is short for "manual". Man pages are written in a very terse style that is
often confusing, and you are generally better off getting an explanation from
the Internet.

```
man date
```

Some commands and options take "arguments". That is, you follow the command or
option with more words. Let's tell the `date` command we want to display the
date in Coordinated Universal Time (UTC) at a point back in time. The `-u` flag
specifies that we want UTC. Note that we prefer to call `-u` a _flag_ because
its only behavior is to be on or off (the flag is raised or not). The `-d`
parameter has an argument of `2020-03-15`, which is our previous moment in
time.

```
date -u -d 2020-03-15
date --utc --date 2020-03-15
```

The `date` command itself can also take an argument, which has an arcane
formatting syntax. Let's say we want the typical US-style month/day/year
format. `%m` stands for month, `%d` stands for day, and `%Y` is the 4 digit
version of year (lowercase y for the 2 digit version).

```
date "+%m/%d/%Y"
```

------------------------------------------------------------------------------

## Programming Editor ##

You will spend a lot of time using a text editor designed for programming. A
text editor is sort of like a word processor but without a choice for font
styles, ruler settings, or embedded images. We don't use MS Word, Google Docs
or any other word processor in the course, only text editors. Popular text
editors include:

+ Visual Studio Code
+ BBedit (Mac only)
+ Notepad++ (Windows only)
+ Caret (Chromebook only)
+ Sublime Text
+ Atom

If you're using a VM, the Linux distribution will come bundled with an
acceptable editor like FeatherPad or gedit. However, you're encouraged to
explore other editors. You will be spending a lot of time editing code, so you
might as well use one you like. A lot of programmers use an IDE (integrated
development environment). This is sort of like having your editor, terminal,
and other useful stuff all in one application.

------------------------------------------------------------------------------

## Home Directory ##

When you open your graphical file browser, it has a default view. This might be
your recent files, desktop, or some other place on your file system. Similarly,
when you open your terminal application, it also has a default view, which we
call its focus. By default, the focus of your terminal is your home directory.
To see the contents of your home directory, open the terminal application and
use the `ls` command to list and sort its contents.

```
ls
```

Linux and Mac users will see familiar folder names like Desktop, Documents,
Downloads, as well as other folders or files you may possess in your home
directory. In Unix, we call folders "directories". They mean the same thing.
Windows-WSL and Windows-Cygwin users will not see names after `ls` because no
default directories were created for you. That's okay. We will be creating some
of our own very soon.

Your home directory is located at a specific address in your filesystem. The
root of the Unix filesystem is `/`. All directories and files are
hierarchically under "slash". For example, your home directory might be in
`/home/your_name` or `/Users/your_name`. The exact location depends on your
operating system. Let's examine the path to your home directory with the `pwd`
command, which stands for "print working directory".

```
pwd
```

To change directory, use the `cd` command. Let's change to the root directory
and verify that the focus of the terminal is indeed `/` using `pwd`.

```
cd /
pwd
```

This should have reported simply `/`. Try examining the root of the filesystem
with `ls`.

```
ls
```

You should see a bunch of short names, which include `bin` and `etc`, `home`,
`sbin`, `usr`, and `var`. Depending on your OS, there may be other names as
well. You can look inside a directory by giving `ls` an argument. Let's try
listing what's in the bin directory.

```
ls bin
```

The output shows _some_ of the core programs provided by Linux. Note that even
though the current focus of your terminal is `/`, you were able to `ls` a
different directory. You can `ls` any path, not just the one with the current
focus.

To get back to your home directory, use `cd` without any arguments. Verify your
focus is your home directory using `pwd`.

```
cd
pwd
```

### Mac ###

Your home directory path is: `/Users/{username}`

### Windows - WSL ###

In Windows, you have 2 completely separate filesystem hierarchies, one for
Windows and one for Linux. Note that `{unixname}` is not known until you
install a Linux. Use the `\\wsl$` to find it.

- From Linux
	- To Linux home: `/home/{username}`
	- To Windows home: `/mnt/c/Users/{usernme}`
- From Windows
	- To Linux home: `\\wsl$\{unixname}\home\{username}`
	- To Windows home: `C:\Users\{username}`


### Windows - Cygwin ###

- From Cygwin
	- To Cygwin home: `/home/{username}`
	- To Windows home: `/cygdrive/c/Users/{usernme}`
- From Windows
	- To Cygwin home: `C:cygdrive64\home\{username}`
	- To Windows home: `C:\Users\{username}`


### Linux ###

Your home directory path is: `/home/username`

### Code Directory ###

We are going to organize all of our programming efforts in a directory called
`Code`. Use `pwd` to ensure your focus is your home directory. If you are in
another directory, use `cd` to get back to our home. Once your focus is set to
home, use `mkdir` to create the `Code` directory.

```
cd
mkdir Code
```

### File Naming Conventions ###

Most of the time, we use lowercase for everything. There is one common
exception: directories in your home directory are often upppercase (e.g.
Documents, Downloads, etc.). This is why `Code` is capitalized and not `code`.

+ Use lowercase letters in general
+ Use underscores or dashes to separate words (e.g. `human_genome.fa.gz`)
+ Dots are usually reserved for file type extensions (e.g. `poetry.txt`)
+ Avoid using spaces or punctuation in your folder or file names

------------------------------------------------------------------------------

## Git ##

Git is a very popular document management system. While it was designed for
source code management, it can be used to manage all kinds of projects. Git
allows multiple people to work on the same files without anyone over-writing
anyone else's work. You will always know who did what and when.

A "repository" is a collection of files and folders. Each repository has a
specific intent. You might start a repo (slang for repository) to store a
collection of cooking recipes, or maybe to write a book with a couple other
co-authors. If you have a computer-based project, Git is a great way to manage
the project.

### GitHub Account ###

GitHub is a website that lets you store your git repositories for free. It's
secure and backed up. There are several similar sites, but GitHub is the most
popular. Every bioinformatics developer should have a GitHub account. Your
repositories and activity are part of your CV. If you don't have a GitHub
account, it's time to point your web browser to [GitHub](https://github.com)
and create an account.

Choose a username. It's okay to be clever, but don't be silly. Remember, this
will be part of your CV. After setting your email and password, choose the free
plan and then answer a few questions about your interests to create your
account. Go to your email to verify your email address.

### Create a Repository ###

It's time to create your first repository. Before we begin, we need to talk a
little about ownership, privacy, and security.

When you create a repo, you own it. You can read it, write to it, or even
delete it. Later, you can invite collaborators who can join you in your
efforts, but by default, only you can make edits.

When a repo is created, it can be either _Public_ or _Private_. A Public
repository allows other people to download a copy of your repo. This is called
_cloning_. There is no security risk in cloning a Public repository (unless you
put sensitive info in there). If people modify their clones, it does not affect
your files. If you want people to be able to edit files in your repo, you have
to invite them as collaborators.

A Private repository is invisible to everyone but you. You can add
collaborators to Public or Private repos and specify what kinds of permissions
each collaborator may have. As the owner, you can change a repo from Public to
Private and back. Most of my repos are public because I believe in openly
sharing (but hands off my sandwich).

Now let's go make a repo. Go to the GitHub website and click on the green "New"
button to create a new repo. Name this "mcb185_homework". Making it public may
make it easier to get help from the instructors. Click the checkboxes to
initialize with a README, add a .gitignore, and add a license. Scroll through
the .gitignore options until you get to "Python". Choose whichever license you
like. I generally use MIT. Click the "Create Repository" and you will be
transported to your new, mostly empty repo.

### Personal Access Token ###

When you interact with the GitHub website, you use a username and password (and
possibly multi-factor authentication). When you interact with GitHub using the
CLI, you **cannot use your website password**. Instead you have to use a
"personal access token" (PAT). So the first thing we need to do is to generate
a PAT.

Log into GitHub and then click on the icon in the top right corner. This will
drop down a menu where you will find "Settings". Follow that link and you will
get to your various account settings. Scroll down to the bottom to find
"Developer Settings". On the next page you will see "Personal access tokens".
Click on the link to "Generate a personal access token".

In the "Note" you might put in "programming" or something. It doesn't matter.

For "Expiration" choose the "No expiration" option.

Click on the "repo" checkbox, which will also check the subordinate boxes.
Finally, go to the bottom of the page and click "Generate token".

This personal access token is given to you once. Copy it and save it somewhere
safe (you could use a Google Doc). You can never get to this PAT again. Ever.
However, you can generate a new one anytime you like, so if you lose your PAT,
you can just generate a new one.

### Cloning Repos from the CLI ###

Your mcb185_homework repo is located on GitHub, but not in your Linux
environment. Type the following commands in your terminal, substituting
`YOUR_GITHUB_HANDLE` for whatever your GitHub user name is.

```
cd
cd Code
git clone https://github.com/YOUR_GITHUB_HANDLE/mcb185_homework
ls
```

You should now see your homework directory when you `ls`. Also clone the MCB185
repo so that you have all of the course content on your computer. You might be
asking yourself why MCB185 is capitalized. That's because you're not supposed
to modify it. Think of the contents there as read-only. Note that the URL below
has my name in it intentionally. Don't substitute your name.

```
git clone https://github.com/iankorf/MCB185
ls
```

You should now see both the `mcb185_homework` and `MCB185` repos in your `Code`
directory. If you don't see these directories in your home directory, stop and
get help now. Do not proceed thinking you will get back to this later.

### Git Commands ###

Enter your homework repository and check its status. If the `cd` command below
shows an error, the focus of your terminal may have changed. Make sure that the
output of your `pwd` command is your `Code` directory before attempting to
change directory to your homework directory.

```
cd mcb185_homework
git status
```

The output of `git status` should show the following:

```
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

Let's modify a file and see what happens. Edit the `README.md` file with your
text editor and save it. If you can't find the file, ask for help.

After saving your changes, do another `git status`.

```
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
```

The output shows that `README.md` has been modified. There are some suggestions
about what you might like to do next. We will choose the `add` command. Do
another `git status` afterward.

```
git add README.md
git status
```

The output shows `README.md` is now ready to be committed.

```
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   README.md
```

To commit changes, we use `commit` along with a message after `-m`. In the
example below, note that the phrase is in quotes. This is required for
multi-word messages. If the message was simply "update", you wouldn't need the
quotes.

```
git commit -m "my first commit"
```

If this is the first time you've done a `commit` on your computer, you will get
an error message like the following.

```
Author identity unknown

*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: unable to auto-detect email address (got 'ianko@7600-4600.(none)')
```

Do as the prompt says, typing the two `git config --global` commands, replacing
"you@example.com" with the email address you have associated with GitHub and
replacing "Your Name" with whatever your GitHub username is.

Now try running the `git commit -m "my first commit"` again (did you remember
to use the up arrow instead of typing?). The new output is shown below.

```
[main 0d04f3a] my first commit
 1 file changed, 4 insertions(+), 1 deletion(-)
```

The last thing we need to do is to upload our changes to GitHub so that the
code is not only on our local computer, but also on the website. This is done
with the `push` command.

```
git push
```

You will be prompted for your username. You might not see any text as you type.
Next, you will be prompted for your password. Again, the text may be invisible.
This is **not** your GitHub password. This is your PAT (personal access token).
Copy-paste this into the terminal. Sometimes copy-paste doesn't work with
keyboard shortcuts, so use the right-click context menu instead.

You will eventually tire of copy-pasting your PAT every push. If you want your
computer to remember your password, do the following.

```
git config --global user.name "username"
git config --global credential.helper store
```

The next time you do a `git push` you will probably have to use your PAT one
more time, but not in the future.

Now let's go to the GitHub website. Look at your `README.md` there and verify
that the text has changed. If it has not, try reloading the page, and if you
still don't see your changes ask for help.

------------------------------------------------------------------------------

## Text and Markdown ##

Most of the files we work with in Linux are plain text files. Many things
change in this world, but not the format of text files.

There are two main types of files you will encounter: text and binary. You can
view text files with `less` and edit them with `nano`, for example. All of the
programs we write in this course will be plain text files. You can also view
and edit binary files but they look like gobbledygook, not English. If you want
to see what a binary file looks like, try the following.

```
less /bin/ls
```

You may have to hit the 'y' key to see the output. You're looking at the
machine code for the `ls` program. It's not meant to be human-readable. Hit the
'q' key to get out of `less`. So what makes a file text or binary? A text file
typically uses only the byte values from 0-127 (decimal) or 00-7F (hex). Binary
files use all values from 0-255 (00-FF). Really, all files are binary, but text
files are a special case of binary files that are meant to be human readable
and follow the ASCII convention of only using 0-127. Thinking back to the last
unit, all of the bytes in a plain text file are less than 128. That means the
way to tell if a file is binary or not is to see if there are any bytes with a
1 in the first position.

- `01111111` 127 dec, 0x7F (ASCII)
- `10000000` 128 dec, 0x80 (binary)

### Markdown ###

Text files are incredibly simple. There are no choices of ruler settings, font
family, font style, lists, or tables you expect to find in a word processing
document. However, sometimes you want part of a text file to look like a
heading, or boldface, or a list. There are lots of ways you can imagine doing
that from the use of capital letters to punctuation. Markdown is a global
standard for formatting text files. If you follow the standard, you can turn
your plain text documents into beautifully formatted HTML or PDF that has
actual headings, hyperlinks, font styles, lists, etc.

To find out how to write Markdown, check out the website linked below. This is
the official home of vanilla Markdown. There are a few customizations of
Markdown that add a few more things like tables.

[Markdown](https://daringfireball.net/projects/markdown)

Another way to learn Markdown is to compare an HTML or PDF file to its original
Markdown plain text source document. If you're viewing this document on GitHub,
you're viewing it formatted as HTML. You can examine the raw text either on the
website or in your copy of the repo.

------------------------------------------------------------------------------

## Hello World ##

The first program you write in any language is "hello world". This is something
minimal that shows that your programming environment is working. We are going
to write hello world programs in both shell and python.

### 00hello.sh ###

Change directory to your homework repo and create a file with the `touch`
command.

```
cd
cd Code/mcb185_homework
touch 00hello.sh
```

Open your editor, find this file, and create this one-line script.

```
echo "hello world"
```

Save the file. Go back to the terminal and run the program.

```
sh 00hello.sh
```

If all goes well, you should see your welcome message in the terminal. If you
don't, stop now and get help. Don't continue on thinking you'll fix this later.

### 01hello.py ###

Let's make the equivalent program in Python.

```
touch 01hello.py
```

Open your editor, find this file using the GUI, and write the following
one-liner.

```
print('hello world')
```

Save the file. Now run the program.

```
python3 01hello.py
```

If all goes well, you should see your welcome message in the terminal. If you
don't, stop now and get help. Don't continue on thinking you'll fix this later.

Now let's add your programs to your homework repo. `git status` will show that
neither file is tracked. So let's `add` them, create a `commit` message, and
then `push` them back to the website. Remember, you don't use your website
password here, but rather your github personal access token (PAT). You'll have
to copy-paste that, as it's a bit too long to type.

If you get an error, it may be because the copy-paste didn't work. Do a
right-click-based paste rather than using the keyboard shortcut.

```
git add 00hello.sh 01hello.py
git commit -m new
git push
```

Check the GitHub website. Both of your new files should now be in the repo. If
they are not, refresh the page or get help if that's not the problem.

It might seem like git is a lot of effort just to upload your code to a
website. If that's all git did, it would be too much effort, but git allows you
to do a lot more. Git tracks every change you make to a file, allowing you to
rewind it to any point in time. Git allows you to make a _branch_ of related
work and then later merge it back in with the main trunk if desired. More
importantly, git allows multiple developers to work simultaneously on the same
project without destroying each others work. We aren't using those advanced
features yet. Right now, our focus is on backing up our code and logging our
programming activity to the GitHub website.

------------------------------------------------------------------------------

## Resist Copy-Paste ##

There are a lot of commands to type in this unit and throughout the course.
Copy-pasting them will result in you getting better at copy-paste. Typing the
commands will result in you remembering them later. One of the goals of this
course is for you to gain expertise and confidence with the CLI. Typing will
help you improve your CLI skills and memory. Copy-paste will not. You will not
have copy-paste available when you take a written exam.

------------------------------------------------------------------------------

## Shortcuts ##

Typing is bad for your health. Seriously, if you type all day, you will end up
with a repetitive stress injury. Don't type for hours at a time. Make sure you
schedule breaks. Unix has several ways to save your fingers (that do not
involve copy-paste).

### Tilde Expansion ###

Your home directory is such an important place that Linux has a shortcut. It's
the tilde `~` character, which is probably at the top left of your keyboard.
When you type the tilde followed by a path, the tilde expands to the location
of your home directory.

```
cd ~/Code
pwd
```

### Tab Completion ###

Probably the most important finger saver in Linux is **tab completion**. When
you hit the tab key, the shell completes the rest of the word for you if it can
guess what you mean. Try typing `his` and then the tab key.

```
his
```

This fills in the word `history`, which is the name of a Unix command. Hit
return and you will see all the commands you have typed in this terminal. If
`his` didn't fill in `history` it's because you have another command that
starts with `his`. Hit the tab key again, and the terminal will report the
names of those other commands. Try following with a `t` to make `hist` and then
tab-complete again.

### Up Arrow ###

Instead of re-typing long commands, you can go backwards through your command
history with the up-arrow. Try hitting the up-arrow several times and you'll
backtrack through all the commands you've typed. Use the left and right arrows
to position the cursor if you want to edit parts of the line. To get out of
this, and many other situations, type Control-C. That is, hit the control key
and then the letter "c" (not uppercase). In text, Control-C is abbreviated ^C
with a capital letter even though it's lowercase.

After using the up arrow, you may want to jump to the start or end of a line to
modify it. Use Control-A to get to the start and Control-E for the end.

+ ^C break out of what I'm doing
+ ^A start of CLI
+ ^E end of CLI

### Wildcards ###

One of the most useful time-saving tricks in the shell is the use of the `*`
character as a wildcard. The `*` character matches missing characters if it
can. We'll see this a lot later. The first line below lists your Code
directory. The second line lists all of the items in your Code directory
(performs `ls` on `MCB185`, `mcb185_homework`, and anything else in there). The
third line lists all of the markdown files in the `MCB185/course` directory
(markdown files use the `.md` suffix).

```
ls ~/Code
ls ~/Code/*
ls ~/Code/MCB185/course/*.md
```

### Aliases ###

Another great way to save keystrokes is to create aliases for your favorite
commands. See the section on Shell Customization below.

------------------------------------------------------------------------------

## Viewing Files ##

The most common programs for viewing files are these:

+ `cat` - dump the contents of files
+ `head` - print the first 10 lines of a file
+ `tail` - print the last 10 lines of a file
+ `more` - page through a file
+ `less` - page through a file with more control
+ `zless` - like `less` but works with compressed files

Let's give them a test drive.

```
cd ~/Code/MCB185
cat README.md
```

You can display multiple files with the wildcard. Here's how to dump all of
the markdown files in the directory.

```
cat *.md
```

The `head` and `tail` programs show 10 lines of text at the top or bottom of a
file.

```
head README.md
tail README.md
```

If you want more or less lines, just add the number of lines after a dash.

```
head -5 README.md
tail -15 README.md
```

To read a file one page at a time, use `more` or `less`. Use the "f" and "b"
keys to move forward or backward one page. You can also use the spacebar to
move forward one page. To quit the program, use the "q" key.

```
more README.md
less REAMDE.md
zless data/GCF_000005845.2_ASM584v2_genomic.fna.gz
```

Most Unix programs have descriptive names or initialisms. `cat` is short for
catenate. `head` and `tail` are pretty self-explanatory. `more` shows you more
of a file. `less` does more than `more` because sometimes less is more (Unix
culture is full of puns). Compressed files often have the letter "z" associated
with them, so `zless` makes sense as a variant of `less` that works with
compressed files.

------------------------------------------------------------------------------

## Absolute and Relative Paths ##

When you open a terminal application, the focus of your shell begins in your
home directory. Let's verify this. Open a new terminal and use the `pwd`
command to print your working directory.

```
pwd
```

The `pwd` program reports the "path" to your location. A "path" is a chain of
directories, separated by forward slashes, optionally ending in a file. So
`/home/username/Code` is a path as is `/home/username/Code/MCB185/README.md`
(the second example ends in a file). Every path that begins with a slash is an
"absolute path". A "relative path" does not start with a slash. For example,
`Code/MCB185` is a relative path to a directory and `Code/MCB185/README.md` is
a relative path to a file.

Starting from your home directory, use `less` to display the `README.md` above.
Do this both with an absolute path and a relative path. Tilde provides the
absolute path.

```
less ~/Code/MCB185/README.md   # absolute
less Code/MCB185/README.md     # relative
```

Now change directory to the `MCB185` directory and display the file again using
both absolute and relative paths.

```
cd Code/MCB185
less ~/Code/MCB185/README.md   # absolute
less README.md                 # relative
```

The `.` character represents your current directory. So these two commands are
equivalent.

```
less README.md                 # relative
less ./README.md               # relative
```

The `..` token represents the parent directory. Change directory to `data` and
once again read the same file using both absolute and relative paths.

```
cd data
less ~/Code/MCB185/README.md   # absolute
less ../README.md              # relative
```

### Review ###

+ any path that begins with the filesystem root `/` is an absolute path
+ paths that begin with the tilde shortcut `~/` are also absolute
+ paths that do not begin with `/` are relative paths
+ `.` and `..` are relative paths to your current and parent directories

Here are some examples

+ `/bin` absolute path
+ `~/Code` absolute path (`~` is an absolute path to your home directory)
+ `REAMDE.md` relative path to file in current directory
+ `./README.md` also relative path to file in current directory
+ `../README.md` relative path to file in parent directory

### Practice ###

Change directory to your home using one of these methods

```
cd
cd ~
```

List the contents of your `mcb185_homework` directory and also the `MCB185`
directory using a single command and relative paths. Use tab-completion after
'C' and also after 'm' or 'M'.

```
ls Code/mcb185_homework Code/MCB185
```

Change directory to your homework directory and list the contents of the MCB185
data directory. Use tab completion and relative paths with 'M' and 'd'.

```
cd Code/mcb185_homework
ls ../MCB185/data
```

Change to your MCB185 data directory using absolute path. Verify with `pwd`. Go
back to your home directory using relative paths and verify.

```
cd ~/Code/MCB185/data
pwd
cd ../../..
pwd
```

------------------------------------------------------------------------------

## stdout, stdin, stderr ##

When you issue commands like `ls`, the output that is sent to your terminal is
called Standard Output (stdout). Output doesn't have to go to your terminal.
You can choose to send it to a file or to another program.

The `>` operator re-directs stdout to a file. Let's try that with the `ls`
command.

```
cd ~
ls Code/MCB185
ls Code/MCB185 > foo
```

Notice that the second `ls` command didn't print anything to the terminal.
That's because the contents are in the file "foo". You can dump those out to
the terminal with `cat`.

```
cat foo
```

Instead of sending stdout to a file, let's pipe it to another command. Here,
the stdout of `ls` will be sent to the Standard Input (stdin) of the word
counting program `wc` via the pipe `|` operator.

```
ls Code/MCB185 | wc
```

Some programs, like `wc` can read from both stdin and file.

```
wc foo
```

So `ls > foo` followed by `wc foo` does the same thing as `ls | wc` without
having any intermediate file. Unix pipes are a very powerful way to chain
programs to each other.

There is also the `<` operator. This sends standard input (stdin) from a file
to a program. The keyboard is the usual source of stdin.

```
wc < foo
```

What do you think this does?

```
wc < foo > bar
```

Here, the contents of the file `foo` are sent to `wc` as stdin, and then `wc`
sends its stdout to the file `bar`, which contains the `wc` output.

+ `>` sends the stdout of a program to a file
+ `<` sends the contents of a file to the stdin of a program
+ `|` connects the stdout of one program to the stdin in of another

In addition to stdin and stdout, there is another stream of data called
Standard Error (stderr). This is meant to be used for error messages or logging
messages rather than data. Provided you don't have a file named `crap` on your
computer, the `ls` command below will report an error to your terminal. Since
there was no stdout, the file `bar` is empty. You can verify that `bar` is
empty with any of the file reading tools already introduced or `ls -l` which
shows a longer listing of file attributes, including a `0` for the size of
`bar`.

```
ls crap > bar
ls -l
```

------------------------------------------------------------------------------

## Creating and Modifying Files ##

### nano ###

There are a number of ways to create a new file in Linux. The `touch` command,
which we saw last unit, will create an empty file. As we just saw, you can also
create files by re-directing stdout using `>`. If you need to make quick edits
to a file, you will find the `nano` program useful. This is a terminal-based
text editor that allows you to create new files or edit existing files. Let's
create a new file called `baz` using `nano`.

```
nano baz
```

Start typing and you will see text appear on your screen. Write a few lines of
bad poetry. Move the cursor with the arrow keys. The bottom of the screen shows
some of the control keys used to interact with `nano` . To write the file, hit
^O (that means hold the control key down and type lowercase "o"). Hit the
return key to confirm and then exit the program with ^X. Display the file with
any of the usual programs like `cat`, `head`, `less`, etc.

```
head baz
```

### Moving and Renaming ###

The `mv` command is used to both rename and move files. Let's first rename your
`baz` file to `poetry.txt`.

```
mv baz poetry.txt
```

Next, let's use `mv` to move your poetry into your homework directory.

```
mv poetery.txt Code/mcb185_homework
```

If that last line gave you an error message ending with "No such file or
directory" it's because you did one of two things.

1. You copy-pasted the line
2. You typed the whole line verbatim

The reason for the error is that `poetery` has been intentionally misspelled.
There are several intentional misspellings in this unit to encourage you to use
your brain rather than be lazy.

If you copy-pasted, consider dropping the course. You have been told not to
copy-paste and your stubborn laziness or inability to seek help will be a
hindrance moving on.

If you typed the whole path, you are congratulated for your amazing attention
to detail. Also you're acting like a robot. Hopefully you can break of that
mindset and start acting like a thinking student.

If you noticed the misspelling and continued to type out the whole command
without using tab-completion, you're a CLI novice. Don't worry, we all start
there.

Moving onward, make sure that your homework repo contains your poetry file and
that everything is spelled correctly.

```
ls Code/mcb185_homework
```

### Copying ###

The `cp` command is used to make a copy of a file. Let's make an additional
copy of the poetry in your homework directory back in your home directory. The
command line below reads as "copy the poetry.txt file from my homework
directory to my current location", where the dot is your current location. It's
easy to miss the dot, which is why there is a line below pointing it out. You
now have two files with the exact same names and file contents, but in two
different locations.

```
cd
cp Code/mcb185_homework/poetry.txt .
# don't type this line, look here  ^
```

### Comparing ###

If you do a long listing, you will see that both files have the same size.

```
ls -l poetry.txt Code/mcb185_homewor/poetry.txt
```

But do they have the exact same contents? They should, since you just made
copies, but how would you verify that?

Edit `~/poetry.txt` in `nano` and change just one character. While the file
sizes remain the same, their contents are now different. To see the differences
between two files, use `diff`.

```
diff poetry.txt Codes/mcb185_homework/poetry.txt
```

You will see a report showing exactly which lines are different from each
other. While `diff` is great for comparing small text files, you wouldn't use
it to validate that two compressed genome sequence files have the same
sequence. For that, you would use `sum` to perform a checksum, which is a
pseudo-unique number whose value is based on the entire file contents.

```
sum poetry.txt Code/mcb185_homework/potery.txt
```

The first column is the checksum value. Since they are different, the file
contents are different. Is it possible for two different files to share the
exact same checksum? Yes, but it's unlikely. For example, the probability that
two files have the same MD5 checksum is about 3.4e-38.

### Directories ###

Let's tidy up a bit by creating a directory with `mkdir` and then moving the
files from the previous sections into that directory. Notice that the `mv`
command can take multiple arguments. The last argument is the directory and the
previous ones are files.

```
mkdir stuff
mv foo bar poetry.txt stuff
ls stuff
```

To remove a directory, use the `rmdir` command. However, `rmdir` will not
remove a directory if it has any files in it. So this command will fail. Try it
anyway.

```
rmdir stuff
```

To remove all of the files in `stuff` we could do the following very dangerous
operation.

```
rm stuff/ *
```

The reason this is dangerous is that there is an accidental space between
`stuff/` and the `*`. The way this command is interpreted is "remove the file
called stuff and also everything else". `stuff` is a directory, not a file, so
the first argument is an error. However, `*` matches everything in the current
working directory, so all your files will get deleted!

Instead, `cd` into `stuff` and then remove everything inside. Then leave the
directory and remove it.

```
cd stuff
rm *
cd ..
rmdir stuff
```

------------------------------------------------------------------------------

## Compression ##

Data files can be very large. For this reason, they are often compressed.
However, once compressed, they don't look like normal text files.

From your homework directory, `head` the compressed GFF of E.coli, which you
can find in the MCB185 data directory. Files that end in `.gz` have been
compressed with `gzip`.

```
cd ~/Code/mcb185_homework
head ../MCB185/data/GCF_000005845.2_ASM584v2_genomic.gff.gz
```

What is all of that? It's the compressed version of the file. It isn't meant to
be human readable. It's meant to save space.

Now let's make a copy of this file in your homework directory. While we could
`cp` the file, let's so something more fun. We'll use `cat` to stream the file
to stdout, and `>` to redirect that to a simpler file name.

```
cat ../MCB185/data/GCF_000005845.2_ASM584v2_genomic.gff.gz > ecoli.gff.gz
```

Examine its size with `ls -lh`, which is about 430K.

```
ls -lh
```

Gzipped files can be uncompressed with `gunzip`. Do that and inspect the file
size. 2.5M is a lot bigger than 430K. While neither 2.5M nor 430K is very
large, some data files are huge, and the ~6-fold compression observed here can
be very useful.

```
gunzip ecoli.gff.gz
ls -lh
```

When you `gzip` or `gunzip` a file, the default behavior is to create a new
file and destroy the old one. You have a file called `ecoli.gff` but the
original file `ecoli.gff.gz` is gone. If you `gzip` the `ecoli.gff` file, it
will become `ecoli.gff.gz`, destroying the uncompressed one in the process. If
you want to keep the original file, simply pass the `-k` parameter to `gzip` or
`gunzip`.

```
gunzip -k ecoli.gff.gz
ls -lh
```

Large data files are often kept compressed and never "inflated". To view a
compressed file, use `zless` instead of `less` (some versions of `less` will
actually read compressed files - try it and see).

```
zless ecoli.gff.gz
```

To use tools like `wc` on compressed files, stream them to stdout using the
`-c` flag and then pipe that to `wc`.

```
gunzip -c ecoli.gff.gz | wc
```

Now that we know we don't need uncompressed files, get rid of `ecoli.gff`.

```
rm ecoli.gff
```

You also don't need multiple copies of identical data on your computer. You
should also get rid of `ecoli.gff.gz` and always use the original file.

```
rm ecoli.gff.gz
```

------------------------------------------------------------------------------

## Soft Links ##

Even though tab-completion exists, files names like
`MCB185/data/GCF_000005845.2_ASM584v2_genomic.gff.gz` can be painful to look
at. Wouldn't it be nice if we could just call it something simpler like
`ecoli.gff.gz`? Of course we can, and we do this with soft links (also called
symbolic links or short cuts). Navigate to your homework directory and then
use `ln -s` to create a symbolic link.

```
cd ~/Code/mcb185_homework
ln -s ../MCB185/data/GCF_000005845.2_ASM584v2_genomic.gff.gz ./ecoli.gff.gz
```

The `ln` command above shows the use of relative paths but you can also use
absolute paths. Let's examine the file with `zless`. It looks just like the
original because it is a shortcut to the original. But it's not a copy. The
file isn't duplicated. Some genome files are really big. The human genome is 3
billion bases. Copying the whole file takes up space on your computer. Making a
shortcut takes almost no space.

```
zless ecoli.gff.gz
```

If you remove the symbolic link, it does not remove the original file.

```
rm ecoli.gff.gz
ls ~/Code/MCB185/data
```

+ Do not make duplicates of data files
+ Do not create uncompressed versions of data files
+ Do make soft links to data files and give them convenient names

------------------------------------------------------------------------------

## Extracting Text ##

Create a soft link to the compressed gff file from the last section and name it
`ecoli.gff.gz`. Now examine it with `zless`.

GFF files are tab-delimited text files that contain information about
sequences. Like many file formats, lines that begin with `#` are comments (NOT
hashtags) and are not considered part of the data, though they may contain some
meta-data. Each tab-delimited field has a specific type of information. For
example, fields 4 and 5 contain the coordinates of a sequence feature, and
field 3 reports what kind of feature it is.

### cut, sort, and uniq ###

Let's extract all of the features using `cut`. In the command below, `-f 3`
tells `cut` we want to extract column 3. By default `cut` splits fields on tab
characters, which is what gff uses. If the file used spaces or commas, we would
have to change the delimiter to match the file. For example, `cut -d " "` uses
spaces as a delimiter and `cut -d ","` uses comma as a delimiter.

```
gunzip -c ecoli.gff.gz | cut -f 3
```

Running that command, you should see a lot of "gene" and "CDS" features. There
are other things in there too. How many? One way to examine the output is with
`sort`.

```
gunzip -c ecoli.gff.gz | cut -f 3 | sort
```

This streamed a lot of stuff passed us too quickly to see, including a lot of
tRNAs (because the sort is alphabetical). You could try piping the output to
`less`, but paging through that would be horrible.

```
gunzip -c ecoli.gff.gz | cut -f 3 | sort | less
```

Instead, we can pass the `-u` flag to `sort`, which will restrict it to unique
text only.

```
gunzip -c ecoli.gff.gz | cut -f 3 | sort -u
```

That's better. In addition to "CDS", "gene", and "tRNA", there are other
features. However, there are also some comment lines that don't belong because
they aren't data. We can remove comments with `grep -v`. `grep` is an
incredibly powerful program that lets you search for specific patterns of text
(see more below). Here, we are only using it to skip over lines that begin with
a `#` symbol.

```
gunzip -c ecoli.gff.gz | grep -v "^#" | cut -f 3 | sort -u
```

To get the number of counts for each feature, we can pass the sorted list
through `uniq`. This program removes duplicate lines. When used with the `-c`
flag, it counts occurrences of each line.

```
gunzip -c ecoli.gff.gz | grep -v "^#" | cut -f 3 | sort | uniq -c
```

If you want to be really fancy and sort the list by how many of each feature
there are, you can pass the output through another `sort`. This time, we will
pass the `-n` and `-r` flags so that the sort is numeric and in reverse order.
Multiple flags can often be condensed so that `-n -r` is `-nr`.

```
gunzip -c ecoli.gff.gz | grep -v "^#" | cut -f 3 | sort | uniq -c | sort -nr
```

The output is as follows:

```
4494 gene
4337 CDS
 207 exon
 145 pseudogene
  99 ncRNA
  86 tRNA
  50 mobile_genetic_element
  48 sequence_feature
  22 rRNA
   1 region
   1 origin_of_replication
```

### grep ###

`grep` is such a powerful and useful tool that it deserves a little more
attention. Head over to `MCB185/data` where you'll find `dictionary.gz`. Did
you ever wonder which words have a double "aa" in them. Let `grep` do the work
for you.

```
cd ~/Code/MCB185/data
gunzip -c dictionary.gz | grep "aa"
```

To count the number of words, you can pipe the output to `wc` or pass the `-c`
flag to `grep`. The two commands below do the same thing.

```
gunzip -c dictionary.gz | grep "aa" | wc -l
gunzip -c dictionary.gz | grep -c "aa"
```

The double-a's in those words could occur anywhere in the word. If we want only
those words that begin with double-a, we use the special `^` symbol to bind the
pattern to the start. Recall that we just saw the use of `^` when removing the
comment lines from GFF.

```
gunzip -c dictionary.gz | grep "^aa"
```

The special symbol that means "bind pattern at the end" is `$`. Here are the
words that end with double-a.

```
gunzip -c dictionary.gz | grep "aa$"
```

Another special symbol is `.` (a dot). This matches any single letter. For
example, let's look for all words that have the letter `z` one letter apart.

```
gunzip -c dictionary.gz | grep "z.z"
```

Ah, but now you're wondering about the words that have different numbers of
letters between the z's. The `*` modifier means zero or more. The following
finds all the words with any number of letters between the z's including none.

```
gunzip -c dictionary.gz | grep "z.*z"
```

To get the behavior of "one or more intervening letters" we could pipe the
previous command to another grep and remove all double-z's, but that doesn't
really do what we want.

```
gunzip -c dictionary.gz | grep "z.*z" | grep -v "zz"
```

Instead, we use `+` to mean "one or more". The "basic" regular expression
syntax requires one to backslash the `+` while the "extended" syntax (signaled
with the `-E` flag) does not. The extended version is similar to what we will
use in Python much later in the course.

```
gunzip -c dictionary.gz | grep "z.\+z"
gunzip -c dictionary.gz | grep -E "z.+z"
```

Let's play a little bit more with extended syntax. Here's an example of how you
can require the middle letters to be 3 to 4 characters long. The curly brackets
specify a range.

```
gunzip -c dictionary.gz | grep -E "z.{3,4}z"
```

To specify an unlimted upper bound, use the comma by itself.

```
gunzip -c dictionary.gz | grep -E "z.{3,}z"
```

You can also search for specific classes of letters. For example, let's require
that the middle letters be one or more of the vowels, a, e, i, o, or u. A
character class is created with square brackets.

```
gunzip -c dictionary.gz | grep -E "z[aeiou]+z"
```

You can also create anti-character classes by putting a `^` symbol right after
the opening bracket. Yes, `^` is used both for binding a pattern to the start
and also for creating anti-classes.

```
gunzip -c dictionary.gz | grep -E "z[^aeiou]+z"
```

------------------------------------------------------------------------------

## Shell Scripting ##

The interactive shell you're using is itself a scripting language. All the
commands you've been using can be put in a file and re-used later.

Using your favorite editor, create the following file and save it to your
homework repo as `02status.sh`.

```
date
uname -a
printenv
python3 --version
ls -R ~/Code
```

The output of this script will help the instructors if you run into Linx/Python
problems. Here's an explanation of each line.

1. Reports the date
2. Reports the full name of your flavor of Unix
3. Reports your environment variables (not covered in this unit)
4. Reports the version of Python you have installed
5. Reports the directories and files in your Code directory

```
sh 02status.sh
```

Save the output of the report as `03report.txt`.

```
sh 02status.sh > 03report.txt
```

------------------------------------------------------------------------------

## Shell Customization ##

When you start up a terminal, the shell usually reads a login script in your
home directory. The purpose of the login script is personalize your CLI
experience. For example, perhaps you always type `ls -F` when listing
directories and you wished that `ls` showed file types by default. You can do
that in your the login script.

The name of your login script depends on your shell.

```
printenv SHELL
```

+ `/bin/bash` - `.bashrc` or `.bash_profile` or `.profile`
+ `/bin/zsh` - `.zshrc`

Note the leading `.` on the filenames above. This means these files are
normally hidden. Use the `-a` flag to show all files.

```
cd
ls -a
```

If you don't see any of the files above, create one. Make sure the focus of
your terminal is your home directory. Then create the file name based on the
SHELL. Place the following contents at the end of the file.

```
alias ls="ls -F"
```

Now, every time you give the `ls` command, you will actually be doing `ls -F`.
I type `git status` so often that I have an alias for that: `gs`.

Here are some common customizations.

```
alias ..="cd .."
alias la="ls -a"
alias ll="ls -l"
alias rm="rm -i"  # prompt user before removing file
alias cp="cp -i"  # prompt user before overwriting file
```

------------------------------------------------------------------------------

## 04spellingbee.sh ##

Have you ever seen the New York Times Spelling Bee? In this game, you are given
7 letters in the shape of a hexagon. The middle letter must be used in every
word, but the outer 6 letters can be used any number of times. Words must be at
least 4 letters long. Create a command line that solves the puzzle below. If
you solved the problem correctly, you should find 50 words. Hint: you will need
to chain `grep` more than once.

```
   O
Z     N
   R
I     C
   A
```

Now that you have solved the puzzle, save the command line in a script called
`04spellingbee.sh`. The script must run from your `mcb185_homework` directory
and access the dictionary in the `MCB185/data` directory. Do not move the
script to the `data` directory or the `dictionary.gz` to your homework
directory.

`git push` the following files into your `mcb185_homework` GitHub repository.

+ `00hello.sh`
+ `01hello.py`
+ `02status.sh`
+ `03report.txt`
+ `04spellingbee.sh`
