import streamlit as st
from agents.farmer_advisor import load_model, predict_yield
from agents.market_researcher import analyze_market_trends
from utils.db_utils import init_db, insert_prediction
from dashboard.dashboard import render_dashboard
from utils.recommendition import recommend_crop, recommend_fertilizer

# Initialize DB
init_db()

st.set_page_config(page_title="🌱 AI Sustainable Farming", layout="centered")
st.title("🌾 AI-Powered Sustainable Farming System")

menu = st.sidebar.selectbox("Choose a Role", ["Farmer Advisor", "Market Researcher", "📊 Prediction Dashboard","🌾 Crop Recommendation", "🧪 Fertilizer Recommendation"])
#menu = st.sidebar.selectbox("Menu", ["🏠 Home", "🌱 Make Prediction", "📊 Prediction Dashboard", ])



if menu == "Farmer Advisor":
    st.header("📊 Predict Crop Yield")

    soil_ph = st.slider("Soil pH", 4.0, 9.0, 6.5)
    moisture = st.slider("Soil Moisture (%)", 0.0, 100.0, 25.0)
    temperature = st.slider("Temperature (°C)", 5.0, 45.0, 27.0)
    rainfall = st.number_input("Rainfall (mm)", value=50.0)
    fertilizer = st.number_input("Fertilizer Usage (kg)", value=80.0)
    pesticide = st.number_input("Pesticide Usage (kg)", value=5.0)
    crop_type = st.selectbox("Crop Type", ["Wheat", "Rice", "Corn", "Soybean"])

    if st.button("🚜 Predict Yield"):
        crop_map = {'Wheat': 0, 'Rice': 1, 'Corn': 2, 'Soybean': 3}
        encoded_crop = crop_map[crop_type]

        features = [
            soil_ph, moisture, temperature, rainfall,
            fertilizer, pesticide, encoded_crop
        ]

        try:
            model = load_model()
            yield_pred = predict_yield(model, features)

            st.success(f"Predicted Yield: 🌾 **{yield_pred:.2f} tons/hectare**")

            # Only pass 8 values as expected by the DB
            insert_prediction([
                soil_ph,
                moisture,
                temperature,
                rainfall,
                fertilizer,
                pesticide,
                crop_type,
                yield_pred
            ])
        except Exception as e:
            st.error(f"Prediction failed: {e}")


elif menu == "Market Researcher":
    st.header("📈 Market Trend Analysis")
    market_data = analyze_market_trends()
    if isinstance(market_data, str):
        st.error(market_data)
    else:
        st.dataframe(market_data)

elif menu == "📊 Prediction Dashboard":
    render_dashboard()

elif menu == "🌾 Crop Recommendation":
    st.subheader("🌾 Intelligent Crop Recommendation")
    soil_ph = st.number_input("Soil pH", min_value=0.0, max_value=14.0, step=0.1)
    moisture = st.slider("Soil Moisture (%)", 0, 100)
    temperature = st.slider("Temperature (°C)", 0, 50)
    rainfall = st.slider("Rainfall (mm)", 0, 500)

    if st.button("Recommend Crop"):
        crop = recommend_crop(soil_ph, moisture, temperature, rainfall)
        st.success(f"🌱 Recommended Crop: **{crop}**")
elif menu == "🧪 Fertilizer Recommendation":
    st.subheader("🧪 Smart Fertilizer Recommendation")
    crop_type = st.selectbox("Select Crop", ["Rice", "Wheat", "Maize", "Groundnut", "Others"])

    if st.button("Recommend Fertilizer"):
        fertilizer = recommend_fertilizer(crop_type)
        st.success(f"🧪 Recommended Fertilizer for {crop_type}: **{fertilizer}**")
