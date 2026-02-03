import pandas as pd

def validate_data(df):
    checks = {
        "missing_pct": df.isnull().mean(),
        "negative_sales": (df["Weekly_Sales"] < 0).sum(),
        "duplicate_rows": df.duplicated().sum()
    }
    return pd.DataFrame(checks)

if __name__ == "__main__":
    df = pd.read_csv("data/raw/walmart_sales.csv")
    report = validate_data(df)
    print(report)
