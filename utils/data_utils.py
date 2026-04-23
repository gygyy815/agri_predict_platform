import pandas as pd
import numpy as np

def process_csv(filepath):
    """Read and preprocess CSV file"""
    df = pd.read_csv(filepath)
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date')
    return df

def generate_advice(forecast):
    """Generate AI advice based on prediction"""
    last_price = forecast['Predicted Price'].iloc[0]
    future_prices = forecast['Predicted Price'].values
    trend = "upward" if future_prices[-1] > last_price else "downward"
    avg_price = np.mean(future_prices)
    
    advice = f"""
    <p>Price Trend: <strong>{trend.upper()}</strong></p>
    <p>Average Predicted Price (next 7 days): <strong>{avg_price:.2f}</strong></p>
    <p>Recommendation: {'Consider selling now' if trend == "downward" else 'Hold or buy more stock'}</p>
    """
    return advice
