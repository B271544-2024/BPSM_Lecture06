#!/bin/bash
awk -F'\t' 'BEGIN {OFS="\t"} !/^#/ {
	if ($NF >=400){
		print $0,400 >> "/localdisk/home/s2746775/Exercises/Lecture06/outfiles/group.out"
	} else if ($NF >= 300){
		print $0,300 >> "/localdisk/home/s2746775/Exercises/Lecture06/outfiles/group.out"
	} else if ($NF >= 200){
		print $0,200 >> "/localdisk/home/s2746775/Exercises/Lecture06/outfiles/group.out"
	} else if ($NF >= 100){
		print $0,100 >> "/localdisk/home/s2746775/Exercises/Lecture06/outfiles/group.out"
	} else {
		print $0,0 >> "/localdisk/home/s2746775/Exercises/Lecture06/outfiles/group.out"
	}
}' /localdisk/home/s2746775/Exercises/Lecture06/blastoutput2.out
