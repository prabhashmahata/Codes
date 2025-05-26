#!/bin/bash

X=1
while  [  $X -le 100 ]
do
cd  TRAJ$X/
echo TRAJ$X
cd RESULTS
$NX/dynout2xyz.pl
cp  dyn.xyz  trajmovie$X
cp -f trajmovie$X ../../movie1 
cd ../../
X=$((X+1))
done
