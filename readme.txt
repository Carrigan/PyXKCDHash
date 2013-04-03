XKCD April Fools 2013 Hash Competition Solver

Requirements:
Python 3.2 with PySkein (http://pythonhosted.org/pyskein/)

This program computes Skein1024 hashed sequentially based on a string. I believe that the
string used to generate the hash code on almamater.xkcd.com was a phrase or word, and thus
this program iterates through phrases and words as follows:

a
b
c 
.
.
x
y
z
aa
ba
ca
..
..
..
xz
yz
zz
aaa
baa
caa
...
...
...

And so forth.

Stats:
On my i5, each core can check roughly 2m hashes per minute. With all 4 running, that equates 
to 8m hashes per minutes. If we assume that we get a new output for every input for all 2^1024 
outcomes (not likely), this algorithm would still take upwards of 4.27533x10^295 years to find
a match.

May the odds be ever in your favor.
