#!/bin/bash

X=91
while  [  $X -le 120 ]
do
cd  TRAJ$X/
echo TRAJ$X/
rm -r TEMP
cp INFO_RESTART/control.dyn .
sbatch batch_job.sh
cd ../
X=$((X+1))
done
