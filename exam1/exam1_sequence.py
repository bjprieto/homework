import random

# Initialize variables
n = 10*2
x = 0.5941
seq = ''


# Generate random sequence
for i in range(n):
	r = random.random()
	if r < x: seq += random.choice('CG')
	else: seq += random.choice('AT')

# Get percent nucleotides
a = 0
t = 0
g = 0
c = 0

for nt in seq:
	if nt == 'A': 	a += 1
	elif nt == 'T': t += 1
	elif nt == 'G': g += 1
	else:			c += 1

print(a/n, t/n, g/n, c/n)

# Print kmers, reveal palindromes
print(seq)
k = 3
for i in range(len(seq) -k+1):
	k2 = k // 2
	kmer = seq[i:i+k]
	first = kmer[:k2]
	second = kmer[-k2:]
	rc = ''
	for nt in second: 
		if nt == 'A': rc += 'T' 
		if nt == 'T': rc += 'A' 
		if nt == 'G': rc += 'C' 
		if nt == 'C': rc += 'G' 
	print(kmer, end='')
	if first == rc: print('*', end='')
	print('')