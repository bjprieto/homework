#!/usr/bin/env python3

# 50dust.py

# Write a better version of your 42dust.py program
# Your program must have the following properties

# 1. has option and default value for window size (DONE)
# 2. has option and default value for entropy threshold (DONE)
# 3. has a switch for N-based or lowercase (soft) masking (DONE)
# 4. works with uppercase or lowercase input files (DONE)
# 5. works as an executable (DONE)
# 6. outputs a FASTA file wrapped at 60 characters (DONE)

# Optional: make the algorithm faster (see 29gcwin.py for inspiration) (DONE)
# Optional: benchmark your programs with different window sizes using time 
# (DONE)

# Hint: make a smaller file for testing (e.g. e.coli.fna in the CLI below)



import argparse # for taking system inputs as arguments
import mcb185 # for reading fasta files
import math # for entropy calculations
import random # for testing randomly generating sequences

# Note: Way slower than previous unit's version (42dust) due to method used to 
# generate the filtered sequence with the full window sub; needs optimization

# Times
# 42dust | head == real: 0.448-0.467s (n = 5)
# 50dust | head == real: 13.496-13.843s (n = 5) (week 7)
# %diff 50:42 ~= 3000% slower >:(

# 50dust | head == real: 1.179-1.355 (n = 5) (week 9)
# %diff 50:42 ~= 280% slower, much better :)

# Note: Executable as '50dust'



# Initialize argument parser
parser = argparse.ArgumentParser(
	description='Reads a given nucleotide sequence FASTA file,\
	performs an entropy filter on it with a given window and threshold,\
	and returns the filtered sequence.')

# Set positional argument
parser.add_argument('file', type=str, metavar='<path>',
	help='nucleotide sequence fasta file')

# Set optional named arguments with default values
parser.add_argument('--w', required=False, type=int, metavar='<int>',
	default=11, help='entropy filter window size [%(default)i]')
parser.add_argument('--t', required=False, type=float,
	default=1.4, metavar='<float>', 
	help='entropy threshold [%(default).2f]')
parser.add_argument('--s', required=False, action='store_true',
	help='disable nucleotide masking [off]')

# Finish argument parser setup
arg = parser.parse_args()


# Entropy calculator for a given window sequence
def scal(win):

	# Initialize variables
	nts = ['A', 'T', 'G', 'C'] # list of nucleotide identities
	nt_counts = [0]*4 # count of each nucleotide in a given sequence
	nt_probs = [] # probabilities of each nucleotide in a given sequence
	h = 0 # Shannon entropy
	
	# Calculate probabilities
	
	# Take nuc counts
	for nt in win: 
		if nt in nts: nt_counts[nts.index(nt)] += 1
	
	# Convert counts to probs
	for count in nt_counts: nt_probs.append(count/len(win))
	
	# Calculate Shannon entropy given probs
	for prob in nt_probs:
		if prob != 0: h -= prob * math.log2(prob)
		
	return h
	
	
	
# Entropy filter
def sfil(seq, winlen):
 
	# Initialize variables
	win = seq[:winlen].upper() # sequence window
	fil_seq = [nt.upper() for nt in seq] # copy of entire sequence
	
	# Iterates over each window, replacing the original seq with a filtered one
	for pos in range(len(seq)):
	
		# Window sequence determined by window's start position
		if pos in range(len(seq)-winlen+1):
	
			# Slide window
			if pos != 0: win = (win[1:]+seq[pos+winlen-1]).upper()
		
			# Entropy
			h = scal(win)
		
			# Replace window if it fails the entropy threshold given settings
			
			# Unmasked/soft filtering
			if h < arg.t and arg.s == True:
				for nt in range(pos, pos+winlen):
					fil_seq[nt] = fil_seq[nt].lower()
			
			# Masked/hard filtering
			elif h < arg.t and arg.s == False:
				for nt in range(pos, pos+winlen):
					fil_seq[nt] = 'N'
		
		# Print sequence in rows of 60 characters
		if (pos+1) % 60 == 0: yield(fil_seq[pos-59:pos+1])
		
	# Print the remaining sequence
	if len(seq) % 60 != 0: yield(fil_seq[len(seq)-(len(seq)%60):])
		

# # Test functions with a randomly generated sequence
# # Initialize variables
# seq = '' 
# n = 121 # sequence length
# 
# # Generate a random sequence
# for i in range(n):
# 	seq += random.choice('ATG')
# 	
# # Check block
# print(seq+'\n')
# for i in sfil(seq, arg.w): print(i)

# Perform entropy filter on the given file
for desc, seq in mcb185.read_fasta(arg.file):

	# Print genome description
	print('>'+desc) 
	
	# Print the filtered sequence
	for line in sfil(seq, arg.w): print(''.join(line))

"""
python3 50dust.py -w 11 -t 1.4 -s e.coli.fna  | head
>NC_000913.3 Escherichia coli str. K-12 substr. MG1655, complete genome
AGcttttcattctGACTGCAACGGGCAATATGTCTCTGTGTggattaaaaaaagagtgTC
TGATAGCAGCTTCTGAACTGGTTACCTGCCGTGagtaaattaaaattttattgaCTTAGG
TCACtaaatactttaaCCAATATAGGCATAGCGCACAGacagataaaaattacaGAGTac
acaacatccaTGAAACGCATTAGCACCACCATtaccaccaccatcaccaTTACCACAGGT
AACggtgcgggctgACGCGTACAGgaaacacagaaaaaagccCGCACCTGACAGTGCggg
ctttttttttcgaCCAAAGGTAACGAGGTAACAACCATGCGAGTGTTGAAGTTCGGCGGT
ACATCAGTGGCAAATGCAGAACGTTTTCTGCGTGTTGCCGATATTCTGGAAAGCAATGCC
AggcaggggcaggtggCCAccgtcctctctgcccccgccaaaatcaccaaccacctGGTG
GCGATgattgaaaaaaccattaGCGGCCAGGATGCTTTACCCAATATCAGCGATGCCGAA
"""
