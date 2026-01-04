Unit 1.1: Encoded Information
=============================

## Bits ##

Do you know how information is stored in your computer? You may have heard the
terms "bits" and "bytes" but do you know what those are? A bit is a binary
digit, containing either a 0 or 1. It is effectively an off/on switch. Imagine
a clock that reports time with a single, red light bulb. The time of day could
be represented as follows:

- Off day
- On night

That's not very useful. How would one distinguish morning from afternoon? With
more lights. Let's add a second light, this one yellow. This provides 4
combinations.

- Red off, yellow off = morning
- Red off, yellow on = afternoon
- Red on, yellow off = evening
- Red on, yellow on = night

Instead of using red and yellow lights, let's use columns to represent the
different colors and 0 or 1 to show if it is on or off.

- `00` = morning
- `01` = afternoon
- `10` = evening
- `11` = night

While this is a better clock, it's still not very good. What we need is more
accuracy, which will take more switches. Each time we add a switch, it doubles
the number of combinations.

- `000` = dawn
- `001` = morning
- `010` = noon
- `011` = afternoon
- `100` = dusk
- `101` = evening
- `110` = midnight
- `111` = graveyard shift

The number of combinations is simply 2^n, where n is the number of switches. To
represent each hour, we would need 24 combinations. That cannot be achieved
with 4 switches (16 combinations) but could be with 5 (32 combinations). What
if we also wanted to specify every minute? That's 24 hours x 60 minutes = 1440
time points. We could do that with 11 switches (2048 combinations).

## Bytes ##

For historical reasons, most of the time we work with bits, we aggregate them 8
at a time. 8 bits = 1 byte. A byte is 8 bits in a row. Here are some 8-bit
numbers.

- `00000000` 0
- `00000001` 1
- `00000010` 2
- `00000100` 4
- `00000101` 5
- `01000001` 65
- `11111111` 255

Writing things out in binary is tedious, so bytes are generally written in
_hexadecimal_ notation. In base 2, there are 2 symbols: 0 and 1. In base 10
(ordinary decimal) there are 10 symbols: 0, 1, 2, 3, 4, 5, 6, 7, 8 , and 9. In
base 16 (hexadecimal), there are 16 symbols: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A,
B, C, D, E, and F. So the symbol `B` in hexadecimal means 11 in decimal. To
specify that a number is in hex, it is sometimes proceeded with 0x. Therefore
0xB is 11, but hex numbers are generally 2 digits: 0x0B. Here are some numbers
in decimal, binary, and hexadecimal.

| Binary     | Dec | Hex  |
|:-----------|:---:|:----:|
| `00001001` |   9 | 0x09 |
| `00001011` |  11 | 0x0B |
| `00001111` |  15 | 0x0F |
| `00010000` |  16 | 0x10 |
| `00100001` |  33 | 0x21 |
| `01111111` | 127 | 0x7F |
| `10000000` | 128 | 0x80 |

Have you ever seen internet addresses of the form 192.168.1.1? Ever wondered
what those 4 numbers are? Each one is a byte. So each one can have a value from
`00000000` to `11111111`. In other words, each value can be from 0x00 to 0xFF.
Or more familiarly, from 0 to 255. These same byte notations are used all over
the place in computers. For example, you may have had to dig up the MAC (media
access control) address of your network adapter, which may have looked like
`f0:18:98:e9:f2:be`. Each of those number-like things separated by a colon is a
byte in the range of 0x00 to 0xff (upper and lowercase don't matter in
hexadecimal).

## ASCII ##

Back at the dawn of computers, people needed to store text information too.
This resulted in ASCII encoding where each byte represents something you could
type at an English language keyboard. Every symbol (letters, numerals,
punctuation) gets its own ASCII value. Here is the ASCII table from 32 to 127
(`0x20` to `0x7E`).


| Dec | Hex  |  C  | Dec | Hex  |  C  | Dec | Hex  |  C  |
|:---:|:----:|:---:|:---:|:----:|:---:|:---:|:----:|:---:|
|  32 | `20` | ` ` |  64 | `40` | `@` |  96 | `60` |  `  |
|  33 | `21` | `!` |  65 | `41` | `A` |  97 | `61` | `a` |
|  34 | `22` | `"` |  66 | `42` | `B` |  98 | `62` | `b` |
|  35 | `23` | `#` |  67 | `43` | `C` |  99 | `63` | `c` |
|  36 | `24` | `$` |  68 | `44` | `D` | 100 | `64` | `d` |
|  37 | `25` | `%` |  69 | `45` | `E` | 101 | `65` | `e` |
|  38 | `26` | `&` |  70 | `46` | `F` | 102 | `66` | `f` |
|  39 | `27` | `'` |  71 | `47` | `G` | 103 | `67` | `g` |
|  40 | `28` | `(` |  72 | `48` | `H` | 104 | `68` | `h` |
|  41 | `29` | `)` |  73 | `49` | `I` | 105 | `69` | `i` |
|  42 | `2a` | `*` |  74 | `4a` | `J` | 106 | `6a` | `j` |
|  43 | `2b` | `+` |  75 | `4b` | `K` | 107 | `6b` | `k` |
|  44 | `2c` | `,` |  76 | `4c` | `L` | 108 | `6c` | `l` |
|  45 | `2d` | `-` |  77 | `4d` | `M` | 109 | `6d` | `m` |
|  46 | `2e` | `.` |  78 | `4e` | `N` | 110 | `6e` | `n` |
|  47 | `2f` | `/` |  79 | `4f` | `O` | 111 | `6f` | `o` |
|  48 | `30` | `0` |  80 | `50` | `P` | 112 | `70` | `p` |
|  49 | `31` | `1` |  81 | `51` | `Q` | 113 | `71` | `q` |
|  50 | `32` | `2` |  82 | `52` | `R` | 114 | `72` | `r` |
|  51 | `33` | `3` |  83 | `53` | `S` | 115 | `73` | `s` |
|  52 | `34` | `4` |  84 | `54` | `T` | 116 | `74` | `t` |
|  53 | `35` | `5` |  85 | `55` | `U` | 117 | `75` | `u` |
|  54 | `36` | `6` |  86 | `56` | `V` | 118 | `76` | `v` |
|  55 | `37` | `7` |  87 | `57` | `W` | 119 | `77` | `w` |
|  56 | `38` | `8` |  88 | `58` | `X` | 120 | `78` | `x` |
|  57 | `39` | `9` |  89 | `59` | `Y` | 121 | `79` | `y` |
|  58 | `3a` | `:` |  90 | `5a` | `Z` | 122 | `7a` | `z` |
|  59 | `3b` | `;` |  91 | `5b` | `[` | 123 | `7b` | `{` |
|  60 | `3c` | `<` |  92 | `5c` | `\` | 124 | `7c` | `|` |
|  61 | `3d` | `=` |  93 | `5d` | `]` | 125 | `7d` | `}` |
|  62 | `3e` | `>` |  94 | `5e` | `^` | 126 | `7e` | `~` |
|  63 | `3f` | `?` |  95 | `5f` | `_` |

Some things you type at the keyboard represent "whitespace". For example, when
you hit the spacebar, it inserts 32 or 0x20, which represents a single space.
The tab key (0x09) inserts an invisible character that "snaps" to various
positions, usually multiples of 4 or 8. The "return" key ends a line and starts
a new line. Weirdly, the return key does slightly different things on Linux and
Windows. In Linux, return inserts a linefeed character (0x0A). On Windows, the
return key inserts two characters, the carriage return (0x0D) followed by
linefeed (0x0A).

| Dec | Hex | Meaning
|:---:|:---:|:---------
|   9 |  09 | tab
|  10 |  0A | linefeed (LF)
|  13 |  0D | carriage return (CR)
|  32 |  20 | space

A plain text file is simply a file of ASCII values. For example, here are
several ASCII values. There are spaces between them below so that you can see
them better, but in an actual file they are all smushed together.

```
48 65 6C 6C 6F 0D 0A 77 6F 72 6C 64 21 04
```

If you open this stream of bytes in a program that can read plain text files
(e.g. Linux `less`, VS Code, MS Word, etc.) it will look like this:

```
Hello
World!
```

If you look up each character in the ASCII table you will see that everything
matches up really well until the "o" of "Hello". The next two characters `0D`
and `0A` are not displayed because they signify the end of a line in Windows.
If this file was created in Linux or MacOS, the end of line would be just `0A`.
There is also an additional `04` at the very end that signals "end of
transmission", in other words, the end of the file.

### Source Code Editors ###

Software developers generally write text files with a plain text editing
program. There are hundreds of applications for editing plain text such as
Notepad on Windows. More commonly, developers use programs specifically
designed for editing source code. These include applications like VS Code,
Sublime Text, Vim, Emacs, Notepad++ (Windows only), and BBedit (Mac only). In
this course, you will spend a lot of time working in a source code editor.

### UTF-8 ###

If you look at the ASCII table, you will see that it has good support for the
English language, but what about all the other languages in the world? How does
one represent something like the alchemical symbol for water: 🜁? (Were you
surprised that this is an official symbol?) The most common way to encode plain
text files is in UTF-8, which is sort of like ASCII except that there are
special signals to extend the alphabet to more symbols. In ASCII, each symbol
is 1 byte. In UTF-8, there can be up to 4 bytes for some symbols. UTF-8 has
"variable width encoding" where some symbols like ASCII captial A are just one
byte and other symbols, like alchemical water are more than 1 byte. This is
sort of like Morse Code where different letters and numerals have different
numbers of dots and dashes. Most modern plain text editors and programming
languages understand UTF-8, which means you can write programs in whatever
language you like. That said, most people write in English.

### Fonts and Styles ###

When you write in plain text, there is no specific font or style. Documents
that allow such changes need extra instructions to specify these and other
formatting options. How are rulers, margins, headers, footers, page breaks,
fonts, and styles specified? Each program has its own way of doing it. This is
why documents written in one application don't work in another.

## Colors ##

Another place you may have seen hexadecimal notation is to represent colors. In
a computer, color is made by mixing three wavelengths of light: red, green, and
blue. Each of those wavelengths can have an intensity from 0 to 255, which in
hex is 0x00 to 0xFF of course. For example, if you want to make bright red, you
use `FF` in the red channel, `00` in the green channel, and `00` in the blue
channel. The most efficient way to write this is to mash them all together as
`FF0000`. This can also be written as 0xFF0000. You will often see hexadecimal
color prepended with a `#` sign as `#FF0000`.

Here are some common colors:

+ `#FF0000` Red (only the red channel)
+ `#00FF00` Green (only the green channel)
+ `#0000FF` Blue (only the blue channel)
+ `#000000` Black (all channels off)
+ `#FFFFFF` White (all channels on)
+ `#808080` Gray (all channels at half)

If you examine the color spectrum, the yellow wavelength is about halfway
between red and green. So how do we make a color halfway between the two? By
turning on those two channels. Your eyes cannot distinguish the difference
between a yellow light and an equal amount of red and green light. It should
come as no surprise that halfway betwen green and blue is a greenish-blue color
called cyan. But what if you mix blue and red? Your brain turns the linear
color spectrum into a circle and the mixture is called magenta.

+ `#FFFF00` Yellow
+ `#00FFFF` Cyan
+ `#FF00FF` Magenta

What about the other colors, such as orange? Orange isn't halfway between any
of the channels. However, it is halfway between red and yellow. To make orange,
we have to decrease the green channel so that the average is closer to red. How
about we cut the green in half? `#FF8000` = Orange.

At this point, you're probably asking yourself, "but what about all of that
stuff I learned in art class where red + green = brown?". Paints are not photon
emissions. You have to think about paint colors in the absorption spectrum. Red
pigment blocks the green and blue spectrums, allowing red to reflect.
Similarly, green pigment blocks the red and blue spectrums, allowing green to
reflect. When you mix pigments, you average the absorptive properties of the
two. So a mixture of red + green pigments completely block the blue spectrum
and allow about half of the red and green to reflect. What is a low amount of
red light plus a low amount of green light? If we were to express that in hex
it would look like `#808000`, which is a dark yellow, which is brown-ish.

You will find lists of official HTML color names in these files:

+ `MCB185/data/colors_basic.tsv`
+ `MCB185/data/colors_extended.tsv`

### Image Files ###

Now that you know how colors are encoded, you might be wondering how images and
photos are stored. There are many, many graphic file formats. In general, there
are 3 types of graphics files.

1. Pixel map
2. Vector graphics
3. Mixtures

A pixel map is a 2-dimensional field of colors. Screenshots and photos are
pixel maps. When you take a screenshot of your computer, the size of the screen
and the color of each pixel are stored.

A vector graphic format, such as SVG, stores mathematical descriptions of
shapes. So rather than storing the individual pixels of a circle, it stores the
mathematical representation of a circle. This can be a much more compact
representation of an image. The image also scales well and never looks
"pixelated". However, creating vector graphic images is usually more work for
the artist than a pixel map.

Some file formats, like PDF, allow one to mix pixel maps and vector graphics
(in addition to formatted text).

Let's get back to pixel maps, since they are easy to understand. To make a
pixel-based image file, you only need 3 things:

1. The width of the image
2. The height of the image
3. A list of pixel colors that is width x height in number

A pixel map file is therefore a very simple format. We could even make up our
own file format. Let's call it Simple Pixmap. The start of the file will be
something distinguishing so that a program that reads it will not be confused
about its contents. We'll use `smplpxl` for this header info. Next, we need to
have some width and height. If we reserve 2 bytes for each, we have a maximum
image size of 65536 pixels in each dimension. That's pretty big, but we want to
be more future-proof, so we make it 4 bytes, which is about 4 billion in each
dimension. The first 16 bytes of the file are specified like this.

- 7 bytes: smplpxl
- 1 byte: not used, `00` by default
- 4 bytes width
- 4 bytes height

What comes next? All of the pixels. How many are there? Width times height.
Here is the complete image file for an image that is 3 pixels wide and 2 pixels
tall. The top row has 3 pixels: white, medium gray, and black. The second row
has 3 pixels: red, green, blue.

This is how it is logically constructed (show as hexadecimal).

- Header: `73 6d 70 6c 70 78 6c 00` = `smplpxl` followed by 00
- Width: `00 00 00 02` = 4-byte integer meaning 2
- Height: `00 00 00 02`= 4-byte integer meaning 2
- Pixels:
	- `FFFFFF` = white
	- `808080` = gray
	- `000000` = black
	- `FF0000` = red
	- `00FF00` = green
	- `0000FF` = blue


Here's how it would be stored in a file.

```
736d706c70786c000000000300000002FFFFFF808080000000FF000000FF000000FF
```

Here, spaces and annotation have been added for readability, but this is not
what is actually stored in the file.

```
736d706c70786c 00 00000003 00000002 FFFFFF 808080 000000 FF0000 00FF00 0000FF
s m p l p x l     width=3  height=2 white  gray   black  red    green  blue
```

The image file formats you use every day, like PNG, GIF, JPG, etc are all
similar to this. You might reflect on how big a screen capture file is. A
typical desktop computer has a 1920x1080 screen. That's about 2 million pixels.
Each pixel has 3 bytes of color. That's a total of about 6 megabytes. Note that
the E. coli genome is about 4.5 million bp. If you store E. coli sequence as
ASCII characters, that's 4.5 megabytes. A typical screen capture therefore
contains a little more data than a typical bacterial genome (note that both
colors and nucleotides can be compressed to reduce their size, but this is a
matter for another day).

## Floating Point Numbers ##

All of the encodings so far have been related to integers. What about numbers
like Pi or e? How does one encode something with a decimal point and
potentially with never-ending digits? The simple answer is "not precisely".

A "floating point" number has 3 components:

- A positive or negative sign
- An exponent, which may be negative or positive
- A significand, which is just a bunch of numbers

Floating point numbers are stored in a manner that is very similar to
scientific notation. We can describe Avogadro's number as 6.022x10^23. In
computer-speak we would write this as 6.022e23, where the `e` means exponent in
base 10. Here, the sign is positive, the exponent is 23 and the significand is
6022. Similarly, we would write the electonic charge of a single electron as
1.602e-19. Here the sign is positive, the exponent is negative, and the
significand is 1602. Both Avogadro's number and the charge of an electron have
more digits than the 4 digits of precision shown here. Floating point numbers
in a computer are similarly imprecise. As a simple example, the number 0.1
cannot be exactly represented in a computer (using the most common IEEE 754
encoding). The closest number to 0.1 is 1.00000000000000005551e-1. As a result,
some of the math performed by your computer is approximate and not exact.

The most common implementation of floating point, IEEE 754, has a maximum value
of approximately 1.79e308. Larger numbers result in "overflow" and get reported
as infinity. Similarly, the smallest positive number is about 1e-323. Going
closer to zero results in "underflow" which gets represented by zero. If you
have ever bounced on the multiply or divide key on a calculator and ended in
ERROR or 0, this will feel familiar.

## File Types ##

In order for a computer application to be able to correctly interpret a file,
it needs to know what kind of file it is. Is it plain text, MS Word, PDF, HTML,
SVG, GIF, PNG, JPG, etc? By convention, a file should have an extension, which
is typically 3 letters, but may be more or less. An extension is supposed to
uniquely identify a file type, but sometimes people make up their own
extensions. Here are some common extensions.

- .doc MS Word (legacy)
- .docx MS Word (current)
- .pdf portable document format
- .png portable network graphics
- .gif graphical image fille
- .html hypertext markup language (web pages)
- .exe executable program in MS Windows

Each file extension is often associated with an icon when using a graphical
user interface. A GUI often hides the extension so that a Word document will
look like a MS Word document called "CV" rather than the actual file name
"CV.docx".

What happens if a file has the wrong extension? If you double-click the file,
it will open up in the wrong application and result in an error.

What if a file doesn't have an extension? Many files in Linux do not have file
extensions. If they have "executable permissions" they are programs, not data
files. If a file does not have executable permission, it's probably a plain
text file. We'll see more about Linux programs and files later. The complete
list of file types used in this course are the following

- plain text files
	- `.txt` standard text file
	- `.md` Markdown text file
- text-based programming languages files
	- `.sh` shell script
	- `.py` python program
- text-based data files
	- `.csv` comma-separated values
	- `.tsv` tab-separated values
	- `.json` Javascript Object Notation
- text-based bioinformatics data files
	- `.fa`, `.fasta`, `.faa`, `.fna` are all fasta files
	- `.gff` general feature format
	- `.vcf` variant call format
	- `.gbff` GenBank flat file
	- `.transfac` Transfac file
- compressed files
	- `.gz` compressed with gzip

A compressed file has two extensions, one for the compression algorithm and one
for the original file type. For example, if you compress the C.elegans genome
with the `gzip` program, it might be in a compressed fasta file called
`C.elegans.fa.gz`.

## Hierarchical Organization ##

There are many ways to organize files on a computer.

- No organization: find by search
- Tagged: search by tag
- Application: found via application
- Hierarchy: organized in directories (folders)

Some people don't bother organizing their files: some files are in the
Downloads folder, some are in the Documents folder, and some are in unknown
locations. How does a person who doesn't organize their files find anything?
Using the search function of their computer. When looking for a file, they
might remember some part of the content such as the word 'vitae'. Finding files
by their contents can be an efficient way to find a specific file or it may
result in many files to look through. It depends on how you tailor the search.

A sligthly more organized method is to specifically tag files. For example, the
user might tag all files having to do with MCB185 with `#mcb185`. This allows
them to retrieve all files with any given tag. The downside of tagging is that
you have to remember to add tags. Some kinds of metadata don't need user
interaction, such as the last time the file was edited. Searching for files by
date is sort of like tagging in that you aren't looking through the file
itself, but rather metadata associated with a file.

On your phone or tablet, most files are organized by application. You find your
web pages in your browser application and your notes in your notes application.
This kind of organization is good for personal things, but not a good way to a
mixture of files that are part of a project.

Most scientific projects involve multiple files. There may be documents that
describe what was done, images from a microscope, source code for programs,
etc. While the files may all be very different from each other, they are all
related to the same project. Organizing by project involves putting the files
in the same folder (directory) and possibly creating additional folders
(subdirectories) for better internal organization. Project-based organization
is hierarchical.

Your computer's file system is organized hierarchically. Each operating system
has its own idea of how things should be organized, so Windwos, Mac, and Linux
are all organized a little differently from each other.

If you have not previously organized your files hierarchically, you will need
to start doing that. An organized computer environment is a requirement for
this course.
