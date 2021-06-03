#!/usr/bin/env python3

import sys

# Write a program that predicts if a protein is trans-membrane
# Trans-membrane proteins have the following properties
#	Signal peptide: https://en.wikipedia.org/wiki/Signal_peptide
#	Hydrophobic regions(s): https://en.wikipedia.org/wiki/Transmembrane_protein
#	No prolines in hydrophobic regions (alpha helix)
# Hydrophobicity is measured via Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot
# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa
#hph == hydrophobic helix
name = []
protein = []
seq = open('Data/at_prots.fa')
line = seq.readline()
Proline = 'P'

def kd(seq):
	h = 0
	for aa in seq:
		if aa == 'I': h+= 4.5
		if aa == 'V': h+= 4.2
		if aa == 'L': h+= 3.8
		if aa == 'F': h+= 2.8
		if aa == 'C': h+= 2.5
		if aa == 'M': h+= 1.9
		if aa == 'A': h+= 1.8
		if aa == 'G': h+= -0.4
		if aa == 'T': h+= -0.7
		if aa == 'S': h+= -0.8
		if aa == 'W': h+= -0.9
		if aa == 'Y': h+= -1.3
		if aa == 'P': h+= -1.6
		if aa == 'H': h+= -3.2
		if aa == 'E': h+= -3.5
		if aa == 'Q': h+= -3.5
		if aa == 'D': h+= -3.5
		if aa == 'N': h+= -3.5
		if aa == 'K': h+= -3.9
		if aa == 'R': h+= -4.5
	return h / len(seq)
with open(sys.argv[1]) as orf:
	seq = []
	for line in orf.readlines():
		line = line.rstrip()
		if line.startswith('>'):
			words = line.split()
			n = words[0]
			name.append(n[1:])
			if len(seq) > 0: protein.append(''.join(seq))
			seq = []
		else:
 			seq.append(line)
	protein.append(''.join(seq))
def hph(seq, w, t):
	for i in range(len(seq) - w + 1):
		frame = seq[i: i+w]
		if kd(frame) > t and Proline not in frame:
			return True
	return False
for name, seq in zip(name, protein):
	nterm = seq[:30]
	cterm = seq[30:]
	if hph(nterm, 8, 2.5) and hph(cterm, 11, 2.0):
		print(name)
	





"""
for i in range(100):
	line = seq.readline()
	for c in range(0, 30-wsp+1):
		h = 0
		window =  line[c :c+wsp]	
		for aa in window:
			if aa == 'I': h+= 4.5
			if aa == 'V': h+= 4.2
			if aa == 'L': h+= 3.8
			if aa == 'F': h+= 2.8
			if aa == 'C': h+= 2.5
			if aa == 'M': h+= 1.9
			if aa == 'A': h+= 1.8
			if aa == 'G': h+= -0.4
			if aa == 'T': h+= -0.7
			if aa == 'S': h+= -0.8
			if aa == 'W': h+= -0.9
			if aa == 'Y': h+= -1.3
			if aa == 'P': h+= -1.6
			if aa == 'H': h+= -3.2
			if aa == 'E': h+= -3.5
			if aa == 'Q': h+= -3.5
			if aa == 'D': h+= -3.5
			if aa == 'N': h+= -3.5
			if aa == 'K': h+= -3.9
			if aa == 'R': h+= -4.5
		if h/wsp > kd and Proline not in window:
			print(i, 'True', window, h/wsp, line)


python3 Programs/transmembrane.py Data/at_prots.fa
AT1G75120.1
AT1G10950.1
AT1G75110.1
AT1G74790.1
AT1G12660.1
AT1G75130.1
"""