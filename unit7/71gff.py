# 71gff.py

# Write a program that converts genes in gff into JSON
# Use the minaturized version of the C. elegans genome (included) this time
# Organize the genes onto chromosomes
# Print the number of genes on each chromosome to stderr
# Your code should mimic the output below

# Hint: your outer data structure is a dictionary

# Note: gene names are stored differently here than the last file




import argparse # Take CLI arguments
import gzip # Open and read gff
import re # Extract genes
import json # Report extracted genes



# Initialize argument parser
parser = argparse.ArgumentParser(description=
	'Converts eukaryotic gene information from a gff file into JSON.')
parser.add_argument('file', type=str, metavar='<path>', help='gff file')
arg = parser.parse_args()



# Goes through each line and extracts gene information if present on the line
with gzip.open(arg.file, 'rt') as fp:
	
	# Initialize important variables
	genome = {} # all chromosomes and their respective genes
	chr = None  # chromosome
	# lineN = 0 # find semantic errors (1/2)
	
	for line in fp.readlines():
		
		## Find semantic errors (2/2)
		# lineN += 1 
 		# print(lineN)
 		
 		# Search for gene entries
		if re.search('gene\s+\d', line):
		
			if re.search('\w+', line).group() != chr: 
				
				# Return previous chromosome gene entries if on to a new one
				if chr != None: genome[f"{chr}"] = genes
				
				# Set up new chromosome ID and new gene
				chr = re.search('\w+', line).group()
				genes = []
		
			# Extract relevant information
			gen_dict = {} # genes on the current chromosome
			gene     = re.search('(Alias=)(\S+)', line).group(2) # gene name
			span     = re.search('(gene\s+)(\d+)(\s+)(\d+)', line) # gene locus
			strand   = re.search('[+-]', line).group() # which strand
			
			# Store relevant information
			gen_dict["gene"]   = f"{gene}"
			gen_dict["beg"]    = f"{span.group(2)}"
			gen_dict["end"]    = f"{span.group(4)}"
			gen_dict["strand"] = f"{strand}"
			
			# Return gene entry
			genes.append(gen_dict)
	
	# Return last chromosome gene entries
	genome[f"{chr}"] = genes



# Report results
for chr in genome.keys(): print(chr, len(genome[chr])) # gene count per chr
print(json.dumps(genome, indent = 4)) # report gene entries

"""
python3 71gff.py elegans
I 37
II 57
III 37
IV 41
MtDNA 2
V 41
X 45
{
    "I": [
        {
            "gene": "Y74C9A.6",
            "beg": 3747,
            "end": 3909,
            "strand": "-"
        },
        {
            "gene": "Y74C9A.3",
            "beg": 4116,
            "end": 10230,
            "strand": "-"
        },
...
"""
