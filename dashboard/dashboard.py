import sqlite3
import pandas as pd
import streamlit as st

def render_dashboard():
    st.header("📊 Prediction Dashboard")
    try:
        conn = sqlite3.connect("database/farming_system.db")
        cursor = conn.cursor()
        cursor.execute("SELECT soil_ph, soil_moisture, temperature, rainfall, fertilizer_usage, pesticide_usage, crop_type, predicted_yield FROM predictions")
        rows = cursor.fetchall()
        conn.close()

        if rows:
            df = pd.DataFrame(rows, columns=[
                "Soil pH", "Soil Moisture", "Temperature", "Rainfall",
                "Fertilizer Usage", "Pesticide Usage", "Crop Type", "Predicted Yield"
            ])
            st.dataframe(df)
        else:
            st.info("No predictions have been recorded yet.")
    except Exception as e:
        st.error(f"Failed to load dashboard: {e}")
