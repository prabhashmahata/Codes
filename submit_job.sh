#!/bin/bash

X=126
while  [  $X -le 150 ]
do
cd  TRAJ$X/
sbatch batch_job.sh
cd ../
X=$((X+1))
done
