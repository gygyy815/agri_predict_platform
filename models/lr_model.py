import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def lr_predict(df):
    """Linear Regression prediction"""
    df = df.reset_index(drop=True)
    X = np.array(range(len(df))).reshape(-1, 1)
    y = df['Price'].values
    model = LinearRegression()
    model.fit(X, y)
    future_X = np.array(range(len(df), len(df)+7)).reshape(-1, 1)
    forecast = model.predict(future_X)
    result_df = pd.DataFrame({'Predicted Price': forecast})
    return result_df
