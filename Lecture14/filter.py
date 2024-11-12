lines=list(open('data.csv'))
species_name=[line.rstrip().split(',')[0] for line in lines]
sequence=[line.rstrip().split(',')[1] for line in lines]
gene_name=[line.rstrip().split(',')[2] for line in lines]
expression_level=[line.rstrip().split(',')[3] for line in lines]

for i in range(0,len(lines)):
    if species_name[i] in ("Drosophila melanogaster","Drosophila simulans"):
        print("q1: ",gene_name[i])

for i in range(0,len(lines)):
    if len(sequence[i])>=90 and len(sequence[i])<110:
        print("q2:",gene_name[i])

for i in range(0,len(lines)):
    if (sequence[i].count('a')+sequence[i].count('t'))/len(sequence[i])<0.5 and int(expression_level[i])>200:
        print("q3:",gene_name[i])

for i in range(0,len(lines)):
    if gene_name[i].startswith('k') or gene_name[i].startswith('h') and species_name[i]!="Drosophila melanogaster":
        print("q4:",gene_name[i])

for i in range(0,len(lines)):
    content=sequence[i].count('a')+sequence[i].count('t')/len(sequence[i])
    if content>0.65:
        print(gene_name[i]," ","AT larger than 0.65")
    elif content<0.45:
        print(gene_name[i]," ","AT less than 0.45")
    else:
        print(gene_name[i]," ","AT between 0.45 and 0.65")