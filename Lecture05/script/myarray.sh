#!/bin/bash
# Set lots of variables
count=0; fnr=0; IFS=$'\t';
wantedcountry="Mozambique"
inputfile="/localdisk/home/s2746775/Exercises/Lecture05/example_people_data.tsv"
inputfilelength=$(wc -l ${inputfile} | cut -d ' ' -f1)
outputfile="/localdisk/home/s2746775/Exercises/Lecture05/outfiles/Country.${wantedcountry}.details"
# Initial actions
rm  -f *.details
unset my_array
declare -A my_array
# Main actions
while read name email city birthday_day birthday_month birthday_year country
do
fnr=$((fnr + 1))
# echo "Line number: ${fnr}"
if [ "$name" != "name" ] && [ "$name" != "" ] && [ "$country" == "$wantedcountry" ]
   then
   count=$((count+1));
   my_array[${count}]="${fnr}\t${name}\t${country}"
   # echo -e "${my_array[${count}]}"
fi
# End of the file
if test ${fnr} -eq ${inputfilelength}
 then
# echo -e "\n### Here are the end of file results for ${wantedcounty}:" > ${outputfile}
 for i in "${my_array[@]}"; do echo -e "$i" >> ${outputfile}; done
 fi
done <  ${inputfile}
