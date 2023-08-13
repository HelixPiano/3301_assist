import pandas as pd


def read_csv_file() -> pd.DataFrame:
    df = pd.read_csv("LP/readeasiertranscript2.csv")
    return df
