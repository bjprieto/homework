# 40aacomp.py

# Make a program that reports the amino acid composition in a file of proteins

# Note: you are not allowed to import any libraries except gzip and sys

# Hint: gzip.open(sys.argv[1], 'rt')

# Variation: use 20 named variables
# Variation: use a list

import sys # to receive stdin as variables
import gzip # to unzip compressed data

def main(protfile):
	aas = [i for i in 'ACDEFGHIKLMNPQRSTVWY'] # amino acids
	prots = get_prots(protfile, aas)
	get_aacomp(prots, aas)

# In a file of protein sequences, processes the file by cutting out non-seq
# information and joining the sequences into a string
def get_prots(protfile, aas):
	
	# Set variables
	seq = ''
	
	# Process the protein sequences into one large sequence without the 
	# extraneous information
	for line in protfile:
		if line[0] in aas:
			line = line.rstrip()
			seq += line
		else: continue
		
	return seq

# Gives the amino acid composition given a sequence
def get_aacomp(seq, aas):

	# Set variables
	aan = [0]*20 # amino acid counts
	
	# Var1: Count each residue as you go down the sequence and present results
	# to stdout all at once. 2.02-2.15s
	
	# Count amino acid residues
	for residue in seq:
		for aa in aas:
			if residue == aa: aan[aas.index(aa)] += 1
		
	# Generate table of amino acid composition to stdout
	for aa, count in zip(aas, aan):
		print(aa, count, f'{count/len(seq):.4f}')
	
# 	# Var2: Go down the entire sequence counting for one residue and print
# 	# to stdout sequentially. 2.14-2.20s (slightly slower; expected)
# 	
# 	# Count amino acid residues.
# 	for aa in aas:
# 		for residue in seq:
# 			if residue == aa: aan[aas.index(aa)] += 1
# 		print(aa, aan[aas.index(aa)], f'{aan[aas.index(aa)]/len(seq):.4f}')

# Perform amino acid composition analysis
main(gzip.open(sys.argv[1], 'rt'))

"""
python3 40aacomp.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_protein.faa.gz
A 126893 0.0954
C 15468 0.0116
D 68213 0.0513
E 76890 0.0578
F 51796 0.0389
G 97830 0.0736
H 30144 0.0227
I 79950 0.0601
K 58574 0.0440
L 142379 0.1071
M 37657 0.0283
N 51896 0.0390
P 59034 0.0444
Q 59178 0.0445
R 73620 0.0554
S 76865 0.0578
T 71428 0.0537
V 94237 0.0709
W 20297 0.0153
Y 37628 0.0283
"""
