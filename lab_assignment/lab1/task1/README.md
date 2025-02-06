# Task 1: Print Database Schema

## Overview

This task involves working with a SQLite database file (`data/sales.db`) to extract and display its schema in a structured and reusable manner. The goal is to create a function that prints the names of all tables along with their column names, sorted alphabetically.

## Requirements

1. **Locate the Database File**: Ensure the `data/sales.db` file exists in your project directory.
2. **Function Implementation**: Create a Python function `print_db_schema` in `code/task1.py` that:
   - Accepts a database filename as input.
   - Prints the names of all tables in alphabetical order.
   - For each table, prints its column names sorted alphabetically, separated from the table name by `": "` (colon followed by space).
   - Handles invalid filenames gracefully by printing `"Invalid filename provided"`.

### Example Output

If the database contains two tables (`telephone` and `alpha`) with the following fields:

- **telephone**: `zip_code`, `number`
- **alpha**: `name`, `lastname`, `id`

The output of the function should be:

- **alpha**: `id`, `number`, `lastname`
- **telephone**: `number`, `zip_code`