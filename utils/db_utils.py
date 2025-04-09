import sqlite3
import os

# Ensure database folder exists
os.makedirs("database", exist_ok=True)

DB_PATH = os.path.join("database", "farming_system.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            soil_ph REAL,
            soil_moisture REAL,
            temperature REAL,
            rainfall REAL,
            fertilizer_usage REAL,
            pesticide_usage REAL,
            crop_type TEXT,
            predicted_yield REAL
        )
    ''')
    conn.commit()
    conn.close()

def insert_prediction(data):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO predictions (
            soil_ph, soil_moisture, temperature, rainfall,
            fertilizer_usage, pesticide_usage, crop_type, predicted_yield
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', data)
    conn.commit()
    conn.close()
