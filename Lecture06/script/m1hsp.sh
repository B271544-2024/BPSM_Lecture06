#!/bin/bash
cut -d $'\t' -f 2 /localdisk/home/s2746775/Exercises/Lecture06/blastoutput2.out | uniq -c | awk -F' ' '!/^#/ && $1 > 1 {print $0}' | wc -l |cut -d ' ' -f 1
