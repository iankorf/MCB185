Unit 2: Iteration
=================

## Contents ##

+ [Tuples](#tuples)
+ [Iteration](#iteration)
    + [while](#while)
    + [for i in range()](#for-i-in-range)
    + [for item in container](#for-item-in-container)
+ [Nesting](#nesting)
    + [21fizzbuzz.py](#21fizzbuzzpy)
+ [Practice Problems](#practice-problems)
+ [Practice Solutions](#practice-solutions)
    + [triangular()](#triangular)
    + [factorial()](#factorial)
    + [poisson()](#poisson)
    + [nchoosek()](#nchoosek)
    + [euler()](#euler)
    + [is_prime()](#is_prime)
    + [nilakantha()](#nilakantha)
+ [Random Numbers](#random-numbers)
+ [Compound Assignment](#compound-assignment)
+ [More Practice](#more-practice)
    + [Monty Pi-thon](#monty-pi-thon)
    + [D&D Stats](#dd-stats)
+ [Homework](#homework)
    + [22fibonacci.py](#22fibonaccipy)
    + [23triples.py](#23triplespy)
    + [24savingthrows.py](#24savingthrowspy)
    + [25deathsaves.py](#25deathsavespy)
+ [Assessment Example](#assessment-example)

------------------------------------------------------------------------------

## Tuples ##

Create a new `20demo.py` program in your homework repo and bring it up in your
editor.

A tuple is a collection of values separated by a comma, and it has its own data
type called `tuple`. Notice that when you print a tuple, the output includes
parentheses and commas between the values.

```python
t = 1, 2  # this is a tuple
print(t)
print(type(t))
```

A tuple can contain a mixture of types.

```python
person = 'Steve', 21, 57891.50 # name, age, yearly income
print(person)
```

In the last unit, all of the functions returned a single value. But surely
a function can return multiple values. Yes, by returning a tuple. The following
function returns the midpoint of a line as a tuple.

```python
def midpoint(x1, y1, x2, y2):
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    return x, y
```

The next bit of code is numbered so we can talk about individual lines.

```python
1   print(midpoint(1, 2, 3, 4))
2   m = midpoint(1, 2, 3, 4)
3   mx, my = midpoint(1, 2, 3, 4)
4   print(mx, my)
```

Line 1 calls the `midpoint()` function and the output is directly sent to the
`print()` function. As you should expect, the output includes parentheses and a
comma between the values.

Line 2 assigns the variable `m` to the return value of the midpoint() function.
`m` is a tuple. This single variable contains 2 separate values.

Line 3 "unpacks the tuple". That is, the caller knows that the function returns
two values, so the caller provides 2 separate named variables, `mx`, and `my`.

Line 4 prints the separate values.

What if you use the strategy of Line 2 and you still want to get to the
individual values? Each item in a tuple gets a numeric index starting at 0. The
syntax is shown below. Note the square brackets.

```python
print(m[0], m[1])
```

It's almost always better to unpack a tuple into named variables rather than
use numeric indices.

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

### for item in container ###

`for` loops can be used to iterate over items in a container. We will see much
more of this next unit when we examine strings and lists. In this unit, our
containers are tuples.

```python
basket = 'milk', 'eggs', 'bread'
for thing in basket:
    print(thing)
```

In the code above, `basket` is a tuple containing some grocery items. The code
steps through the basket one item at a time. The first time through the loop,
`thing` is equal to "milk". The second time, `thing` is "eggs". The last time,
`thing` is "bread".

You could also use the `range()` function and numeric indices. In the code
below, `len()` returns the number of items in the basket.

```python
for i in range(len(basket)):
    print(basket[i])
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

### 21fizzbuzz.py ###

One of the classic interview questions is FizzBuzz. Make a program that writes
out the numbers from 1 to 100. If the number is divisible by 3, write Fizz
instead. If the number is divisible by 5, write Buzz instead. If the number is
divisible by both 3 and 5, write FizzBuzz.

------------------------------------------------------------------------------

## Practice Problems ##

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

## Practice Solutions ##

Try to solve the problems with another student before examining the solutions
below.

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
as 1. Use a conditional for that special case (line 2). Second, when
multiplying values, you cannot initialize at zero or you will always get zero.
So factorial must initialize at 1 (line 3).

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
any factor smaller than itself. If it fails to find any factors, it eventually
returns `True`.

```python
def is_prime(n):
    for den in range(2, n//2 +1):
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

The simplest function is `random.random()`, which produces a number 0 <= X < 1.

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


## More Practice ##

### Monty Pi-thon ###

Write a program that estimates pi using Monte Carlo methods. Generate random
values for x and y from 0 to 1. Calculate the distance to the origin. If the
distance is less than 1, the point is inside the circle. The ratio of points
that fall inside compared to the total is pi/4. Output each iteration and watch
as the ratio gets closer to pi. Use an endless `while` loop in your program and
stop it with ^C.

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

## Homework ##

Check the following programs into your homework repo.

+ `20demo.py`
+ `21fizzbuzz.py`
+ `22fibonacci.py`
+ `23triples.py`
+ `24savingthrows.py`
+ `25deathsaves.py`

### 22fibonacci.py ###

A classic programming interview question is to write a program that reports the
first 10 numbers from the Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.
This is a tricky problem. You need to initialize and keep track of 2 previous
values.

### 23triples.py ###

Write a program that finds all Pythagorean triples for triangles with sides `a`
and `b` less than 100. For example, 3, 4, 5 is a triple: 3^2 + 4^2 = 5^2. Hint:
all sides, including the hypotenuse, must be integers. A good way to test for
an integer is like: `if c % 1 == 0`.

### 24savingthrows.py ###

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

Write a program that simulates saving throws against DCs of 5, 10, and 15. Make
a table showing the probability of success normally, with advantage, and with
disadvantage.

### 25deathsaves.py ###

Death saves are a little different than normal saving throws. If your health
drops to 0 or below, you are unconscious and may die. Each time it is your
turn, roll a d20 to determine if you get closer to life or fall deeper into
death. If the number is less than 10, you record a "failure". If the number is
10 or greater, you record a "success". If you collect 3 failures, you "die". If
you collect 3 successes, you are "stable" but unconscious. If you are unlucky
and roll a 1, it counts as 2 failures. If you're lucky and roll a 20, you gain
1 health and have "revived". Write a program that simulates death saves. What
is the probability one dies, stabilizes, or revives?

------------------------------------------------------------------------------

## Assessment Example ##

1. Re-write `fizzbuzz` as fast as you can.

2. Write a program that that estimates pi using the Gregory-Leibniz series.
`pi/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 ...`. Make the program run endlessly.

3. Halflings get advantage on death saves. Modify your program to determine the
halfling rate for death, stable, and revive.

4. Explain how you would get question 2 to end (a) after some number of
iterations or (b) after reaching some level of precision.
