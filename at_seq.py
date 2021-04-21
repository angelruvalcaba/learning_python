#!/usr/bin/env python3

import random
random.seed(1) # comment-out this line to change sequence each time

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence

bp = 30
seq = ''
at = 0.6

seq = ''
for i in range(bp):
	nt = random.choice('AAACCGGTTT')
	seq += nt
print(len(seq))
sum = 0
k = len(seq)
for i in range(len(seq) -1):
	if seq[i] == 'A' or seq[i] == 'T':
		i = 1
		sum += i
TA = sum/k
print(TA)
print(seq)


"""
python3 at_seq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
