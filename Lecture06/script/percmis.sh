#!/bin/bash
awk -F'\t' '!/^#/ {print $5 / $4 * 100 > "/localdisk/home/s2746775/Exercises/Lecture06/outfiles/percmis.out"}' /localdisk/home/s2746775/Exercises/Lecture06/blastoutput2.out
