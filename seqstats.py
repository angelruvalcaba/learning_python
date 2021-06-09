#!/usr/bin/env python3
import mcb185
import argparse
import statistics

parser = argparse.ArgumentParser(description='stats about sequence')
# required arguments
parser.add_argument('--file', required=True, type=str,
	metavar='<str>', help='required fasta file')
arg = parser.parse_args()
length = []
for name, seq in mcb185.read_fasta(arg.file):
	#print(name, len(seq))
	length.append(len(seq))
length.sort()
total = sum(length)
print('total length is', total)
print('# of seqs is', len(length))
print('min is', min(length))
print('max is', max(length))
print('sum is', sum(length))
print('mean is', statistics.mean(length))
print('median is', statistics.median(length))
#print(length)


print('n50 is', mcb185.n50(length))
	

# Write a program that computes statistics about a fasta file
#   Number of sequences
#   Total length
#   Minimum and maximum lengths
#   Average and median lengths
#   N50 length
# Use argparse
# Make useful functions and add them to your library

