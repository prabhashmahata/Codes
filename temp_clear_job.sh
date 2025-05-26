#!/bin/bash

X=1
while  [  $X -le 150 ]
do
cd  TRAJ$X/
echo TRAJ$X/
rm -r TEMP
rm -r DEBUG/TEMP
cd ../
X=$((X+1))
done
