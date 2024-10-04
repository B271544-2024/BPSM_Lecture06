#!/bin/bash
awk -F'\t' '!/^#/ { print $2 > "/localdisk/home/s2746775/Exercises/Lecture06/outfiles/subacc.out" }' /localdisk/home/s2746775/Exercises/Lecture06/blastoutput2.out
