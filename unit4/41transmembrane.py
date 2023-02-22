# 41transmembrane.py

# Write a program that predicts which proteins in a proteome are transmembrane

# Transmembrane proteins are characterized by having
#    1. a hydrophobic signal peptide near the N-terminus
#    2. other hydrophobic regions to cross the plasma membrane

# Both the signal peptide and the transmembrane domains are alpha-helices
# Therefore, they do not contain Proline

# Hydrophobicity can be measured by Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot

# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa

# Hint: copy mcb185.py to your homework repo and import that
# Hint: create a function for KD calculation
# Hint: create a function for hydrophobic alpha-helix
# Hint: use the same function for both signal peptide and transmembrane

import sys
import mcb185
	
# Read a fasta file and determine potential transmembrane proteins
def get_tmprot(protfile):
	
	# Check block (1/3)
# 	count = 0

	for desc, seq in mcb185.read_fasta(protfile):

		# Check block (2/3)
# 		print(desc, seq[:30]+'//'+seq[30:], sep ='\n')

		# Determine if the sequence has a signal peptide
		has_sig = has_hahelix(seq[:30], 8, 2.5)

		# Determine if the sequence has a transmembrane domain
		has_tmem = has_hahelix(seq[30:], 11, 2.0)

		# Check block (3/3)
# 		if has_sig == True and has_tmem == True: 
# 			print('\n')
# 			count += 1
# 		if count == 3: break
		
		# Print results
		if has_sig == True and has_tmem == True: print(desc)

def score_kd(seq):
	
	# Initialize variables
	kd_sum = 0 # hydropathy sum
	aas = 'IVLFCMAGTSWYPHEQDNKR' # all amino acid one-letter codes
	
	# Corresponding hydropathy scores 
	# for each amino acid in the same order as aas
	scores = [4.5, 4.2, 3.8, 2.8, 2.5, 1.9, 1.8, -0.4, -0.7, -0.8, -0.9, -1.3,
	-1.6, -3.2, -3.5, -3.5, -3.5, -3.5, -3.9, -4.5] 
	
	# Calculate hydropathy score
	for residue in seq:
		for aa in aas:
			if residue == aa: kd_sum += scores[aas.index(aa)]
	
	# Kyte-Doolittle hydropathy score
	kd = kd_sum/len(seq) 
		
	return kd

def has_hahelix(seq, w_len, thresh):
	for pos in range(len(seq) - w_len + 1):
		
		# Enable window sliding
		window = seq[pos:pos + w_len]
		
		# Calculate KD value
		kd = score_kd(window)
		
		# Determine if the window is capable of having a hydrophobic alpha helix
		# based on the given threshold
		if kd > thresh and 'P' not in window:
			# print(window, pos, kd, sep = '\t') # check
			return True
		else: continue
		
	return False



# Generate and test a random sequence with the main parts of main()
# import random
# 
# for i in range(3):
# 
# 	# Generate and print the random sequence
# 	seq = ''
# 	for nt in range(60): seq += random.choice('IVLFCMAGTSWYPHEQDNKR')
# 	print(seq[:30]+'//'+seq[30:], sep ='\n')
# 
# 	# Determine if the sequence has a signal peptide
# 	has_sig = has_hahelix(seq[:30], 8, 2.5)
# 
# 	# Determine if the sequence has a transmembrane domain
# 	has_tmem = has_hahelix(seq[30:], 11, 2.0)
# 
# 	# Print results
# 	if has_sig == True and has_tmem == True: print('\n')
# 	else: print('NO\n')



# Return transmembrane proteins in the file
get_tmprot(sys.argv[1])

"""
python3 41transmembrane.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_protein.faa.gz
NP_414560.1 Na(+):H(+) antiporter NhaA [Escherichia coli str. K-12 substr. MG1655]
NP_414568.1 lipoprotein signal peptidase [Escherichia coli str. K-12 substr. MG1655]
NP_414582.1 L-carnitine:gamma-butyrobetaine antiporter [Escherichia coli str. K-12 substr. MG1655]
NP_414607.1 DedA family protein YabI [Escherichia coli str. K-12 substr. MG1655]
NP_414609.1 thiamine ABC transporter membrane subunit [Escherichia coli str. K-12 substr. MG1655]
NP_414653.1 protein AmpE [Escherichia coli str. K-12 substr. MG1655]
NP_414666.1 quinoprotein glucose dehydrogenase [Escherichia coli str. K-12 substr. MG1655]
NP_414695.1 iron(III) hydroxamate ABC transporter membrane subunit [Escherichia coli str. K-12 substr. MG1655]
NP_414699.1 PF03458 family protein YadS [Escherichia coli str. K-12 substr. MG1655]
NP_414717.2 CDP-diglyceride synthetase [Escherichia coli str. K-12 substr. MG1655]
...
"""
