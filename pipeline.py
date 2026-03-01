import json
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

from generator.peptide_generator import generate_peptide
from features.feature_extraction import extract_features


# MBG kurallarını yükle
with open("data/biological_rules.json") as f:
    rules = json.load(f)

# ML veri setini yükle
df = pd.read_csv("data/amp_dataset.csv")

X = df[["length", "net_charge", "hydrophobic_ratio"]]
y = df["label"]

# Modeli eğit
model = RandomForestClassifier(n_estimators=50)
model.fit(X, y)


# Kural kontrol fonksiyonu
def passes_rules(features):

    length_ok = rules["length_range"][0] <= features["length"] <= rules["length_range"][1]
    charge_ok = rules["charge_range"][0] <= features["net_charge"] <= rules["charge_range"][1]
    hydro_ok = rules["hydrophobicity_range"][0] <= features["hydrophobic_ratio"] <= rules["hydrophobicity_range"][1]

    return length_ok and charge_ok and hydro_ok


approved_peptides = []

for i in range(20):

    peptide = generate_peptide(20)
    features = extract_features(peptide)

    if passes_rules(features):

        prediction = model.predict([[
            features["length"],
            features["net_charge"],
            features["hydrophobic_ratio"]
        ]])[0]

        if prediction == 1:
            approved_peptides.append((peptide, features))


print("\nUygun adaylar:\n")

for p in approved_peptides:
    print(p)