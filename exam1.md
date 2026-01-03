Exam #1 Questions
=================

- Most exam questions will be identical to those below
- Some exam questions will be variations of those below
- Some exam questions may be completely new

## Encoded Information

1. How many combinations of lights can be made with a typical traffic light?

2. Convert the number 9 from decimal to binary.

3. Convert the number 1011 to decimal and hexadecimal.

4. Convert the hexadecimal number A5 to decimal.

5. What are the ASCII values for capital A and lowercase A? Report as both
decimal and hexadecimal.

6. How are Unix line endings different from Windows?

7. What is UTF-8?

8. How is the color Orange represented in a computer? Use both decimal and
hexadecimal representations.

9. An error message shows up on your screen which says "Use of uninitialized
value". You decide to ask for help. First, you copy-paste the text into
Discord. Then you take a screenshot of your computer screen, which is 1920x1080
and upload that file. Finally, you also take a picture using your phone, which
has a 14 megapixel camera, and upload that file. Compare the data size of each
action.

10. Describe the difference between integers and floating point numbers inside
a computer.

11. What do the terms "overflow" and "underflow" mean?

12. What file extension is used for Python files?

13. What kinds of things are stored in `.tsv` files?

14. What does it mean if a file is named `myfile.fa.gz`?

## Unix

1. Exapand the initialism "CLI".

2. Define "terminal" and "shell".

3. Define "argument" as it applies to Unix commands.

4. What is your favorite editor program?

5. You type the commands below. What is the result?

```bash
cd ~/Code/mcb185_homework
cd data
pwd
```

6. You type the commands below. What is the result?

```bash
cd ~/Code/mcb185_homework
cd data
cd ../../..
pwd
```

7. What is the path to your homework directory?

8. What does `git push` do?

9. What does ^C mean?

10. What programs can you use to view a text file?

11. Write a command line the searches a file for the word "frog" and saves all
lines with "frog" to a file called "pond".

12. Write a command that moves all PNG files from your Downloads folder to your
Documents folder.

13. Write a command line that extracts the third column from a TSV file and
counts the occurences of each word.

14. How could you make is so that every time you type `ls` the shell actually
performs `ls -F` instead?


## Python

0. Write a program `hello.py` that prints "hello world" to the terminal.

1. Write a program `maths.py` that assigns variables, performs some math
operations, and prints the results. For example, assign variables `a` and `b`,
calculate the hypotenuse `c`, and print the results.

2. Write a program `ascii.py` that prints out the ASCII decimal values for `A`
and `a` separated by a comma.

3. Write a program `bits.py` that prints the base 2 logarithm of pi and e to 5
digits of precision. Separate the values with a tab. Use `math.log2()`,
`math.pi`, and `math.e`.

4. Write a function `ftoc(x)` that converts Fahrenheit to Celsius. 32F equals
0C and 212F equals 100C.

5. Write a function `mph_to_kph(x)` that converts miles per hour to kilometers
per hour. There are 0.62137 miles in a kilometer.

6. Write a function `is_int(x)` that determines (returns Boolean) if the input
parameter is equal to an integer (has remainder 0 when divided by 1).

7. Write a function `is_prob(x)` that determines (returns Boolean) if a number
is a valid probability (x >= 0 and x <= 1).

8. Write a function `complement(nt)` that returns the complement of a DNA
letter.

9. Write a function `phred_to_prob(c)` that converts a PHRED quality symbol
into an error probability.

10. Write a function `prob_to_phred(p)` that converts a probability into a
PHRED quality symbol.

11. Write a function `pythagoras(a, b)` that returns the hypotenuse of a right
triangle with sides of length a and b.

12. Write a function `max3(a, b, c)` that returns the maximum of 3 numbers. You
my not use the `max()` function or any list methods.

13. Write a function `distance(x1, y1, x2, y2)` that computes the Cartesian
distance between two points on a graph.

14. Write a function `triangular(n)` that returns the triangular number (the
sum of the integers from 1 to n) for a non-negative integer.

15. Write a function `factorial(n)` that returns the factorial of a
non-negative integer.

16. Write a function `is_prime(n)` that determines (returns Boolean) if an
integer is a prime number.

17. Write a program `fizzprime.py` that prints the numbers from 1 to 100. If
the number is divisible by 3 print Fizz instead. If it is divisible by 5 print
Buzz instead. If it is divisible by both, print FizzBuzz instead. If the number
is prime, immediately follow the output with a `*`.

18. Write a program `fibonacci.py` that prints out the first 100 numbers of the
Fibonacci sequence.

19. Write a program `euler.py` that estimates the value of e (2.71828...) by
computing the infinite sum of 1/n!. Stop the calculation when the estimate runs
out of precision (repeats the same value twice). Print the current estimate
each time through the loop. You may use `math.factorial()`.

20. Write a program `nilakantha.py` that estimates Pi using the Nilakantha
series (Pi = 3 + 4/2x3x4 - 4/4x5x6 + 4/6x7x8 ...). Terminate the loop when
upper and lower bounds are within 1e-6 of the actual value. Print the current
estimate each time through the loop.

------------------------------------------------------------------------------
