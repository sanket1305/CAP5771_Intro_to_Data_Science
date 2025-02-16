import os
import pandas as pd

def print_csv_schema(csv_filename):
  # check if file exists
  if not os.path.exists(csv_filename):
    print("Invalid filename provided")
  else:
    # extract filename to print
    filename = csv_filename.split('/')
    print(filename[-1][:-4] , end = ": ")

    # read csv file into dataframe
    df = pd.read_csv(csv_filename)

    # extract cols from data and process them
    list_cols = sorted(df.columns)

    for col in range(len(list_cols)):
      if col != 0:
        print(",", end = " ")
      print(list_cols[col], end ="")
