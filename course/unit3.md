Unit 3: Practical Programming
=============================

30demo

## Files ##

Most data is stored in files. To read file data, you must open the file, stream
data from it, and close it when done. Here's the canonical structure for
reading a file line-by-line.

```python
fp = open(path)
for line in fp:
    do_something_with(line)
fp.close()
```

The `open()` function creates a new type of variable which is commonly called a
"file pointer" which is why the variable is abbreviated `fp`. If you use the
`type()` function you will see it has a much longer name: `_io.TextIOWrapper`.
The `open()` function takes a "path" argument, which is a relative or absolute
path to a file.

The `for` loop iterates through the file until there are no more lines to read.

The `do_something_with(line)` is a stand-in for whatever is going to happen
next.

The `fp.close()` statement closes the file. One common source of errors is
forgetting to close a file handle. This can result in some strange errors.
Python has an alternate block structure for reading files that uses the `with`
keyword.

```python
with open(path) as fp:
    for line in fp:
        do_something_with(line)
```

Note that there is no close operation. Files are automatically closed when
program execution goes beyond the `with` block. This second construction is the
one used most often.


### Compressed Files ###

Reading compressed files is really simple. We only need to make 2 changes to
the typical structure.

1. `import gzip`
2. change `open(path)` to `gzip.open(path, 'rt')`

This code snippet reads a compressed file and reports its contents to stdout.
This is effectively the same thing as `gunzip -c path` on the command line.

```python
import gzip
with gzip.open(path, 'rt') as fp:
    for line in fp:
        print(line, end='')
```

Because reading compressed files is so simple, there is no need to uncompress
any gzipped files.

## 31cdslength.py ##

Examine the GFF file describing the E. coli genes using the command below.

```
zless ~/Code/MCB185/data/GCF_000005845.2_ASM584v2_genomic.gff.gz
```

There are a few comment lines at the top of the file. The other lines describe
genes and other features. We examined this file with `cut` and `uniq` way back
in unit 1.

Create a program called `31cdslength.py` that reports the lengths of
protein-coding genes in the E. coli genome. The program will need to perform
the following tasks as it reads each line of the file.

1. Skip over comment lines
2. Find CDS features (or skip over all non-CDS features)
3. Extract the begin and end coordinates
4. Convert the coordinates to integers
5. Report the length of the CDS (end - begin + 1)

Type the following lines and observe how the code works. Delete it all and
re-write it from a blank page.

```python
import gzip
import sys

with gzip.open(sys.argv[1], 'rt') as fp:
    for line in fp:
        if line[0] != '#':
            words = line.split()
            if words[2] == 'CDS':
                beg = int(words[3])
                end = int(words[4])
                print(end - beg + 1)
```

### continue ###

The `continue` statement is used to immediately end the current iteration of
the loop and restart it with the next iteration. In some languages it is called
`next`. The code below does the exact same thing as the code above, however, it
is philosophically very different. The code below gets rid of the problem cases
(comments and lines without CDS) and then operates on what is left. The code
above selects specific lines to process.

```python
with gzip.open(sys.argv[1], 'rt') as fp:
    for line in fp:
        if line[0] == '#': continue
        words = line.split()
        if words[2] != 'CDS': continue
        beg = int(words[3])
        end = int(words[4])
        print(end - beg + 1)
```

Stylistically, the code that uses `continue` is preferred. Heavily nested code
is difficult to read.

------------------------------------------------------------------------------

## Reading FASTA Files ##

Sequences are often stored in FASTA format. A single sequence record has a
definition line (defline) followed by multiple lines of sequence. Here's an
example of a FASTA file.

```
>NP_414547.1 DNA binding and peroxide stress response protein YaaA
MLILISPAKTLDYQSPLTTTRYTLPELLDNSQQLIHEARKLTPPQISTLMRISDKLAGINAARFHDWQPDFTPANARQAI
LAFKGDVYTGLQAETFSEDDFDFAQQHLRMLSGLYGVLRPLDLMQPYRLEMGIRLENARGKDLYQFWGDIITNKLNEALA
AQGDNVVINLASDEYFKSVKPKKLNAEIIKPVFLDEKNGKFKIISFYAKKARGLMSRFIIENRLTKPEQLTGFNSEGYFF
DEDSSSNGELVFKRYEQR
```

The defline begins with `>` and is immediately followed by an identifier that
is usually a unique identifier for the sequence (NP_414547.1 is a unique
identifier at NCBI). The rest of the defline can have any descriptive
information.

This record has 4 sequence lines. There isn't any standard on how long each
sequence line is, but 60 and 80 characters is common. Some people put all of
their sequence on a single, long line.

Multi-FASTA files have more than one sequence record. Here's an example with
two. There is no way of knowing if a FASTA file has more than one record in it
until you read it.

```
>NP_414542.1 thr operon leader peptide
MKRISTTITTTITITTGNGAG
>NP_414565.1 DUF2575 domain-containing protein YaaY
MCRHSLRSDGAGFYQLAGCEYSFSAIKIAAGGQFLPVICAMAMKSHFFLISVLNRRLTLTAVQGILGRFSLF
```

### 32fasta.py and mcb185.py Library ###

Reading FASTA files is a little bit awkward because there is no end-of-record
delimiter. Records start with `>` but the end is either signaled by a new
record or the end of the file. To make our lives a little simpler, we're going
to import a FASTA file reader from the MCB185 repo.

Create `32fasta.py` and add the following to the top.

```python
import mcb185
```

If you try running your program, you will get a `ModuleNotFoundError`. Python
doesn't know where the `mcb185.py` library file is. There are several places it
looks, and one of those is your current directory. Make a soft link from
`MCB185/mcb185.py` to your homework directory so that it appears `mcb185.py` is
in your homework repo.

```
cd ~/Code/mcb185_homework
ln -s ~/Code/MCB185/src/mcb185.py .
```

Libraries are collections of reusable functions. We've used them in the past.
For example, `import math` gave us access to the math library and `math.log2()`
was one of the functions we called. You can make your own libraries for your
favorite functions (which we will do a little later).

### Stepping Through FASTA Files ###

Start your `32fasta.py` file like this:

```python
import sys
import mcb185

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    print(defline[:30], seq[:40], len(seq))
```

Run it like this.

```
python3 32fasta.py ../MCB185/data/A.thaliana.fa.gz
python3 32fasta.py ../MCB185/data/C.elegans.fa.gz
python3 32fasta.py ../MCB185/data/D.melanogaster.fa.gz
```

Each iteration of the `for` loop retrieves the next record from the FASTA file.
Each record is returned as a tuple containing the definition line and the
sequence (as a single string, not a bunch of lines). The function works with
both normal and compressed files. If you want to see how it works, there's
nothing stopping you from looking.

## Sequence Composition: 33ntcomp.py ##

Let's write a program `33ntcomp.py` that calculates the composition of
nucleotides in a FASTA file. This is a very simple modification of the previous
program. We will make several variations of this program. The first one
calculates the GC composition of each sequence separately.

### GC Composition ###

```python
1    import sys
2    import mcb185
3
4    for defline, seq in mcb185.read_fasta(sys.argv[1]):
5        defwords = defline.split()
6        name = defwords[0]
7        gc = 0
8        for nt in seq:
9            if nt == 'C' or nt == 'G': gc += 1
10       print(name, gc/len(seq))
```

### Individual Variables ###

If you were paying attention while running `32fasta.py` you would have noticed
that the A. thaliana file had a bunch of Ns in it. Let's modify the program so
that it counts 5 nucleotides (ACGTN), not just Cs and Gs. One way to solve this
problem is to create individual variables for each nucleotide and a stack of
if-elif-else statements that assigns them individually. Replace lines 7-10
above with the following:

```
7	A = 0
8	C = 0
9	G = 0
10	T = 0
11	N = 0
12	for nt in seq:
13	    if   nt == 'A': A += 1
15	    elif nt == 'C': C += 1
16	    elif nt == 'G': G += 1
17	    elif nt == 'T': T += 1
18	    else:           N += 1
19	print(name, A/len(seq), C/len(seq), G/len(seq), T/len(seq), N/len(seq))
```

### List Variation ###

A slight variation is to create a list to hold the counts. Here, line 7
initializes a list called `counts`. There is still a stack of if-elif-else, but
instead of assigning named variables, the assignments are at specific indices
of the list variable `counts`.

```python
7   counts = [0, 0, 0, 0, 0] # A, C, G, T, N
8   for nt in seq:
9       if   nt == 'A': counts[0] += 1
10      elif nt == 'C': counts[1] += 1
11      elif nt == 'G': counts[2] += 1
12      elif nt == 'T': counts[3] += 1
13      else:           counts[4] += 1
14  print(name, end=' ')
15  for n in counts: print(n/len(seq), end=' ')
16  print()
```

### Indexing with str.find() ###

The next variation of the code introduces a named string `nts` on line 7 that
contains the nucleotides to search for. You'll see why this is important later.

Line 8 shows a shortcut for assigning a bunch of zeroes.

The major change is to replace the if-elif-else stack with `str.find()`. Each
`nt` retrieved from the sequence is compared to the alphabet in `nts`. If the
letter is found, its index is returned. For example, if the letter is a 'G',
the index in 'ACGT' is 2 and the code does `counts[2] += 1` (line 9).
Conveniently, if there are any unknown letters, they get a -1 index, and get
dumped into the counts for 'N'. This is the exact behavior of the if-elif-else
stack in the previous code.

```python3
7   nts = 'ACGTN'
8   counts = [0] * len(nts)
9   for nt in seq:
10     idx = nts.find(nt)
11     counts[idx] += 1
12  print(name, end=' ')
13  for n in counts: print(n/len(seq), end=' ')
14  print()
```

### Counting any letter ###

If you want to count all letters, you have to make the alphabet container
mutable (e.g. a list).

Lines 7 and 8 create empty containers. These are initialized whenever a new
letter is seen (lines 11 and 12)

The rest of the code is similar except for the use of `list.index()` instead of
`str.find()`. The printing is a little different. Make sure to try this on the
A. thaliana genome sequence. You'll see that Chr2 is a little different from
the others.

```python
7   nts = []
8   counts = []
9   for nt in seq:
10       if nt not in nts:
11          nts.append(nt)
12          counts.append(0)
13      idx = nts.index(nt)
14      counts[idx] += 1
15  print(name)
16  for nt, n in zip(nts, counts):
17      print(nt, n, n/len(seq))
18  print()
```

### Counting with str.count() ###

The final variation, in this unit, is the use of `str.count()` to count
specific letters. Here, we iterate through the letters of the alphabet, getting
the counts for each one. For example, in the first iteration, the letter is
'A'. On line 9, we simply ask `seq` to count how many As it has.

```python
7   print(name, end=' ')
8   for nt in 'ACGTN':
9      print(seq.count(nt) / len(seq), end=' ')
10  print()
```

This solution is both tidy and efficient but you have to specify the alphabet
ahead of time, and what if the file has some letter you weren't expecting?

## Central Dogma ##

Given that this is a programming class for biologists, we should probably make
some typical sequence metabolism functions that do things like transcription,
reverse-complement, and translation. We'll end up using these functions
multiple times, so it's time to create your first library.

### sequence.py ###

Create a file called `sequence.py` in your homework repo.

### Transcription ###

Transcription converts 'T' to 'U'. The `str.replace()` method searches for
substrings and converts those to other substrings. Recall that strings are
immutable, so the original string isn't modified. `str.replace()` returns a
modified copy. Put this function in `sequence.py`.

```python
def transcribe(dna):
	return dna.replace('T', 'U')
```

### Reverse-Complement ###

When working with DNA, we often need to work with the reverse-complement
strand. Let's make a function that does that and add it to our library.

```python
1   def revcomp(dna):
2       rc = []
3       for nt in dna[::-1]:
4           if   nt == 'A': rc.append('T')
5           elif nt == 'C': rc.append('G')
6           elif nt == 'G': rc.append('C')
7           elif nt == 'T': rc.append('A')
8           else:           rc.append('N')
9       return ''.join(rc)
```

Line 2 creates a list `rc` to hold the new sequence. At the end, the function
will return a string version of this list with `str.join()` (line 9).

Line 3 steps backwards through the sequence using slice syntax.

Lines 4-8 do the complementing. Note that any letters that are not ACGT get
converted to N, which isn't the best behavior. If you want to see a more
thorough and confusing version, see `mcb185.anti_seq()`.

### test_sequence.py ###

In order to test the functions in our library, we need a program that imports
the library and calls its functions. Create a file called `test_sequence.py`

```python
import sequence

print(sequence.transcribe('ACGT'))
print(sequence.revcomp('AAAACGT'))
```

Most software engineers create "unit tests" and "integration tests" that call
library functions with various arguments. These tests ensure that code works
properly, that unexpected input is handled correctly, and that new changes to
the code still provide the same output as the old code. We don't do any
automated testing in this class, but automated testing is standard in a
professional setting. It's sort of like wearing latex gloves in lab. If you're
not doing unit tests or you aren't wearing gloves, you're not being very
professional.

### Translation ###

Converting nucleotide sequences to proteins isn't as simple as transcription or
reverse-complement. First, we have to retrieve codons by stepping through the
nucleotide sequence 3 letters at a time. Then we have to convert codons to
amino acids. Let's write a minimal translation function in `sequence.py`. This
function only recognizes start and stop codons. Everything else gets converted
to 'X'.

```python
1   def translate(dna):
2       aas = []
3       for i in range(0, len(dna), 3):
4           codon = dna[i:i+3]
5           if   codon == 'ATG': aas.append('M')
6           elif codon == 'TAA': aas.append('*')
7           elif codon == 'TAG': aas.append('*')
8           elif codon == 'TGA': aas.append('*')
9           else:                aas.append('X')
10   return ''.join(aas)
```

Line 2 initializes an empty list for the amino acids. Each codon that is
translated will be append to this list.

Line 3 steps through indices by threes. The value of `i` will contain the
starting index of each codon.

Line 4 creates a codon, which is a 3-letter slice starting from the current
index of `i`.

Lines 5-9 do the actual translation. One way of performing the translation is
with a giant stack of if-elif-else statements. It's highly abbreviated here.

Line 10 returns the amino acid list as a string.

Let's put some test code in `test_sequence.py` that demonstrates the use of the
function.

```python
print(sequence.translate('ATGCCCTAA')) # should return MX*
```


Here's an alternative way to write the translation function:

```python
1   def translate(dna):
2       codons = ('ATG', 'TAA', 'TAG', 'TGA')
3       aminos = 'M***'
4       aas = []
5       for i in range(0, len(dna), 3):
6           codon = dna[i:i+3]
7           if codon in codons:
8               idx = codons.index(codon)
9               aa = aminos[idx]
10              aas.append(aa)
11          else:
12              aas.append('X')
13       return ''.join(aas)
```

Lines 2-3 create parallel containers that match up codons to amino acids.

Lines 7-12 do the translation. The strategy here is very similar the
letter-counting code that used `str.find()`. Lists and tuples don't have a
`find()` method, so we have to use `index()`. Unfortunately, this throws errors
if the codon isn't found. So first we ask if the codon is `in` the tuple, then
we ask for its position with `index()`. Once we have the position in `idx`, we
can retrieve the amino acid `aa` from the string as `aminos[idx]`. Finally, we
append `aa` to the growing protein.

Note that the `idx` and `aa` variables are only used once. They don't really
need to exist. Lines 8-10 could be written as a single line:

```python
aas.append(aminos[codons.index(codon)])
```

While this one-liner shows a bit more programming sophistication, it doesn't
make the code more readable or more efficient.

If you want a more complete version of translation, you can call
`mcb185.translate()`.

------------------------------------------------------------------------------

## Sliding Window Algorithms ##

The `translate()` function we just wrote was a specialized form of "sliding
window algorithm". The canonical form is shown below.

```python
1   w = 10
2   s = 1
3   for i in range(0, len(seq) -w +1, s):
4       subseq = seq[i:i+w]
```

Line 1 sets the size of the window. For translation, this is 3 because codons
have a length of 3.

Line 2 sets the step size. For translation, this is 3. That is, each codon is 3
nt apart. In many windowing algorithms, the step size is 1.

Line 3 moves the window along the sequence. The example shows the 3 argument
version of `range()`. The third argument `len(seq) -w +1` is critical to
prevent the window from running off the end of the sequence.

Line 4 creates a subsequence as a slice using the current offset `i` and the
window size `w`. For translation, the subsequence is a codon.

### 34skew.py ###

Let's write a program that uses a sliding window algorithm to compute GC
composition and GC-skew along the length of a sequence.

First, let's create the functions for `gc_comp()` and `gc_skew()`. These sound
like useful functions we might want to use again, so let's put them into
`sequence.py`. `gc_comp()` is so simple it's not worth discussing.

```python
def gc_comp(seq):
    return (seq.count('C') + seq.count('G')) / len(seq)
```

The only difficulty in `gc_skew()` is that it's possible for windows to have no
Gs or Cs in them.

```python
def gc_skew(seq):
    c = seq.count('C')
    g = seq.count('G')
    if c + g == 0: return 0
    return (g - c) / (g + c)
```

The calling goes in `test_sequence.py`.

```python
s = 'ACGTGGGGGGCATATG'
print(sequence.gc_comp(s))
print(sequence.gc_skew(s), sequence.gc_skew(sequence.revcomp(s)))
```

Now that we know those functions work, let's toss them into the canonical
windowing algorithm. Save this as `28skewer.py`.

```python
1   seq = 'ACGTACGTGGGGGACGTACGTCCCCC'
2   w = 10
3   for i in range(len(seq) -w +1):
4       s = seq[i:i+w]
5       print(i, sequence.gc_comp(s), sequence.gc_skew(s))
```

Line 1 is very important here. When writing, testing, and debugging code, make
the problem small enough that you can calculate it by hand. When given a
problem, such as "compute GC-skew in 1000 bp windows in the E.coli genome",
don't work with the genome until the code has been thoroughly tested on a tiny
subset. It's much easier to visualize and debug 50 letter than 4.5 million.

Line 5 calls the composition and skew functions you just added to your library.

One problem with `34skew.py` is that it is computationally inefficient. Each
window is counted and then forgotten. Imagine counting 1000 bp windows by hand.
Let's say you get 500 Gs and 500 Cs. How many Gs do you think the next window
will have? The answer is 499, 500, or 501. You're losing 1 nt on the left and
gaining a new nt on the right. The counts can't change by more than just those
2 letters. So why bother re-counting everything in the middle?

A much more efficient algorithm only counts the initial window. After that, it
"moves" the window by dropping off one nucleotide on the left and adding one on
the right.

Re-write `34skew.py` using the more efficient algorithm and then calculate
GC-skew and GC composition in 1000 nt windows in the E.coli genome.

For debugging purposes you might find it very useful to write the program
twice: once using the wasteful strategy and once using the faster algorithm.
When making performance optimizations it's easy to make mistakes. Having a
simpler solution helps debug the more difficult problem.

If you're so inclined, try timing the simple and fast algorithms with the
`time` program. Use various window sizes to see how much that affects compute
time. Your command line might look like the following. Here, it is assumed your
program takes 2 arguments: the window size (1000) and a soft-linked fasta file
(because the original name is so long).

```
time python3 34skew.py ecoli.fa.gz 1000
```

Here's what I get for the time difference between the slow and fast algorithms.
The slow algorithm scales linearly (with a minor Y offset). The fast algorithm
is not really affected by window size.

| Size | Slow | Fast |
|:----:|:----:|:----:|
|   10 | 4.27 | 3.50 |
|  100 | 5.35 | 3.61 |
| 1000 | 15.3 | 3.65 |
| 2000 | 26.3 | 3.81 |
| 3000 | 36.1 | 3.79 |
| 4000 | 47.7 | 3.71 |
| 5000 | 59.0 | 3.73 |

How do I know that both algorithms get the same answer? By using `diff` or
`sum` on their output, of course.

### 35transmembrane.py ###

Write a program that predicts which proteins in a proteome are transmembrane.
Transmembrane proteins are characterized by having:

+ a hydrophobic signal peptide near the N-terminus
+ other hydrophobic regions to cross the plasma membrane

Hydrophobicity can be measured in many ways. We'll use Kyte-Doolittle for its
historical importance.

https://en.wikipedia.org/wiki/Hydrophilicity_plot

+ signal peptide: 8 aa long, average KD >= 2.5, first 30 aa
+ transmembrane region: 11 aa long, average KD >= 2.0, after 30 aa

Both the signal peptide and the transmembrane regions are alpha-helices
Therefore, they do not contain proline.

For the E.coli proteome, your output should look something like this:

```
NP_414560.1 Na(+):H(+) antiporter NhaA [Escherichia coli str
NP_414568.1 lipoprotein signal peptidase [Escherichia coli s
NP_414582.1 L-carnitine:gamma-butyrobetaine antiporter [Esch
NP_414607.1 DedA family protein YabI [Escherichia coli str.
NP_414609.1 thiamine ABC transporter membrane subunit [Esche
NP_414653.1 protein AmpE [Escherichia coli str. K-12 substr.
NP_414666.1 quinoprotein glucose dehydrogenase [Escherichia
NP_414695.1 iron(III) hydroxamate ABC transporter membrane s
NP_414699.1 PF03458 family protein YadS [Escherichia coli st
NP_414717.2 CDP-diglyceride synthetase [Escherichia coli str
```

## Sets ##

A set is a mutable container, but all of the elements are unique and the
elements are not ordered.

```python
s = {'A', 'C', 'G'}
print(s)
```

Try running this multiple times. Did you notice the order of the elements isn't
the same each time? Did you notice the curly brackets that indicate the variable
is a set?

To add items to a set, use the `add()` method.

```python
s.add('T')
print(s)
```

Because it is a set, adding the same element doesn't do anything.

```python
s.add('A')
print(s)
```

Since it doesn't have order, the following code generates an error:

```python
print(s[2])
```

Right about now, you're probably thinking that sets are useless. However, they
are very efficient for looking things up. For large collections, looking up
items in a set can be thousands of times faster than a list.

## Dictionaries ##

A dictionary is like a list, but the indices are strings instead of numbers.

+ `list[0]` - `0` is a numeric index
+ `dict['hey']` - `'hey'` is a string index

Unlike lists, there is no `append()` for dictionaries. Each item in a
dictionary exists as a key:value pair. The key is the string in square brackets
('hey' above). The value is anything you can put in a variable.

An empty dictionary is created either with empty braces or the `dict()`
function.

```python
d = {}
d = dict()
```

To make a dictionary with predefined items, use curly braces and key:value
pairs as shown below.

```python
d = {'dog': 'woof', 'cat': 'meow'}
print(d)
```

Both dictionaries and sets are displayed with curly brackets. The difference is
that dictionaries are key:value pairs, whereas sets are just values. Like sets,
dictionaries are also very efficient for lookups.

To access items use square brackets.

```python
print(d['cat'])
```

To add new items to a dictionary, assign a new key:value pair.

```python
d['pig'] = 'oink'
print(d)
```

To change the value of an item, access it with its key.

```python
d['cat'] = 'mew'
print(d)
```

To delete an item, use `del`.

```python
del d['cat']
print(d)
```

If you try to access a key that doesn't exist, you get an error.

```python
print(d['rat'])
```

To check if a key exists, use the keyword `in` just as you would with a list or
a set.

```python
if 'dog' in d: print(d['dog'])
```

### Iteration ###

There are several ways to iterate through a dictionary. The standard `for` loop
iterates over the keys in the order in which they were created. To get to a
specific element, use the key as an index to the dictionary.

```python
for key in d: print(f'{key} says {d[key]}')
```

The most common way to iterate through a dictionary is with `dict.items()`.

```python
for k, v in d.items(): print(k, 'says', v)
```

Again, you should always unpack your tuples. Consider how awful the following
looks.

```python
for thing in d.items(): print(thing[0], thing[1])
```

If you want just the keys or just the values, Python has methods `dict.keys()`
and `dict.values()` that return iterable objects. If you want these as actual
lists, coerce them with `list()`.

```python
print(d.keys(), d.values(), list(d.values()))
```

------------------------------------------------------------------------------

## Lookup Tables ##

Dictionaries are tidy and efficient for looking up values from a table. In the
last unit, you had to write a function that computed the average hydrophobicity
for a peptide. There were several strategies.

The most labor-intensive way is to make a stack of conditionals. Don't add this
to your demo.

```python
def kd_cond(seq):
    kd = 0
    for aa in seq:
        if   aa == 'I': kd += 4.5
        elif aa == 'V': kd += 4.2
        elif aa == 'L': kd += 3.8
        elif aa == 'F': kd += 2.8
        elif aa == 'C': kd += 2.5
        elif aa == 'M': kd += 1.9
        elif aa == 'A': kd += 1.8
        elif aa == 'G': kd += -0.4
        elif aa == 'T': kd += -0.7
        elif aa == 'S': kd += -0.8
        elif aa == 'W': kd += -0.9
        elif aa == 'Y': kd += -1.3
        elif aa == 'P': kd += -1.6
        elif aa == 'H': kd += -3.2
        elif aa == 'E': kd += -3.5
        elif aa == 'Q': kd += -3.5
        elif aa == 'D': kd += -3.5
        elif aa == 'N': kd += -3.5
        elif aa == 'K': kd += -3.9
        elif aa == 'R': kd += -4.5
    return kd/len(seq)
```

Another way is to index parallel lists. While this is a lot less code than the
example above, it is basically the same linear search. Don't add this either.

```python
aas = 'IVLFCMAGTSWYPHEQDNKR'
kds = (4.5, 4.2, 3.8, 2.8, 2.5, 1.9, 1.8, -0.4, -0.7, -0.8, -0.9, -1.3,
    -1.6, -3.2, -3.5, -3.5, -3.5, -3.5, -3.9, -4.5, 0)

def kd_list(seq):
    kd = 0
    for aa in seq:
        idx = aas.find(aa)
        kd += kds[idx]
    return kd/len(seq)
```

The better way is to use a dictionary. The code is cleaner and runs faster
because dictionaries, like sets, are designed for fast lookups.

```python
kdtable = {
    'I':  4.5, 'V':  4.2, 'L':  3.8, 'F':  2.8, 'C':  2.5, 'M': 1.9, 'A': 1.8,
    'G': -0.4, 'T': -0.7, 'S': -0.8, 'W': -0.9, 'Y': -1.3, 'P':-1.6, 'H': -3.2,
    'E': -3.5, 'Q': -3.5, 'D': -3.5, 'N': -3.5, 'K': -3.9, 'R': -4.5
}

def kd_dict(seq):
    kd = 0
    for aa in seq: kd += kdtable[aa]
    return kd/len(seq)
```

------------------------------------------------------------------------------

## Categorical Data ##

Dictionaries aren't only for looking up previous information, but categorizing
new information.

### 36countgff.py ###

Remember way back in Unit 0 when we crafted a CLI to count all of the features
in a GFF?

```
gunzip -c ecoli.gff.gz | grep -v "^#" | cut -f 3 | sort | uniq -c | sort -nr
```

Let's do the equivalent in python. Start a new program called `37countgff.py`
and add the following lines.

```python
1   count = {}
2   with gzip.open(sys.argv[1], 'rt') as fp:
3       for line in fp:
4           if line.startswith('#'): continue
5           f = line.split()
6           feature = f[2]
7           if feature not in count: count[feature] = 0
8           count[feature] += 1
9   for f, n in count.items(): print(f, n)
```

Line 1 creates an empty dictionary that will eventually fill up with key:value
pairs where the key will be the feature type (e.g. 'gene') and the value will
be the number of times it has been seen.

Line 4 uses `line.startswith()` instead of `line[0]` to introduce this useful
function. There is also a `str.endswith()`.

Lines 5-6 retrieve the feature name from the line.

Line 7 is critical. If the feature type isn't in the dictionary, we must create
a key in the dictionary before we can start counting.

Line 8 does the counting under the assumption that the feature is already in
the table, which it must be due to Line 7.

Lines 9 reports the counts of each feature.

An alternative way of writing lines 7 and 8 is below.

```python
7           if feature not in count: count[feature] = 1
8           else:                    count[feature] += 1
```

### Composition, again ###

Previously, we saw several strategies for counting nucleotides in sequences.

1. Create named variables `A`, `C`, `G`, `T` and an if-elif-else stack
2. Create a single list, but still use an if-elif-else stack
3. Create parallel lists and use `str.find()` for indexing
4. Use `str.count()` on each nucleotide

Another way to count letters is with a dictionary. The strategy is identical to
the gff counting strategy.

```python
count = {}
for nt in seq:
    if nt not in count: count[nt] = 0
    count[nt] += 1
```

### Sorting ###

There are times when you want to sort a dictionary by keys or values. One way
to do this is to pipe your program output through Linux `sort`. The first line
below sorts the output by the feature name. The second line sorts the second
column `-k 2` numerically `-n`. The two options can be collapsed as `-nk2`. The
`k` must come after the `n` because it has an argument, so `-kn2` would not
work.

```
python3 36countgff.py ecoli.gff.gz | sort
python3 36countgff.py ecoli.gff.gz | sort -n -k 2
python3 36countgff.py ecoli.gff.gz | sort -nk2
```

But what if you want the sort to occur inside python? Sorting by keys is really
easy. The `sorted()` function sorts the keys of count.

```python
    for k in sorted(count): print(k, count[k])
```

Sorting by values is more complex. Consider the rest of this section as
optional content. For an in-depth explanation, see the following:
https://realpython.com/python-lambda

The `sorted()` function needs a list of things to sort. By default, this is the
keys. We want to sort items based on their values, so we have to send
`sorted()` the values of the items. Here's the code.

```python
    for k, v in sorted(count.items(), key=lambda item: item[1]):
        print(k, v)
```

Lambda functions are tiny anonymous functions. This lambda function reads the
tuple `item` and returns the second element `item[1]` as the return value. You
can use this exact same construct with `item[0]` and it will sort by keys
rather than values.

Probably the best way to understand lambda functions is to substitute a named
function that does the exact same thing. In the code below, `key=by_value`
calls the `by_value()` function on each tuple to get the _thing_ used for
sorting (in this case the value).

```python
def by_value(tuple):
    return tuple[1]

for k, v in sorted(count.items(), key=by_value):
    print(k, v)
```

------------------------------------------------------------------------------


## K-mers ##

K-mers are used in a variety of bioinformatics analyses. A k-mer is simply a
sequence of length k, where k is a small integer. The subsequences of sliding
window algorithms are k-mers. Individual nucleotides are k-mers of length 1.

### 37kmercount.py ###

To explore k-mers, let's make a new program: `37kmercount.py`. As the name
suggests, it will count kmers.

```python
1   k = int(sys.argv[2])
2   kcount = {}
3   for defline, seq in mcb185.read_fasta(sys.argv[1]):
4       for i in range(len(seq) -k +1):
5           kmer = seq[i:i+k]
6           if kmer not in kcount: kcount[kmer] = 0
7           kcount[kmer] += 1
8   for kmer, n in kcount.items(): print(kmer, n)
```

Line 1 sets up a command line parameter for the value of k.

Line 2 is the empty dictionary that will hold key:value pairs of k-mers and
their counts.

Line 3 should be very familiar by now.

Line 4 is the typical windowing algorithm.

Line 5 creates a variable whose name does an excellent job of describing its
contents.

Lines 6-7 set or increase the counts of each observed k-mer.

Line 8 is the output.

Run the program as follows:

```
python3 37kmercount.py ecoli.fa.gz 1
```

Try increasing the value for k on the command line. With each increase, you see
4 times as many k-mers. Well, until you get to 7. 4^7 is 16,384 but `wc` shows
there's only 16,383. One of the k-mers is missing.

```
python3 37kmercount.py ecoli.fa.gz 7 | wc
```

Which k-mer is missing? One way to find out is to generate all possible k-mers
and check them against the `kcount` dictionary. We'll use `itertools.product()`
to generate all possible kmers. Throw the following code in your demo if you
want to see it in action.

```python
import itertools
for nts in itertools.product('ACGT', repeat=2):
    print(nts)
```

Add the following to `37kmercount.py`.

```python
1   import itertools
2   for nts in itertools.product('ACGT', repeat=k):
3       kmer = ''.join(nts)
4       if kmer in kcount: print(kmer, kcount[kmer])
5       else:              print(kmer, 0)
```

Line 3 joins the tuple `nts` into a string so that we can use it to index our
dictionary. Any kmers that aren't found will be reported with 0 counts.

```
python3 37kmercount.py ecoli.fa.gz 7 | sort -nk2 | head
```

The k-mer 'GCCTAGG' doesn't exist in the E.coli genome (on the positive
strand). It does exist if you reverse-complement the genome.


------------------------------------------------------------------------------


## Argparse ##

"Real" Unix programs have a CLI that provides a "usage statement" and command
line options. To see the usage statement for `head` and many other commands,
follow it with the `--help` parameter.

```
head --help
```

A usage statement provides a brief synopsis of how to use the command. It
should state what the command does, and what options and arguments it takes.
Python provides this functionality in the `argparse` library.

### Positional Arguments ###

Let's create a program with a simple, but proper, CLI. Start a file called
`38dust.py` and type in the following:

```python
1   import argparse
2
3   parser = argparse.ArgumentParser(description='DNA entropy filter.')
4   parser.add_argument('file', type=str, help='name of fasta file')
5   parser.add_argument('size', type=int, help='window size')
6   parser.add_argument('entropy', type=float, help='entropy threshold')
7   arg = parser.parse_args()
8   print('dusting with', arg.file, arg.size, arg.entropy)
```

Line 1 imports the library.

Line 3 creates the argument parser object in a variable called `parser`.

Line 4 adds a "positional argument" for the path to a FASTA file.

Line 5 adds a positional argument for the window size and specifies that it is
an integer.

Line 6 adds a positional argument for the entropy threshold, which is a float.

Line 7 creates the `arg` object by harvesting the values on the command line
and assigning them to various properties. For example, `arg.file` contains the
path to the FASTA file. Similarly, `arg.size` is the window size and
`arg.entropy` is the entropy threshold.

Line 8 is just something that will print when we give the program the proper
number and type of arguments.

Try running the program `python3 38dust.py` and observe the usage statement.

```
usage: 39dust.py [-h] file size entropy
39dust.py: error: the following arguments are required: file, size, entropy
```

If you don't give the program any arguments, it responds with a brief usage
statement telling you what it requires, in this case an optional argument `-h`
and 3 required positional arguments: `file`, `size`, and `entropy`. To get more
information, type `python3 38dust.py -h`. Here, the `-h` stands for help and
the usage statement provides more detail, including the final line, which tells
you that you can also get to this message with a longer version: `--help`.

```
usage: 38dust.py [-h] file size entropy

DNA entropy filter.

positional arguments:
  file        name of fasta file
  size        window size
  entropy     entropy

options:
  -h, --help  show this help message and exit
```

Try running it with the correct number and types of values.

```
python3 38dust.py e.coli.fa.gz 20 1.4
```

### Named Arguments ###

The arguments for `file`, `size`, and `entropy` were all positional. That is,
there were in a strict order. In contrast, named arguments are optional and can
occur in any order. This is very much like python where the `print()` function
has positional arguments (the things you want printed) as well as optional
named arguments like `sep=` and `end='`.

```python
print('first', 'second')                       # positional only
print('first', 'second', sep='\t', end='\n')   # named
print('first', 'second', end='\n', sep='\t')   # named, different order
```

Let's change `size` and `entropy` to be named parameters. Like the `print()`
function in python, they will have default values and can appear in any order.

In the code below, `size` is now `--size` with `default=20`. Similarly.
`entropy` is now `--entropy` and `default=1.4`. Inside the program, they are
accessed exactly as before: `arg.size` and `arg.entropy`.

To advertise the default values in the usage statement use `%(default)`. This
is appended with `s`, `i` or `f` to indicate string, int or float. `.3f` is 3
digits of precision, using the same formatting as f-strings.

```python
parser = argparse.ArgumentParser(description='DNA entropy filter.')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('--size', type=int, default=20,
    help='window size [%(default)i]')
parser.add_argument('--entropy', type=float, default=1.4,
    help='entropy threshold [%(default).3f]')
arg = parser.parse_args()
print('dusting with', arg.file, arg.size, arg.entropy)
```

Try observing the new usage statement advertising the default parameters. Also
try overriding the defaults.

```
python3 38dust.py
python3 38dust.py e.coli.fa.gz
python3 38dust.py e.coli.fa.gz --size 15 --entropy 1.2
```

### Flags ###

Another typical option is a flag that turns on/off some behavior. Let's create
a flag so that the program can soft-mask sequences (use lowercase letters
instead of 'N'). Add the line with "lower" and modify the print to show the
value.

```python
parser = argparse.ArgumentParser(description='DNA entropy filter.')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('--size', type=int, default=20,
    help='window size [%(default)i]')
parser.add_argument('--entropy', type=float, default=1.4,
    help='entropy threshold [%(default).3f]')
parser.add_argument('--lower', action='store_true', help='soft mask')
arg = parser.parse_args()
print('dusting with', arg.file, arg.size, arg.entropy, arg.lower)
```

Try it.

```
python3 38dust.py e.coli.fa.gz
python3 38dust.py coli.fa.gz --lower
```

### Short and Long ###

Let's add one more convenience, which is the ability to use both short and long
argument names. So `--size` can be `-s` and `--entropy` can be `-e`. This is a
simple modification to the named arguments.

```python
parser.add_argument('-s', '--size', type=int, default=20,
    help='window size [%(default)i]')
parser.add_argument('-e', '--entropy', type=float, default=1.4,
    help='entropy threshold [%(default).3f]')
```

------------------------------------------------------------------------------


## Multiple Dimensions ##

Up to now, almost all of the data has been 1-dimensional. Strings, tuples,
lists, and dictionaries are all 1-dimensional. The first 2-dimensional thing
was `sys.argv`. You may not have recognized that. The following command shows
that `sys.argv` is a list with a single element: the name of your program, and
of course you can access that by indexing.

```python
print(sys.argv)
print(sys.argv[0])
```

What you might not have appreciated, is that you can access individual
characters with another set of brackets.

```python
print(sys.argv[0][3])
```

A list of strings is a 2-dimensional data structure. The strings are the first
dimension. The letters are the second. As soon as we put containers inside
other containers, you have a multi-dimensional data structure. The containers
don't even have to be the same type or "shape".

```python
d = [
    'hello',
    (3.14, 'pi'),
    [-1, 0, 1],
    {'year': 2000, 'month': 7}
]
print(d[0][4], d[1][0], d[2][2], d[3]['month'])
```

### Arrays and Matrices ###

The words 'array' and 'list' are sometimes used interchangeably. In some
languages, they mean the exact same thing. In Python they do not. We have been
working with lists since unit 3. But Python also defines arrays, which are
linear containers where all elements are the exact same type (e.g. int). Arrays
are constructed with the `array()` function. We aren't using arrays in this
course. One of the most popular Python libraries is 'numpy', which also defines
arrays as `numpy.array()`. We also aren't using numpy arrays.

Matrices are multi-dimensional arrays. Matrices are rectangular (each dimension
has the same number of elements) and like arrays, all values are of the same
type. Computationally, arrays and matrices are much more efficient than lists.
Once you start doing computationally-intensive tasks, 'numpy' and other
libraries will become very useful.

------------------------------------------------------------------------------

## Records ##

One of the most important data types is the list of dictionaries. Sometimes
this will be called a list of objects, list of structs, or list of records.

A record is a data type with various named _fields_. For example, a record for
a sequencing oligo might look like this:

```python
oligo = {
    'Name': 'SO116',
    'Length': 18,
    'Sequence': 'ATTTAGGTGACACTATAG',
    'Description': 'SP6 promoter sequencing primer'
}
```

A catalog is a list of records.

```python
catalog = []
catalog.append(oligo)
```

Lists of records can be very large, so we generally don't type them in. We
typically read them in from files. Examine `MCB185/data/primers.csv`, which has
some sequencing primers from a catalog. Here's how we read a CSV file into a
list of records.

```python
1   def read_catalog(filepath):
2       catalog = []
3       with open(filepath) as fp:
4           for line in fp:
5               if line.startswith('#'): continue
6               name, length, seq, desc = line.rstrip().split(',')
7               record = {
8                   'Name': name,
9                   'Length': length,
10                  'Sequence': seq,
11                  'Description': desc
12              }
13              catalog.append(record)
14      return catalog
```

Line 6 is a new construction. `str.rstrip()` removes characters from the
right-hand side of a string. In this case, without any parameters, it removes
the newline character(s). This works on both Unix (LF) and Windows (CRLF) line
endings. `line.rstrip()` returns a string. Instead of putting that string into
a named variable, we can split it immediately by calling `str.split()` to
retrieve a list from the comma-separated values on the line.

Lines 7-12 create the record. Note that you don't need to name a record before
appending it. Lines 7-13 could be replaced by the following (but should it?).

```python
catalog.append({'Name': name, 'Length': length, 'Sequence': seq, 'Description': desc})
```

Now that we have a function that reads a catalog, we can load it and access
its records.

```python
catalog = read_catalog('primers.csv')
for primer in catalog:
    print(primer['Name'], primer['Description'])
```

### Dicts of Lists ###

Previously, we counted k-mers in sequences. What if instead of counting them,
we wanted to know the location of each k-mer on the sequence? Here's what the
code looked like before. Take note of lines 4-5.

```python
1   kcount = {}
2   for i in range(len(seq) -k +1):
3       kmer = seq[i:i+k]
4       if kmer not in kcount: kcount[kmer] = 0
5       kcount[kmer] += 1
```

In order to record locations of k-mers, we need to turn the initialization of 0
into an initialization of an empty list. And then instead of counting k-mers,
we need to append their locations.

```python
1   seq = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGT'
2   k = 2
3   kloc = {}
4   for i in range(len(seq) -k +1):
5       kmer = seq[i:i+k]
6       if kmer not in kloc: kloc[kmer] = []
7       kloc[kmer].append(i)
8   print(kloc)
```

Line 6 associates a new empty list with each new dictionary key.

Line 7 appends the location `i` on the list called `kloc[kmer]`.

We didn't change much code, but the behavior is now very different. You could
use the k-mer counting code on huge genomes and it wouldn't end up using any
more memory than a tiny genome. However, if you're storing the locations of
every k-mer, the lists could grow large enough to crash your computer.

------------------------------------------------------------------------------

## Complex Data ##

The bread and butter of most data scientists are 2-dimensional structures we
call spreadsheets, dataframes, or tables. But some kinds of data don't fit
conveniently into 2 dimensions. Take a look at the GenBank file corresponding
to the E.coli genome.

```
zless ~/Code/MCB185/data/GCF_000005845.2_ASM584v2_genomic.gbff.gz
```

Some parts, like DEFINITION, look like simple key:value pairs. Other parts,
like REFERENCE contains a list of 19 papers. Each paper contains some key:value
pairs. In Python, we might make a data structure like the one below. It
contains a mixture of dictionaries and lists.

```python
{
    "locus": "NC_000913",
    "length": 4641652,
    "type": "DNA",
    "definition": "Escherichia coli str. K-12 substr. MG1655, complete...",
    "reference": [
        {
            "authors": "Riley,M., Abe,T., Arnaud,M.B., Berlyn,M.K...",
            "title": "Escherichia coli K-12: a cooperatively...",
            "journal": "Nucleic Acids Res. 34 (1), 1-9 (2006)",
            "pubmed": 16397293
        },
        {
            "authors": "Hayashi,K., Morooka,N., Yamamoto,Y., Fujita,K...",
            "title": "Highly accurate genome sequences of Escherichia...",
            "journal": "Mol. Syst. Biol. 2, 2006 (2006)",
            "pubmed": 16738553
        }
    ]
}
```

### JSON ###

Did you notice the sudden switch to double quotes? That's because the code
above is also compatible with the data exchange standard called JSON
(Javascript Object Notation). It's very similar to Python with some exceptions.

- Double-quotes only
- Boolean values are `true` and `false` (lower case instead of title case)
- Trailing commas are not allowed on the last element of a block
- There are no comments

Python provides the `json` library for reading and writing JSON. When working
with complex data structures, `json.dumps()` can be a useful way of examining
the structure.

```python
truc = {
    'animals': {'dog': 'woof', 'cat': 'meow', 'pig': 'oink'},
    'numbers': [1.09, 2.72, 3.14],
    'is_complete': False,
}
print(json.dumps(truc, indent=4))
```

------------------------------------------------------------------------------

## Regular Expressions ##

One of the oldest but still useful ways to analyze protein sequences are
PROSITE patterns. The rules specify exact and partial matches. Here are some
examples.

+ `R-G-D` means proteins with the peptide "RGD" in them
+ `X` means any amino acid
+ `[ST]-X-[RK]` means S or T followed by any amino acid, followed by R or K
+ `[ILV](3,5)` any mixture of 3 to 5 of these hydrophobic amino acids
+ `{P}` means not proline
+ `<M` means begins with methionine
+ `>W` means ends with tryptophan

If you're thinking to yourself that these rules sound a bit like `grep`, you
are correct. Both PROSITE and `grep` are regular grammars. `grep` stands for
"general regular expression parser". Python has a regular expression library,
`re`, that allows you to search, extract, and replace substrings with inexact
matching.

### 39prosite.py ###

Let's explore regular expressions in the context of PROSITE patterns. Start a
program `39prosite.py` and start stepping through E.coli proteins (in
MCB185/data of course). Print the names of any sequences matching the PROSITE
pattern "D-K-T-G-T". This is easily solved by dropping the dashes and searching
with `in`.

```python
for defline, seq in mcb185.read_fasta(sys.argv[1]):
    if 'DKTGT' in seq: print(defline)
```

The regular expression version isn't much different. `re.search()` takes two
arguments, a _pattern_ and a string. In this case, the pattern is "DKTGT" and
the string is the sequence.

```python
for defline, seq in mcb185.read_fasta(sys.argv[1]):
    if re.search('DKTGT', seq): print(defline)
```

`D-K-T-G-T` is a subset of a larger PROSITE pattern for P-type ATPases
phosphorylation site (PDOC00139). The full pattern is: `D-K-T-G-T-[LIVM]-[TI]`.
The character class `[LIVM]` means any one of leucine, isoleucine, valine, or
methionine. Similarly `[TI]` is a choice of two amino acids. We can't use `in`
to make a match to this fuzzy pattern, but we can with regex, which uses the
exact same syntax for the character classes we used back in Unit 1 with `grep`.

```python
for defline, seq in mcb185.read_fasta(sys.argv[1]):
    if re.search('DKTGT[LIVM][TI]', seq): print(defline)
```

Let's try a more complex pattern: `C-x(2,4)-C-x(3)-[LIVMFYWC]-x(8)-H-x(3,5)-H`.
This is the pattern for C2H2 zinc-finger proteins (PS00028). The `x` stands for
any amino acid while the number in parentheses stands for a range. `x(2,4)`
means 2 to 4 amino acids while `x(3)` means exactly 3.

In regular expressions, `.` means any symbol rather than `x`. Also, regex uses
curly braces for ranges rather than parentheses. Therefore `x(2,4)` becomes
`.{2,4}`.

```python
for defline, seq in mcb185.read_fasta(sys.argv[1]):
    if re.search('C.{2,4}C.{3}[LIVMFYWC].{8}H.{3,5}H', seq): print(defline)
```

Regular expressions can also extract the text they match. Each pair of
parentheses is called a match group. The example below has only one group,
which is the entire pattern.

```python
1   pat = '(C.{2,4}C.{3}[LIVMFYWC].{8}H.{3,5}H)'
2   for defline, seq in mcb185.read_fasta(sys.argv[1]):
3       m = re.search(pat, seq)
4       if m: print(m.group(1))
```

Line 1 abstracts the pattern into a variable. Imagine iterating through a list
of patterns in an outer loop.

Line 3 assigns the search to a variable. The variable will either have a value
of `None`, which is logically `False`, or it will contain a "match object". The
variable is named `m` as an abbreviation for "match".

Line 4 retrieves the matched substring if `m` has a value that can be
considered `True` (most things are `True` except `None`, `False`, 0, and empty
containers).

Ultimately, the pattern matches: "CHACEIACVMAHNDEQHVLSQHH".

Regular expressions are very powerful, and we have barely scratched the
surface. The Internet has a lot of good guides on regular expressions.

------------------------------------------------------------------------------

## Unit 3 Finalization ##

- `30demo.py`
- `31cdslength.py`
- `32fasta.py`
- `33ntcomp.py`
- `34skew.py`
- `35transmembrane.py`
- `36countgff.py`
- `37kmercount.py`
- `38dust.py`
- `39prosite.py`
