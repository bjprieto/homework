# kmerator7.py

# Takes a fasta file and kmer length and returns the found kmers and their 
# positions

import sys
import mcb185

# Initialize variables
fp = sys.argv[1]
k = int(sys.argv[2])
kmers = {}

for desc, seq in mcb185.read_fasta(fp):
# 	print(desc)
	for pos in range(len(seq)-1-k):
		kmer =  seq[pos:pos+k]
		if kmer not in kmers: kmers[kmer] = [pos]
		else:				  kmers[kmer].append(pos)

# for kmer, pos in kmers.items():
# 	print(kmer, pos)