#!/bin/bash
count=0
unset IFS
IFS=$'\t'
while read name email city birthday_day birthday_month birthday_year country; do if [ "$name" != "name" ] && [ "$name" != "" ]; then count=$((count+1)); echo -e "${count}\t${name}\t${city}\t${country}" >> noblank.txt; fi; done < example_people_data.tsv
