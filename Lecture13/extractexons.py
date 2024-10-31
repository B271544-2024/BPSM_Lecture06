position=[]
with open("exons.txt","r") as exons:
    for eachline in exons:
        position.extend(eachline.strip().split(','))

exonslist=[]
with open("genomic_dna2.txt","r") as seq:
    fullseq=seq.read().strip()

for i in range(int(len(position)/2)):
    exonslist.append(fullseq[int(position[2*i])-1:int(position[2*i+1])])

with open("pureexons.txt","w") as pureexons:
    for item in exonslist:
        pureexons.write(f'{item}')
