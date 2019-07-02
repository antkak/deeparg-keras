from Bio import SeqIO
from Bio.Seq import Seq
import sys
from Bio.SeqRecord import SeqRecord


fo = sys.argv[2]
kmer_size = int(sys.argv[4])
tag = sys.argv[3]

step = 5;

reads = []

for record in SeqIO.parse(open(sys.argv[1]),'fasta'):
    seq = str(record.seq);
    j=0
    for i in range(0, len(seq)-kmer_size,step):
        key = tag+'_'+record.id+'|'+str(j)
        reads.append(SeqRecord(Seq(seq[i:i+kmer_size]), id=key, name='', description=''));
        j+=1

SeqIO.write(reads, open(fo, 'w'), 'fasta')