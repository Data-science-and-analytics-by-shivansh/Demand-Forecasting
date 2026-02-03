import pandas as pd
from prophet import Prophet

def train_prophet(df, store_id):
    store_df = df[df["Store"] == store_id][["Date", "Weekly_Sales"]]
    store_df.columns = ["ds", "y"]

    model = Prophet(
        yearly_seasonality=True,
        weekly_seasonality=False
    )
    model.fit(store_df)

    future = model.make_future_dataframe(periods=12, freq="W")
    forecast = model.predict(future)
    
    return forecast[["ds", "yhat"]]

if __name__ == "__main__":
    df = pd.read_csv("data/processed/model_ready_data.csv", parse_dates=["Date"])
    forecast = train_prophet(df, store_id=1)
    forecast.to_csv("outputs/forecasts.csv", index=False)
