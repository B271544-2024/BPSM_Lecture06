#!/bin/bash
awk -F'\t' 'BEGIN { OFS = "\t" } !/^#/ && $5 > 20 && $4 <100 { print $0 > "/localdisk/home/s2746775/Exercises/Lecture06/outfiles/l100al.out" }' /localdisk/home/s2746775/Exercises/Lecture06/blastoutput2.out
