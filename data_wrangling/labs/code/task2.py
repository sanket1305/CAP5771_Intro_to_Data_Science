# WRITE YOUR CODE HERE
import csv
import sqlite3

def show_transaction_type_stats():
    input_db_path = "../output/cleaned_data.db"
    input_conn = sqlite3.connect(input_db_path)
    input_cursor = input_conn.cursor()

    query = "SELECT transaction_type, COUNT(*) FROM Orders GROUP BY transaction_type"
    input_cursor.execute(query)

    for transaction_type in input_cursor.fetchall():
        print(transaction_type[0], end = ": ")
        print(transaction_type[1])
    # print(input_cursor.fetchall())

    # close connections to both DBs
    input_conn.close()
  
def standardize_transaction_type():
    input_db_path = "../output/cleaned_data.db"
    input_conn = sqlite3.connect(input_db_path)
    input_cursor = input_conn.cursor()

    query = "SELECT * FROM (SELECT order_id, user_id, order_number, order_dow, order_hour_of_day, days_since_prior_order, lower(REPLACE(REPLACE(transaction_type, ' ', ''), '-', '')) as transaction_type, checkout_value FROM Orders)"
    input_cursor.execute(query)

    # print(input_cursor.fetchall())
    rows = input_cursor.fetchall()

    column_names = [desc[0] for desc in input_cursor.description]

    csv_file = "../output/task2_output.csv"
    with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        
        # Write header
        writer.writerow(column_names)
        
        # Write data
        writer.writerows(rows)


show_transaction_type_stats()
standardize_transaction_type()