import json
import pandas as pd
import joblib

from features.feature_extraction import extract_features

# Load biological rules
with open("data/biological_rules.json") as f:
    rules = json.load(f)

# Load food context
with open("data/food_context.json") as f:
    food = json.load(f)

# Load trained model
model = joblib.load("ml/model.pkl")

# Load peptide database
db = pd.read_csv("data/database_peptides.csv")


def passes_biological_rules(features):
    return (
        rules["length_range"][0] <= features["length"] <= rules["length_range"][1]
        and rules["charge_range"][0] <= features["net_charge"] <= rules["charge_range"][1]
        and rules["hydrophobicity_range"][0] <= features["hydrophobic_ratio"] <= rules["hydrophobicity_range"][1]
    )


def check_food_compatibility(features):
    suitable_foods = []

    for f in food["food_matrices"]:

        ok = True

        if f["salt_ratio"] > 2 and features["net_charge"] < 3:
            ok = False

        if f["pH"] < 6 and features["hydrophobic_ratio"] > 0.65:
            ok = False

        if f["fat_content"] == "high" and features["hydrophobic_ratio"] < 0.3:
            ok = False

        if ok:
            suitable_foods.append(f["product"])

    return suitable_foods


approved = []

for seq in db["sequence"]:

    features = extract_features(seq)

    if passes_biological_rules(features):

        prediction = model.predict(pd.DataFrame([features]))[0]

        if prediction == 1:

            foods = check_food_compatibility(features)

            if foods:
                approved.append((seq, foods))


print("\nUygun adaylar:\n")

for seq, foods in approved:
    print(seq)
    print("Uygun olduğu gıdalar:", ", ".join(foods))
    print()