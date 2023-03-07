# 62orfs.py

# Make a program that finds open reading frames in the E. coli genome
# Your program should read a fasta file
# There should be an optional minimum ORF size with a default value of 300 nt
# The output should be a table showing 4 columns
#     1. parent sequence identifier
#     2. begin coordinate
#     3. end coordinate
#     4. strand
#     5. first 10 amino acids of the protein

# Hint: use argparse, mcb185.read_fasta(), and mcb185.translate()
# Hint: don't use the whole genome for testing

# Note: your genes should be similar to those in the real genome

import argparse
import mcb185
import re

parser = argparse.ArgumentParser(
	description='Finds open reading frames for each given nucleotide FASTA file\
	 and returns the identifier, range, and first 10 amino acids'
)
	
parser.add_argument('file', type=str, metavar='<path>', help='fasta file')
parser.add_argument('-l', type=int, metavar='<int>', required=False,
	default=300, help='minimum ORF size [%(default)i]')

arg = parser.parse_args()

anti = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}

# non re version
# def get_orfs(seq, strand):
# 	orfs = []
# 	start_pos = 0
# 
# 	while True:
# 		for pos in range(start_pos, len(seq)-1):
# 			cd = seq[pos:pos+3]
# 			if cd == 'ATG':
# 				pseq = mcb185.translate(seq[pos:], 1)
# 				if pseq == None: break
# 				if len(pseq) >= (arg.l/3):
# 					orfs.append((iden, pos+1, pos+len(pseq)*3, strand,
# 								 pseq[:10]))
# 					start_pos = pos+len(pseq)*3
# 					break
# 		if pseq == None or start_pos >= (len(seq)-arg.l): return orfs

# re version (non-functional)
# def get_orfs(seq, strand):
# 	orfs = []
# 	start_pos = 0
# 	count = 0
# 
# 	while True:
# 		cd = re.search('ATG', seq[start_pos:])
# 		pseq = mcb185.translate(seq[cd.start():], 1)
# 		if pseq == None: break
# 		end = cd.start()+len(pseq)*3
# 		print(end)
# 		start_pos = end+1
# 		
# 		count += 1
# 		if count == 10: break
# 		
# 		if len(pseq) >= (arg.l/3):
# 			orfs.append((iden, pos+1, end, strand, pseq[:10]))
# 		if pseq == None or start_pos >= (len(seq)-arg.l): return orfs



for desc, seq in mcb185.read_fasta(arg.file):
	iden = re.search('\w+.\S+', desc)
	iden = iden.group()
	
	aseq = ''
	for nt in seq[::-1]: aseq += anti[nt]
	print(mcb185.translate(seq[::-1], 3))

# 	all_orfs = get_orfs(aseq, '-')
# 	all_orfs = get_orfs(seq, '+')
# 	all_orfs = all_orfs + get_orfs(seq, '+')

# for iden, start, end, strand, pseq in all_orfs:
# 	print(iden, start, end, strand, pseq)

"""
python3 62orfs.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.fna.gz
NC_000913.3 108 500 - MVFSIIATRW
NC_000913.3 337 2799 + MRVLKFGGTS
NC_000913.3 2801 3733 + MVKVYAPASS
NC_000913.3 3512 4162 - MSHCRSGITG
NC_000913.3 3734 5020 + MKLYNLKDHN
NC_000913.3 3811 4119 - MVTGLSPAIW
NC_000913.3 5310 5738 - MKIPPAMANW
NC_000913.3 5683 6459 - MLILISPAKT
NC_000913.3 6529 7959 - MPDFFSFINS
NC_000913.3 7366 7773 + MKTASDCQQS
"""