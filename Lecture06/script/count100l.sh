#!/bin/bash
awk -F'\t' 'BEGIN { OFS = "\t" } !/^#/ && $4 < 100 { print $0 }' /localdisk/home/s2746775/Exercises/Lecture06/blastoutput2.out | wc -l | cut -d $'\t' -f 1 > ../outfiles/count100l.out
