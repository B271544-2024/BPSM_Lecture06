def base_counter(sequence, threshold):
    count=0
    AA=['A', 'T', 'G', 'C']
    length=len(sequence)
    for aa in AA:
        count+=sequence.upper().count(aa.upper())
    percentage=round(count/length*100)
    # if undetermined bases over threshold
    if 100-percentage>threshold:
        return True
    else:
        return False

assert base_counter('ATGCATGCNN',20)==False
assert base_counter('ATGCATGCNN',19)==True