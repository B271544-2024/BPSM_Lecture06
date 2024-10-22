#!/usr/bin/env python3
my_dna="ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
exon1=my_dna[:63]
exon2=my_dna[91-1:]
exon=exon1+exon2
intron=my_dna[63:90]
print("exon: ",exon)
print("length of exon: ",str(len(exon)))
print("exon percent: ",str(len(exon)/len(my_dna)*100))
print("sequence",exon1+intron.lower()+exon2)
