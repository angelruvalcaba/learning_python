#!/usr/bin/env python3

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places
# Use all three formatting methods
dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT' # feel free to change
sum = 0
k = len(dna)
for i in range(len(dna) -1):
	if dna[i] == 'G' or dna[i] == 'C':
		i = 1
		sum += i
GC = sum/k
print("%.2f" % GC)
print('{:.2f}'.format(GC))
print(f'{GC:.2f}')
"""
python3 gc.py
0.42
0.42
0.42
"""
