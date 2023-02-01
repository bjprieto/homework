# 26anti.py

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

# Variation: try this with the range() function and slice syntax

dna = 'ACTGAAAAAAAAAAA'


# Initialize variables
r_comp = '' # Reverse complement strand seq

# Iterate over each nucleotide in the seq while generating the reversed
# complement strand seq
for i in range(0, len(dna), 1):
	nt = dna[i-1]
	if nt == 'A':   r_comp += 'T'
	elif nt == 'T': r_comp += 'A'
	elif nt == 'G': r_comp += 'C'
	else:           r_comp += 'G'
	
print(r_comp)

"""
python3 26anti.py
TTTTTTTTTTTCAGT
"""
