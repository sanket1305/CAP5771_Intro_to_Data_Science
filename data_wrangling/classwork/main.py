import pandas as pd
from descriptive_utils import describe_data

file_path = "./Data/Melbourne_housing_FULL.csv"
df = pd.read_csv(file_path)

describe_data(df)

print(df.head())