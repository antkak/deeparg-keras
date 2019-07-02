import sys
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

# This script makes a set of reads from the input fasta file. For sequences with low number of reads, it does oversampling. When making a training/test prediction this code should be used only and only in the TRAINING step. NEVER USE IT FOR THE VALIDATION SET!.
# This script should be used also for making the production (released to public) models. 

def chunkstring(string, length):
    pieces = range(0, len(string), length)+range(length/2, len(string), length) + range(length/3, len(string), length);
    return (string[0+i:length+i] for i in pieces)

fi=sys.argv[1] # fastafile from besthit
fo=sys.argv[2]
tag=sys.argv[3]
read_length = sys.argv[4]

# input output tag 

minory_class = {
    # "beta_lactam":5136,
    # "bacitracin":4200,
    # "macrolide-lincosamide-streptogramin":1109,
    # "aminoglycoside":915,
    # "polymyxin":879,
    # "multidrug":875,
    # "chloramphenicol":600,
    # "fosfomycin":291,
    # "tetracycline":271,
    # "glycopeptide":209,
    # "quinolone":147,
    # "trimethoprim":83,
    # "unknown":56,
    "kasugamycin":33,
    "rifampin":24,
    "fosmidomycin":23,
    "sulfonamide":21,
    "peptide":13,
    "tetracenomycin":8,
    "aminocoumarin":6,
    "fusidic_acid":6,
    "mupirocin":5,
    "thiostrepton":4,
    "triclosan":4,
    "qa_compound":3,
    "streptothricin":3,
    "tunicamycin":3,
    "na_antimicrobials":2,
    "puromycin":2,
    "elfamycin":1,
    "nitrofuratoin":1
}

reads=[]

for record in SeqIO.parse(fi, "fasta"):
    seqn = str(record.seq);
    id = record.id.replace('|FEATURES', '');

    try:
        rep = 50 - minory_class[id.split('|')[2]]
        minory_class[id.split('|')[2]] = minory_class[id.split('|')[2]] + 1;
    except:
        rep = 1
    
    l=0
    for r in range(rep):
        chunks = chunkstring( seqn, int(read_length) );
        for k in chunks:
            if len(k)>25:
                rseq = Seq(k);
                rid = tag+"_"+id+'|'+str(l);
                reads.append(SeqRecord(rseq, id=rid, name='', description=''));
                l+=1;
            
SeqIO.write(reads, open(fo, 'w'), 'fasta')