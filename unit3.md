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


### 35skew.py ###

One problem with `34skew.py` is that it is computationally inefficient. Each
window is counted and then forgotten. Imagine counting 1000 bp windows by hand.
Let's say you get 500 Gs and 500 Cs. How many Gs do you think the next window
will have? The answer is 499, 500, or 501. You're losing 1 nt on the left and
gaining a new nt on the right. The counts can't change by more than just those
2 letters. So why bother re-counting everything in the middle?

A much more efficient algorithm only counts the initial window. After that, it
"moves" the window by dropping off one nucleotide on the left and adding one on
the right.

Re-write `34skew.py` as `35skew.py` using the more efficient algorithm and then
calculate GC-skew and GC composition in 1000 nt windows in the E.coli genome.

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
time python3 35skew.py ecoli.fa.gz 1000
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

### 36colorname.py ###

Write a program that provides the closest official color name given some red,
green, and blue values. For example, given the color values 200, 0, 50, your
program should report a shade of red. You will find color definitions in the
`colors_basic.tsv` and `colors_extended.tsv` in `MCB185/data`.

The first few lines of your program should look something like this.

```
import sys

colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])
```

Your commands should look something like this:

```
python3 36colorname.py ~/Code/MCB185/data/colors_extended.tsv 200 0 50
```

Hint: this algorithm is not very different from `minimum()` except that the
number you are trying to minimize is the difference between the input RGB
values and those of a named color. You will have to keep track of both the
minimum distance and the name of its corresponding color.

To calculate the distance between an input color and a named color, you can use
taxi-cab distance. This is very similar to `dkl()` except that the loop sums up
the absolute difference of each pair of values. It therefore doesn't assume
probabilities or have problems with zero values.

```
def dtc(P, Q):
	d = 0
	for p, q in zip(P, Q):
		d += abs(p - q)
	return d
```

Alternatively, you could use sum of squares, Euclidean distance (square root of
sum of squares), convert to probabilities and use `dkl()`, etc.

### 37dust.py ###

Prior to doing sequence searches, people often mask low complexity sequence to
prevent finding huge numbers of meaningless alignments. One of the common
programs that does this task is called `dust`. Write a python version.

+ Input: multi-FASTA file of DNA
+ Output: multi-FASTA file of DNA with low complexity regions masked
+ Change all low-complexity regions to 'N' in the output
+ Provide parameters for fasta file, window size, and entropy

Your command line should look like the one below, provided you soft-linked the
FASTA file and defined the window size as 20 and entropy threshold at 1.4.

```
python3 37dust.py ecoli.fa.gz 20 1.4
```

Your output should look like this provided you wrapped the lines at 60
characters (wrapping is like translation: it skips by the window size).

```
>NC_000913.3 Escherichia coli str. K-12 substr. MG1655, complete genome
AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTC
TGATAGCAGCTTCTGAACTGGTTACCTGCCGNNNNNNNNNNNNNNNNNNNNNNNCTTAGG
TCACTAAATACTTTAACCAATATAGGCATAGCGCACAGACAGATAAAAATTACAGAGTAC...
```

### 38cdsfinder.py ###

Write a program that finds open reading frames in the E. coli genome.

+ Input: multi-FASTA file of DNA
+ Output: multi-FASTA file of proteins
+ Must perform a six-frame translation
+ Proteins must be at least 100 amino acids long
+ Proteins must start with 'M' and end with '*'
+ Deflines must have unique identifiers

The command line should look something like this.

```
python3 38cdsfinder.py ecoli.fa.gz 100
```

The output should eventually look like this.

```
>NC_000913.3-prot-0
MRVLKFGGTSVANAERFLRVADILESNARQGQVATVLSAPAKITNHLVAMIEKTISGQDALPNISDAERIFAEL...
>NC_000913.3-prot-1
MKTASDCQQSKDSENNACHQRGKIKRKTQGAGNGVRLNSAENYAIGDEQKDGEQNAHPAHPQPARHIPCRSATK...
```

### 39transmembrane.py ###

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

## Unit 3 Finalization ##

- `30demo.py`
- `31cdslength.py`
- `32fasta.py`
- `33ntcomp.py`
- `34skew.py`
- `35skew.py`
- `36colorname.py`
- `37dust.py`
- `38cdsfinder.py`
- `39transmembrane.py`
