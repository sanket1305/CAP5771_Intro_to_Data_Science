# Task 4 : Marketing (CSV)

## Overview
The marketing team at GatorRetailNYC uses third-party software that only allows them to export their data as CSV files. These files store information about various campaigns that the team launches. Explore the `campaigns.csv` file as an example.

Implement the following functions in `main.py`:

### 1. `print_csv_schema(csv_filename: str) -> None`
This function takes the path of a csv file and prints the column names sorted alphabetically. 

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
- If an invalid filename is provided (missing or not an `.xlsx` file), print:
  ```
  Invalid filename provided.
  ```