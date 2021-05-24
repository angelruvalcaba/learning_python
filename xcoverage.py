#!/usr/bin/env python3

# Write a program that simulates random read coverage over a chromosome
# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line
# Note that you will not sample the ends of a chromosome very well
# So don't count the first and last parts of a chromsome

import sys
import random
gs = int(sys.argv[1])
nr = int(sys.argv[2])
rl = int(sys.argv[3])
#make empty genome (like calendar)
genome = []
for i in range(gs):
	genome.append(0)

for i in range(nr): #genome is read nr times, starting at random spots for a span of 5 bases
	start = random.randint(0, gs-rl) #can't include sequencing beyond the ends
	end = start + rl
	for j in range(start, end):
		genome[j] += 1 #each point per hit
#print(genome)
max = genome[rl] #hits at position 5, excluding ends again
min = genome[rl]
print(genome[rl])
total = 0
for hits in genome[rl:-rl]: #excluding ends
	if hits > max: max = hits
	if hits < min: min = hits
	total += 1
print(min,max, total/(gs - 2 * rl))

"""
python3 xcoverage.py 1000 100 100
5 20 10.82375
"""
