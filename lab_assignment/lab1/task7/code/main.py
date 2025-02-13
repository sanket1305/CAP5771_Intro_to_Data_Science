import pandas as pd
import sqlite3

# 1. function to print total salary bill per year 
def total_salary_bill_per_year():
    # connect to the SQLite database (input)
    db_path = '../data/output.db'
    conn = sqlite3.connect(db_path)

    # query to get aggregated salary bills (by year) from table
    query = "SELECT year, round(sum(salary),2) as total_salary_bill FROM Salary GROUP BY year ORDER BY year"
    df_from_db = pd.read_sql(query, conn)

    # process and print all the rows from query result
    for index, row in df_from_db.iterrows():
        print(str(int(row['year'])) + " " + str(row['total_salary_bill']))
    
    conn.close()

# 2. function to print sum of bonus given per year
def total_bonus_by_year():
    # connect to the SQLite database (input)
    db_path = '../data/output.db'
    conn = sqlite3.connect(db_path)

    # query to get aggregated salary bills (by year) from table
    # query = "SELECT year, sum(bonus) as total_bonus FROM Bonus where year='2015'"
    query = "SELECT year, round(sum(bonus), 2) as total_bonus FROM Bonus GROUP BY year ORDER BY year"
    df_from_db = pd.read_sql(query, conn)

    # process and print all the rows from query result
    for index, row in df_from_db.iterrows():
        # formatting is required to convert 1 decimnal point values to 2 decimal points
        print(f"{int(row['year'])} {row['total_bonus']:.2f}")
    conn.close()

# 3. function to print all-time month-wise hiring count
def monthly_hiring_stats():
    # connect to the SQLite database (input)
    db_path = '../data/output.db'
    conn = sqlite3.connect(db_path)

    # query to get aggregated salary bills (by year) from table
    # query = "SELECT year, sum(bonus) as total_bonus FROM Bonus where year='2015'"
    query = "SELECT date_of_joining FROM Employees"
    df_from_db = pd.read_sql(query, conn)

    # checked data type of column and converted to datetime to extract month
    # print(df_from_db.dtypes)
    df_from_db['date_of_joining'] = pd.to_datetime(df_from_db['date_of_joining'], errors='coerce')
    # df_from_db['month'] = df_from_db['date_of_joining'].dt.month            # this gives you the month in integer format
    df_from_db['month'] = df_from_db['date_of_joining'].dt.strftime("%m")   # this gives you the month in string format

    # print(df_from_db)

    month_counts = df_from_db['month'].value_counts().sort_index()
    # print(month_counts.describe, type(month_counts))

    # process and print all the rows from query result
    for month, count in month_counts.items():
        print(f"{month} {count}")
    conn.close()
    

# 4. function to print most expensive acquisition
def most_costly_acquisition():
    # connect to the SQLite database (input)
    db_path = '../data/output.db'
    conn = sqlite3.connect(db_path)

    # query to get most expensive acquisition
    query = "SELECT max(cost) as cost FROM Acquisitions"
    df_from_db = pd.read_sql(query, conn)

    # process and print all the rows from query result
    for index, row in df_from_db.iterrows():
        print(str(row['cost']))
    conn.close()

# 5. function to print most expensive "Office" acquisition
def most_costly_office_acquisition():
    # connect to the SQLite database (input)
    db_path = '../data/output.db'
    conn = sqlite3.connect(db_path)

    # query to get most expensive "Office" acquisition
    query = "SELECT max(cost) as cost FROM Acquisitions where type = 'Office'"
    df_from_db = pd.read_sql(query, conn)

    # process and print all the rows from query result
    for index, row in df_from_db.iterrows():
        print(str(row['cost']))
    conn.close()

if __name__ == "__main__":
    total_salary_bill_per_year()
    total_bonus_by_year()
    monthly_hiring_stats()
    most_costly_acquisition()
    most_costly_office_acquisition()