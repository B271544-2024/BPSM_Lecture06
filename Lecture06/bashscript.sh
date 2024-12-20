#!/bin/bash

# Delete any exercise output files from previous runs
rm -f *.exercise.out

# Initial variable values at start
goodlines=$(grep -v "#" ${inputfile} | wc -l | cut -d ' ' -f1)
unset IFS
unset dataline
shortHSP=0; 
hspcounter=0;
echo -e "We have ${goodlines} data lines for processing...\n"

# Initialise a bash array for multiple HSPs, called it dupS_acc
dupS_acc=()

# HSP score cuts chosen, and their output files
group1cut=150
group2cut=250
group3cut=350
outfile1="${outputpath}/HSPscore.${group1cut}.exercise.out"
outfile2="${outputpath}/HSPscore.${group2cut}.exercise.out"
outfile3="${outputpath}/HSPscore.${group3cut}.exercise.out"
outfile4="${outputpath}/HSPscore.morethan.${group3cut}.exercise.out"

# Remove any existing versions of the output files
rm -f ${outfile1} ${outfile2} ${outfile3} ${outfile4}

# Read in the whole line at first
while read wholeline
do
# echo "Line is ${wholeline}"

# Don't want the input lines that start with #
# Uses a substring notation: offset from first character, length wanted
if test ${wholeline:0:1} != "#"
	then
	dataline=$((dataline+1))

# Split the line into the fields we want
read Q_acc S_acc pc_identity alignment_length mismatches gap_opens Q_start Q_end S_start S_end evalue bitscore <<< ${wholeline}

# We need to ensure that ${bitscore} is an integer number not a real/float!
bitscore=$(printf "%.0f\n" ${bitscore})

# list the subject accession for all HSPs
echo -e "${dataline}\t${Q_acc}\t${S_acc}" >> ${outputpath}/Subject_accessions.exercise.out

# List the alignment length and percent ID for all HSPs
echo -e "${dataline}\t${alignment_length}\t${pc_identity}" >> ${outputpath}/al_leng_pcID.exercise.out

# Show the HSPs with more than 20 mismatches
if test ${mismatches} -gt 20
 then
 echo -e "${dataline}\tmore than 20 mismatches:\t${Q_acc} ${S_acc} ${mismatches}"
fi

# list the first 20 HSPs that have fewer than 20 mismatches
if test ${mismatches} -lt 20
 then
 hspcounter=$((hspcounter+1))
 if test ${hspcounter} -le 20
  then
  hsp_array+=${wholeline}
  echo -e "${dataline}\t${hspcounter}\t${wholeline}" >> ${outputpath}/Fewer.than20MM.exercise.out
 fi
fi

# how many HSPs are shorter than 100 amino acids?
if test ${alignment_length} -lt 100
 then
 shortHSP=$((shortHSP+1))
fi


# list the top ten highest (best) HSPs.
# BLAST output default is to give the best first
if test ${dataline} -le 10
 then
 echo -e "${dataline}\t${wholeline}" >> ${outputpath}/Top10.HSPs.exercise.out
fi

# list the start positions of all matches where the
# HSP Subject accession includes the letters string AEI.
if [[ ${S_acc} == *"AEI"* ]]; then
 echo -e "${dataline}\t${S_acc} contains AEI: \
    Subject starts at ${S_start}, Query starts at ${Q_start}" \
    >> ${outputpath}/AEIinSubjectAcc.starts.exercise.out 
fi

# how many subject sequences have more than one HSP?
if test ${S_acc} == ${pre_acc}  
 then
 dupecount=$((dupecount+1))
 if [[ dupecount == 1 ]]; then
  dupS_acc=${S_acc}
 fi

# Some might have more than 2: use wildcard pattern matching to see
# if we have it already
 if [[ $dupS_acc == *${S_acc}* ]]; then
  echo ""
  else
  dupS_acc+=(${S_acc})
 fi
fi
pre_acc=${S_acc}

# what percentage of each HSP is made up of mismatches? This is a rounded
# number as bash doesn't do floating point maths...
MMpercent=$((100*${mismatches}/${alignment_length}))
echo -e "${dataline}\t${alignment_length}\t${mismatches}\t${MMpercent}" \
   >> ${outputpath}/Mismatchpercent.exercise.out

# allocate HSPs into different groups based on their scores
scorebin=1
if [ ${bitscore} -gt ${group3cut} ]; then
     scorebin=4
fi
if [ ${bitscore} -le ${group3cut} ] && [ ${bitscore} -gt ${group2cut} ]; then
     scorebin=3
fi
if [ ${bitscore} -le ${group2cut} ] && [ ${bitscore} -gt ${group1cut} ]; then
     scorebin=2
fi

# Use a case statement to send the output to the relevant file
scoregroupdetails=$(echo -e "${dataline}\t${Q_acc}\t${S_acc}\t${bitscore}")
case $scorebin in
  4)
    echo -e "${scoregroupdetails}" >> ${outfile4}
    ;;
  3)
    echo -e "${scoregroupdetails}" >> ${outfile3}
    ;;
  2)
    echo -e "${scoregroupdetails}" >> ${outfile2}
    ;;
  1)
    echo -e "${scoregroupdetails}" >> ${outfile1}
    ;;
esac

# END BLOCK EQUIVALENT
if test ${dataline} -eq ${goodlines}
 then
 echo -e "\n\nENDBLOCK\n\nThere were ${shortHSP} HSPs shorter than 100 amino acids"
 echo -e "There were ${#dupS_acc[@]} Subjects with multiple HSPs"
fi
fi  
# was not a commented line in the blast data

# The input file gets brought in here, it's a variable whose value
# we can change if we want to use a different file as input...
done < ${inputfile}
