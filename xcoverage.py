#!/usr/bin/env python3

# Write a program that simulates random read coverage over a chromosome
# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line
# Note that you will not sample the ends of a chromosome very well
# So don't count the first and last parts of a chromsome

import sys
import random
g = sys.argv[1]
n = sys.argv[2]
l = sys.argv[3]
dup = []
genome = []


"""
python3 xcoverage.py 1000 100 100
5 20 10.82375
"""
