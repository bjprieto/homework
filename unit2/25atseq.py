# 25atseq.py

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence

# Note: set random.seed() if you want repeatable random numbers

# Initialize module and variables
import random
at_sum = 0 # Count of AT nucleotides in the seq
seq = '' # DNA seq

# Produce a random string seq of nucleotides with length 30
for i in range(30):
	nt = random.choice('ATGC')
	if nt == 'A' or nt == 'T': at_sum += 1
	seq += nt	

# Print seq length, AT fraction, and seq
print(len(seq), at_sum/len(seq), seq)	

"""
python3 25atseq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
