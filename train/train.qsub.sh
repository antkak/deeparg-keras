#!/bin/bash
#PBS -l nodes=1:ppn=1:gpus=1
#PBS -l walltime=20:00:00
#PBS -q normal_q
#PBS -A computeomics
#PBS -W group_list=newriver


source /work/newriver/gustavo1/deeparg/venv/bin/activate

module load jdk/1.8.0 cuda/7.0.28 gcc/4.7.2 atlas/3.11.36  openmpi/1.8.5
python /groups/metastorm_cscee/deepARG/deeparg-ss/argdb/train_arc.py
# python /groups/metastorm_cscee/deepARG/deeparg-ss/argdb/train_arc_genes.py

exit;
