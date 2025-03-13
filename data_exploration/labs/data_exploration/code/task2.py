import glob
import os
import pandas as pd

def list_excel_files(dir_path):
  # path for checking all depths of current dir_path
  path = dir_path + "**/*.xlsx"

  list_files = glob.glob(path, recursive=True)
  list_files.sort()

  for item in list_files:
    item = item.split('/')

    # if file appears in nested dir,
    # there can be multiple / involved,
    # take last one, it will be file name
    print(item[-1])

def print_excel_schema(filename):
  # check if file is xlsx and if it exists
  if not os.path.exists(filename) or filename[-5:] != ".xlsx":
    print("Invalid filename provided")
  else:
    # read excel file
    extracted_file = pd.ExcelFile(filename)

    # extract sheet names
    sheets = extracted_file.sheet_names
    sheets.sort()

    # read each sheet of file into a dataframe
    for sheet in sheets:
        df = pd.read_excel(filename, sheet_name=sheet)
        print(sheet, end = ": ")
        
        # sort columns before diplay
        sorted_columns = sorted(df.columns)

        for col in range(len(sorted_columns)):
            if col != 0:
                print(",", end = " ")
            print(sorted_columns[col], end = "")
        print()

list_excel_files('data/')
print_excel_schema('data/Employee_Data_1.xlsx')