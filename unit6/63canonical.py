# 63canonical.py

# You probably learned that ATG is the only start codon, but is it?
# Write a program that reports the start codons from the E. coli genome
# Your program must:
#    1. read GCF_000005845.2_ASM584v2_genomic.gbff.gz at the only input
#    2. use a regex to find CDS coordinates
#    3. count how many different start codons there are

# Note: the sequence is at the end of the file
# Note: genes on the negative strand are marked complement(a..b)

# Hint: you can read a file twice, first to get the DNA, then the CDS
# Hint: check your CDS by examining the source protein

import re # extract relevant info
import argparse # take CLI arguments
import gzip # for file handling



# Initialize argument parser
parser = argparse.ArgumentParser(
	description = 'Reports start codon counts from a gbff file.')
	
parser.add_argument('file', type=str, metavar='<path>', help='gbff file')

arg = parser.parse_args()



# Initialize key variables
anti = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
starts = {}
cds = {}



# Get start codons
with gzip.open(arg.file, 'rt') as fp:

	for line in fp.readlines():
	
		# Get start codon positions
		pos_match = re.search('(CDS\s+)(\D+)(\d+)(\.\.)(\d+)', line)
		if pos_match:
		
			# Process the codon positions based on the strand
			comp_match = re.search('complement', line)
			
			if comp_match:
				start = int(pos_match.group(5))
				is_comp = True
					
			else: 
				start = int(pos_match.group(3))
				is_comp = False
				
			starts[start] = is_comp
			# print(pos_match.group(), start, is_comp) # check 

## Check format
# for x, y in starts.items(): print(x, y)

# Get genome
with gzip.open(arg.file, 'rt') as fp:

	# Initialize variables
	found_genome = False
	seq_str = ''

	# Skip over all lines until the genome is found, then extract the full seq
	for line in fp.readlines():
		is_genome = re.search('ORIGIN', line)
		
		if is_genome: 
			found_genome = True
			continue
		
		if found_genome == True:
			seqs = re.finditer('[atgc]\w+', line)
			for seq in seqs: seq_str += seq.group().upper()
			
# Get start codon counts
for pos in starts.keys():

	# Get codon based on start position and which strand it's on
	if starts[pos] == True:
		cd = ''
		acd = seq_str[pos-3:pos]
		for nt in acd[::-1]: cd += anti[nt]
	else: cd = seq_str[pos-1:pos+3-1]
	
	# Save start codon
	if cd not in cds: cds[cd] = 1
	else:			  cds[cd] += 1
	
# Report results
# obs = 0 # check count sum (1/4)
# expected = 3883+338+80+14 check count sum (2/4)

for cd, count in cds.items(): 
	print(cd, count)
	
# 	obs += count (3/4)
# print(obs, expected) # check count sum(4/4)
# don't know why, but I'm missing one ATG codon somewhere; will revisit

"""
python3 63canonical.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.gbff.gz
ATG 3883
GTG 338
TTG 80
ATT 5
AGT 1
AAA 1
AGC 1
TTC 1
TAA 1
CGT 1
CTG 2
GAC 1
"""
