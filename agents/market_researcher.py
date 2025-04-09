import pandas as pd

def analyze_market_trends(csv_path='data/market_researcher_dataset.csv'):
    try:
        df = pd.read_csv(csv_path)
        top_products = df.sort_values(by='Demand_Index', ascending=False).head(5)
        return top_products[['Product', 'Demand_Index']]
    except Exception as e:
        return f"Error reading market data: {e}"
