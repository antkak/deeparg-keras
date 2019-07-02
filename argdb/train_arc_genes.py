
import sys
import os

path = sys.argv[1]
version = sys.argv[2]

os.system("mkdir -p "+path+"/"+version)

# path = '.'

import process_blast

# load the alignment sequences (samples) from where the model is trained.
alignments1 = process_blast.make_alignments_json(
    path+"/database/"+version+"/train_genes.tsv", iden=30, eval=1, len=25, BitScore=True)

# create the dataset for modeling the classifier.


import make_XY
data = make_XY.make_xy2(alignments1)

# train a deep learning algorithm. it uses 70% for training and 30% for validation. There is not negative dataset here
# For production it uses the whole dataset for training, there is not testing step!

import train_deepARG
deepL = train_deepARG.main(data)

#   this is used to store the parameters of the neural network.

import cPickle
cPickle.dump(deepL['parameters'], open(
    path+"/model/"+version+"/metadata_LS.pkl", "w"))
deepL['clf'].save_params_to(path+"/model/"+version+"/model_LS.pkl")
