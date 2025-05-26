#!/bin/bash

X=301
while  [  $X -le 400 ]
do
##cd  TRAJ$X/
##echo TRAJ$X
##cd RESULTS
##$NX/dynout2xyz.pl
##cp  dyn.xyz  trajmovie$X
##cp -f trajmovie$X ../../movie1 
tail -15 trajmovie$X > fincoord$X
cp fincoord$X  coord_movie
##cd ../../
X=$((X+1))
done
