import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style


def read_dataset():
    df = pd.read_csv('/root/python/DataAnalysis-Python/sample_datasets/Metadata_Country_API_SP.POP.TOTL.FE.IN_DS2_en_csv_v2.csv')
    return df

if __name__ == "__main__":
    df = read_dataset()