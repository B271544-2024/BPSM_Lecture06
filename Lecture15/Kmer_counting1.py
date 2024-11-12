def kmer_counting1(dna='',size=8,n=5):
    dna=str(input("Enter your dna sequence: "))
    size=int(input("Enter your kmersize: "))
    n=int(input("Enter your threshold: "))
    offset=1
    seqlist=[]
    for i in range(0,len(dna),offset):
        if len(dna[i:])>=size:
            seqlist.append(dna[i:i+size])
    savelist=[]
    for i in range(0,len(seqlist)):
        if seqlist.count(seqlist[i])>n and seqlist[i] not in savelist:
            savelist.append(seqlist[i])
            # print(seqlist[i])
    return savelist

print(kmer_counting1())