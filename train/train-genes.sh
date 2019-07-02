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

python $rootdir/argdb/train_arc_genes.py


