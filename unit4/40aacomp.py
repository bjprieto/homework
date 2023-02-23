# 40aacomp.py

# Make a program that reports the amino acid composition in a file of proteins

# Note: you are not allowed to import any libraries except gzip and sys

# Hint: gzip.open(sys.argv[1], 'rt')

# Variation: use 20 named variables
# Variation: use a list

import sys # to receive stdin as variables
import gzip # to unzip compressed data

# Report amino acid composition of a fasta file of protein sequences	
protfile = gzip.open(sys.argv[1], 'rt') # protein sequence fasta file

# Initialize variables
seq = ''

# Process the protein sequences into one large sequence without the 
# extraneous information
for line in protfile:
	if line[0] != '>':
		line = line.rstrip()
		seq += line
	else: continue

aas = [i for i in 'ACDEFGHIKLMNPQRSTVWY'] # amino acids
aan = [0]*20 # amino acid counts
aacomps = []

# Count amino acid residues and yield amino acid compositions
for aa in aas:
	for residue in seq:
		if residue == aa: aan[aas.index(aa)] += 1
	aacomp = aa, aan[aas.index(aa)], f'{aan[aas.index(aa)]/len(seq):.4f}'
	aacomps.append(aacomp)

for nt_stats in aacomps: 
	print(nt_stats[0], nt_stats[1], nt_stats[2])

protfile.close()

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
