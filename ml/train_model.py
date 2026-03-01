import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# veri yükle
df = pd.read_csv("data/amp_dataset.csv")

X = df[["length", "net_charge", "hydrophobic_ratio"]]
y = df["label"]

model = RandomForestClassifier(n_estimators=50)
model.fit(X, y)

# test
test_peptide = [[20, 6, 0.5]]
prediction = model.predict(test_peptide)

print("Antimikrobiyal olasılığı:", prediction[0])
