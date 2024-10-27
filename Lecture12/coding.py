#!/usr/bin/python3
import os,subprocess,shutil
import sys

subprocess.call("esearch -db nucleotide -query \"AJ223353[accession]\" | efetch -format fasta | grep -v \">\" > AJ223353_noheader.fasta3",shell=True)
remotefile_singleline=open("AJ223353_noheader.fasta3").read().upper().replace("\n","")

local_seq = open("plain_genomic_seq.txt").read().upper().strip().replace("\n","")
local_seq_singleline_reallyDNA = local_seq.replace("X","").replace("S","").replace("K","").replace("L","")

# define the coding position
startcoding=29
endcoding=409
# acquire fragments
remotefrag1=remotefile_singleline[:startcoding-1]
remotefrag2=remotefile_singleline[startcoding-1:endcoding]
remotefrag3=remotefile_singleline[endcoding:]

with open("remote_frag1.fasta","w") as my_file1:
	my_file1.write(">AJ223353_frag1_"+str(len(remotefrag1))+"\n"+remotefrag1)

with open("remote_frag2.fasta","w") as my_file2:
	my_file2.write(">AJ223353_frag2_"+str(len(remotefrag2))+"\n"+remotefrag2)

with open("remote_frag3.fasta","w") as my_file3:
	my_file3.write(">AJ223353_frag3_"+str(len(remotefrag3))+"\n"+remotefrag3)

with open("remote_frag.fasta","w") as my_file4:
	my_file4.write(">AJ223353_frag_"+str(len(remotefrag1)+len(remotefrag3))+"\n"+remotefrag1+remotefrag3)

# define the coding position
startcoding=64
endcoding=90
# acquire fragments
localfrag1=local_seq_singleline_reallyDNA[:startcoding-1]
localfrag2=local_seq_singleline_reallyDNA[startcoding-1:endcoding]
localfrag3=local_seq_singleline_reallyDNA[endcoding:]

with open("local_frag1.fasta","w") as my_file5:
	my_file5.write(">localseq_frag1_"+str(len(localfrag1))+"\n"+localfrag1)

with open("local_frag2.fasta","w") as my_file6:
	my_file6.write(">localseq_frag2_"+str(len(localfrag2))+"\n"+localfrag2)

with open("local_frag3.fasta","w") as my_file7:
	my_file7.write(">localseq_frag3_"+str(len(localfrag3))+"\n"+localfrag3)

with open("local_frag.fasta","w") as my_file8:
	my_file8.write(">localseq_frag_"+str(len(localfrag1)+len(localfrag3))+"\n"+localfrag1+localfrag3)


with open("All_exons.fasta", "w") as exons_out:
	exons_out.write(">AJ223353_exon_"+str(len(remotefrag2))+"\n"+remotefrag2+"\n")
	exons_out.write(">localexon1_"+str(len(localfrag1))+"\n"+localfrag1+"\n")
	exons_out.write(">localexon2_"+str(len(localfrag3))+"\n"+localfrag3)


with open("All_noncoding.fasta","w") as introns_out:
	introns_out.write(">AJ223353_noncoding1_"+str(len(remotefrag1))+"\n"+remotefrag1+"\n")
	introns_out.write(">AJ223353_noncoding2_"+str(len(remotefrag3))+"\n"+remotefrag3+"\n")
	introns_out.write(">localseq_intron_"+str(len(localfrag2))+"\n"+localfrag2)


