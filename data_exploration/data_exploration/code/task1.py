import os
import sqlite3

def print_db_schema(filename):
  # check if file with given filename exists
  if not os.path.exists(filename):
    print("Invalid filename provided")
  else:
    db_path = filename
    conn = sqlite3.connect(db_path)
    # connection to DB was successful

    cursor = conn.cursor()

    # get all tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    table_list = []

    # extract table names and add them to list
    # sqlite is case sensitive, hence using lower function 
    # (which will be used as key for sorting)
    for item in tables:
      table_list.append((item[0].lower(), item[0]))
    table_list.sort()

    # we don't need key (_) any more after sorting
    for _, table in table_list:
      # display table name
      print(table, end = ": ")

      # get column names for each table
      query = "SELECT * FROM " + table
      cursor.execute(query)

      # description is used to extract all columns names
      table_content = cursor.description

      # parse the column names and get it in proper format for sorting
      col_list = []
      num_cols = len(table_content)

      for ind in range(len(table_content)):
        col_list.append((table_content[ind][0].lower(), table_content[ind][0]))
      col_list.sort()

      # after sorting, print all columns
      for col in range(num_cols):
        if col != 0:
          print(",", end = " ")
        print(col_list[col][1], end = "")
      
      print()

print_db_schema('data/sales.db')