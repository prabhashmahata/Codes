#!/bin/bash
#SBATCH --job-name=single_water     # Job name
#SBATCH -p SHORT               # Partition
#SBATCH -N 1                  # Number of nodes
#SBATCH -n 8                 # Number of CPU cores
#SBATCH -t 4:00:00            # Job time
#SBATCH --mem=100GB           # Min memory requested per node (MB)
##SBATCH -A p32761            # Project number
#SBATCH --mail-type=ALL
#export dftb
echo "Starting date" 'date'
module load orca/6.0.0
module load mpi/ompi-4.1.1-gnu
module list
/share/apps/orca/6.0.0/bin/orca test.inp > test.log
echo "End date" 'date'
