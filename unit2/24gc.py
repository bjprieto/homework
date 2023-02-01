# 24gc.py

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT'

# Initialize loop variables
gc_count = 0 # Count of GC nucleotides in the seq
total_count = 0 # Total number of nucleotides in the seq

# Calculate GC%
for nt in dna:
	if nt == 'G' or nt == 'C': gc_count += 1
	total_count += 1

# Print Results
gc_perc = gc_count/total_count # Percent GC nucleotides in the seq
print(f'{gc_perc:.2f}')

"""
python3 24gc.py
0.42
"""
