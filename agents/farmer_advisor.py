# import joblib
# import numpy as np
# import os

# def load_model():
#     model_path = os.path.join(os.path.dirname(__file__), 'yield_predictor.pkl')
#     try:
#         model = joblib.load(model_path)
#         return model
#     except Exception as e:
#         raise Exception(f"Model loading failed: {e}")

# def predict_yield(model, features):
#     try:
#         # Ensure input is 2D array
#         features_array = np.array(features).reshape(1, -1)
#         prediction = model.predict(features_array)
#         return prediction[0]
#     except Exception as e:
#         raise Exception(f"Prediction failed: {e}")
# agents/farmer_advisor.py
import joblib
import numpy as np
import os

def load_model():
    model_path = os.path.join(os.path.dirname(__file__), "yield_predictor.pkl")
    return joblib.load(model_path)

def predict_yield(model, features):
    try:
        features_array = np.array([features])
        prediction = model.predict(features_array)
        return prediction[0]
    except Exception as e:
        return f"{e}"
