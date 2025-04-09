import joblib
import numpy as np
import os

# Construct the correct model path (relative to this file)
model_path = os.path.join(os.path.dirname(__file__), 'yield_predictor.pkl')

# Load the trained model
try:
    model = joblib.load(model_path)
    print("✅ Loaded model type:", type(model))
except Exception as e:
    print(f"❌ Failed to load model: {e}")
    model = None

def predict_yield(soil_ph, soil_moisture, temperature, rainfall, fertilizer_usage, pesticide_usage, crop_type):
    try:
        if model is None:
            return "Model not loaded."

        # Ensure crop_type is already mapped (Wheat=0, Rice=1, Corn=2, Soybean=3)
        features = np.array([[soil_ph, soil_moisture, temperature, rainfall, fertilizer_usage, pesticide_usage, crop_type]])
        
        prediction = model.predict(features)
        return prediction[0]
    except Exception as e:
        return f"Prediction failed: {e}"
