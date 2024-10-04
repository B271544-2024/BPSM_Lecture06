#!/bin/bash
awk -F'\t' 'BEGIN { OFS = "\t" } !/^#/ && $2 ~ /AEI/ { print $9 > "/localdisk/home/s2746775/Exercises/Lecture06/outfiles/AEI.out" }' /localdisk/home/s2746775/Exercises/Lecture06/blastoutput2.out
