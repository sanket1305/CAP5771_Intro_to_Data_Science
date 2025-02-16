import pandas as pd
import descriptive_utils as desc_utils

file_path = "./Data/Melbourne_housing_FULL.csv"
df = pd.read_csv(file_path)

desc_utils.describe_data(df)