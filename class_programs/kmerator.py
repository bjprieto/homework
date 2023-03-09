# kmerator.py

# Reads a fasta file, and returns the expecte, observed, and log odd frequencies
# of each kmer given a klen. Written for nucleotide files, but works for protein
# fasta files as well

import mcb185
import sys
import math

# Take system inputs and initialize variables
file = sys.argv[1] # fasta file handle
klen = int(sys.argv[2]) # kmer length
nts = {} 
kmers = {}
nt_tot = 0 # count of all nts
kmer_tot = 0 # count of all kmers

# Take nt, kmer counts
for name, seq in mcb185.read_fasta(file):

	# Take nt counts
	for nt in seq:
		if nt not in nts: nts[nt] = 1
		else:			  nts[nt] += 1
		nt_tot += 1
	
	# Take kmer counts
	for pos in range(len(seq)-klen+1):
		kmer = seq[pos:pos+klen]
		if kmer not in kmers: kmers[kmer] = 1
		else:				  kmers[kmer] += 1
		kmer_tot += 1

# Check block (1/2): Counts
# for nt, count in nts.items(): print(nt, count)
# for kmer, count in kmers.items(): print(kmer, count)

# Convert counts to freqs
for nt in nts: nts[nt] /= nt_tot
for kmer in kmers: kmers[kmer] /=  kmer_tot

# Check block (2/2): Freqs
# for nt, freq in nts.items(): print(nt, f'{freq:.3f}')
# for kmer, freq in kmers.items(): print(kmer, f'{freq:.3f}')

# Compare obs and expected freqs
for kmer in kmers:
	
	exp = 1 # expected frequency
	
	for nt in kmer: exp *= nts[nt]
	log_odd = math.log2(kmers[kmer]/exp)
	
	print(kmer, f'{kmers[kmer]:.3f}', f'{exp:.3f}', f'{log_odd:.3f}', sep='\t')