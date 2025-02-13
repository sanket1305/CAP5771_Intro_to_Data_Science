# Task 7: Data Insights (SQL)

## Overview
In this task, we will use SQL queries to extract insights from the dataset. The queries should not be hard-coded, as they will be tested against a hidden dataset. All float values must be converted to strings with 2-decimal precision. 

Implement the following functions in `code/task7.py`:

----

### 1. `total_salary_bill_per_year() -> None`
This function retrieves and prints the total salary bill for each year in ascending order.

#### Output Format (space-separated)
```
2000 5579
2001 9987
...
```

----

### 2. `total_bonus_by_year() -> None`
This function retrieves and prints the sum of bonus given per year in ascending order of the year.

#### Output Format (space-separated)
```
2000 985
2001 887
...
```

----

### 3. `monthly_hiring_stats() -> None`
This function retrieves and prints all-time month-wise hiring count in ascending order of the month (integer)

#### Output Format (space-separated)
```
1 888
2 24
...
12 87
```

----

### 4. `most_costly_acquisition() -> None`
This function retrieves and prints value of most expensive acquisition.

#### Output Format
```
4990816.47
```

----

### 5. `most_costly_office_acquisition() -> None`
This function retrieves and prints value of most expensive "Office" acquisition.

#### Output Format
```
4977294.42
```

----

### 6. `product_wise_campaign_spending() -> None`
This function retrieves and prints all-time month-wise hiring count in ascending order of the month (integer)

#### Output Format (space-separated)
```
1 888
2 24
...
12 87
```

----

### 7. `top_5_products_by_sales() -> None`
This function retrieves and prints name of the top 5 products with maximum sales, in order

#### Output Format
```
Wireless Mouse
Portable Fan
Fitness Tracker
LED Desk Lamp
Portable Grill
```

----

### 8. `top_5_retail_stores_by_sales() -> None`
This function retrieves and prints name of the top 5 retail stores with maximum sales, in order

#### Output Format
```
GatorRetailNYC @ Pittsburgh
GatorRetailNYC @ Seattle
GatorRetailNYC @ Hartford
GatorRetailNYC @ Tampa
GatorRetailNYC @ Brooklyn
```

----