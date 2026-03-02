import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Veri yükle
df = pd.read_csv("data/amp_dataset.csv")

X = df[["length", "net_charge", "hydrophobic_ratio"]]
y = df["label"]

# Model oluştur
model = RandomForestClassifier(n_estimators=50)
model.fit(X, y)

# Modeli kaydet
joblib.dump(model, "ml/model.pkl")

print("Model başarıyla kaydedildi.")
