# Data Exploration Tasks

This section contains tasks related to exploring data from different departments at GatorRetailNYC. The tasks involve working with SQLite, Excel, JSON, and CSV files.

## Table of Contents

- [Task 1: Sales Data (SQLite)](#task-1-sales-data-sqlite)
- [Task 2: Human Resources Team (Excel)](#task-2-human-resources-team-excel)
- [Task 3: Acquisitions (JSON)](#task-3-acquisitions-json)
- [Task 4: Marketing (CSV)](#task-4-marketing-csv)
- [License](#license)


## Task 1: Sales Data (SQLite)

### Overview

Locate the `data/sales.db` database file and implement the following function in `main.py`:

#### `print_db_schema(directory: str) -> None`

This function takes the path of a directory and prints the names of all tables in alphabetical order. For each table, print its corresponding column names sorted alphabetically, separated from the table name by a ": ".

#### Example

If we had two tables, named `telephone` and `alpha` with fields as follows:

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


## Task 2: Human Resources Team (Excel)

### Overview

The HR team maintains hiring records and annual reports in Excel files from 2015 to 2025. These files are consolidated into a folder named `data` in your file tree.

Implement the following functions in `main.py`:

#### 1. `list_excel_files(directory: str) -> None`

This function takes the path of a directory and prints a list of Excel file names in alphabetical order. Non-Excel files should be ignored.

#### Example

If the directory contains the following files:

```sh
$ ls
tasks.csv  Jane.xlsx  Jon.xlsx  Jake.xlsx  report.docx
```

Calling the function should print:

```python
Jake.xlsx
Jane.xlsx
Jon.xlsx
```


#### 2. `print_excel_schema(filename: str) -> None`

This function takes the name of an Excel file as input and prints the schema (sorted column names) for each sheet in the file. Sheets are processed in alphabetical order of their names.

#### Example

If `example.xlsx` contains two sheets with the following columns:

```
sheet_Z: zip_code, number
sheet_A: name, lastname, id
```

Calling the function should print:

```
sheet_A: id, lastname, name
sheet_Z: number, zip_code
```


#### Error Handling

- If an invalid filename is provided (missing or not an `.xlsx` file), print:

```
Invalid filename provided.
```


## Task 3: Acquisitions (JSON)

### Overview

The acquisitions team employs JSON to store data due to the loose structure of attributes present. We have the `acquisitions.json` file in the `data` folder which contains a list of acquisitions. Each object in the list may have a different set of keys.

Implement the following functions in `main.py`:

#### 1. `analyze_json(directory: str) -> None`

This function takes the path of a directory and prints out all the different keys present in all the JSON objects and also displays the number of occurrences of each key.

#### Example

If `example.json` contains the following data:

```json
[
  {
    "name": "Jon Doe",
    "age": 10,
  },
  {
    "name": "Jane Doe",
    "age": 10,
    "salary": 105000
  }
]
```

Calling the function should print:

```
age: 2
name: 2
salary: 1
```


#### 2. `print_json_schema(filename: str) -> None`

This function takes the name of a JSON file as input and prints the schema of the file. The schema of a JSON is its list of keys present in all the objects, sorted in alphabetical order. File name and JSON attributes should be separated by a ": ". Remove the file extension from the filename.

#### Example

If `sample.json` contains the following structure:

```json
[
  {
    "name": "Jon Doe",
    "age": 10,
  },
  {
    "name": "Jane Doe",
    "age": 10,
    "salary": 105000
  }
]
```

Calling the function should print:

```
sample: age, name, salary
```


#### Error Handling

- If an invalid filename is provided (missing or not an `.json` file), print:

```
Invalid filename provided.
```


## Task 4: Marketing (CSV)

### Overview

The marketing team uses third-party software that only allows them to export their data as CSV files. These files store information about various campaigns.

Implement the following function in `main.py`:

#### `print_csv_schema(csv_filename: str) -> None`

This function takes the path of a CSV file and prints the column names sorted alphabetically.

#### Example

If the CSV file (named `sample.csv`) contents were as follows:

```
name, lastname, id
jane, doe, 1
jon, doe, 3
```

The function should output:

```
sample: id, lastname, name
```


#### Error Handling

- If an invalid filename is provided (missing or not an `.csv` file), print:

```
Invalid filename provided.
```

## License

MIT License