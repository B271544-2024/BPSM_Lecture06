def get_percentage1(sequence,AA):
    length=len(sequence)
    count=sequence.upper().count(AA.upper())
    percentage=count/length*100
    return percentage

assert round(get_percentage1("MSRSLLLRFLLFLLLLPPLP", "M")) == round(5)
assert round(get_percentage1("MSRSLLLRFLLFLLLLPPLP", "r")) == round(10)
assert round(get_percentage1("MSRSLLLRFLLFLLLLPPLP", "L")) == round(50)
assert round(get_percentage1("MSRSLLLRFLLFLLLLPPLP", "Y")) == round(0)