import gzip
import sys

def anti_seq(seq):
	"""get the reverse-complement of a sequence"""
	comp = str.maketrans('ACGTRYMKWSBDHVacgtrymkwsbdhv',
		'TGCAYRKMWSVHDBtgcayrkmwsvhdb')
	anti = seq.translate(comp)[::-1]
	return anti

def read_fasta(filename):
	"""iteratively read records from a FASTA file"""
	if   filename == '-':          fp = sys.stdin
	elif filename.endswith('.gz'): fp = gzip.open(filename, 'rt')
	else:                          fp = open(filename)
	name = None
	seqs = []
	while True:
		line = fp.readline()
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
