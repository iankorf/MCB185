Unit 1.3: Python Basics
=======================

## Hello, again ##

Create a new file called `10demo.py` and save it in your `mcb185_homework`
repo. `touch` the file into existence and then open it in your text editor
(e.g. VS Code, Notepad++, BBedit, etc.).

```
cd ~/Code/mcb185_homework
touch 10demo.py
```

We used the `print()` function before to output "hello world". Edit `10demo.py`
so that it prints out "hello, again". Save your work, then go to your terminal
and run the program.

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
Absolute value is a function called `abs()`. There is also `pow()`, which is
mostly identical to the exponentiation operator `**` and `round()`, which
rounds off floating point numbers.

| Function              | Purpose
|:----------------------|:---------------------------
| `abs(x)`              | absolute value of `x`
| `pow(x, y)`           | `x` to the power of `y`
| `round(x, ndigits=3)` | round off `x` to 3 digits

What about logarithms and such? Those are in the math library. In order to use
those functions you must `import math` in your code. Import statements usually
go at the top of your program. If you import functions from a library (`math`
is the name of a library), you must prefix the function name with the library
name. Try out some of the functions below.

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

It's time to update your repo with the code you've writtens so far.

```sh
git add 10.demo.py
git commit -m update
git push
```

You should push regularly.

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
is neater than using spaces.

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

The variables `a` and `b` are the "parameters" (or "arguments") of the
function. The calculation is stored in variable `c`, which is then sent back to
the "caller". Let's see this in action.

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

Now would be another good time to `git push`.

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

## Function Practice ##

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

After all that work, another `git push` is in order.

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
working with biological sequences as strings quite a bit, but not until later.

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
only one `else`, but there can be any number of `elif`. In an `if-elif-else` construct, the first condition that satisfies the condition is the only th

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

### Boolean Chains ###

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

## More Function Practice ##

Write a function that determines if a number is an integer. A good name for
such a function would be `is_integer()` or `isinteger()`. Functions with
Boolean return values often have `is` in their prefix. To solve this problem,
try using `//` or `%`.

Write a function that determines if a number is a valid probability.

Write a function that returns the molecular weight of a DNA letter. If the
letter doesn't match any nucleotide, return `None`.

Write a function that returns the complement of a DNA letter, returning `None`
if the letter isn't DNA.

When was that last time you did a `git push`?

------------------------------------------------------------------------------

## Style ##

Code should be both correct and well-formed.

1. Correctness - does the code solve the problem?
2. Style - is the code easy for another developer to understand?

Correctness is easier to evaluate than style, but style is at least as
important. Incorrect code can usually be fixed quickly. Code with poor style is
confusing and difficult to maintain/extend. Here's a typical scenario in a
biology lab. A postdoc writes some code and then leaves. The PI asks the
graduate student to continue working on the project. However, the code is
poorly formed and the graduate student can't understand what it does. Instead
of reusing the old code, she reinvents the whole project from the beginning.
Unfortunately, when she leaves, the next student has the same problem.

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

(4) Don't indent simple if-elif-else type constructs when the block is a
one-liner.

(5) There is no space between a function and its opening parentheses. Note that
`return` is a keyword, not a function, so it doesn't have parentheses.

+ Yes: `print('hello')`
+ No: `print ('hello')`
+ Yes: `return a`
+ No: `return(a)`
+ No: `return (a)`

### Naming ###

Variables sometimes have very short names that implicitly describe their type.
It's okay for short-lived variables to have such short names, but for
longer-lived variables, you should use more descriptive names. Here are some
conventions used in this course.

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

------------------------------------------------------------------------------

## Even More Function Practice ##

Write a function that returns the maximum of 3 numbers. To be clear, the
function takes 3 input parameters and returns the single largest one.

Given values for true positives, false positives, true negatives, and false
negatives, write functions that return sensitivity, specificity, and F1 score.

Write a function that returns the Shannon entropy for nucleotide counts A, C,
G, T. It should work even in the case where there are zero counts for one or
more letters.

------------------------------------------------------------------------------

## Homework: 11oligo.py ##

Write a function that returns the oligo melting temperature given the number of
As, Cs, Gs, and Ts in the oligo. Use these two methods.

1. For oligos <= 13 nt, Tm = (A+T)*2 + (G+C)*4
2. For longer oligos, Tm = 64.9 + 41*(G+C -16.4) / (A+T+G+C)

Demonstrate that your program works by computing the Tm of several oligos of
different sizes. For example:

```python
print(tm(5, 7, 3 4))
```

## Homework: 12phred.py ##

Write functions that convert quality value symbols into error rates and
vice-versa. The `ord()` function returns the ASCII value of a letter. The
`chr()` function turns an ASCII value into a letter.

Demonstrate the functions work by calling them several times. Edge cases should
return `None`.

```python
print(char_to_prob('A'))
print(prob_to_char(0.001))
```

Now is another good time to `git push`.

------------------------------------------------------------------------------

## Iteration ##

The solution to most complex problems involves some kind of iteration. For
example, if you want to compute the standard deviation for a set of numbers,
you must iterate through the values, squaring the differences to the mean.
Iteration is also called looping.

### while ###

The `while` loop is the simplest type of loop. It is formed in the manner
below, which does not represent actual code, so don't write this. The `while`
word is followed by an expression that can be evaluated as `True` or `False`.
This is followed by an indented code block.

```
while <boolean expression is True>:
    do_something
```

Add the following lines to your demo program and run it. The Boolean expression
in this case is the value `True`, which means this loop will never end.
Interrupt the endless output by typing ^C (control-C).

```python
while True:
    print('hello')
```

One way to break a loop is with the `break` statement. In the example below, we
create a variable `i` that will be used to store an integer. Each time through
the loop, the value of `i` increases: `i = i + 1`. Once `i` reaches 3, the
loop breaks.

```python
i = 0
while True:
    i = i + 1
    print('hey', i)
    if i == 3: break
```

A better way to break a `while` loop is to provide some kind of condition when
the Boolean expression is no longer True.

```python
i = 0
while i < 3:
    i = i + 1
    print('hey', i)
```

The loop doesn't have to start at 0, increment by 1, or end before 5. The
modified code below starts at 1, ends before 10, and skips by 3s.

```python
i = 1
while i < 10:
    print(i)
    i = i + 3
print('final value of i is', i)
```

### for i in range() ###

Most loops in Python are `for` loops, not `while` loops. Let's recreate the
last code example using a `for` loop and the `range()` function.

```python
for i in range(1, 10, 3):
    print(i)
```

The `range()` function generates integers given an initial value (1), an
end-before limit (10), and an increment (3).

Most "for i in range()" loops increment by one. For this reason, you can skip
the increment number and use just 2 arguments.

```python
for i in range(0, 5):
    print(i)
```

Also, most "for i in range()" loops also start at zero, meaning you can skip
the initial value and simply give the end-before limit.

```python
for i in range(5):
    print(i)
```

All of these constructions do the exact same thing.

```python
for i in range(5): print(i)
for i in range(0, 5): print(i)
for i in range(0, 5, 1): print(i)
```

------------------------------------------------------------------------------

## Nesting ##

Conditionals can be inside loops. Loops can be inside conditionals. Loops can
be inside of other loops. More abstractly, a code block may contain other code
blocks. Here's a simple loop that iterates over some numbers and reports which
ones are even and odd. If you recall that `range()` automatically starts at 0
and ends before it reaches the limit, you will not be surprised that the loop
goes from 0 to 6 inclusive.

```python
for i in range(7):
    if i % 2 == 0: print(i, 'is even')
    else:          print(i, 'is odd')
```

## Homework: 13fizzbuzz.py ##

One of the classic interview questions is FizzBuzz. Make a program that writes
out the numbers from 1 to 100. If the number is divisible by 3, write Fizz
instead. If the number is divisible by 5, write Buzz instead. If the number is
divisible by both 3 and 5, write FizzBuzz.

------------------------------------------------------------------------------

## Iteration Practice Problems ##

Try to solve the problems below by yourself before looking at the solutions
farther down. These are the kinds of questions that can appear on exams, and
you won't have anything but a pen and paper during an exam.

Write a function that calculates the triangular number. This is the sum of
numbers from 1 to n.

Write a function that calculates the factorial of a number.

Write a function that computes the Poisson probability of k events occurring
with an expectation of n: n^k e^-n / k!

Write a function that solves "n choose k": n! / k!(n - k)!

Write a function that estimates Euler's number: e (2.71828...). This can be
computed as the infinite sum of 1/n!. Choose a finite number of iterations.

Write a function to determine if a number is prime.

Write a function that estimates Pi (3.14159...) using the Nilakantha series.
Again, choose a finite limit.

`Pi = 3 + 4/(2x3x4) - 4/(4x5x6) + 4/(6x7x8) - 4/(8x9x10) ...`

------------------------------------------------------------------------------

## Iteration Practice Solutions ##


### triangular() ###

In order to sum up the numbers, we must have a variable to hold the sum (line
2). This is initialized at 0, and each iteration of the loop adds the current
value of the loop variable (line 4). The finalization step is simply returning
the value of the sum (line 5).

```python
1   def triangular(n):
2       tri = 0
3       for i in range(n+1):
4           tri = tri + i
5       return tri
```

### factorial() ###

There are two tricks to this solution. First, the factorial of zero is defined
as 1. There is a conditional for that special case (line 2). Second, when
multiplying values, you cannot initialize at zero or you will always get zero.
So factorial and other products must initialize at 1 (line 3).

```python
1   def factorial(n):
2       if n == 0: return 1
3       fac = 1
4       for i in range(1, n + 1):
5           fac = fac * i
6       return fac
```

### poisson() ###

Now that you have a factorial function, `poisson()` is simple.

```python
def poisson(n, k):
    return n**k * math.e**-n / factorial(k)
```

### nchoosek() ###

Again, once you create a function, you can use it to make other functions.

```python
def nchoosek(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))
```

### euler() ###

The solution to this problem is very similar to `triangular()` because it
simply sums up a bunch of numbers.

```python
def euler(limit):
    e = 0
    for n in range(limit):
        e = e + 1 / factorial(n)
    return e
```

### is_prime() ###

This algorithm features a short-circuit. It returns `False` as soon as it finds
any factor smaller than itself. If it fails to find any factors, it
_eventually_ returns `True`. The most common error is to make the conditional a
`if-else` construct.

```python
def is_prime(n):
    for den in range(2, n//2):
        if n % den == 0: return False
    return True
```

### nilakantha() ###

The trick to solving this problem is getting the loop to switch back and forth
between adding and subtracting.

```python
def nilakantha(limit):
    pi = 3
    for i in range(1, limit+1):
        n = 2 * i
        d = n * (n+1) * (n+2)
        if i % 2 == 0: pi = pi - 4 / d
        else:          pi = pi + 4 / d
    return pi
```

------------------------------------------------------------------------------

## Random Numbers ##

Random number generators are essential because we often use random expectation
as a background model or null hypothesis. In order to use random numbers, we
`import random` and call the functions therein.

The simplest function is `random.random()`, which produces a number 0 <= x < 1.

```python
for i in range(5):
    print(random.random())
```

The function we will use most often is `random.randint()`. This generates a
random number between two _inclusive_ end points. For example, the following
code simulates rolling a 6-sided die 3 times.

```python
for i in range(3):
    print(random.randint(1, 6))
```

Random numbers in your computer aren't truly random. They are generated
deterministically given a starting _seed_, which is an integer. All of the
random number problems presented here and in your homework problems can be
repeated exactly the same again and again if you set the seed ahead of time.
This can be useful for debugging. If you don't choose a seed, you will be given
one somewhat randomly.

```python
random.seed(1)
print(random.random())
print(random.random())
random.seed(2)
print(random.random())
print(random.random())
random.seed(1)
print(random.random())
print(random.random())
```

In the code above, each call to `random.seed()` resets the random number
generator so that subsequent calls to `random.random()` are repeated.

------------------------------------------------------------------------------

## Compound Assignment ##

The programs in this unit and onward have a lot of variables that need to be
incremented. Instead of writing `x = x + 1` there is a shortcut: `x += 1`. The
compound assignment operators do the math and update the variable at the same
time. We only use the 3 operators in the table below, but there are also
operators for division, modulus, integer division, and exponentiation (and
more).

| Operator | Purpose           | Example
|:---------|:------------------|:--------------------------
| `+=`     | increment         | `a += 1`
| `-=`     | decrement         | `a -= 1`
| `*=`     | multiply & assign | `a *= 2`


## More Iteration Practice ##

### Monty Pi-thon ###

Write a program that estimates pi using Monte Carlo methods. Generate random
values for x and y from 0 to 1. Calculate the distance to the origin. If the
distance is less than 1, the point is inside the circular arc. The ratio of
points that fall inside compared to the total is pi/4. Output each iteration
and watch as the ratio gets closer to pi. Use an endless `while` loop in your
program and stop it with ^C.

### D&D Stats ###

In Dungeons and Dragons, each character is described by 6 statistics (strength,
intelligence, wisdom, dexterity, constitution, charisma). In the old days, each
_stat_ was decided by summing up the values on 3 six-sided dice (3D6). Each
stat therefore has a range of 3-18 and an average of 10.5. Over the years, the
official rules have changed and many players have added their own house rules.
Write a program that determines the average stat value using the various rules
below.

+ 3D6: roll 3 six-sided dice
+ 3D6r1: roll 3 six-sided dice, but re-roll any 1s
+ 3D6x2: roll pairs of six-sided 3 times, taking the maximum each time
+ 4D6d1: roll 4 six-sided dice, dropping the lowest die roll



## Homework: 14fibonacci.py ##

A classic programming interview question is to write a program that reports the
first 10 numbers from the Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.
This is a tricky problem. You need to initialize and keep track of 2 previous
values.

## Homework: 15triples.py ##

Write a program that finds all Pythagorean triples for triangles with sides `a`
and `b` less than 100. For example, 3, 4, 5 is a triple: 3^2 + 4^2 = 5^2. Hint:
all sides, including the hypotenuse, must be integers. A good way to test for
an integer is like: `if c % 1 == 0`.

## Homework: 16savingthrows.py ##

One of the core mechanics of D&D is the "saving throw". When certain events
happen, you need to roll a d20 to figure out if you succeed or not. For
example, you are walking across a frozen lake and it begins to crack underfoot.
If you make a saving throw, you step aside. If you fail, you fall in. Some
saving throws are more difficult than others. If the ice is very thick, the
"difficulty class" (DC) may be only 5. This means you only need to roll a 5 or
higher to succeed. However, if the ice is thin and has a DC of 15, you will
need a roll of 15 or higher to succeed. Certain events may give you "advantage"
or "disadvantage". For example, if you have a rope tied around your waist and a
friend is instructed to pull you aside if anything bad happens, you could have
"advantage". This allows you to roll two d20s and take the larger value. You
may also have disadvantage, for example another "friend" pushes you from
behind, causing you to stumble forward. In this case, you have "disadvantage"
and must take the lower of two d20 rolls.

Write a program that simulates saving throws against DCs of 5, 10, and 15.

## Homework: 17deathsaves.py ##

Death saves are a little different than normal saving throws. If your health
drops to 0 or below, you are unconscious and may die. Each time it is your
turn, roll a d20 to determine if you get closer to life or fall deeper into
death. If the number is less than 10, you record a "failure". If the number is
10 or greater, you record a "success". If you collect 3 failures, you "die". If
you collect 3 successes, you are "stable" but unconscious. If you are unlucky
and roll a 1, it counts as 2 failures. If you're lucky and roll a 20, you gain
1 health and have "revived". Write a program that simulates death saves. What
is the probability one dies, stabilizes, or revives?

## Unit 1.3 Finalization ##

The following programs should be checked into your repo.

- `10demo.py`
- `11oligo.py`
- `12phred.py`
- `13fizzbuzz.py`
- `14fibonacci.py`
- `15triples.py`
- `16savingthrows.py`
- `17deathsaves.py`
