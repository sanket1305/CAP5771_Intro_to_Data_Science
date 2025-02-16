# Task 1 : Sales data (SQLite)

## Overview
Locate the data/sales.db database file in your file tree. Your initial task is to print the database schema. Given your expertise as a data scientist, you know the benefits of developing reusable code.

Implement the following functions in `main.py`:

### 1. `print_db_schema(directory: str) -> None`
This function takes the path of a directory and prints the names of all tables in alphabetical order. For each table, print its corresponding column names sorted alphabetically separated from the table name by a ": " (colon and followed by space).

#### Example
If we had two tables, named `telephone` and `alpha` and their fields were as follows:
```
telephone: zip_code, number
alpha: name, lastname, id
```
Calling the function should print:
```
alpha: id, lastname, name
telephone: number, zip_code
```

#### Error Handling
- If an invalid filename is provided, print:
  ```
  Invalid filename provided.
  ```
