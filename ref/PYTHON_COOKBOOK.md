MCB185 Python Cookbook
======================

This cookbook is a collection of statements, functions, and programs that
illustrate how to perform biology-flavored programming tasks in Python. The
source code is written to be easy to understand rather than to be efficient or
bullet-proof.

## Contents ##

+ Simple solutions
	+ [Swapping 2 variables](#swapping-2-variables)
	+ [Editing a sequence](#editing-a-sequence)
+ Files
	+ [Reading a file of numbers](#reading-a-file-of-numbers)
	+ [Reading CSV and TSV](#reading-csv-and-tsv)
	+ [Reading a FASTA file](#reading-a-fasta-file)
	+ [Reading a multi-FASTA file](#reading-a-multi-fasta-file)
+ Sequences
	+ [Reversing a String](#reversing-a-string)
	+ [Generating Random Sequences](#generating-random-sequences)
	+ [Windowing Algorithms](#windowing-algorithms)
	+ [Calculating Hydropathy](#calculating-hydropathy)
	+ [Translating DNA](#translating-dna)
	+ [Counting K-mers](#counting-kmers)
	+ [Generating K-mers](#generating-kmers)
+ CLI
	+ [Simple CLI](#simple-cli)


## Swapping 2 variables ##

The classic way to swap 2 variables is to use a temporary variable. But in
Python, you can use tuples. The variables can even be different types.

```python
a = 1
b = 'two'
a, b = b, a
print(a, b)
```


## Editing a Sequence ##

Strings are immutable in Python. You can't make a _mutation_ in a sequence if
it's stored as a string. However, you can edit a list. To convert a string to a
list, use the `list()` function. Convert it back with `str.join()`.

```python
seq = list(string)
seq[5] = 'G'        # substitution
seq.pop(3)          # deletion
del seq[3]          # also deletion
seq.insert(1, 'A')  # insertion
seq = ''.join(seq)  # convert to string
```


## Reading a file of numbers ##

To read a file of numbers into a list, convert each number to a `float` and
then append it to a list.

```python
values = [] # empty list
with open(filename) as fp:
	for line in fp:
		values.append(float(line))
```

To make this a function, return the list.

```python
def read_numbers(filename):
	values = [] # empty list
	with open(filename) as fp:
		for line in fp:
			values.append(float(line))
	return values
```

To make this a generator, yield the list, one number at a time. Note that
generators are not part of the MCB185 curriculum.

```python
def read_numbers(filename):
	with open(filename) as fp:
		for line in fp:
			f = float(line)
			yield f

for f in read_numbers(filename): ...
```


## Reading CSV and TSV ##

To read a CSV (comma-separated values) file, split each line at the comma
character into its component columns.

```python
with open(filename) as fp:
	for line in fp:
		cols = line.split(',')
```

To read tab-separated files (TSV) change the comma to a tab.

```python
with open(filename) as fp:
	for line in fp:
		cols = line.split('\t')
```

To read space-separated files, use the default `split()`. This will segment on
any number of spaces including tabs.

```python
with open(filename) as fp:
	for line in fp:
		cols = line.split()
```

If some of the columns have numeric values, you must change them to `int` or
`float` appropriately. If you know exactly how many columns there are, you can
split the line into named variables rather than a list of unknown length. The
function below hands back a list of tuples.

```python
def read_people(filename):
	people = []
	with open(filename) as fp:
		for line in fp:
			name, age, salary = line.split()
			age = int(age)
			salary = float(salary)
			people.append( (name, age, salary) )
	return people
```

An alternative is to write this as a generator where each call to the function
retrieves the next person. The advantage of the generator is that you don't
need to keep all of the people in memory at the same time. Again, generators
are not currently part of MCB185.

```python
def read_people(filename):
	with open(filename) as fp:
		for line in fp:
			name, age, salary = line.split()
			age = int(age)
			salary = float(salary)
			yield name, age, salary

for name, age, salary in read_people(filename): ...
```

## Reading a FASTA file ##

To read a FASTA file into a string, remove the newlines and concatenate the
lines together.

```python
seq = '' # empty string
with open(filename) as fp:
	header = fp.readline() # read one line
	for line in fp:        # iterate through the remaining lines
		seq += line.rstrip()
```

## Reading a multi-FASTA file ##

Reading a multi-FASTA file is a little complicated. Use the code below, which
has some useful features. You will also find this in `MCB185/src/mcb185.py`.

+ It can read from compressed files or stdin
+ It uses `join` to prevent the CPU overhead of concatenation
+ It uses `yield` to reduce memory footprint to a single sequence

```python
import gzip
import sys
def read_fasta(filename):
	if   filename == '-':          fp = sys.stdin
	elif filename.endswith('.gz'): fp = gzip.open(filename, 'rt')
	else:                          fp = open(filename)
	name = None
	seqs = []
	while True:
		line = fp.readline()
		if line == '': break
		line = line.rstrip()
		if line.startswith('>'):
			if len(seqs) > 0:
				yield(name, ''.join(seqs))
				name = line[1:]
				seqs = []
			else:
				name = line[1:]
		else:
			seqs.append(line)

	yield(name, ''.join(seqs))
	fp.close()
```

To iterate over all of the sequences in a file, unpack the tuple in a for loop.

```python
for name, seq in read_fasta(filename): ...
```

## Reversing a String ##

The simplest way to reverse a string is to retrieve a slice in reverse step.

```python
rev = seq[::-1]
```

## Generating Random Sequences ##

To generate a sequence of DNA with equal probabilities of each letter, use
`random.choice()`.

```python
import random
s = ''
for i in range(100):
	s += random.choice('ACGT')
```

An alternative is to use `random.choices()` to generate a tuple of random
letters of length k (which you may want to `join()` into a string as shown).

```python
s = ''.join(random.choices('ACGT', k=100))
```

If you want sequences biased towards AT or GC, split the probability space. The
code below creates sequences that are 70%

```python
s = ''
for i in range(100):
	if random.random() < 0.7:
		if random.random() < 0.5: s += 'A'
		else:                     s += 'T'
	else:
		if random.random() < 0.5: s += 'C'
		else:                     s += 'G'
```

An alternative to the above is to use `random.choices()` with `weights` or
`cum_weights` and a value for `k` that is the length of the sequence.

```python
nts = 'ACGT'
ntp = (0.35, 0.15, 0.15, 0.35)
ntc = (0.35, 0.50, 0.65, 1.00)
s1 = ''.join(random.choices(nts, weights=ntp, k=100))
s2 = ''.join(random.choices(nts, cum_weights=ntc, k=100))
```

To shuffle the letters of a sequence, use `random.shuffle()`. Since strings are
immutable, you must first turn the sequence into a list.

```python
seq = '0123456789'
lseq = list(seq)
random.shuffle(lseq)
seq = ''.join(lseq)
```

## Windowing Algorithms ##

A windowing algorithm moves a window of fixed size along a sequence, doing
_something_ with each window.

```python
seq = ... # from somewhere
w = 10 # window size
for i in range(len(seq) - w + 1):
	win = seq[i:i+w]
	do_something(win)
```

Most windowing algorithms move the window in steps of 1 (as is done implicitly
above). However, sometimes you may want to skip by 3s for codons, in which case
you must use the 3 argument form of `range()`, which specifies the starting
index, the length, and the increment (e.g. 3).

```python
for i in range(0, len(seq), 3):
	codon = seq[i:i+3]
```

To get codons in a different frame, you would start with a different initial
value (e.g. 1 instead of 0).

```python
for i in range(1, len(seq), 3):
	codon = seq[i:i+3]
```

To print out a FASTA file with typical 60-character line lengths, you would
skip by 60.

```python
for i in range(0, len(seq), 60):
	print(seq[i:i+60])
```

Windowing algorithms can be sped up immensely by cacheing previous
calculations. For example, if you move the window over by 1 nt, the GC
composition doesn't change very much. The code for this is homework.


## Translating DNA ##

First, see [Windowing Algorithms](#windowing-algorithms).

Translate each codon using the dictionary below. Note that if a codon contains
an ambiguity code (e.g. `N`), it will not be in the dictionary, and you will
have to translate that codon as `X`. If your sequence contains lowercase
letters, you will need to change them.

```python
gcode = {
	'AAA' : 'K',	'AAC' : 'N',	'AAG' : 'K',	'AAT' : 'N',
	'ACA' : 'T',	'ACC' : 'T',	'ACG' : 'T',	'ACT' : 'T',
	'AGA' : 'R',	'AGC' : 'S',	'AGG' : 'R',	'AGT' : 'S',
	'ATA' : 'I',	'ATC' : 'I',	'ATG' : 'M',	'ATT' : 'I',
	'CAA' : 'Q',	'CAC' : 'H',	'CAG' : 'Q',	'CAT' : 'H',
	'CCA' : 'P',	'CCC' : 'P',	'CCG' : 'P',	'CCT' : 'P',
	'CGA' : 'R',	'CGC' : 'R',	'CGG' : 'R',	'CGT' : 'R',
	'CTA' : 'L',	'CTC' : 'L',	'CTG' : 'L',	'CTT' : 'L',
	'GAA' : 'E',	'GAC' : 'D',	'GAG' : 'E',	'GAT' : 'D',
	'GCA' : 'A',	'GCC' : 'A',	'GCG' : 'A',	'GCT' : 'A',
	'GGA' : 'G',	'GGC' : 'G',	'GGG' : 'G',	'GGT' : 'G',
	'GTA' : 'V',	'GTC' : 'V',	'GTG' : 'V',	'GTT' : 'V',
	'TAA' : '*',	'TAC' : 'Y',	'TAG' : '*',	'TAT' : 'Y',
	'TCA' : 'S',	'TCC' : 'S',	'TCG' : 'S',	'TCT' : 'S',
	'TGA' : '*',	'TGC' : 'C',	'TGG' : 'W',	'TGT' : 'C',
	'TTA' : 'L',	'TTC' : 'F',	'TTG' : 'L',	'TTT' : 'F',
}
def translate(seq):
	pro = []
	for i in range(0, len(seq), 3):
		codon = seq[i:i+3]
		if codon in gcode: aa = gcode[codon]
		else:              aa = 'X'
		pro.append(aa)
	return ''.join(pro)
```

## Calculating Hydropathy ##

First, see [Windowing Algorithms](#windowing-algorithms).

Use the dictionary below or write a stack of `if-elif-else` statements. Also
see the notes about unusual characters or lowercase in Translating DNA.

```python
kdh = {
	'I':  4.5, 'V':  4.2, 'L':  3.8, 'F':  2.8, 'C':  2.5,
	'M':  1.9, 'A':  1.8, 'G': -0.4, 'T': -0.7, 'S': -0.8,
	'W': -0.9, 'Y': -1.3, 'P': -1.6, 'H': -3.2, 'E': -3.5,
	'Q': -3.5, 'D': -3.5, 'K': -3.9, 'N': -3.5, 'R': -4.5,
}
def hydropathy(seq):
	s = 0
	for aa in seq:
		s += kdh[aa]
	return s / len(seq)
```

## Counting K-mers ##

First, see [Windowing Algorithms](#windowing-algorithms).

The first time you 'see' a k-mer, you must add it to the dictionary.
Afterwards, increase counts by one. If you want to pre-populate the dictionary
to include missing k-mers, see [Generating K-mers](#generating-kmers).

```python
seq = 'ACATGAGGATATATAT'
k = 3
kcount = {}
for i in range(len(seq) -k +1):
	kmer = seq[i:i+k]
	if kmer not in kcount: kcount[kmer] = 0
	kcount[kmer] += 1
```

## Generating K-mers ##

`itertools.product()` makes it simple to generate all possible k-mers. The
function generates tuples, so you might want to join them into a string as
shown below. Don't do this with large values of k or you will run out of
memory.

```python
import itertools
k = 3
kcount = {}
for kmers in itertools.product('ACGT', repeat=k):
	kcount[''.join(kmers)] = 0
print(kcount)
```

## Simple CLI  ##

Every program should have a usage statement that provides users with a brief
synopsis of what a program does and what parameters it takes. For example, here
is a simple CLI for the program `dust.py` that masks low complexity regions of
a sequence.

```python
import argparse

parser = argparse.ArgumentParser(description='DNA entropy filter.')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('size', type=int, help='window size')
parser.add_argument('threshold', type=float, help='threshold')
arg = parser.parse_args()
```

When you run the program without any arguments, it reports the following brief
message.

```
usage: dust.py [-h] [--lower] file size threshold
dust.py: error: the following arguments are required: file, size, threshold
```

To get more information about what the program does, run the program again with
`-h` or `--help`.

```
usage: dust.py [-h] [--lower] file size threshold

DNA entropy filter.

positional arguments:
  file        name of fasta file
  size        window size
  threshold   entropy threshold

optional arguments:
  -h, --help  show this help message and exit
```
