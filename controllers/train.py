import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from data.get_data import load_data
from models.linear_model import HousePriceModel
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from data.get_data import load_data
from models.linear_model import HousePriceModel

df = load_data()

# Kullanılacak özellikleri seçiyoruz
features = ["sqft_living", "bedrooms", "bathrooms", "floors"]
X = df[features]
y = df["price"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model eğitme
model = HousePriceModel()
model.train(X_train, y_train)

# Test verisi ile tahmin yapma
y_pred = model.predict(X_test)

# Performans ölçümü
mae = mean_absolute_error(y_test, y_pred)
print(f"Mean Absolute Error (MAE): {mae}")

# Modeli kaydetme
model.save_model()
