seqlist=['ATTGTACGG', 'AATGAACCG', 'AATGAACCC', 'AATGGGAAT']
count=0

for i in range(0,len(seqlist)-1):
    for k in range(i+1,len(seqlist)):
        print('processing seq ',i+1,'and seq ',k+1)
        count=0
        for j in range(0,len(seqlist[i])):
            if seqlist[i][j]==seqlist[k][j]:
                count+=1
        print(count/len(seqlist[0]))