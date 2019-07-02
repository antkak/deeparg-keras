import sys
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

''' 
    This script is designed for building a set of training genes when the classes don't have enough # of genes. For instance, if some categories only have 2 genes, it is better to oversaple the same gene multiple times, thus, there are more data that represent that category.
'''

fi=sys.argv[1] # fastafile from besthit
fo=sys.argv[2] # output file
tag=sys.argv[3] # tag used for start of the genes

# input output tag
minority_class = {}

for record in SeqIO.parse(fi, "fasta"):
    id = record.id.split('|');
    type = id[3]
    try:
        minority_class[type]+=1
    except:
        minority_class[type] = 1;

genes=[]

print(minority_class)
l=0

for record in SeqIO.parse(fi, "fasta"):
    seqn = str(record.seq);
    id = record.id.replace('|FEATURES', '');
    
    type = record.id.split('|')[3];
    # print type

    try:
        
        if minority_class[type] < 20:
            # print minority_class[type]
            rep =  20 - minority_class[type]
            # print minority_class[type]+2
            minority_class[type] = minority_class[type] + 1;
        else:
            rep = 1 
    except:
	    rep = 1

    for r in range(rep):
        rid = str(l)+"_"+tag+"_"+id;
        genes.append(SeqRecord(record.seq, id=rid, name='', description=''));
        l+=1;

fo = open(fo, "w")
SeqIO.write(genes, fo, "fasta")

print(minority_class)