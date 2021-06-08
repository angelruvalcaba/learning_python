#!/usr/bin/env python3

# Write a program that does the following
# 1. generates N random sequences
# 2. each sequence has GC composition S and length L
# 3. calculate GC in a sliding window of size W
# 4. calculate entropy in a sliding window of size W
#
# Parameters N, S, L, and W are command line parameters
# Hint: write functions
import math
import random
import sys
N = int(sys.argv[1])
S = float(sys.argv[2])
L = int(sys.argv[3])
W = int(sys.argv[4])
print(N, S, L, W)
bp = 'ATCG'
nt = 0
GC = 0
c = 0
for i in range(N):
	seq = ''
	for j in range(L):
		nt = random.choice('ATCG')
		seq += nt
	for c in range(L - W):
		c += 1
		window = seq[c-1: c+W]
		print(window, seq)
		GC = window.count('C') + window.count('G')	
		print(GC/W)

		



"""
python3 randomfun.py 1 0.5 15 7
AATTACAGATCGTGT
gc
0.1429
0.2857
0.2857
0.2857
0.4286
0.5714
0.4286
0.5714
0.4286
entropy
1.3788
1.8424
1.8424
1.8424
1.8424
1.9502
1.9502
1.8424
1.8424
"""
