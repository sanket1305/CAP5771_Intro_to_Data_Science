import json
import os
import pandas as pd
import sqlite3

def process_json(json_filename):

    # connect to the SQLite database
    db_name = '../data/output.db'
    conn = sqlite3.connect(db_name)

    # load json file into variable
    with open(json_filename, 'r') as f:
        data = json.load(f)
    
    # json to dataframe conversion
    df = pd.DataFrame(data)

    # format table name
    table_name = json_filename.split('/')[-1]
    table_name = table_name.split('.')[0].capitalize()

    # writing data into table
    df.to_sql(table_name, conn, if_exists='replace', index=False)

    # close db connection
    conn.commit()
    conn.close

# function to process csv file
def process_csv(csv_filename):

    # connect to the SQLite database
    db_name = '../data/output.db'
    conn = sqlite3.connect(db_name)

    # read csv file into dataframe
    df = pd.read_csv(csv_filename)

    # formatting table name
    table_name = csv_filename.split('/')[-1]
    table_name = table_name.split('.')[0].capitalize()

    # write dataframe into table
    df.to_sql(table_name, conn, if_exists='replace', index=False)

    # close db connection
    conn.commit()
    conn.close

def process_db(db_filename):

    # connect to the SQLite database (input)
    db_path = db_filename
    conn = sqlite3.connect(db_path)

    # connect to the SQLite database (output)
    output_db_name = '../data/output.db'
    output_conn = sqlite3.connect(output_db_name)

    # create cursor on input db connection
    cursor = conn.cursor()

    # get all tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    # for each table, get all the data and write it to output table
    for item in tables:
        # fetch all data for given table and convert it into a dataframe
        query = "SELECT * FROM "+item[0]
        df_from_db = pd.read_sql(query, conn)

        # write dataframe to table
        df_from_db.to_sql(item[0], output_conn, if_exists='replace', index=False)
        output_conn.commit()
    
    # close connections to both input and output table
    conn.close()
    output_conn.close()

def process_xls(xls_filename):
    # connect to the SQLite database
    db_name = '../data/output.db'
    conn = sqlite3.connect(db_name)

    # read excel file
    extracted_file = pd.ExcelFile(xls_filename)

    # extract sheet names
    sheets = extracted_file.sheet_names

    # read each sheet of file into a dataframe
    for sheet in sheets:
        # print(sheet)                  # debug

        # read sheet data into datframe and write it to table
        df = pd.read_excel(xls_filename, sheet_name=sheet)
        df.to_sql(sheet, conn, if_exists='append', index=False)
    
        conn.commit()
    
    # close db connection
    conn.close

# function to debug tha output table by printing it
def read_output_db():
    # connect to the SQLite database (input)
    db_path = '../data/output.db'
    conn = sqlite3.connect(db_path)

    # connect to the SQLite database (output)
    output_db_name = '../data/output.db'
    output_conn = sqlite3.connect(output_db_name)

    cursor = conn.cursor()

    # get all tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    # print(len(tables))
    print(tables)

    # extract table names and add them to list
    for item in tables:
        query = "SELECT * FROM "+item[0]
        df_from_db = pd.read_sql(query, conn)

        # display top 5 rows
        print(df_from_db.head())

    # Close the connection
    conn.close()

if __name__ == "__main__":
    print("Hello World!!")

    # List all files and directories in the current directory
    files_in_directory = os.listdir('../data')

    for file in files_in_directory:
        if file[-5:] == ".json":
            process_json('../data/' + file)
        if file[-4:] == ".csv":
            process_csv('../data/' + file)
        if file[-3:] == '.db':
            process_db('../data/' + file)
        if file[-5:] == '.xlsx':
            process_xls('../data/' + file)

    # uncomment below line, if you want to see summary of output db data
    # read_output_db()