import random

amino_acids = list("ACDEFGHIKLMNPQRSTVWY")

def generate_peptide(length=20):
    return "".join(random.choice(amino_acids) for _ in range(length))

for _ in range(3):
    print(generate_peptide())
