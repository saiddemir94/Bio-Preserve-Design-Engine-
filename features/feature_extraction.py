
# Amino asit yuk bilgileri 
charge_map = {
    'K': 1, 'R': 1, 'H': 1,   # pozitif
    'D': -1, 'E': -1         # negatif
}

hydrophobic = set(['A','V','I','L','M','F','W','Y'])

def extract_features(sequence):
    length = len(sequence)

    net_charge = sum(charge_map.get(aa, 0) for aa in sequence)

    hydrophobic_count = sum(1 for aa in sequence if aa in hydrophobic)
    hydrophobic_ratio = hydrophobic_count / length

    return {
        "length": length,
        "net_charge": net_charge,
        "hydrophobic_ratio": hydrophobic_ratio
    }

# test
if __name__ == "__main__":
    seq = "KKLRLLRIFKFLRLLKIFRK"
    print(extract_features(seq))
