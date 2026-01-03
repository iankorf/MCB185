Exam #3 Questions
=================

- Most exam questions will be identical to those below
- Some exam questions will be variations of those below
- Some exam questions may be completely new

## 2D Loops

41. Write a program `print_matrix.py <alphabet> <plus> <minus>` that displays a
simple scoring matrix for matches and mismatches. The program must have the
alphabet and scores as command line arguments. Given the command line shown,
the output should match exactly.

```
python3 print_matrix.py ACGT +1 -1
   A  C  G  T
A +1 -1 -1 -1
C -1 +1 -1 -1
G -1 -1 +1 -1
T -1 -1 -1 +1
```

42. Write a program `triples.py <n>` that finds all Pythagorean Triples with
sides from 1 to `n` (e.g. 100). There should be no duplicates. For example,
3-4-5 is a Pythagorean Triple, but 4-3-5 is really the same thing and should
not be reported.

43. Write a program `birthday1.py <c> <n>` that simulates the birthday paradox
(the probability that two people in a classroom have the same birthday is > 50%
once the class size is 23 or more). Use a list for the people, not the
calendar. `c` and `n` represent the size of the calendar (e.g. 365) and number
of people (e.g. 23).

44. Write a program `birthday2.py <c> <n>` as before but use a list for the
calendar, not the people.

45. Write a function `polya(dna)` that returns the length of the longest
stretch of As in a dna sequence.

46. Write a program `char_count.py` that prints out the character count of each
character in a file. Invisible characters should be displayed by their ASCII
value rather than the character.

## Sequences

47. Write a function `read_fasta(file)` that reads a FASTA file and returns the
definition line and the sequence.

48. Write a program `gc_analysis.py <fasta> <window>` that computes the average
GC composition and GC skew of a sequence in windows. The two command line
arguments are file name and window size.

49. Write a program `dust.py <fasta> <window> <threshold>` that masks low
complexity DNA sequences, replacing low entropy regions with `N`. Command line
arguments include the file name, window size, and entropy threshold.

50. Write a function `read_fastas(file)` that reads sequences from a
multi-FASTA file, returning one at a time.

## Regex

51. Write a program `queen.py <string>` that solves the NYT Spelling Bee. The
command line argument is the 7 letters, starting with the central letter.

52. Write a program `prosite.py <pattern>` that allows users to search for
prosite patterns in a FASTA file.

## Sets and Dictionaries

53. Write a program `birthday3.py <c> <n>` as before, but use a set.

54. Write a better version of `jaccard.py <file1> <file2>` using sets.

55. Write a better version of `hydropathy(pro)` using a dictionary.

56. Write a better version of `translate(dna)` using a dictionary.

57. Write a function `kmer_count(seq, k)` that breaks up a sequence into kmers
and returns a dictionary of their counts.

58. Write a program `orfeome.py <size>` that estimates the rate of gene-sized
open reading frames per megabase of random sequence. You may assume the
existence of your `translate(dna)` function. The CLI should include the minimum
size of an ORF.

59. Write a program `transmembrane.py <fasta>` that predicts which proteins in
a proteome are embedded in the plasma membrane. Transmembrane proteins are
characterized by having a hydrophobic signal peptide near the N-terminus (first
30 aa) and another hydrophobic region (after 30 aa) to cross the plasma
membrane. Assume the signal peptide is 8 aa long and has average KD >= 2.5 The
transmembrane region is 11 aa long and KD >= 2.0. Neither region may have
prolines. You may assume the existence of your `hydropathy(pro)` function and a
dictionary of hydropathy values.

60. Write a function `read_transfac(file)` that reads a transfac file
describing a position weight matrix, and returns a data structure that indexes
position and nucleotide (e.g. `pwm[pos][nt]`).

------------------------------------------------------------------------------
