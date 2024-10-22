#!/usr/bin/env python3
my_dna="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
print("A count: ",str(my_dna.count('A')))
print("T count: ",str(my_dna.count('T')))
print("A+T percent: ",str((my_dna.count('A')+my_dna.count('T'))/len(my_dna)))
