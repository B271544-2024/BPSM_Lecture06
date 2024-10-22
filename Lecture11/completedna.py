#!/usr/bin/env python3
my_dna="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
replaced_dna=my_dna.replace('T','a').replace('A','t').replace('C','g').replace('G','c')
replaced_dna=replaced_dna.upper()
print("replaced: ",replaced_dna)
