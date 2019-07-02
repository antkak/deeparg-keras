#!/bin/bash
#PBS -q p100_normal_q
#PBS -l walltime=20:00:00
#PBS -l nodes=1:ppn=10:gpus=1
#PBS -A computeomics
#PBS -W group_list=newriver

echo "Allocated GPU with ID $CUDA_VISIBLE_DEVICES"
echo "Activate virtual environment: "
export PYTHONNOUSERSITE=True
source /groups/metastorm_cscee/deeparg/environments/deeparg/bin/activate
module load cuda/8.0.44 cudnn gcc atlas

rootdir=/home/gustavo1/deeparg-ss/
version='v2'

cd $rootdir
chmod +x ./bin/diamond
python ./train/generate_short_reads.py ./database/$version/features.fasta ./database/$version/train_reads.fasta train_reads 31
./bin/diamond blastp \
--db ./database/$version/features.dmnd \
--query ./database/$version/train_reads.fasta \
--id 30 --evalue 1e-10 --sensitive \
-k 20000 -p 10 \
-a ./database/$version/train_reads
./bin/diamond view -a ./database/$version/train_reads.daa -o ./database/$version/train_reads.tsv
python $rootdir/argdb/train_arc.py $rootdir $version


python ./train/generate_train_genes.py ./database/$version/features.fasta ./database/$version/train_genes.fasta train
./bin/diamond blastp \
--db ./database/$version/features \
--query ./database/$version/train_genes.fasta \
--id 30 --evalue 1e-10 --sensitive \
-k 20000 \
-a ./database/$version/train_genes
./bin/diamond view -a ./database/$version/train_genes.daa -o ./database/$version/train_genes.tsv
python $rootdir/argdb/train_arc_genes.py $rootdir $version