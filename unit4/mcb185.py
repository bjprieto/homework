# mcb185.py

import sys
import gzip

def read_fasta(filename):

	if   filename == '-':          fp = sys.stdin
	elif filename.endswith('.gz'): fp = gzip.open(filename, 'rt')
	else:                          fp = open(filename)

	name = None
	seqs = []

	while True:
		line = fp.readline();
		if line == '': break
		line = line.rstrip()
		if line.startswith('>'):
			if len(seqs) > 0:
				yield(name, ''.join(seqs))
				name = line[1:]
				seqs = []
			else:
				name = line[1:]
		else:
			seqs.append(line)

	yield(name, ''.join(seqs))
	fp.close()

def translate(tslr, cseq, rf):
	
	pseq = ''

	for pos in range(rf-1, len(cseq), 3):
		
		cd = cseq[pos:pos+3].upper()
		
		if cd in tslr: pseq += tslr[cd]
		else:			pseq += 'X'
		
		if pseq[-1] == '*': return pseq
