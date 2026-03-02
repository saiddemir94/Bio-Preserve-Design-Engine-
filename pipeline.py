import json
import pandas as pd
import joblib

from features.feature_extraction import extract_features

# Biyolojik kuralları yükle
with open("data/biological_rules.json") as f:
    rules = json.load(f)

# Food context yükle
with open("data/food_context.json") as f:
    food = json.load(f)

# Eğitilmiş modeli yükle
model = joblib.load("ml/model.pkl")

# Veritabanı peptitleri yükle
db = pd.read_csv("data/database_peptides.csv")


def passes_biological_rules(features):
    length_ok = rules["length_range"][0] <= features["length"] <= rules["length_range"][1]
    charge_ok = rules["charge_range"][0] <= features["net_charge"] <= rules["charge_range"][1]
    hydro_ok = rules["hydrophobicity_range"][0] <= features["hydrophobic_ratio"] <= rules["hydrophobicity_range"][1]
    return length_ok and charge_ok and hydro_ok


def passes_food_context(features):

    # Tuzlu ortam → düşük charge dezavantaj
    if food["salt_ratio"] > 2:
        if features["net_charge"] < 3:
            return False, "Tuzlu ortamda stabil değil"

    # Asidik ortam → aşırı hidrofobik yapı bozulabilir
    if food["pH"] < 6:
        if features["hydrophobic_ratio"] > 0.65:
            return False, "Asidik ortamda yapısal bozulma riski"

    # Yağlı ortam → çok düşük hidrofobiklik tutunamaz
    if food["fat_content"] == "high":
        if features["hydrophobic_ratio"] < 0.3:
            return False, "Yağlı ortamda yüzeye tutunamaz"

    return True, f"{food['product']} ortamına uygundur"


approved = []

for seq in db["sequence"]:

    features = extract_features(seq)

    # 1️⃣ Biyolojik filtre
    if passes_biological_rules(features):

        # 2️⃣ ML değerlendirme
        prediction = model.predict(pd.DataFrame([features]))[0]

        if prediction == 1:

            # 3️⃣ Food stabilite kontrolü
            food_ok, note = passes_food_context(features)

            if food_ok:
                approved.append((seq, features, note))


print("\nUygun adaylar:\n")

for seq, feat, note in approved:
    print(seq)
    print("→", note)
    print()