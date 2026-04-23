import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA

def arima_predict(df):
    """ARIMA model prediction"""
    series = df['Price'].values
    model = ARIMA(series, order=(1,1,1))
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=7)
    result_df = pd.DataFrame({'Predicted Price': forecast})
    return result_df
