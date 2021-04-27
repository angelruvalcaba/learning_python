#!/usr/bin/env python3

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median
# No, you cannot import the stats library!

import sys
import math
p = []
i= 0
for s in sys.argv[1:]:
	p.append(int(s))
#Count	
for i in range(len(p)):
	i += 1
print(i)
p.sort()
#Min
print(float(p[0]))
#Max
print(float(p[-1]))
#Std. Dev
x = 0
mean = sum(p)/i
print(mean)
for n in range(len(p)):
	x += (n-mean)**2
SD = (x/i)**(1/2)
print(SD)
#Median
print(p)
pos1 = int((i+1)/2)
pos2 = (i/2)
pos3 = (pos1+pos2)/2
r = i%2

if r == 0:
	print([pos3-1]) #must subtract 1 because of python numbering system
elif r!= 0: print(float(p[pos1-1]))

	
"""

python3 stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
