import pandas as pd

data = {
    "name": ["Lota", "Sarah", "James", "Aisha", "Tunde"],
    "role": ["ML Engineer", "Data Engineer", "MLOps Engineer", "ML Engineer", "Data Engineer"],
    "salary": [45000, 50000, 35000, 48000, 42000],
    "years": [2, 4, 0, 3, 1]
}

df = pd.DataFrame(data)
print(df)