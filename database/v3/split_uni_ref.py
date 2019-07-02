with open('features.fasta','r') as f:
	lines = f.readlines()

with open('uniprot.fasta', 'w') as fu:
	with open('reference.fasta', 'w') as fr:
		for i in range(0,len(lines),2):
			t = lines[i].split('|')[2]
			if t == 'UNIPROT':
				fu.write(lines[i])
				fu.write(lines[i+1])
			else:
				fr.write(lines[i])
				fr.write(lines[i+1])





