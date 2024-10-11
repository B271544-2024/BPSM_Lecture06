#!/bin/bash
count=0
while IFS=$'\t' read name email city birthday_day birthday_month birthday_year country; do if [ "$name" != "name" ] && [ "$name" != "" ]; then count=$((count+1));echo -e "${count}\t${name}\t${city}\t${country}" >> "/localdisk/home/s2746775/Exercises/Lecture05/outfiles/peopleincountry/${country// /}.txt"; fi; done < /localdisk/home/s2746775/Exercises/Lecture05/example_people_data.tsv
