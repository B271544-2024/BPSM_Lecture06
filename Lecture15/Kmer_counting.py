def kmer_counting(dna,size=8,n=5):
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

print(kmer_counting('ATGCATCATG',2,2))