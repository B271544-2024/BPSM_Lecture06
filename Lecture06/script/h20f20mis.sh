#!/bin/bash
awk -F'\t' 'BEGIN { OFS = "\t" } !/^#/ && $5 < 20 { print $0 }' /localdisk/home/s2746775/Exercises/Lecture06/blastoutput2.out | head -20  > ../outfiles/h20f20mis.out
