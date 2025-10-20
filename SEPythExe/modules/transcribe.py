

def transcribe(seq):
    mapping = str.maketrans("GCTA", "CGAU")

for dna in "AGGTC", "TTGACT", "ATGGCA":
    print(dna.translate(mapping))