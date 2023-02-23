#!/usr/bin/env python3

# 42dust.py

# Write a program that performs entropy filtering on nucleotide fasta files
# Windows that are below the entropy threshold are replaced by N

# Program arguments include file, window size, and entropy threshold

# Output should be a fasta file with sequence wrapped at 60 characters

# Hint: use the mcb185 library
# Hint: make up some fake sequences for testing

# Note: don't worry about "centering" the entropy on the window (yet)

import sys
import mcb185
import random
import math

# Take system arguments
seq = sys.argv[1] # genome fasta file
winlen = int(sys.argv[2]) # window length
sthresh = float(sys.argv[3]) # entropy threshold
		
# Calculates entropy of a given sequence
def scal(win):

	# Initialize variables
	nts = 'ATGC' # nucleotide identities
	counts = [0]*4 # nucleotide counts given a DNA sequence
	probs = [] # probabilities of each nucleotide in a given DNA sequence

	# Tally instances of each nucleotide
	for residue in win:
		for nt in nts:
			if residue == nt: counts[nts.index(nt)] += 1
	
	# Generate probabilities
	for count in counts: probs.append(count/len(win))
	
	# Calculate Shannon entropy
	h = 0 # Shannon entropy
	
	# Calculate Shannon entropy
	for pi in probs: 
		if pi != 0: h -= pi * math.log2(pi)
		
	return h

# Calculates entropy with window sliding on a given sequence
def scal_slide(seq, winlen, sthresh):

	# Filtered sequence
	fil_seq = []

	# Filters window sequence, replacing sequences lacking in information
	# with 'N' at the first position
	for pos in range(len(seq)-winlen+1):

		# Initialize variables
		win = seq[pos:pos+winlen] # Window sequence
		h = scal(win) # Shannon entropy of the window sequence
		
		# Perform 'N'-substitution based on entropy threshold
		if h >= sthresh: fil_seq.append(seq[pos])
		else: fil_seq.append('N')
		
		# Report filtered sequence in lines of 60 characters
		if len(fil_seq) >= 60: 
			yield(''.join(fil_seq))
			fil_seq = []
	
	# Prints the remaining sequence in lines of 60 characters
	for nt in range(len(seq)-winlen+1, len(seq)): 
		fil_seq.append(seq[nt])
		
		if len(fil_seq) >= 60: 
			yield(''.join(fil_seq))
			fil_seq = []
		
# # Generate test sequence
# tseq = ''
# for i in range(180): tseq += random.choice('ATGC')
# 
# # Test sequence run
# print(tseq)
# for seq in (tseq, winlen, sthresh): print(seq)

# Performs an entropy filter on a given DNA sequence fasta file based on 
# given window length and entropy threshold, printing the filtered sequence 
for seq in mcb185.read_fasta(seq):
	print('>'+seq[0])
	for line in seq[1:]:
		for nts in scal_slide(line, winlen, sthresh): print(nts)

"""
python3 42dust.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.fna.gz 11 1.4
>NC_000913.3 Escherichia coli str. K-12 substr. MG1655, complete genome
AGNTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTNNNNNNNAAAAAGAGTGTC
TGATAGCAGCTTCTGAACTGGTTACCTGCCGTGNNNNNNNNNNNATTTTATTGACTTAGG
TCACNNAATACTTTAACCAATATAGGCATAGCGCACAGNCNNNNAAAAATTACAGAGTNN
ACAACATCCATGAAACGCATTAGCACCACCATNNNNNNNACCATCACCATTACCACAGGT
AACNGTGCGGGCTGACGCGTACAGNNNNNNNNGAAAAAAGCCCGCACCTGACAGTGCNNN
NNNTTTTTTTCGACCAAAGGTAACGAGGTAACAACCATGCGAGTGTTGAAGTTCGGCGGT
ACATCAGTGGCAAATGCAGAACGTTTTCTGCGTGTTGCCGATATTCTGGAAAGCAATGCC
ANNCANGGGCAGGTGGCCANCGNNNNNNNTNNNCCCGNNNNNNNNNCCAACCACCTGGTG
GCGATNATTGNNAAAACCATTAGCGGCCAGGATGCTTTACCCAATATCAGCGATGCCGAA
...
"""
