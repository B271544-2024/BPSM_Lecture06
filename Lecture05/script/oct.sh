#!/bin/bash
count=0;while IFS=$'\t' read name email city birthday_day birthday_month birthday_year country; do if [ "$name" != "name" ] && [ "$name" != "" ]; then count=$((count+1)); if [ $birthday_month -eq 10 ]; then echo -e "${count}\t${name}\t${birthday_month}\t${country}" >> /localdisk/home/s2746775/Exercises/Lecture05/outfiles/oct.txt; fi; fi; done < /localdisk/home/s2746775/Exercises/Lecture05/example_people_data.tsv
cut -f4 oct.txt | sort | uniq -c | sort -k1,1nr | tee >(wc)
