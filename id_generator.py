from turtle import update
from uuid import uuid4
import pandas as pd

FILE_NAME = "rappers.csv"

def update_id_column(filename):
    df = pd.read_csv(filename)
    parial_df = df.loc[df["id"].isnull()]
    parial_df["id"] = [uuid4() for _ in range(len(parial_df.index))]
    print(parial_df)
    df.loc[df["id"].isnull()] = parial_df
    df.to_csv(filename, index=False)

update_id_column(filename=FILE_NAME)