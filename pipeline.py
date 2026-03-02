import json
import pandas as pd
import joblib

from features.feature_extraction import extract_features

# Kuralları yükle
with open("data/biological_rules.json") as f:
    rules = json.load(f)

# Modeli yükle
model = joblib.load("ml/model.pkl")

# Veritabanını yükle
db = pd.read_csv("data/database_peptides.csv")


def passes_rules(features):
    length_ok = rules["length_range"][0] <= features["length"] <= rules["length_range"][1]
    charge_ok = rules["charge_range"][0] <= features["net_charge"] <= rules["charge_range"][1]
    hydro_ok = rules["hydrophobicity_range"][0] <= features["hydrophobic_ratio"] <= rules["hydrophobicity_range"][1]
    return length_ok and charge_ok and hydro_ok


approved = []

for seq in db["sequence"]:

    features = extract_features(seq)

    if passes_rules(features):

        prediction = model.predict(pd.DataFrame([features]))[0]

        if prediction == 1:
            approved.append((seq, features))

print("\nUygun adaylar:\n")

for a in approved:
    print(a)
