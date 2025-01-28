import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# 1. Load and preprocess dataset
df = pd.read_csv("clothes_size.csv").dropna()
encode = {"size": {"XXS": 0, "XS": 1, "S": 2, "M": 3, "L": 4, "XL": 5, "XXL": 6, "XXXL": 7}}
df = df.replace(encode)

# 2. Split data
X = df.iloc[:, :-1]
y = df['size']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 3. Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# 4. Save model to pickle file
with open("size_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model trained and saved as 'size_model.pkl'.")