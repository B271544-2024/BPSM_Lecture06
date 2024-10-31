# sequence="abcdefghijk"
size=30
offset=3
dnalist=[]

'''
count=(len(sequence) - size) // offset + 1
for i in range(count):
    dnalist.append(sequence[i*offset:i*offset+size])
print(dnalist)
'''

'''
for i in range(0,len(sequence),offset):
    if len(sequence[i:])>=size:
        dnalist.append(sequence[i:i+size])
print(dnalist)
'''

lines=list(open("remote_frag2.fasta"))
sequence=lines[1].strip()
# print(sequence)

for i in range(0,len(sequence),offset):
    if len(sequence[i:])>=size:
        dnalist.append(sequence[i:i+size])

print(dnalist)

seqlen=[]
for frag in range(0,len(dnalist)):
    seqlen.append((dnalist[frag].count('G')+dnalist[frag].count('C'))/len(dnalist[frag])*100)
    print(dnalist[frag]+f": {seqlen[frag]:.1f}")

for i in range(0,len(dnalist)):
    with open("./files/"+"frag"+str(i)+".fasta",'w') as seqfile:
        seqfile.write("> "+str(i)+" "+f'{seqlen[i]:.1f}'+"\n"+dnalist[i])

with open("./files/"+"allfrag.fasta","w") as seqfile:
    for i in range(0,len(dnalist)):
        if i<len(dnalist)-1:
            seqfile.write("> "+str(i)+" "+f'{seqlen[i]:.1f}'+"\n"+dnalist[i]+"\n")
        else:
            seqfile.write("> "+str(i)+" "+f'{seqlen[i]:.1f}'+"\n"+dnalist[i])
    
