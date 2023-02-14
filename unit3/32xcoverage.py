# 32xcoverage.py

# Write a program that simulates a shotgun resequencing project
# How uniformly do the reads "pile up" on a chromosome?
# How much of that depends on sequencing depth?

# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line

# Hint: make the problem smaller, so it's easier to visualize and debug
# Hint: if you don't understand the context of the problem, ask for help
# Hint: if you are undersampling the ends, do something about it

# Note: you will not get exactly the same results as the command line below

import sys
import random

# Initialize conditions
gsize = int(sys.argv[1]) # genome size
geno = [0]*gsize         # read counts for every nucleotide in the genome
readn = int(sys.argv[2]) # number of reads to perform
readl = int(sys.argv[3]) # length of reads

# Perform reads
for read in range(readn):
	pos = random.randint(0, gsize-readl) # position
	for i in range(readl): geno[pos+i] += 1
	# print(pos) # check

# Trim undersampled ends of the genome
genoW = geno[readl:-readl]

# I found that frequently, positions readl+1 and readl-1 weren't all that
# undersampled, but it was more accurate to exclude those positions in
# case they happened to be undersampled for further calculations

# Check block
# print(geno)
# print(genoW)

# Calculate stats
min = min(genoW)
max = max(genoW)
avg = sum(genoW)/len(genoW)

# Print results
print(min, max, f'{avg:.5f}')

"""
Archived suboptimal code

# Exclude the undersampled ends from calculations
start = None                      # start position of the 'working genome'
end = None                        # end position of the 'working genome'
genoS = [reads for reads in geno] # 'sorted genome' to organize read counts
genoS.sort()

# First quartile of the read counts as lowest tolerated value for end trimming
tol = genoS[int(len(geno)/4)] 

# Determine start of the working genome
for reads in range(len(geno)-1):
	if geno[reads] >= tol: 
		start = reads
		break

# Determine end of the working genome
for reads in range(-1, -len(geno)-1, -1):
	if geno[reads] >= tol: 
		end = reads + 1
		break

# Create working genome based on determined ends
if end != 0: genoW = geno[start:end] # 'working genome' for calculations
else:        genoW = geno[start:]
"""		

"""
python3 32xcoverage.py 1000 100 100
5 20 10.82375
"""
