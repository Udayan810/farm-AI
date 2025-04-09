# utils/recommendation.py

def recommend_crop(soil_ph, moisture, temperature, rainfall):
    if 6.0 <= soil_ph <= 7.5:
        if moisture >= 60 and temperature > 25 and rainfall >= 150:
            return "Rice"
        elif moisture >= 50 and 20 <= temperature <= 25 and 50 <= rainfall < 150:
            return "Wheat"
        elif moisture >= 40 and temperature > 24 and rainfall < 100:
            return "Maize"
        elif moisture >= 30 and temperature > 22 and rainfall < 75:
            return "Sugarcane"
    elif 5.5 <= soil_ph < 6.0:
        if moisture >= 45:
            return "Groundnut"
    elif soil_ph < 5.5:
        return "Millet"
    
    return "Sorghum"

def recommend_fertilizer(crop_type):
    fertilizers = {
        "Rice": "Urea + DAP",
        "Wheat": "NPK 15-15-15",
        "Maize": "Nitrogen-rich fertilizer",
        "Sugarcane": "Potassium + Urea",
        "Groundnut": "Gypsum + Phosphate",
        "Millet": "Compost + Biofertilizers",
        "Sorghum": "Organic Compost",
        "Others": "Compost + Organic Manure"
    }
    return fertilizers.get(crop_type, fertilizers["Others"])
