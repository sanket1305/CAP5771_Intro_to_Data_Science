# WRITE YOUR CODE HERE
import os
import sqlite3

def remove_legacy_products():
    # connect to source db
    input_db_path = "../data/raw_data.db"
    input_conn = sqlite3.connect(input_db_path)
    input_cursor = input_conn.cursor()

    # connect to output/target db
    output_db_path = "../output/cleaned_data.db"
    output_conn = sqlite3.connect(output_db_path)
    output_cursor = output_conn.cursor()

    # get list of all tables
    query = "SELECT name FROM sqlite_master WHERE type='table';"
    input_cursor.execute(query)
    tables = input_cursor.fetchall()
    
    # print(tables)     # debug

    # for each table, read and write to output table
    for table in tables:
        table_name = table[0]

        # extract schema for each table
        query = f"SELECT sql FROM sqlite_master WHERE type='table' AND name = ?"
        input_cursor.execute(query, (table_name,))
        schema = input_cursor.fetchone()[0]

        # check if schema is visible for each table 
        # print(schema)   # debug

        # create table in output DB
        output_cursor.execute(schema)

        # read all records from input DB
        query = f"SELECT * FROM {table_name}"
        input_cursor.execute(query)
        records = input_cursor.fetchall()

        # insert all records in output DB
        if records:
            query_params = ', '.join(["?" for _ in records[0]])
            query = f"INSERT INTO '{table_name}' VALUES ({query_params})"
            output_cursor.executemany(query, records)
    
    # verify the number of records
    input_cursor.execute("SELECT count(*) FROM OrderProducts;")
    # print(input_cursor.fetchall())

    output_cursor.execute("SELECT count(*) FROM OrderProducts;")
    initial_records = output_cursor.fetchall()
    initial_records = initial_records[0][0]
    # print(initial_records)

    query = "DELETE FROM OrderProducts WHERE product_id NOT IN (SELECT product_id FROM Products where discontinued = 0)"
    output_cursor.execute(query)

    output_cursor.execute("SELECT count(*) FROM OrderProducts;")
    final_records = output_cursor.fetchall()
    final_records = final_records[0][0]
    # print(final_records)

    print(initial_records - final_records)

    # save changes to DB
    output_conn.commit()

    # close connections to both DBs
    input_conn.close()
    output_conn.close()
  
remove_legacy_products()