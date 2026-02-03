import pandas as pd

def etl():
    df = pd.read_csv("data/raw/walmart_sales.csv", parse_dates=["Date"])
    
    df = df.sort_values(["Store", "Date"])
    
    for lag in [1, 2, 4]:
        df[f"lag_{lag}"] = df.groupby("Store")["Weekly_Sales"].shift(lag)
    
    df["rolling_4wk_avg"] = (
        df.groupby("Store")["Weekly_Sales"]
        .shift(1)
        .rolling(4)
        .mean()
    )
    
    df = df.dropna()
    df.to_csv("data/processed/model_ready_data.csv", index=False)

if __name__ == "__main__":
    etl()

