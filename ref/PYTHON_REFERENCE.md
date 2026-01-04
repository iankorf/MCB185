MCB185 Python Reference
=======================

This Python Reference contains a subset of the Python language used in MCB185.

## Table of Contents ##

+ [Style](#style)
+ [Comments](#comments)
+ [Print](#print)
+ [Variables](#variables)
+ [Math](#math)
+ [Strings](#strings)
+ [Exceptions](#exceptions)
+ [Lists](#lists)
+ [Slices](#slices)
+ [Conditionals](#conditionals)
+ [Loops](#loops)
+ [Functions](#functions)
+ [Random](#random)
+ [Files](#files)
+ [Dictionaries](#dictionaries)
+ [Regex](#regex)
+ [CLI](#cli)


## Style ##

Spacing Rules:

(1) Use a maximum line length of 79 characters (most of the time).

(2) Use 1 space around/after most operators, just like in English. But don't be
robotic about it, as sometimes it's clearer not to use spaces.

- Yes: "Hello, my name is Ian. What's your name?"
- No: "Hello,my name is Ian.What's your name?"
- No: "Hello, my name is  Ian .  What's your name?"
- Yes: `if a > b: a, b = b, a`
- No: `if a>b:a,b=b,a`
- Yes: `print('hello', end='')` there is no space around keyword `=`
- Yes: `c = (a**2 + b**2) ** 0.5` the interior looks better without spaces

(3) Use vertical spacing (blank lines) to separate logic, just as you would use
paragraph structure in English.

(4) Use spaces for lining up single `if-elif-else` type constructs.

```python
if   nt == 'A': comp = 'T'
elif nt == 'C': comp = 'G'
elif nt == 'G': comp = 'C'
elif nt == 'T': comp = 'A'
else:           sys.exit('unknown nucleotide', nt)
```

Naming Rules:

- Variable and function names are generally all lowercase
- Multi-word variables may use snake case, but not mixedCase

```python
widowsize   = 60  # yes
window_size = 60  # yes
windowSize  = 60  # no
```

Variables sometimes have very short names that implicitly describe their type.
It's okay for loop variables to have such short names, but for longer-lived
variables, you should use more descriptive names.

- `i`, `j`, `k`, and `n` are integers
- `f`, `x`, and `y`, are floating point numbers
- `p` and `q` are probabilities
- `a`, `b`, and `c` are often numbers: ax^2 + bx + c or a^2 + b^2 = c^2
- `c` by itself is a character
- `s` is a string
- `fp` is a file pointer

For biological sequences it's common to use these shorthands:

- `nt` and `aa` are single characters of nucleotides or amino acids
- `seq` is often used for a biological sequence
- `dna`, `rna`, `tx` are nucleotide strings
- `pro` and `pep` are protein/peptide strings

Use single quotes for strings rather than double quotes.

- `s = 'hello'` yes
- `s = "hello"` no

Lists are often plural versions of descriptive names. If the word is very long,
use an abbreviation. Using singluar and plural names allows for intuitive looop
constructs such as:

```python
for name in names: ...
```

- `probs` is a list of probabilities
- `params` is a list of parameters
- `seqs` is a list of sequences

Despite being containers, dictionaries are generally not plural. Sometimes
people use a `2` in a dictionary as it indicates key-value relationships. For
example, a dict that counts kmers might be called `kmer2count`. A better
alternative is to call it `kmercount` or `kmer_count`.

In general, variable names are nouns that describe the contents of the
variable, not the type. Similarly, function names should be verbs that describe
what the function does.

- `s = 'ACGT'` not as descriptive as `nts = 'ACGT'`
- `my_list` doesn't describe what the list contains
- `buttons` is an approrpiate name for a list of buttons
- `translate()` is better than `protein()` for converting nts to aas
- `optimize()` doesn't describe what is being optimized

## Comments ##

Comments should be used to describe intentions, not trivialities

- `a = 9.8 # set the value of a to 9.8` no, trivial
- `a = 9.8 # default gravity` yes

Multi-line comments using triple-quotes are useful in debugging for blocking
out large sections of code. When using triple-quotes, use double-quote `"`
rather than single quote `'` so that you don't interfere with normal strings
(which should be single quoted as described above).

## print() ##

In MCB185, we use f-strings only, and not the printf-style or str.format()
constructions found in older Python.

| Code                        | Output
|:----------------------------|:-----------------------------------------
| `print('hello')`            | "hello" followed by a newline to stdout
| `print(a, b)`               | values a and b, separated by a space
| `print(a, b, sep=',')`      | values a and b, separated by a comma
| `print(a, end='')`          | value of a, no newline at end
| `print(f'{a + b})`          | value of a + b interpolated in f-string
| `print(f'{a/b:.3f}')`       | value of a / b with 3 digits after .
| `print(f'{a/b:.3g}')`       | value of a / b in scientific notation
| `print(a, file=sys.stderr)` | print `a` to stderr rather than stdout


## Variables ##

In Python, variables are given a type as they are created. There is no way to
create a variable without a type, but once a variable has been created with one
type, it can be reassigned to another type.

```python
n = 1               # integer
f = 1.0             # floating point number
s = '1'             # string
v = None            # None
b = True            # Boolean
t = (1, 2)          # tuple
a = [1, 2]          # list
d = {'cat': 'meow'} # dictionary
fp = open(filename) # file pointer
```

The `type()` function returns the type of a variable.

| Type                          | Meaning
|:------------------------------|:---------------------------------
| `<class 'int'>`               | integer
| `<class 'float'>`             | number with a decimal point
| `<class 'str'>`               | string (text)
| `<class 'NoneType'>`          | a non-value useful for debugging
| `<class 'bool'>`              | Boolean (True or False)
| `<class 'tuple'>`             | a collection of fixed values
| `<class 'list'>`              | a collection of mutable values
| `<class 'dict'>`              | a dictionary of key, value pairs
| `<class '_io.TextIOWrapper'>` | file pointer

The `int()`, `float()`, and `str()` functions are useful to convert values from
one type to another.


## Math ##

Math operators work as you expect, except `=` is used for assignment not
equality. Unfamiliar operators include `//` for integer division and `%`
(modulo) for the remainder after integer division. Absolute value is provided
as the function `abs()`.

| Operator | Purpose           | Example
|:---------|:------------------|:--------------------------
| `=`      | assignment        | `a = 2`
| `+`      | addition          | `a = b + c`
| `-`      | subtraction       | `a = b - c`
| `*`      | multiplication    | `a = b * c`
| `/`      | division          | `a = b / c`
| `**`     | exponentiation    | `a = b ** c`
| `//`     | integer divide    | `a = 5 // 2 # 2`
| `%`      | remainder         | `a = 5 % 2  # 1`
| `()`     | precedence        | `c = (a**2 + b**2)**0.5`
| `+=`     | increment         | `a += 1`
| `-=`     | decrement         | `a -= 1`
| `*=`     | multiply & assign | `a *= 2`

Basic math functions include:

| Function              | Purpose
|:----------------------|:---------------------------------------------
| `abs(x)`              | absolute value of x
| `pow(x, y)`           | x to the power of y
| `round(x, ndigits=3)` | round off x to some number of digits after .

Comparison operators are unsurprising except that `==` is used for equality
(because `=` is used for assignment).

| Operator | Purpose           | Example
|:---------|:------------------|:----------------------
| `==`     | equality          | `if a == b:`
| `!=`     | inequality        | `if a != b:`
| `<`      | less than         | `if a < b:`
| `>`      | greater than      | `if a > b:`
| `<=`     | less or equal     | `if a <= b:`
| `>=`     | greater or equal  | `if a >= b:`

Constants from the `math` library include:

| Constant      | Meaning
|:--------------|:---------------------------
| `math.pi`     | 3.14159...
| `math.e`      | 2.71828...

Functions from the `math` library include:

| Function            | Purpose
|:--------------------|:---------------------------------------------
| `math.ceil(x)`      | round `x` up
| `math.floor(x)`     | round `x` down
| `math.log(x)`       | `x` in log base e
| `math.log2(x)`      | `x` in log base 2
| `math.log10(x)`     | `x` in log base 10
| `math.sqrt(x)`      | square root of `x`
| `math.pow(x, y)`    | `x` to the power of `y`
| `math.factorial(n)` | factorial of integer n
| `math.isclose(a, b)`| returns True if `a` is nearly identical to `b`


## Strings ##

Some of the familar mathematical operators are also used for text.

| Operator | Purpose           | Example
|:---------|:------------------|:------------------------
| `=`      | assignment        | `s = 'hello'`
| `+`      | concatenation     | `s = 'hello' + 'world'`
| `*`      | repetition        | `polyA = 'A' * 100`
| `\`      | special symbols   | `tab = '\t'`
| `in`     | membership        | `if 'GAATTC' in dna:`
| `[]`     | slice             | see Slices below

Comparison operators work just like their numeric counterparts except that
strings are compared by their ASCII values.

+ 'A' is less than 'B'
+ 'B' is less than 'a' (all capital letters are less than lowercase)
+ '1' is less than '10' (as 'a' is less than 'ace')
+ '2' is greater than '1000' (as 'b' is greater than 'ant')

A few useful character and string operations use function syntax:

| Function  | Purpose
|:----------|:---------------------------------------------
| `len(s)`  | get the length of a string
| `chr(n)`  | get the character whose ASCII value is `n`
| `ord(c)`  | get the ASCII value of the character `c`

Most string operations use method syntax `s.method()`.

| Method              | Purpose
|:--------------------|:------------------------------------------------
| `s.count(s1)`       | number of occurrences of `s1` in `s`
| `s.endswith(s1)`    | True if `s` ends with `s1`
| `s.startswith(s1)`  | True if `s` starts with `s1`
| `s.find(s1)`        | position of `s1` in `s` or -1 if not found
| `s.upper()`         | returns an uppercase copy of s
| `s.lower()`         | returns a lowercase copy of s
| `s.rstrip()`        | remove characters from the end, usually newline
| `s.upper()`         | uppercase version of s
| `s.lower()`         | lowercase version of s
| `s.rstrip()`        | strip characters from the right (spaces by default)
| `s.replace(a, b)`   | convert substring `a` to `b`
| `s.join(list)`      | join elements of `list` with `s` between
| `s.split(s1)`       | split `s` into a list of strings at every `s1`


## Exceptions ##

The current version of MCB185 does not cover this material.

There are times when programs run into illegal instructions or instructions
that lead to illegal values. For example, you cannot divide by zero. An attempt
to do so leads to a ZeroDivisionError.

```
n = 1/0
ZeroDivisionError: division by zero
```

A common source of errors occurs when converting strings to numbers. This
produces a ValueError.

```
f = float('1e-5o') # that's the letter o, not the numeral 0
ValueError: could not convert string to float: '1e-5o'
```

When errors like these occur, your progam exits and reports the error. But what
if you wanted the program to keep running and skip over the erroneous data?
This is where `try` and `except` come in. The `try` block is code that you want
to try running. The `except` block handles what to do in case of failure.

```
v = '1e-5o'
try:
	f = float(v)
except ValueError:
	print('error converting', v)
```


## Tuples & Lists ##

Tuples are created with parentheses. Lists are created with square brackets.
Tuples cannot be changed, but lists can. Both tuples and lists are indexed with
square brackets.

```python
tup = (1, 2, 'cat', 'dog')
lis = [1, 2, 'cat', 'dog']
print(tup[2]) # cat
print(lis[3]) # dog
```

Some useful list/tuple operations use function syntax:

| Function            | Purpose
|:--------------------|:--------------------------------------------------
| `len(list)`         | get the length of a list
| `min(list)`         | get the minimum value (illegal to use in class)
| `max(list)`         | get the maximum value (illegal to use in class)
| `sum(list)`         | get the sum of all values (illegal to use in class)
| `sorted(list)`      | return a copy of the sorted list (or tuple)
| `enumerate(list)`   | iterates through tuples of index and item
| `zip(list1, list2)` | simultaneously iterate through multiple lists
| `list(string)`      | returns an array of single characters
| `list(dict)`        | returns the keys as a list
| `list(dict.keys())` | as above

Most list operations use method syntax `list.method()`.

| Method              | Purpose
|:--------------------|:------------------------------------------------
| `list.append(a)`    | add `a` to the end of a list
| `v = list.pop()`    | remove and return the last item
| `list.copy()`       | return a (shallow) copy of the list
| `list.count(a)`     | count the number of times `a` occurs in list
| `list.extend(v)`    | add list v to list
| `list.find(a)`      | return index of element matching a or -1 on fail
| `list.index(a)`     | return index of element matching a or an error
| `list.sort()`       | sort the list in place
| `list.reverse()`    | reverse the list in place

## Slices ##

Slice syntax is a succinct way to access individual elements or segments of a
string, list, or tuple.

| Example      | Value    | Explanation
|:-------------|:---------|:----------------------------------------------
| `s = abcdef` |          | example string
| `s[0]`       | 'a'      | first element
| `s[1]`       | 'b'      | second element
| `s[0:1]`     | 'a'      | slice from first, ending *before* second
| `s[0:2]`     | 'ab'     | slice from first, ending *before* third
| `s[:2]`      | 'ab'     | from implicit begin, ending before element 2
| `s[3:]`      | 'def'    | from position 3 to implicit end
| `s[:]`       | 'abcdef' | from implicit begin to implicit end
| `s[::-1]`    | 'fedcba' | from begin to end, backwards
| `s[::2]`     | 'ace'    | from begin to end by twos


## Conditionals ##

The standard conditional is the `if-elif-else` stack. The first expression that
evalutes to True is the only one that is executed.

```
x = 2
if   x < 5:       print('this will print')
elif x % 2 == 0:  print('this will not print because the one above did')
else:             print('this will also not print')
```

You can peform a one line if-else with a conditional expression.

```
x = 'even' if value % 2 == 0 else 'odd'
```

Python versions 3.10 and greater support the `match` statement.

```
match nt:
	case 'A': da = 491
	case 'C': da = 467
	case 'G': da = 507
	case 'T': da = 482
	case _: sys.exit('not a dNTP')
```

## Loops ##

| Statement                    | Meaning
|:-----------------------------|:--------------------------------------------
| `for i in range(3):`         | iterate 0, 1, 2
| `for i in range(0, 3):`      | iterate 0, 1, 2
| `for i in range(1, 3):`      | iterate 1, 2
| `for i in range(0, 7, 3):`   | iterate 0, 3, 6
| `for i in range(3, -1, -1):` | iterate 3, 2, 1, 0
| `for nt in dna:`             | for each nucleotide letter in a dna sequence
| `for n in numbers:`          | for each number in a list of numbers
| `for s in sys.argv[1:]`      | for each parameter on the command line
| `while True:`                | infinite loop
| `break`                      | exit the loop now
| `continue`                   | restart the loop now
| `for i, v in enumerate(t):`  | provide index and value for every item in `t`
| `for a, b in zip(t1, t2):`   | step through containers `t1` and `t2`

For `enumerate()`, `zip()` and related iterators, always unpack the tuple into
named variables.

```python
pets = ('cat', 'dot', 'rat')
for i, pet in enumerate((pets): # yes, unpack the tuple
	print(i, pet)
for thing in enumerate(pets):   # no, don't index it numerically
	print(thing[0], thing[1])
```


## Functions ##

Functions are created with the `def` keyword. Functions usually have
_positional_ arguments, meaning the arguments are in a specific order.
Functions may return multiple values. Here is a function with 3 positional
arguments that returns a tuple of 2 values.

```python
def quadratic(a, b, c):
	x1 = -b - math.sqrt(b**2 - 4*a*c) / 2*a
	x2 = -b + math.sqrt(b**2 - 4*a*c) / 2*a
	return x1, x2
```

Functions can have named parameters, which are placed after positional
arguments and may occur in any order. For example, a `translate()` function
might translate coding sequence in frame 0 by default, but can also translate
in other reading frames using an optional `frame` parameter.

```python
def translate(seq, frame=0):
	cds = ''
	for i in range(frame, len(seq) -2, 3):
		cds += seq[i:i+3]
	return cds
translate('ATGACG')    # implicitly use frame 0
translate('ATGACG', 1) # use frame 1
```

## Random ##

The random library is used to create random(-ish) numbers. If you want to
reproduce the same random numbers over and over (useful for debugging), set the
random seed to any integer value.

| Statement                | Meaning
|:-------------------------|:----------------------------------------
| `random.random()`        | a random variable from 0 almost 1
| `random.seed(i)`         | set the random seed
| `random.randint(a, b)`   | a random integer from a to b, inclusive
| `random.gauss(m, s)`     | random number with mean m, and stdev s
| `random.choice('ACGT')`  | a random letter: A, C, G, or T
| `random.shuffle(list)`   | randomize positions


## Files ##

Files are opened and closed as follows:

```python
fp = open(filename)
fp.close()
```

Files are automatically closed when using a `with open` construction. Here's
the preferred code to open a file, read it line-by-line, and automataically
close it:

```python
with open(filename) as fp:
	for line in fp:
		# do something with each line
```

To open a compressed file, use `gzip.open()` and include an additional argument
`rt` to read as text, as shown below.

```python
with gzip.open(filename, 'rt') as fp:
```


## Dictionaries ##

Dictionaries are created with curly brackets and indexed with square brackets.
Dictionaries consist of key:value pairs.

```python
d = {'cat': 'meow', 'dog': 'woof', 'rat': 'squeak'}
print(d['cat'])  # meow
```

The assignment operator `=` adds new elements to the dictionary. It also
overwrites previous values.

```python
d['pig'] = 'oink'  # new pair
d['cat'] = 'mew'   # overwrite previous value
```

To check if a key exists, use the `in` keyword.

```python
if 'cow' not in d: d['cow'] = 'moo'
```

To remove a key from a dictionary, use the `del` keyword.

```python
del d['cow']
```

There are several methods that are useful for looping over the keys or values
of a dictionary. The order of keys is the order in which they were created.

| Method              | Purpose
|:--------------------|:------------------------------------------------
| `d.items()`         | iterates key, value pairs
| `d.keys()`          | returns a list of keys
| `d.values()`        | returns a list of values


Use the `items()` method to iterate over a tuple of key/value pairs. A `for`
loop iterates over the keys of a dictionary. These 3 loops do the same thing.

```python
for k, v in d.items(): print(k, v)
for k in d.keys(): print(k, d[k])
for k in d: print(k, d[k])
```

Sometimes you want to sort a dictionary by keys and sometimes by values. The
syntax for this is a little arcane, using a lambda function.

```python
d = { ... }
for k, v in sorted(d.items(), key=lambda x: x[1]): ...
```


## Regex ##

Regular expressions can be used to search a string for a sub-string. You can
also do this with `in`.

```python
import re
s = 'abcdefghij'
if 'e' in s: print('found with in')
if re.search('e', s): print('found with regex')
```

The power of regular expressions is that they let you specify a _fuzzy_ pattern
and retrieve matches to that pattern. In the example below `\w+` indicates any
characters that make up words. The parentheses associate what was found into
group 1. If there was a second pair of parentheses, the contents would go into
group 2.

```python
m = re.search('e(\w+)i', s)
if m: print(m.group(1))     # prints fgh
```

Regex syntax is a little arcane. Here is a subset of the regex rules.

| Pattern    | Meaning
|:-----------|:---------------------------------------------------------
| `a`        | matches the letter 'a' but not 'A'
| `\w`       | matches any word symbol (letters, numbers, underscore)
| `\W`       | matches any non-word symbol
| `\d`       | matches any digit (0-9)
| `\D`       | matches any non-digit
| `.`        | matches anything
| `\.`       | matches an actual dot
| `\w+`      | matches 1 or more word symbols
| `\w*`      | matches 0 or more word symbols
| `[ab]`     | matches a or b
| `[^ab]`    | matches everything except a and b
| `[ab]+`    | matches a or b, 1 or more times
| `[a-d]`    | matches a, b, c, d
| `()`       | used for capturing matches into groups
| `\(`       | matches a left parenthese


## CLI ##

Values on the command line are in the `sys.argv` list. You could therefore
harvest parameters from the command line as follows:

```python
import sys
filename = sys.argv[1]
k = int(sys.argv[2])
h = float(sys.argv[3])
```

While you _can_ read values directly from `sys.argv`, it's better to use
`argparse`. This allows you to control input type, provide optional arguments,
and display a standard usage statement. See the `PYTHON_COOKBOOK.md` file for
more information.
