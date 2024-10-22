#!/usr/bin/env python3
my_dna="ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
print("positon: ",my_dna.find('GAATTC'))
print("fragment1: ",str(my_dna.find('GAATTC')+1))
print("fragment2: ",str(len(my_dna)-(my_dna.find('GAATTC')+1)))
