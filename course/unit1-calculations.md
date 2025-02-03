Unit 1: Calculations
====================

## Contents ##

+ [Hello, again](#hello-again)
+ [Comments and Whitespace](#comments-and-whitespace)
    + [Comments](#comments)
    + [Whitespace](#whitespace)
+ [Math](#math)
    + [Numbers](#numbers)
    + [Math Operators](#math-operators)
    + [Math Functions](#math-functions)
    + [Numbers Aren't Real](#numbers-arent-real)
+ [Variables](#variables)
    + [Assignment](#assignment)
    + [Type](#type)
+ [Functions](#functions)
    + [Block Structure](#block-structure)
+ [Practice](#practice)
+ [Strings](#strings)
+ [Conditionals](#conditionals)
    + [if](#if)
    + [Boolean](#boolean)
    + [Chaining](#chaining)
    + [Floating Point Warning](#floating-point-warning)
    + [Sting Comparison](#string-comparison)
    + [Mismatched Type Error](#mismatched-type-error)
    + [None Type](#none-type)
+ [More Practice](#more-practice)
+ [Style](#style)
    + [Spacing](#spacing)
    + [Naming](#naming)
+ [Even More Practice](#even-more-practice)
+ [Homework](#homework)
    + [11oligo.py](#11oligopy)
    + [12phred.py](#12phredpy)
+ [Assessment Example](#assessment-example)

------------------------------------------------------------------------------

## Hello, again ##

Create a new file called `10demo.py` and save it in your `mcb185_homework`
repo. `touch` the file into existence and then open it in your text editor
(e.g. FeatherPad, Notepad++, BBedit, etc.).

```
cd ~/Code/mcb185_homework
touch 10demo.py
```

We used the `print()` function in Unit 0 to output "hello world". Edit
`10demo.py` so that it prints out "hello, again". Save your work, then go to
your terminal and run the program.

```
python3 10demo.py
```

If you don't see the output "hello, again", stop now and get help.

------------------------------------------------------------------------------

## Comments and Whitespace ##

### Comments ###

The line you wrote with the `print()` function is called a _statement_.
Programs are made up of many statements, but not everything in a program is a
statement. Another important type of line is a "comment". Any line that begins
with `#` (pound, hash) symbol is a comment. Comments may also be used at the
end of a line, at which point, the rest of the line is a comment.

Modify your program with comments as shown below. It's a good idea to put a
comment in your programs with your name.

```python
# 10demo.py by your_name
print('hello, again') # greeting
```

Python also has multi-line comments. These begin and end with triple quotes.
Note that we generally use single quotes, like in `hello, again`, but for
multi-line comments we generally use double quotes.

```python
"""
This is a
multi-line
comment
"""
```

### Whitespace ###

Another important type of line is a blank line. Use blank lines to separate
different _thoughts_ much as you would use paragraphs to separate different
thoughts.

The comment with your program name and author name is like a header. It's very
different from the code that follows, and should have vertical spacing between
the code that follows. We call this vertical spacing "whitespace".

```python
# 10demo.py by your_name

print('hello, again') # greeting
```

Whitespace is also used to separate different tokens (words, symbols) in
statements to provide clarity. This is much like using spaces as part of
punctuation. Note how the lack of horizontal whitespace below impedes
readability.

```python
#10demo.pybyyourname
print('hello,again')#greetingformattedbadly
```

Clarity is much more important than saving keystrokes. Use vertical and
horizontal whitespace to improve clarity.

------------------------------------------------------------------------------

## Math ##

### Numbers ###

The values 1, 1.0, and '1' are all different in Python. 1 is an integer. 1.0 is
a floating point number, which means that it has a decimal, and '1' is text
with the numeral "1". You can do math with 1 and 1.0, but not '1'. Python
understands scientific notation. 1.5e-2 means 1.5 times 10 to the -2 power
(0.015).

Add the following line to `10demo.py`. We'll be adding a lot more lines to the
file as we go.

```python
print(1.5e-2)
```

### Math Operators ###

Python has the typical mathematical operators you're familiar with and uses
parentheses to force precedence. There are also some operators that you may not
have seen before. The `//` operator performs an integer division. That is, it
throws away the remainder. The `%` operator is called "modulo". It provides the
remainder after performing an integer division. Modulo will be very useful to
us later, as it is used to assign reading frame to DNA.

Try adding some `print()` statements to your demo program and observe the
output.

| Operator | Purpose           | Example             | Output
|:---------|:------------------|:--------------------|:------
| `+`      | addition          | `print(1 + 1)`      | 2
| `-`      | subtraction       | `print(1 - 1)`      | 0
| `*`      | multiplication    | `print(2 * 2)`      | 4
| `/`      | division          | `print(1 / 2)`      | 0.5
| `**`     | exponentiation    | `print(2 ** 3)`     | 8
| `//`     | integer divide    | `print(5 // 2)`     | 2
| `%`      | remainder         | `print(5 % 2)`      | 1
| `()`     | precedence        | `print(5 * (2 + 1))`| 15

### Math Functions ###

Some typical mathematical transformations are not provided with operators. You
might expect `|-1|` to produce the absolute value of -1, but it does not.
Absolute value is a function called `abs()`. There is also `pow()` and
`round()`.

| Function              | Purpose
|:----------------------|:---------------------------
| `abs(x)`              | absolute value of `x`
| `pow(x, y)`           | `x` to the power of `y`
| `round(x, ndigits=3)` | round off `x` to 3 digits

What about logarithms and such? Those are in the math library. In order to use
those functions you must `import math` in your code. Import statements usually
go at the top of your program. Try out some of the functions below.

| Function            | Purpose
|:--------------------|:-----------------------------
| `math.ceil(x)`      | round `x` up
| `math.floor(x)`     | round `x` down
| `math.log(x)`       | `x` in log base e
| `math.log2(x)`      | `x` in log base 2
| `math.log10(x)`     | `x` in log base 10
| `math.sqrt(x)`      | square root of `x`
| `math.pow(x, y)`    | `x` to the power of `y`
| `math.factorial(n)` | factorial of integer n

The math library also defines some useful constants.

+ `math.e`:  2.71828...
+ `math.pi`: 3.14159...
+ `math.inf`: infinity
+ `math.nan`: not a number (e.g. 0/0)

Here's what my demo program looks like. Notice that there are multiple ways to
do powers and roots.

```python
# 10demo.py by Ian Korf

import math

print('hello, again')
print(1.5e-2)
print(1 + 1)
print(2**3)
print(pow(2, 3))
print(math.pow(2, 3))
print(2**0.5)
print(math.sqrt(2))
print(math.log(2))
#print(1 / 0)           # divide by zero error
#print(math.log(0))     # math domain error
#print(math.sqrt(-1))   # math domain error
```

### Numbers Aren't Real ###

Numbers inside your computer aren't exactly what you think they are. While
integers (ints) have exact values, floating point numbers (floats) are
approximations with finite precision. For example, the value 0.1 isn't exactly
equal to 0.1.

```python
print(0.1 * 1)
print(0.1 * 3)
```

Why is `0.1 * 3` equal to 0.30000000000000004? Because the number 0.1 can't be
represented exactly by the IEEE754 standard for storing 8-byte floats. Python
sometimes hides the imprecision from you and shows you 0.1 instead of its
actual value: 0.100000001490116119384765625.

------------------------------------------------------------------------------

## Variables ##

### Assignment ###

We don't usually do math inside `print()` statements. We usually store numbers
inside variables and do math with the variables. The `=` sign is used to assign
numbers (and other types of values).

The code below computes the hypotenuse `c` given sides `a` and `b`.

```python
a = 3                       # side of triangle
b = 4                       # side of triangle
c = math.sqrt(a**2 + b**2)  # hypotenuse
print(c)
```

Note the use of comments to explain the intent of the variables. This is
generally not necessary if you use descriptive variable names. Take note of how
neat the code looks with all of the comments aligned vertically. Also note the
use of `a**2` rather than `a ** 2`. There are some cases where not using spaces
is neater than using spaces, for example with unary operators like `-` and `**`
that work on a single number rather than two numbers.

### Type ###

When variables are created, they always have a type. In the code above, `a` and
`b` are both ints because their numerical values don't have decimals. The
`math.sqrt()` function creates floats. Consequently, `c` is a float. To see the
type of a variable, use the `type()` function.

```python
print(type(a), type(b), type(c))
```

This is the first place we have used the `print()` function with multiple
arguments. When given multiple things to display, the function puts spaces
between the values. You can change the separator from a space to anything else.
For example, let's change the separator to a comma followed by a space using
the optional `sep=` syntax, and the `end=` to create a custom ending.

```python
print(type(a), type(b), type(c), sep=', ', end='!\n')
```

The `\n` in the line above means "newline". This creates vertical space. If you
don't use that, the cursor in the terminal will stay on the previous line. The
default behavior is `print(sep=' ', end='\n')`.

------------------------------------------------------------------------------

## Functions ##

Functions are reusable code constructs that form the backbone of computer
programs. Functions are created with the `def` keyword, followed by the unique
name of the function. A set of parentheses after the function name specifies
the inputs. A `return` statement is used to terminate the function. Let's make
the calculation of the hypotenuse into a reusable function.

```python
def pythagoras(a, b):
	c = math.sqrt(a**2 + b**2)
	return c
```

The variables `a` and `b` are the "parameters" of the function. The calculation
is stored in variable `c`, which is then sent back to the "caller". Let's see
this in action.

```python
hyp = pythagoras(3, 4)
print(hyp)
```

This could all have been simplified a little. There is no reason to create the
variable `c`.

```python
def pythagoras(a, b):
	return math.sqrt(a**2 + b**2)
```

There was also no need to create the variable `hyp`.

```python
print(pythagoras(3, 4))
```

### Block Structure ###

Functions, and other structures we will use later in the class, have "block
structure". Blocks show hierarchy. All of the code "owned" by the function is
indented one level. Block structure is very much like a hierarchical outline
or the document structure for a journal article.

```
I. Introduction
	A. Review of literature
	B. Statement of problem
	C. Brief synopsis
II. Methods
	A. Data sources
	B. Procedures
III. Results
	A. Experiment 1
		a. Table
	B. Experiment 2
		a. Figure 1
		b. Figure 2
IV. Discussion
```

If there is only 1 statement in a block, you may omit the indentation.

```python
def pythagoras(a, b): return math.sqrt(a**2 + b**2)
```

------------------------------------------------------------------------------

## Practice ##

Write functions that compute the areas, circumferences, or volumes of simple
shapes like squares, rectangles, circles, spheres, etc.

```python
def circle_area(r): return math.pi * r**2
def rectangle_area(w, h): return w * h
```

Of course, you can use your own function in other functions. The area of a
triangle is half the area of a rectangle, so one could call the rectangle
function and divide by two (but in practice this is less efficient because the
math is so simple).

```python
def triangle_area(w, h): return rectangle_area(w, h) / 2
```

Here are some more ideas of simple functions for practice.

- Convert temperature from F to C or vice-versa
- Convert speed from MPH to KPH or vice-versa
- Compute DNA concentration from OD260
- Compute the arithmetic mean of 3 numbers
- Compute the geometric mean of 3 numbers
- Compute the harmonic mean of 3 numbers
- Compute the distance between 2 points in a graph

Don't be surprised if these show up in your assessment.

------------------------------------------------------------------------------

## Strings ##

So far, all of the variables we have seen have been numbers of some kind. But
you can also store letters in variables. A collection of zero or more letters
inside quotes is known as a string. In your first program, 'hello world' was a
string. Note that both 'hello world' and "hello world" are exactly the same
thing. In Python, we use single quotes because it's one less keypress compared
to double quotes.

```python
s = 'hello world'
print(s, type(s))
```

Since this is a class that features bioinformatics programming, we will be
working with biological sequences as strings quite a bit, but not until unit 3.

------------------------------------------------------------------------------

## Conditionals ##

### if ###

A "conditional statement" makes choices about what to do next. The simplest
form of a conditional is the `if` construction. In the code below, the
`print()` statement only runs if `a` has the same value as `b`. Note that
equality uses a double equals sign `==`. That's because a single equals sign is
used for assignment. Try changing `b` so that they are unequal and observe the
behavior.

```python
a = 2
b = 2
if a == b:
    print('a equals b')
```

Did you notice that the `print()` statement was indented? That's because it has
block structure. In the following block, the values of `a` and `b` are only
reported if they are equal.

```python
if a == b:
    print('a equals b')
    print(a, b)
```

If you want the program to always report `a` and `b`, put the second statement
after the block (or before).

```python
if a == b:
    print('a equals b')
print(a, b)
```

The numeric comparison operators are shown below.

| Operator | Purpose           | Example
|:---------|:------------------|:----------------------
| `==`     | equality          | `if a == b:`
| `!=`     | inequality        | `if a != b:`
| `<`      | less than         | `if a < b:`
| `>`      | greater than      | `if a > b:`
| `<=`     | less or equal     | `if a <= b:`
| `>=`     | greater or equal  | `if a >= b:`

Let's put conditionals into practice using a simple function that checks if a
number is evenly divisible by 2.

```python
def is_even(x):
	if x % 2 == 0: return True
	return False

print(is_even(2))
print(is_even(3))
```

### Boolean ###

This may seem weird, but the expression `a == b` has a value and type. We can
explore this by assigning it to a variable.

```python
c = a == b
print(c)
print(type(c))
```

Expressions like `a == b` are Boolean expressions of type `bool` that can have
a value of either `True` or `False`. Try changing the values of `a` and `b` and
observe the value of `c`.

### if-elif-else ###

Much of the time we write conditional statements, there are multiple branches.
In these cases, we use the if-elif-else construct. There is only one `if` and
only one `else`, but there can be any number of `elif`.

```python
if a < b:
	print('a < b')
elif a > b:
	print('a > b')
else:
	print('a == b')
```

When you have a stack of really simple if-elif-else conditions, it's tidy to
format as one-liners and align them horizontally. You cannot do this if each
block has multiple statements.

```python
if   a < b: print('a < b')
elif a > b: print('a > b')
else:       print('a == b')
```

In an if-elif-else construct, only the first true condition is executed.

```python
if   a < b:  print('a < b')
elif a <= b: print('a <= b')
elif a == b: print('this will never print!')
```

### Chaining ###

Boolean expressions can be chained with `and` and `or` and inverted with `not`.

```python
if a < b or a > b: print('all things being equal, a and b are not')
if a < b and a > b: print('you are living in a strange world')
if not False: print(True)
```

### Floating Point Warning ###

If you recall that floating point numbers have finite precision you may not be
surprised that the following code reports that a < b.

```python
a = 0.3
b = 0.1 * 3
if   a < b: print('a < b')
elif a > b: print('a > b')
else:       print('a == b')
```

NEVER test for equality with floating point numbers. Instead, examine their
difference and if that's less than some acceptable precision, consider them to
be the same. Here's how you do that manually.

```python
print(abs(a - b)) # 5.551115123125783e-17
if abs(a - b) < 1e-9: print('close enough')
```

Python has a math function `math.isclose()` that compares two values and
returns `True` if their values are close and `False` otherwise.

```python
if math.isclose(a, b): print('close enough')
```

### String Comparison ###

Strings are compared alphabetically, sort of. They are actually compared by
their ASCII values. This is why "A" is less than "B". But "B" is less than "a"
because all lowercase letters have higher ASCII values than uppercase letters.

```python
s1 = 'A'
s2 = 'B'
s3 = 'a'
if s1 < s2: print('A < B')
if s2 < s3: print('B < a')
```

### Mismatched Type Error ###

If two variables have different types, it usually doesn't make sense to compare
them. That's why the following code results in a "Type Error".

```python
a = 1
s = 'G'
if a < s: print('a < s')
```

------------------------------------------------------------------------------

## None Type ##

So far, we have seen values of type `int`, `float`, `str`, and `bool`. Another
type is `NoneType`, which has a single value `None`. There are a variety of
situations where you may end up with `None`. Consider the following function.

```python
def silly(m, x, b):
	y = m * x + b
```

There is no `return` in the function. `y` is computed but not returned. What
happens when you call the function? You end up with a value of `None`.

```python
print(silly(2, 3, 4))
```

------------------------------------------------------------------------------

## More Practice ##

Write a function that determines if a number is an integer. A good name for
such a function would be `is_integer()` or `isinteger()`. Functions with
Boolean return values often have `is` in their prefix. To solve this problem,
try using `//` or `%`.

Write a function that determines if a number is a valid probability.

Write a function that returns the molecular weight of a DNA letter. If the
letter doesn't match any nucleotide, return `None`.

Write a function that returns the complement of a DNA letter, returning `None`
if the letter isn't DNA.

------------------------------------------------------------------------------

## Style ##

Your code is evaluated on two criteria:

1. Correctness - does the code solve the problem
2. Style - does the code have good "style"

Correctness is easier to grade than style, but style is at least as important.
Incorrect code can usually be fixed quickly. Code with poor style is confusing
and difficult to maintain/extend. Here's a typical scenario in a biology lab. A
postdoc writes some code and then leaves. The PI asks the graduate student to
continue working on the project. However, the code has poor style and the
graduate student can't work with it. Instead, she reinvents the whole project
from the beginning. Unfortunately, when she leaves, the next student has the
same problem.

### Spacing ###

(1) Use a maximum line length of 79 characters (most of the time).

(2) Use 1 space around/after most operators, just like in English. But don't be
robotic about it, as sometimes it's clearer not to use spaces.

+ Yes: "Hello, my name is Ian. What's your name?"
+ No: "Hello,my name is Ian.What's your name?"
+ No: "Hello, my name is  Ian .  What's your name?"
+ Yes: `print(a, b, c)`
+ No: `print(a,b,c)`
+ Yes: `if a > b: a = 1`
+ No: `if a>b:a=1`
+ Yes: `print('hello', end='')` there is no space around keyword `=`
+ Yes: `c = (a**2 + b**2) ** 0.5` the interior looks better without spaces

(3) Use vertical spacing (blank lines) to separate logic, just as you would use
paragraph structure in English.

(4) Use tabs for left side indentation. The use of spaces for indentation flags
your code as potential **cheating**.

(5) Don't indent simple if-elif-else type constructs.

(6) There is no space between a function and its opening parentheses. Note that
`return` is a keyword, not a function, so it doesn't have parentheses.

+ Yes: `print('hello')`
+ No: `print ('hello')`
+ Yes: `return a`
+ No: `return(a)`
+ No: `return (a)`

### Naming ###

+ Variable and function names are generally all lowercase
+ Multi-word variables may use snake case, but not mixedCase

```python
widowsize   = 60  # yes
window_size = 60  # yes
windowSize  = 60  # no
```

Variables sometimes have very short names that implicitly describe their type.
It's okay for short-lived variables to have such short names, but for
longer-lived variables, you should use more descriptive names.

+ `i`, `j`, and `k` are integers
+ `x`, `y`, and `z` are floating point numbers in a graphical context
+ `x` by itself may represent anything
+ `n` by itself is a number
+ `p` and `q` are probabilities
+ `a`, `b`, and `c` are often numbers
+ `c` by itself is a character
+ `s` is a string

For biological sequences it's common to use these shorthands:

+ `nt` and `aa` are single characters of nucleotides or amino acids
+ `seq` is often used for a biological sequence
+ `dna` and `rna` are nucleotide strings
+ `pro` and `pep` are protein/peptide strings

------------------------------------------------------------------------------

## Even More Practice ##

Write a function that returns the maximum of 3 numbers. To be clear, the
function takes 3 input parameters and returns the single largest one.

Given values for true positives, false positives, true negatives, and false
negatives, write functions that return sensitivity, specificity, and F1 score.

Write a function that returns the Shannon entropy for nucleotide counts A, C,
G, T. It should work even in the case where there are zero counts for one or
more letters.

------------------------------------------------------------------------------

## Homework ##

Push the following files to your repo.

- 10demo.py
- 11oligo.py
- 12phred.py

### 11oligo.py ###

Write a function that returns the oligo melting temperature given the number of
As, Cs, Gs, and Ts in the oligo. Use these two methods.

1. For oligos <= 13 nt, Tm = (A+T)*2 + (G+C)*4
2. For longer oligos, Tm = 64.9 + 41*(G+C -16.4) / (A+T+G+C)

Demonstrate that your program works by computing the Tm of several oligos of
different sizes. For example:

```python
print(tm(5, 7, 3 4))
```

### 12phred.py ###

Write functions that convert quality value symbols into error rates and
vice-versa. The `ord()` function returns the ASCII value of a letter. The
`chr()` function turns an ASCII value into a letter.

See https://en.wikipedia.org/wiki/FASTQ_format

Demonstrate the functions work by calling them several times. Edge cases should
return `None`.

```python
print(char_to_prob('A'))
print(prob_to_char(0.001))
```

------------------------------------------------------------------------------

## Assessment Example ##

1. Write a function that computes the distance between 2 points in a graph.

2. Write a function that returns the complement of a DNA letter, returning
`None` if the letter isn't DNA.

3. Write a function `max3()` that returns the maximum of 3 numbers.

4. Why do you think PHRED quality values are -10 * log10 rather than -log2? How
would you modify your program if you thought log2 was better?
