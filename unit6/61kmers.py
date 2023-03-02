# 61kmers.py

# Make a program that reports the kmer counts for a fasta file
# Your program should take 2 arguments:
#    1. The file name
#    2. The size of k

# Hint: use argparse
# Hint: use mcb185.read_fasta()

import argparse # to take and process CLI arguments
import mcb185 # to read fasta

# Initialize argument parser
parser = argparse.ArgumentParser(
	description='Reports the kmer counts for a given nucleotide fasta file.'
)

# Take required arguments
parser.add_argument('file', type=str, metavar='<path>', 
	help='nucleotide fasta file')
parser.add_argument('klen', type=int, metavar='<int>', help='kmer length')

# Finish argument parser setup
arg = parser.parse_args()

# Get kmer counts
kmers = {} # dictionary of kmer_identity:count

for line in mcb185.read_fasta(arg.file):

	# Read only the sequence data, skipping the description
	for seq in line[1:]: 
	
		# Window slide for kmers
		for pos in range(len(seq)-arg.klen+1): 
			
			kmer = seq[pos:pos+arg.klen]
		
			# Tally kmers
			if kmer not in kmers: kmers[kmer] = 1
			else:				  kmers[kmer] += 1

# Print results
for kmer in sorted(kmers):
	print(kmer, kmers[kmer])

"""
python3 60kmers.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.fna.gz 2
AA 338006
AC 256773
AG 238013
AT 309950
CA 325327
CC 271821
CG 346793
CT 236149
GA 267384
GC 384102
GG 270252
GT 255699
TA 212024
TC 267395
TG 322379
TT 339584
"""
