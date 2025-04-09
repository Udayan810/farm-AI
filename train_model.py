import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

# Load dataset
df = pd.read_csv(r'C:\Users\hp\Desktop\ai sustainable farming\data\farmer_advisor_dataset.csv')

# Print to verify columns
print("CSV Columns:", df.columns.tolist())

# Map crop types to integers
crop_map = {'Wheat': 0, 'Rice': 1, 'Corn': 2, 'Soybean': 3}
df['Crop_Type'] = df['Crop_Type'].map(crop_map)

# Corrected feature names
features = [
    'Soil_pH',
    'Soil_Moisture',
    'Temperature_C',
    'Rainfall_mm',
    'Fertilizer_Usage_kg',
    'Pesticide_Usage_kg',
    'Crop_Type'
]
X = df[features]
y = df['Crop_Yield_ton']

# Train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Save the model
os.makedirs(r'C:\Users\hp\Desktop\ai sustainable farming\agents', exist_ok=True)
joblib.dump(model, r'C:\Users\hp\Desktop\ai sustainable farming\agents\yield_predictor.pkl')
print("✅ Model saved at 'agents/yield_predictor.pkl'")
