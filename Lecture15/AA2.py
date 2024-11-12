def get_percentage2(sequence,AA=['A', 'I', 'L', 'M', 'F', 'W', 'Y', 'V']):
    count=0
    length=len(sequence)
    for aa in AA:
        count+=sequence.upper().count(aa.upper())
    percentage=count/length*100
    return percentage

assert round(get_percentage2("MSRSLLLRFLLFLLLLPPLP", ["M"])) == 5
assert round(get_percentage2("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L'])) == 70
assert round(get_percentage2("MSRSLLLRFLLFLLLLPPLP")) == 65