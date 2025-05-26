#!/bin/bash

X=1
while  [  $X -le 5 ]
do
cd  TRAJ$X/
sbatch batch_job.sh
cd ../
X=$((X+1))
done
