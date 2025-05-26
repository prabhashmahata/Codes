#!/bin/bash

X=1
while [ $X -le 150 ]
do
echo TRAJ$X
cp  -rf TRAJ$X runtraj1to150
X=$((X+1))
done

