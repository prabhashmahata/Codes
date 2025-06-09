#!/bin/bash

X=1
while  [  $X -le 56 ]
do
echo p$X
cp totalen.py  p$X
cd p$X
python3 totalen.py
cd ../
cat  p$X/totalenergy.csv >> energy.csv

X=$((X+1))

done
