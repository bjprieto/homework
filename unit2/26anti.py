# 26anti.py

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

# Variation: try this with the range() function and slice syntax

dna = 'ACTGAAAAAAAAAAA'


# Initialize variables
comp = '' # Complement strand DNA, written in the 5' to 3' direction

# Iterate over each nucleotide in the seq while generating the complement 
# strand seq
for i in range(len(dna), 0, -1):
	nt = dna[i-1]
	if nt == 'A': comp += 'T'
	elif nt == 'T': comp += 'A'
	elif nt == 'G': comp += 'C'
	else: comp += 'G'
print(comp)

"""
python3 26anti.py
TTTTTTTTTTTCAGT
"""
