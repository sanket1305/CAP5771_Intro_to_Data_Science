import pandas as pd
import numpy as np

def clean_checkout_values():
    # read csv file into dataframe
    df = pd.read_csv("../output/task2_output.csv")

    # Count rows with non-numeric characters in the specified column
    count_non_numeric = df['checkout_value'].str.contains(r'\D', regex=True).sum()
    # remove non-numeric chars from the column
    df['checkout_value'] = df['checkout_value'].replace({r'[^0-9.]': ''}, regex=True)

    # output
    print("Number of formatted checkout values corrected:", count_non_numeric)

    # Convert the column to numeric values (float)
    df['checkout_value'] = pd.to_numeric(df['checkout_value'])
    count_missing = df['checkout_value'].isna().sum()

    # Replace missing or null values with NaN
    df['checkout_value'] = df['checkout_value'].fillna(np.nan)

    # output
    print("Number of missing values set to NaN:", count_missing)

    # Save the DataFrame to a CSV file
    df.to_csv('../output/task3_output.csv', index=False)

clean_checkout_values()