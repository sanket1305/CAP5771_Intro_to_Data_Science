import pandas as pd
from descriptive_utils import describe_data, count_nulls, describe_numeric, plot_correlations, save_findings_to_pdf

file_path = "./Data/Melbourne_housing_FULL.csv"
df = pd.read_csv(file_path)

num_rows, num_cols, content = describe_data(df)
print(num_rows, num_cols)

describe_numeric(df, ["Rooms", "Car", "Bedroom2", "Bathroom"])

plot_correlations(df, "Rooms")

# save_findings_to_pdf(content)