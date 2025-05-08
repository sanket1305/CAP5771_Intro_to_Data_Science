# Task 6: Data Unification

## Overview
This project focuses on unifying data from various sources into a single SQLite database to enable relationship-based queries. The data is sourced from SQLite (Sales), Excel (HR), JSON (Acquisitions), and CSV (Marketing). The final output is a new SQLite database named `output.db` that consolidates all the data.

The script for this task is implemented in `code/task6.py`.

### Data Sources
1. **SQLite Database**: `data/sales.db`
2. **Excel Files**: All `.xlsx` files in the directory `data/*.xlsx`
3. **JSON File**: `data/acquisitions.json`
4. **CSV File**: `data/campaigns.csv`

### Task Requirements
The script performs the following steps:
1. Reads data from the specified files and formats.
2. Creates a new SQLite database file named `output.db` in the `data` folder.
3. Stores data from all sources into tables within the database, following specific naming conventions.

### Table Naming Instructions
- **Excel Files**: Use the sheet name as the table name. If multiple Excel files have sheets with the same name, merge their data into a single table.
- **JSON Files**: Use the file name as the table name.
- **CSV Files**: Use the file name as the table name.
- **SQLite Files**: Retain the existing table names.

All table names should be in **title case** (e.g., `SheetName`, `FileName`).

### Column Naming Instructions
- **Excel Files**: Use column names as they appear in the Excel files.
- **JSON Files**: Use keys from the JSON files as column names.
- **CSV Files**: Use column names as they appear in the CSV files.
- **SQLite Files**: Retain existing column names.

### Additional Notes
- Convert all date attributes to the format `YYYY-MM-DD` and store them as strings.
- If any invalid input file is provided, print: `Invalid input` text and exit the program.

### Implementation Details
The script utilizes Python libraries such as:
- **Pandas** for reading and processing data from different formats.
- **SQLite3** for creating and managing SQLite databases.

#### Example Workflow
Given the following inputs:
- An Excel file (`hr.xlsx`) with two sheets:
- `Employees`: Columns - Name, Age, Department
- `Salaries`: Columns - EmployeeID, Salary
- A JSON file (`acquisitions.json`) with keys:
- CompanyName, AcquisitionDate, Amount
- A CSV file (`campaigns.csv`) with columns:
- CampaignName, StartDate, EndDate, Budget

The script will produce an SQLite database (`output.db`) with tables:
1. `Employees`: Columns - Name, Age, Department
2. `Salaries`: Columns - EmployeeID, Salary
3. `Acquisitions`: Columns - CompanyName, AcquisitionDate, Amount
4. `Campaigns`: Columns - CampaignName, StartDate, EndDate, Budget

#### Error Handling
If an invalid file is encountered (e.g., missing or unsupported format), print: `Invalid input` text and terminate execution.