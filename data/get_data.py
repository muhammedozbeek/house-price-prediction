import pandas as pd

def load_data():
    """
    Kaggle'dan indirilen veri setini okur ve Pandas DataFrame olarak döndürür.
    """
    df = pd.read_csv("data/house_data.csv")
    return df
