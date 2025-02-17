# Data Cleaning

This project demonstrates the process of cleaning a dataset from Kaggle using Python. The dataset used in this example is the Melbourne Housing Market dataset. Below, you will find structured instructions and code snippets to perform data cleaning effectively.

---

## Table of Contents
1. [Introduction](#introduction)
2. [Dataset Import](#dataset-import)
3. [Data Description](#data-description)
4. [Data Cleaning Steps](#data-cleaning-steps)
5. [Converting Data Types](#converting-data-types)
6. [Notes on Missing Values](#notes-on-missing-values)
7. [Saving the Data Insights into PDF format](#saving-the-data-insights-into-pdf-format)

---

## Introduction
The goal of this project is to clean and prepare the Melbourne Housing Market dataset for analysis. We will:
- Import the dataset.
- Understand its structure using descriptive statistics.
- Perform necessary data cleaning steps, including type conversions and handling inconsistencies.

---

## Dataset Import
To import the dataset from Kaggle, we use the `kagglehub` library. Run the following code to download the data:

``` python
import kagglehub

kagglehub.dataset_download("anthonypino/melbourne-housing-market")
```

The data will be downloaded into the `.cache` folder. Move the files to your working directory using the `mv` command:

``` sh
mv /home/user/.cache/melbourne-housing-market/* ./data_wrangling/Data/
```

---

## Data Description
To understand the dataset, we use a custom utility function `describe_data` from `descriptive_utils.py`. This function provides a detailed summary of each column.

### Function: `describe_data(df)`
The function performs the following tasks:
1. Prints a header indicating that data description is starting.
2. Displays the number of rows and columns in the dataset.
3. Iterates through each column:
   - **Numeric Columns (int or float):**
     - Prints minimum, maximum, mean, and median values.
   - **Categorical Columns (object or category):**
     - Prints the number of unique categories.
     - If there are 10 or fewer categories, prints their names and counts.
   - **Datetime Columns:**
     - Prints earliest date, latest date, and number of unique dates.

Example usage:
```
from descriptive_utils import describe_data

describe_data(df)
```

---

## Data Cleaning Steps
### Observations from Summary
- The dataset contains 21 variables.
- Some variables require clarification:
  - **Type:** Property type
    - h → House
    - u → Unit (Smaller residential properties, such as apartments)
    - t → Townhouse (A distinct category separate from other units)
  - **Method:** Sale method 
    - S → Property sold (Standard sale)
    - SP → Property sold prior (Sold before the scheduled auction)
    - PI → Property passed in (Did not meet the reserve price at auction)
    - VB → Vendor bid (A bid made by the vendor to influence the auction)
    - SA → Sold after (Sold after the auction)
- The `Date` column is incorrectly interpreted as an object type and needs conversion to datetime format (`%d/%m/%y`).

### Steps:
1. Convert the `Date` column to datetime:
```
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%y', errors='coerce')
```
2. Handle mixed date formats if necessary:
```
df['Date'] = pd.to_datetime(df['Date'], format='mixed', errors='coerce')
```

---

## Converting Data Types
To improve efficiency, convert certain columns from `object` or `float64` to `category`. 

### Variables to Convert:
| Column       | Current Type | Target Type |
|--------------|--------------|-------------|
| Type         | object       | category    |
| Method       | object       | category    |
| Postcode     | float64      | category    |
| YearBuilt    | float64      | category    |
| Regionname   | object       | category    |

### Conversion Code:

```
columns_to_category = ['Type', 'Method', 'Postcode', 'YearBuilt', 'Regionname']
for col in columns_to_category:
df[col] = df[col].astype('category')
```

---

## Notes on Missing Values
- Avoid converting numeric columns with missing values (e.g., `float64`) to integer types (`int64`) directly because integers cannot handle missing values in pandas.
- Retain numeric columns as `float64` if they contain missing data.

---

## Saving the Data Insights into PDF format

The `save_findings_to_pdf` function saves multi-line text content, such as data analysis findings, into a PDF using the ReportLab library. It handles page breaks and adds metadata like the report title and generation date.

### Function: `save_findings_to_pdf(content, output_file="data_findings.pdf")`
Parameters:
- content (str): Text to write into the PDF.
- output_file (str): Name of the output PDF file.

Example Usage:
```
findings = "Data Report:\n1. Number of rows: 1000\n2. Missing values in 'Price': 5%"

save_findings_to_pdf(findings, output_file="report.pdf")
```


---

This structured approach ensures that the dataset is clean and ready for further analysis or modeling.
