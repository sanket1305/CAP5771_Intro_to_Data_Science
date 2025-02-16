import pandas as pd

def describe_data(df):
    print("***Describing the data:***")
    num_rows, num_columns = df.shape

    print(f"Number of rows: {num_rows}")
    print(f"Number of columns: {num_columns}")

    print("\nColumn details:")
    for column in df.columns:
        col_data = df[column]
        col_dtype = col_data.dtype
        print(f"\nColumn: {column}, Type: {col_dtype}")

        # if data type is numeric, then calculate min, max, mean, median
        if pd.api.types.is_numeric_dtype(col_data):
            min_val = col_data.min()
            max_val = col_data.max()

            mean_val = col_data.mean()
            median_val = col_data.median()

            print(f"  Min: {min_val}")
            print(f"  Max: {max_val}")
            print(f"  Mean: {mean_val:.2f}")
            print(f"  Median: {median_val}")
        elif pd.api.types.is_categorical_dtype(col_data) or col_data.dtype == 'object':
            # Note 1 in Learning.md
            print()