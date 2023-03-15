# 70gff.py

# Write a program that converts genes in gff into JSON
# Use the E. coli genome gff
# Your code should mimic the output below

import argparse # take CLI arguments
import gzip # read zipped file
import re # extract relevant info
import json # report results

# Initialize argument parser
parser = argparse.ArgumentParser(
	description='Takes genes from a gff file and converts information in JSON.')
parser.add_argument('file', type=str, metavar='<path>', help='gff file')
arg = parser.parse_args()

# Initialize genes list
genes = []

# Get gene information
with gzip.open(arg.file, 'rt') as fp:
	for line in fp.readlines():
	
		if re.search('RefSeq\s+gene', line):
		
			# Extract relevant information
			gen_dict = {}
			gene     = re.search('(gene=)(\w+)', line).group(2)
			span     = re.search('(gene\s+)(\d+)(\s+)(\d+)', line)
			strand   = re.search('[+-]', line).group()
			
			# Store relevant information
			gen_dict["gene"]   = f"{gene}"
			gen_dict["beg"]    = f"{span.group(2)}"
			gen_dict["end"]    = f"{span.group(4)}"
			gen_dict["strand"] = f"{strand}"
			
			genes.append(gen_dict)

# Report results
print(json.dumps(genes, indent = 4))

"""
python3 70gff.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.gff.gz
[
    {
        "gene": "thrL",
        "beg": 190,
        "end": 255,
        "strand": "+"
    },
    {
        "gene": "thrA",
        "beg": 337,
        "end": 2799,
        "strand": "+"
    },
...
"""
