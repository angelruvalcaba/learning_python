#!/usr/bin/env python3

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

dna = 'ACTGAAAAAAAAAAA'
rvdna = ''
for i in range(len(dna) -1, -1, -1) :
	nt = dna[i]
	if   nt == 'A' : rvdna += 'T'
	elif nt == 'T': rvdna += 'A'
	elif nt == 'C': rvdna += 'G'
	elif nt == 'G': rvdna += 'C'
print(rvdna)
	
"""
python3 anti.py
TTTTTTTTTTTCAGT
"""
