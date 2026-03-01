import numpy as np
from sklearn.linear_model import LogisticRegression

# Feature matrix (uzunluk, charge, hidrofobiklik)
X = np.array([
    [20, 5, 0.5],
    [18, 1, 0.2],
    [25, 6, 0.6],
    [15, 0, 0.1]
])

# Labels (1 = etkili, 0 = değil)
y = np.array([1, 0, 1, 0])

model = LogisticRegression()
model.fit(X, y)

# Yeni peptit
new_peptide = np.array([[22, 4, 0.45]])

prediction = model.predict(new_peptide)

print("Tahmin:", prediction)
