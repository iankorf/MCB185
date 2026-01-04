Exam #2 Questions
=================

- Most exam questions will be identical to those below
- Some exam questions will be variations of those below
- Some exam questions may be completely new

Rules:

- No imports are allowed unless explicitly stated

Variable naming conventions:

- `x` by itself can represent anything, but often a float
- `i`, `j`, `k`, and loop variables
- `n` and `m` are integers
- `a`, `b`, and `c` are numbers (sometimes ints, sometimes floats)
- `x`, `y`, and `z` are floats and often Cartesian coordinates
- `x1`, `y1` and `x2`, `y2` are Cartesian pairs
- `p` and `q` are probabilities
- `s` is a string, as are `s1` and `s2`
- `c` by itself is a character (e.g. `for c in s`)
- `strings` is a list of strings as are `strings1` and `strings2`
- `X` is a list of numbers, as are `X1` and `X2`
- `P` and `Q` are probability distributions (histograms)
- `nt` is a character representing a nucleotide
- `dna` is a string of nucleotide symbols
- `aa` is a character representing an amino acid
- `pro` is a string of amino acids
- `seq` is a string of nucleotides or amino acids
- `seqs` is a list of sequences
- `file` is a named file path
- `fp` is a file pointer

21. Write a function `gc_comp(dna)` that returns the GC composition of a
nucleotide sequence. Use the `input()` function  to ask the user for a sequence
and then report its GC composition.

22. Write a function `oligo_tm(dna)` that computes the melting temperature of a
DNA sequence. For oligos <= 13 nt, Tm = (A+T) x 2 + (G+C) x 4. For longer
oligos, Tm = 64.9 + 41 x (G+C -16.4) / (A+T+G+C). Use the `sys.argv` as the
source of the DNA sequence.

23. Write a program `crazycase.py <file>` that converts a file into aLtErNaTiNg
cAsE. Use `sys.argv` to get the file name.

24. Write a function `anti(nt)` that returns the reverse-complement of a DNA
sequence.

25. Write a function `entropy(P)` that returns the entropy of a probability
distribution. The function should check that `P` sums to 1 and report an error
if this is not the case.

26. Write a function `maxstr(strings)` that returns the string with the longest
length in a list of strings.

27. Write a function `minstrlen(strings)` that returns the length of the
shortest string in a list of strings.

28. Write a function `minmax(X)` that returns the minimum and maximum values
from a list of numbers. You may not use `max()`, `min()`, or list methods.

29. Write a function `stats(X)` that returns the mean, standard deviation, and
median for a list of numbers.

30. Write a program `colorname.py <file> <R> <G> <B>` that reports the closest
official HTML color name given some RGB values on the command line. Data is in
the `colors_extended.tsv` file.

31. Write a function `percent_id(s1, s2)` that computes the percent identity
between two strings of equal length (e.g. a pairwise sequence alignment).

32. Write a function `manhattan(X1, X2)` that computes the Manhattan distance
between two lists of numbers.

33. Write a function `dkl(P, Q)` that computes the Kullback-Leibler distance
between two histograms. You should check that P and Q are actually histograms
and you should do _something_ about values of zero.

34. Write a program `jaccard.py <file1> <file2>` that computes the Jaccard
Index (intersection divided by union) for 2 files of names. Create your own
file data to test your program.

35. Write a function `hydropathy(pro)` that computes the average Kyte-Doolitle
hydrophobicity of a protein sequence. Use the variables as defined below.

```
aas = 'ACDEFGHIKLMNPQRSTVWY'
kdh = (1.8, 2.5, -3.5, -3.5, 2.8, -0.4, -3.2, 4.5, -3.9, 3.8, 1.9, -3.5, -1.6,
	-3.5, -4.5, -0.8, -0.7, 4.2, -0.9, -1.3)
```

36. Write a function `translate(dna)` that translates a nucleotide sequence
into a protein sequence. If the codon is partial or has ambiguity symbols,
translate to X. Use the variables defined below. The variable `codons` is a
list of all possible codons `AAA`, `AAC`, `AAG`, `AAT`, `ACA`, ... `TTT` in
alphabetical order.

```
codons = [''.join(t) for t in itertools.product('ACGT', repeat=3)]
trans = 'KNKNTTTTRSRSIIMIQHQHPPPPRRRRLLLLEDEDAAAAGGGGVVVV*Y*YSSSS*CWCLFLF'
```

37. Write a program `monty-pi-thon.py` that estimates Pi by throwing random
darts at Cartesian quadrant 1. Let it run infinitely. For inspiration see
https://en.wikipedia.org/wiki/Monte_Carlo_method

38. Write a function `random_dna(n, X=[0.25, 0.25, 0.25, 0.25])` that returns a
random DNA sequence of length n. The optional named parameter `X` allows the
caller to specify weights for A, C, G, and T sequentially.

39. Write a function `random_subseq(seq, n, k)` that randomly samples a
sequence, returning a list of `n` sub-sequences of length `k`.

40. Write a function `mutate(dna, p)` that randomly mutates a DNA sequence
given some probability `p` of mutation.

------------------------------------------------------------------------------
