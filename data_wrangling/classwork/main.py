import pandas as pd
from descriptive_utils import describe_data, save_findings_to_pdf

file_path = "./Data/Melbourne_housing_FULL.csv"
df = pd.read_csv(file_path)

num_rows, num_cols, content = describe_data(df)

save_findings_to_pdf(content)