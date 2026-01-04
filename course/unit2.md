Unit 2: Learning to Program
===========================

## Strings  ##

Create a demo file for the unit, `20demo.py`,  where you can try out the
various code examples:

A string is a container that holds letters, numbers, punctuation, and other
symbols from your keyboard. A string is synonymous with text. Strings can be
assigned to variables.

```python
s = 'hello world'
print(s)
```

The common string delimiters are the single quote and double quote. You can
also use triple-quotes. But how do you put a quote inside a string if quotes
are used to delimit a string? One way is to put double quotes inside single
quotes or single quotes inside double quotes.

```python
s1 = 'hey "dude"'
s2 = "don't tell me what to do"
print(s1, s2)
```

Another strategy is to backslash the quote to tell python you aren't using it
as a delimiter.

```python
print('hey "dude" don\'t tell me what to do')
```

Backslashes are used to signify special characters. We already saw this once as
`\n` to mean a newline character. There are a variety of other special
characters, but the only other one we use in the class is `\t` which is used to
represent a horizontal tab.

### String Operators ###

Some of the familiar mathematical operators are also used for text.

| Operator | Purpose           | Example
|:---------|:------------------|:------------------------
| `=`      | assignment        | `s = 'hello'`
| `+`      | concatenation     | `s = 'hello' + 'world'`
| `*`      | repetition        | `polyA = 'A' * 100`
| `>`      | comparison        | `if s1 < s2`
| `<`      | comparison        | `if s1 > s2`
| `==`     | comparison        | `if s1 == s2`

Comparison operators work just like their numeric counterparts except that
strings are compared by their ASCII values.

- 'A' is less than 'B'
- 'B' is less than 'a' (all capital letters are less than lowercase)
- '1' is less than '10' (as 'a' is less than 'ace')
- '2' is greater than '1000' (as 'b' is greater than 'ant')

### String Functions ###

The `len()` function returns the length of a string (and other iterables, like
tuples and lists, described later in this unit). We saw the use of `chr()` and
`ord()` in the homework for unit 1.

| Function  | Purpose
|:----------|:---------------------------------------------
| `len(s)`  | get the length of a string
| `chr(n)`  | get the character whose ASCII value is `n`
| `ord(c)`  | get the ASCII value of the character `c`

### Method Syntax ###

All of the functions we have used so far have used "function syntax". Here, the
function name comes first, followed by parameters in parentheses. Most string
operations use "method syntax", where the variable comes first, then a dot,
then the name of the operation, and finally the parentheses.

```python
# don't put this in your 30demo.py
function(string)  # function syntax
string.method()    # method syntax
```

| Method              | Purpose
|:--------------------|:------------------------------------------------
| `s.count(s1)`       | number of occurrences of `s1` in `s`
| `s.endswith(s1)`    | True if `s` ends with `s1`
| `s.startswith(s1)`  | True if `s` starts with `s1`
| `s.upper()`         | uppercase version of s
| `s.lower()`         | lowercase version of s
| `s.rstrip()`        | strip characters from the right (spaces by default)
| `s.replace(a, b)`   | convert substring `a` to `b`

Let's try out some string methods.

```python
print(s.upper())
print(s)
```

Python strings are immutable. That means you can't change them. `s.upper()`
doesn't convert `s` to an uppercase string. It returns a new copy of `s` that
is all uppercase. See if you can figure out what is happening in the following
code.

```python
print(s.replace('o', ''))
print(s.replace('o', '').replace('r', 'i'))
```

### String Formatting ###

What if you want a bit more control over how strings appear, especially in
`print()` statements? For example, what if you only want to show a number with
3 digits of precision? What if you want to right-justify some text? It turns
out that Python provides a lot of power and flexibility in formatting.
Historically, Python has had 3 completely different syntaxes for string
formatting.

1. f-strings - the modern and best way
2. str.format() - an older method
3. printf-style - something that looks a bit like `printf()` from C

To create an f-string, you simply precede a string with a lowercase f. Inside
an f-string, anything in curly brackets is _interpolated_. The code inside
curly brackets is _live_: variables are expanded and functions are called.

Also inside the curly brackets are instructions for how to format the output.

- f for fixed point (default 6)
- e for exponent notation
- < ^ > for left, center, or right justify

Let's see some examples, that will make this arcane syntax more clear.


```python
print(f'{math.pi}')            # does nothing special
print(f'{math.pi:.3f}')        # 3 fixed digits after decimal
print(f'{1e6 * math.pi:e}')    # exponent notation
print(f'{"hello world":>20}')  # right justify with space filler
print(f'{"hello world":.>20}') # right justify with dot filler
print(f'{20:<10} {10}')        # left justify
```

You may see legacy formatting styles in older code. You should use f-strings in
new code, but for completeness, here are the other forms.

In the str.format() style, empty curly braces are filled with the parameters of
the `str.format()` parameters. in the example below, 'str.format' goes into the
first set of curly braces and pi goes into the second set, but with 3 digits of
precision.

```
print('{} {:.3f}'.format('str.format', math.pi))
```

In the printf-style, there is the similar idea that stuff on the right side is
filled in to stuff on the left side. The left side is a string. The right side
is a tuple. There is a "%" in the middle. "%s" means string and "%.3f" means 3
fixed digits of precision.

```python
print('%s %.3f' % ('printf', math.pi))
```

------------------------------------------------------------------------------

## Indexes ##

Each character in a string has an index, which is its position. `seq[0]` is the
first letter of the sequence (most computer languages start counting at 0
rather than 1). `seq[1]` is the second character.

```python
seq = 'GAATTC'
print(seq[0], seq[1])
```

Indexes can be negative, in which case they count backwards from the right,
starting at -1. So `seq[-1]` is the last character of a string.

```python
print(seq[-1])
```

You can iterate through the characters in a string using a `for` loop. If you
don't understand why the `end=''` is in the function and the blank `print()`,
try it with and without.

```python
for nt in seq:
    print(nt, end='')
print()
```

You can also iterate through the letters by their indices using the `range()`
function to generate the indices and `len()` to set the limit.

```python
for i in range(len(seq)):
    print(i, seq[i])
```

------------------------------------------------------------------------------

## Slices ##

A _slice_ is a subset of a container. The slice operator is a pair of square
brackets with a colon inside. Slices work a little like the `range()` function
in that they take an initial position and an end-before limit. The following
code prints the first 5 letters of the string. The `0` represents the initial
position, while the `5` is the end-before limit.

```python
s = 'ABCDEFGHIJ'
print(s[0:5])
```

Like the `range()` function, slices can also have a step size. When omitted,
the step size is assumed to be 1.

```python
print(s[0:8:2])
```

As a shortcut, you may omit either the initial value, which is replaced by 0,
or the final value, which is the length of the string.

```python
print(s[0:5], s[:5])        # both ABCDE
print(s[5:len(s)], s[5:])   # both FGHIJ
```

It may seem a little strange but `s[0]` is the same thing as `s[0:1]`. `s[0]`
indexes a single element. `s[0:1]` is a slice that starts at the zero-th
element and ends before element 1.

`s` is also equivalent to `s[0:len(s)]` and `s[::]`, which explicitly or
implicitly set the bounds of the slice to the whole string. While it is not
very surprising that `s[::1]` is also the same thing, your should definitely
take a long look at `s[::-1]`.

```python
print(s, s[::], s[::1], s[::-1])
```

We will see a lot more slicing next unit. But let's take a look at how easy it
is to slice a string into codons.

```python
dna = 'ATGCTGTAA'
for i in range(0, len(dna), 3):
    codon = dna[i:i+3]
    print(i, codon)
```

------------------------------------------------------------------------------

## Tuples ##

A tuple is container that holds multiple values. Tuples are generally
constructed with comma-separated values (usually in parentheses).

```python
tax = ('Homo', 'sapiens', 9606)  # construct tuple
print(tax)                       # note the parentheses in the output
```

Tuples and strings are immutable. That means you cannot change their contents
by poking at their indices. These two lines generate errors.

```python
s[0] = 'C'
tax[0] = 'human'
```

Tuples are linear containers of values, just like strings, and can be indexed
and sliced using the exact same syntax.

```python
print(tax[0])      # index
print(tax[::-1])   # slice
```

------------------------------------------------------------------------------

## enumerate() and zip() ##

### enumerate() ###

When stepping through containers, it's often useful to have both indices and
values. One way to do this is with the `range()` function.

```python
nts = 'ACGT'
for i in range(len(nts)):
    print(i, nts[i])
```

A tidier alternative is to have `enumerate()` provide you a tuple containing
the index and value in separate named variables.

```python
for i, nt in enumerate(nts):
    print(i, nt)
```

### zip() ###

When stepping through two containers in parallel, you can use `range()` to
simultaneously index separate containers.

```python
names = ('adenine', 'cytosine', 'guanine', 'thymine')
for i in range(len(names)):
    print(nts[i], names[i])
```

The tidier solution uses `zip()` to retrieve an element from each container and
return them to you in a tuple.

```python
for nt, name in zip(nts, names):
    print(nt, name)
```

You can even enumerate the zip as shown below. Here, you have to unpack the
tuples in series using additional parentheses.

```python
for i, (nt, name) in enumerate(zip(nts, names)):
    print(i, nt, name)
```

------------------------------------------------------------------------------

## Lists ##

Lists are similar to tuples except they are constructed with square brackets
and their contents are mutable.

```python
nts = ['A', 'T', 'C']
print(nts)
nts[2] = 'G'
print(nts)
```

Elements can be added to the end of a list with `list.append()`. Like strings,
most operations on lists use method syntax.

```python
nts.append('C')
print(nts)
```

Remove elements from the end of a list with `list.pop()`.

```python
last = nts.pop()
print(last)
```

Lists are sorted with `list.sort()`. Note that all of the elements in the list
must have similar types. You can sort a mixture of ints and floats, but you
cannot mix them with strings.

```python
nts.sort()
print(nts)
nts.sort(reverse=True)
print(nts)
```

If you assign a new variable to an existing list, it is not a copy, but another
name for the same list. In the example below, `nucleotides` is modified and the
modifications also occur in `nts` because both variable names correspond to the
same underlying data.

```python
nucleotides = nts
nucleotides.append('C')
nucleotides.sort()
print(nts, nucleotides)
```

To make a copy, use `list.copy()`. This is a "shallow" copy, meaning that
multi-dimensional lists and other complex data structures are not fully copied.
We don't make deep copies in this class. We also haven't talked about multiple
dimensions yet.

### list() ###

The `list()` function without arguments creates empty lists.

```python
items = list()
print(items)
items.append('eggs')
print(items)
```

You can also create empty lists with empty square brackets.

```python
stuff = []
stuff.append(3)
print(stuff)
```

The `list()` function coerces other "iterables" into lists. For example, it can
convert a string into a list of letters.

```python
alph = 'ACDEFGHIKLMPQRSVW'
print(alph)
aas = list(alph)
print(aas)
```

### split() and join() ###

The `str.split()` method splits strings into lists of strings. This is useful
for segmenting words. By default, the delimiter is any number of spaces.

```python
text = 'good day          to you'
words = text.split()
print(words)
```

For TSV or CSV data, split on `\t` or comma (as shown below).

```python
line = '1.41,2.72,3.14'
print(line.split(','))
```

Lists can be turned into strings by joining them with a delimiter. The
delimiter can be nothing. Here, the list is an argument to a method owned by
the delimiter string (which can be empty).

```python
s = '-'.join(aas)
print(s)
s = ''.join(aas)
print(s)
```

------------------------------------------------------------------------------

## Searching ##

To search for items in containers, you can use `in`, `find()`, and `index()`.

The keyword `in` reads particularly well in conditional statements.

```python
if 'A' in alph: print('yay')
if 'a' in alph: print('no')
```

The `index()` method returns the index of the first element it finds. If it
can't find a matching item, the function throws an error.

```python
print('index G?', alph.index('G'))
print('index Z?', alph.index('Z'))
```

The `find()` method returns the index of the first element it finds or a -1 if
it can't be found. This very useful behavior only works for strings, and not
tuples or lists.

```python
print('find G?', alph.find('G'))
print('find Z?', alph.find('Z'))
```

If you are searching a list or tuple, and you don't know if the element is
in the list, first use `in`.

```python
# don't put this in your 30demo.py, it's just an example
if thing in list: idx = list.index(thing)
```

------------------------------------------------------------------------------

## Practice Problems ##

Write a function that returns the minimum value of a list.

Write a function that returns both the minimum and maximum values of a list.

Write a function that returns the mean of the values in a list.

Write a function that computes the entropy of a probability distribution.

Write a function that computes the Kullback-Leibler distance between two sets
of probability distributions.

## Practice Solutions ##

### minimum() ###

The initialization on line 2 sets the minimum to the first value. If the list
is only 1 item long, this is the minimum. For longer lists, the minimum is
compared to every other value after the first `vals[1:]`. Whenever a value is
less than the current minimum (line 4) the minimum is reset `mini = val`.

```python
1   def minimum(vals):
2       mini = vals[0]
3       for val in vals[1:]:
4           if val < mini: mini = val
5       return mini
```

Note that python has built-in functions `min()`, `max()` and `sum()`.

### minmax() ###

This function is very similar to `minimum()` except that it has 2
initializations (lines 2-3) and 2 return values (line 7). The conditionals on
lines 5-6 could be formed as an `elif`.

```python
1   def minmax(vals):
2       mini = vals[0]
3       maxi = vals[0]
4       for val in vals:
5           if val < mini: mini = val
6           if val > maxi: maxi = val
7       return mini, maxi
```

An alternative way to write this function is to sort the values and then return
the first and last element. The sort method is more computationally expensive
and has a side-effect of re-ordering the list, which the caller might not want.

### mean() ###

Unlike the previous two functions, this one has a finalization step on line 4.
It is possible to write this without finalizing, with `total += val/len(vals)`,
but that increases the number of division calculations.

```python
1   def mean(vals):
2       total = 0
3       for val in vals: total += val
4       return total / len(vals)
```

### entropy() ###

This function should check that the probability distribution in `probs` sums up
to something close to 1.0. It will also run into numerical errors if any of the
values are 0. Can you write it better?

```python
1   def entropy(probs):
2       h = 0
3       for p in probs:
4           h -= p * math.log2(p)
5       return h
6   print(entropy([0.2, 0.3, 0.5]))
```

### dkl() ###

In this function, capital `P` and `Q` stand for probability distributions while
`p` and `q` represent individual values. This example follows more of a math
convention for naming variable (single letters) than software engineering
(descriptive names). Given the K-L is so commonly described by P and Q, using
the math convention is ok.

Note the use of `zip()` on line 3 that simultaneously retrieves probabilities
from `P` and `Q`. It is assumed that `P` and `Q` are containers with the same
length (and also that they sum up to 1 and don't have zeros or negative
numbers). Again, maybe you can improve the function?

Lines 6 and 7 create containers to hold the probability distributions. `p1` is
defined as a list while `p2` is defined as a tuple. That's okay because both
can be zipped in parallel.

```python
1   def dkl(P, Q):
2       d = 0
3       for p, q in zip(P, Q):
4           d += p * math.log2(p/q)
5       return d
6   p1 = [0.4, 0.3, 0.2, 0.1]
7   p2 = (0.1, 0.3, 0.4, 0.2)
8   print(dkl(p1, p2))
```

------------------------------------------------------------------------------

## External Data ##

All of the code examples so far have included the data in the program. Ideally,
programs can be given data from various sources, which might include user
input, a file, or even a network connection.

### input ###

The `input()` function allows python programs to get a line of input from the
user.

```
line = input('type something and hit return: ')
print('that line was', len(line), 'characters long')
```

You may have noticed that the variable `line` has one more character than you
see on screen. That's because `input()` stored the line ending.

We don't generally write interactive programs that ask users to provide input.
This is because biological data can be huge. It's much better to get data from
a file, which we will see shortly.

### sys.argv ###

The variable `sys.argv` is the complete list of words on the command line (argv
is short for argument vector). `sys.argv[0]` is the name of your program.
`sys.argv[1]` is the first argument, if there is one.

```python
import sys
print(sys.argv)
```

Try running your `20demo.py` with additional command line arguments.

```
python3 20demo.py 3.14 2.71
```

This results in the following output:

```
['mcb185_homework/30demo.py', '3.14', '2.71']
```

Things to note:

- There are square brackets because `sys.argv` is a list
- The numeric values have quotes around them because they are strings

### Converting Types ###

Data that you read from `input()`, `sys.argv`, and from files (see below) are
in the form of strings. You have to convert text representations of numbers to
ints and floats before you can do math with them. The `int()` and `float()`
functions do that.

```python
i = int('42')
x = float('0.61803')
print(i * x)
```

What happens if you try to convert something that doesn't look like a number
into a number? Try it.

```python
x = float('hello')
```

There are several ways to interact with error conditions in Python. We do not
go over `assert`, `try`, `except`, or `raise` in MCB185. If you run into an
error and want to provide a custom message, use `sys.exit()`.

### 21entropy.py ###

Create a new program called `21entropy.py`. This calculates the entropy for a
list of probabilities on the command line.

```python
1   import sys
2   import math
3
4   probs = []
5   for arg in sys.argv[1:]:
6       f = float(arg)
7       if f <= 0 or f >= 1: sys.exit('error: not a probability')
8       probs.append(float(arg))
9
10  total = 0
11  for p in probs: total += p
12  if not math.isclose(total, 1.0):
13      sys.exit('error: probs must sum to 1.0')
14
15  h = 0
16  for p in probs:
17      h -= p * math.log2(p)
18
19  print(f'{h:.4f}')
```

Lines 1-2 import the necessary libraries.

Lines 4-8 harvest words on the command line and turn them into probabilities.

Line 4 sets up a container to hold the probabilities used for the calculation.

Line 5 steps through each argument (word) on the command line, using a slice
`sys.argv[1:]` to skip over the first argument, which is the name of the
program.

Line 6 converts the argument into a floating point number.

Line 7 checks to see if the number is a valid probability. The numbers 0 and 1
are considered illegal in this context because values of 0 cause numerical
errors (log(0) and there is no point in calculating the entropy of a single
value of 1.0).

Line 8 adds each floating point number to the container of probabilities.

Line 9 is blank to separate the thoughts of the previous and next code blocks.

Lines 10-13 check if the sum of the probabilities on the command line are equal
to 1.0. Of course, we never ask if floating point values are actually equal to
anything, so we check if they sum nearly to 1.0.

Line 14 is blank to separate the previous sanity check from the calculation of
Shannon entropy.

Lines 15-17 calculate entropy.

Line 18 is again blank to separate calculation from reporting.

Line 19 reports the final value using an f-string.

Now try running it with various values, including those that create errors.

```
python3 21entropy.py 0.5 0.5
python3 21entropy.py 0.25 0.25 0.25 0.25
python3 21entropy.py 0.4 0.3 0.2 0.1
python3 21entropy.py 0.5 0.6
python3 21entropy.py 0.5 -1
```

Now that you understand how the program works, can you delete it and re-write
it again? You might have to write it from scratch during your assessment...

















------------------------------------------------------------------------------

## Pairwise Comparison ##

Given a list of things, a frequent operation is to compare all of the things to
each other. For example, given a list of cities, one might want to compare
their populations or distances from each other. Alternatively, given a list of
proteins, one might want to know which ones are related to each other. Or given
a list of amino acids, their alignment score when paired with each other.

There are 3 typical ways to perform all-vs-all comparisons.

+ all combinations
+ unique pairings allowing self-comparisons (half matrix with diagonal)
+ unique pairings disallowing self-comparisons (half matrix without diagonal)

Given letters A, C, G, T, there are 16 pairwise combinations: AA, AC, AG, AT,
CA, CC, CG, CT, GA, GC, GG, GT, TA, TC, TG, TT. Some of these might be
considered redundant: AC is the same as CA. However if the first letter is the
host for a dinner party and the second letter is a guest, then AC is different
from CA. But does it make sense to be both host and guest? In some cases yes,
but in others, no. This is why there are 3 ways we do pairings. Let's look at
these more graphically.

All combinations
```
  A B C D
A + + + +
B + + + +
C + + + +
D + + + +
```

Half-matrix with diagonal
```
Upper         Lower
  A B C D       A B C D
A + + + +     A +
B   + + +     B + +
C     + +     C + + +
D       +     D + + + +
```

Half-matrix without diagonal
```
Upper         Lower
  A B C D       A B C D
A   + + +     A
B     + +     B +
C       +     C + +
D             D + + +
```

It turns out to be very easy to program loops that make these comparisons. But
it can be a real head-scratcher until you see the answer. Let's just skip to
the answer.

```
for i in range(0, len(list)):
	for j in range(X, len(list)):
```

The variable X above is all you need to change to get the three different kinds
of pairwise comparisons.

- `X = 0`: all combinations
- `X = i`: half-matrix with diagonal
- `X = i+1`: half-matrix without diagonal

------------------------------------------------------------------------------

## Homework: 22stats.py ##

Write a program that reports descriptive stats for numbers on the command line.
Your program should report the following values:

- The number of values
- The minimum and maximum values
- The mean and standard deviation
- The median value

## Homework: 23birthday.py ##

You may have heard of the 'birthday paradox' before. Write a program that
simulates the problem by filling up classrooms of students with randomly chosen
birthdays. Make the number of days in the calendar and the number of people in
the classroom command line arguments. You will have to run this thousands of
times to get an accurate estimate, so have a parameter for the number of
trials.

https://en.wikipedia.org/wiki/Birthday_problem

In this program, you must use a list for the birthdays. For example, if there
are 23 people in the classroom, you will `list.append()` 23 times (unless
you're extra-clever and figure out how to make a short-circuit).

The first few lines of your program should look something like this:

```python
import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])
```

Your command line should look something like this.

```
python3 23birthday.py 10000 365 23
```

And the output should be a little over 50%.

Note that a birthday is simply a number from 0 to 364. You do not need to
generate a month and a day.

## Homework: 24birthday.py ##

This is the same problem as above, but instead of making a list of birthdays
(e.g. 23) make a list from the calendar (e.g. 365). In the previous program,
you appended birthdays to a list. In this one, all possible days are already in
a list, so assigning a birthday is: `calendar[birthday] += 1`.

Another way to think about this problem is to imagine you're throwing darts at
a calendar. A shared birthday is when 2 darts hit the same day.

## Homework: 25scoringmatrix.py ##

A scoring system for aligning nucleotide sequences is often described with 2
values: match and mismatch. For example, +1 for match, -1 for mismatch. Printed
out in a matrix, that would look like this:

```
   A  C  G  T
A +1 -1 -1 -1
C -1 +1 -1 -1
G -1 -1 +1 -1
T -1 -1 -1 -1
```

Write a program that can print out a match-mismatch scoring matrix. The
alphabet, match, and mismatch are all command line parameters. For example, the
command line for generating the matrix above would look like this:

```
python3 25scoringmatrix.py ACGT +1 -1
```

## Unit 2 Finalization ##

- `20demo.py`
- `21entropy.py`
- `22stats.py`
- `23birthday.py`
- `24birthday.py`
- `25scoringmatrix.py`
