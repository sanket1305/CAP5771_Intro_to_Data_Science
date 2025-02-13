import csv
import json
import numpy as np
import os
import pandas as pd
import sqlite3

# function to process json files


def process_json(json_filename):
    print("----------- being json ----------------" + json_filename)
    # output will be stored in this list
    output = []

    # dictionary to keep track of attributes and their data types
    # 0 -> Quant, 1 -> Qual, 2 -> both
    map = {}

    # load json file into variable
    with open(json_filename, 'r') as f:
        data = json.load(f)

    # for each json object in the list
    for element in data:
        # evaluate each key, value pair
        for key, value in element.items():
            # if value is of type int or float then it's quantitative
            is_quantitative = isinstance(value, (int, float))

            if not key in map:
                print(key, value)         # debug
                if (is_quantitative and key[-2:] != 'id') or key[:4] == 'date' or key[-5:] == 'hours':
                    map[key] = 0
                else:
                    map[key] = 1
    print(map)                            # debug

    for attribute in map:
        record = [attribute]

        # add remaining fields
        record.append("acquisitions")
        record.append("")

        # add department
        record.append("Acquisitions")

        # add source_type
        record.append("json")

        # check if qualitative or quantitative
        if map[attribute] == 1:         # 1 is for qualitative
            record.append("qualitative")
        else:                           # 0 is for qunatitative
            record.append("quantitative")

        # append the record to list element
        output.append(record)

    print("----------- end json ----------------" + json_filename)

    # return final processed data from json file
    return output

# function to process csv file


def process_csv(csv_filename):
    print("----------- begin csv ----------------" + csv_filename)

    # output will be stored in this list
    output = []

    # read csv file into dataframe
    df = pd.read_csv(csv_filename)

    # extract cols from data and process them
    list_cols = list(df.columns)

    # first row
    first_row = df.iloc[0].tolist()

    print(list_cols)                # debug
    print(first_row)

    for index in range(len(first_row)):
        record = [list_cols[index]]

        # add remaining fields
        record.append("campaigns")
        record.append("")

        # add department
        record.append("Marketing")

        # add source_type
        record.append("csv")

        # print(first_row[index], type(first_row[0]))
        if (isinstance(first_row[index], (int, float, np.int64, np.integer)) and list_cols[index][-2:] != "id") or list_cols[index][-4:] == "date":
            record.append("quantitative")
        else:
            record.append("qualitative")

        output.append(record)

    print("----------- end csv ----------------" + csv_filename)
    return output


def process_db(db_filename):
    print("----------- begin db ----------------" + db_filename)

    output = []

    db_path = db_filename
    conn = sqlite3.connect(db_path)
    # connection to DB was successful

    cursor = conn.cursor()

    # get all tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    table_list = []

    # extract table names and add them to list
    for item in tables:
        table_list.append(item[0])

    for table in table_list:

        print(table)                # debug

        # get column names for each table
        query = "SELECT * FROM " + table
        cursor.execute(query)

        # description is used to extract all columns names
        table_content = cursor.description
        first_record = list(cursor.fetchall()[0])

        # parse the column names and get it in proper format for sorting
        col_list = []
        num_cols = len(table_content)

        for ind in range(len(table_content)):
            col_list.append(table_content[ind][0])

        print(col_list)             # debug
        print(first_record)         # debug

        for index in range(num_cols):
            # add attribute name
            record = [col_list[index]]

            # add other fields
            record.append(table)
            record.append("")

            # add department
            record.append("Sales")

            # add source_type
            record.append("sql")

            # check data type of variable
            # print(first_record[index], type(first_record[index]))
            if isinstance(first_record[index], (int, float)) and col_list[index][-2:] != "id":
                record.append("quantitative")
            else:
                record.append("qualitative")

            output.append(record)

    print("----------- end db ----------------" + db_filename)
    return output


def process_xls(xls_filename):

    print("---- being xls --------------" + xls_filename)
    output = []

    # read excel file
    extracted_file = pd.ExcelFile(xls_filename)

    # extract sheet names
    sheets = extracted_file.sheet_names

    # read each sheet of file into a dataframe
    for sheet in sheets:
        df = pd.read_excel(xls_filename, sheet_name=sheet)
        print(sheet)                  # debug

        # sort columns before diplay
        list_cols = list(df.columns)
        first_record = df.iloc[0].to_list()

        print(list_cols)              # debug
        print(first_record)

        for index in range(len(list_cols)):
            record = [list_cols[index]]

            # add other fields
            record.append(sheet)

            filename = xls_filename.split('/')[-1]
            filename = filename.split('.')[0]
            record.append(filename)

            # add department
            record.append("HR")

            # add source_type
            record.append("excel")

            # print(first_record[index], type(first_record[index]))
            if (isinstance(first_record[index], (int, float, np.int64, np.int64)) and list_cols[index][-2:] != "id") or list_cols[index][:4] == "date":
                record.append("quantitative")
            else:
                record.append("qualitative")

            output.append(record)
            # print(record)

    print("----- end -------" + xls_filename)
    return output


if __name__ == "__main__":
    # print("Hello World!!")

    output_filename = 'data_dictionary.csv'
    output_filepath = '../exploration/' + output_filename

    # this will be used directly at the end to simply write data in csv file
    output_headers = ['attribute_name', 'attribute_source',
                      'attribute_sub_source', 'department', 'source_type', 'type']
    output_data = []

    # List all files and directories in the current directory
    files_in_directory = os.listdir('../data')

    # print(files_in_directory)

    for file in files_in_directory:
        if file[-5:] == ".json":
            output = process_json('../data/' + file)

            output_data += output
        if file[-4:] == ".csv":
            output = process_csv('../data/' + file)

            output_data += output
        if file[-3:] == '.db':
            output = process_db('../data/' + file)

            output_data += output
        if file[-5:] == '.xlsx':
            output = process_xls('../data/' + file)

            output_data += output

    sorted_data = sorted(output_data, key=lambda x: (
        x[0], x[1], x[2]))
    # sorted_data = output_data

    with open(output_filepath, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(output_headers)

        writer.writerows(sorted_data)
