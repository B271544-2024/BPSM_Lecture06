#!/bin/bash
awk -F'\t' 'BEGIN { OFS = "\t" } !/^#/ { print $3,$4 > "/localdisk/home/s2746775/Exercises/Lecture06/outfiles/alpID.out" }' /localdisk/home/s2746775/Exercises/Lecture06/blastoutput2.out
