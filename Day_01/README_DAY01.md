# Day 01 - Python Bootcamp
*`Topics:`* **argparse, sys, re (modules)**
## Exercise 00: Blockchain

Only lines that fit into certain criteria are considered valid:

- Correct lines are 32 characters long
- They start with exactly 5 zeroes, so e.g. line starting with 6 zeroes is NOT
  considered correct

For the example: 
```
00000254b208c0f43409d8dc00439896
000000434dd5469464f5cafd8ffe3609
00000f31eaabadef948f28d1
e7a1ee0b7de74786a2c0180bcdb632da
0000085a34260d1c84e89865c210ceb4
073f7873a75c457cbb3307d729501cb5
b7c93ff4cc1c4e0486a8fc66605
fe564b26f25e47c393d07e494021479e
a5dff06057d14566b45caef813511738
0000071f49cffeaea4184be3d507086v
```
Your script should print:

```
00000254b208c0f43409d8dc00439896
0000085a34260d1c84e89865c210ceb4
0000071f49cffeaea4184be3d507086v
```

Your code should accept the number of lines as an argument, like this:

`~$ cat data.txt | python blockchain.py 10`


## Exercise 01: Decypher


Your script should be launchable like this:  
`~$ python decypher.py "Have you delivered eggplant pizza at restored keep?"`

and print out the answer as a single word without spaces:  
`Hydepark`

## Exercise 02: Track and Capture

So, as an input your code is given a 2d "image" as text in a file `m.txt`. File contains five
characters over three lines, like this:

```
*d&t*
**h**
*l*!*
```

You may notice that there is a pattern of stars here, with a letter M. All
your code has to do is to print 'True' if this M-pattern exists in a given
input image or 'False' otherwise. Other characters (outside the M pattern)
should be different, so these examples should print out 'False':

```
*****
*****
*****
```

```
*s*f*
**f**
*a***
```

If a given pattern is not 3x5, then 'Error' word should be printed instead.
The file with code should be named `ex02_mfinder.py`.