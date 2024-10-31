dnalist=[]
with open("input.txt","r") as inputfile:
    for eachline in inputfile:
        dnalist.append(eachline.rstrip('\n')[14:])
        print(len(eachline.rstrip('\n')[14:]))

with open("trimdna.txt","w") as trimdna:
    for item in dnalist:
        trimdna.write(f'{item}\n')