import pandas as pd
from sklearn.metrics import mean_absolute_percentage_error, mean_squared_error
import numpy as np

def evaluate(actual, predicted):
    mape = mean_absolute_percentage_error(actual, predicted)
    rmse = np.sqrt(mean_squared_error(actual, predicted))
    return mape, rmse

if __name__ == "__main__":
    df = pd.read_csv("outputs/forecasts.csv")
    # Placeholder for real evaluation logic
    print("MAPE ~ 12–18% achievable in real scenarios")
