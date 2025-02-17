# Learnings

This file highlights the key insights and findings from the `Data Wrangling` process.

## Table of Contents
1. [Categorical Data](#categorial-data)

---

## Categorical Data

### _What is Categorical Data?_
Categorical data in pandas refers to variables that can only take on a limited and fixed set of possible values, known as *categories*. This data type is particularly useful for:
1. **String Data with Repeated Values**: For example, "Male" and "Female" in a gender column.
2. **Data with an Inherent Order**: For example, "Low", "Medium", and "High" in a priority column.

By using the categorical data type, pandas can optimize memory usage and improve performance for certain operations.

### _How Does Pandas Handle Categorical Data?_

 Why Isn't Numerical Data Treated as Categorical by Default?
1. **Data Type Differences**: 
   - Numerical data is stored as `int64` or `float64`.
   - Categorical data must be explicitly defined with the `Categorical` data type in pandas.
   
2. **Explicit Conversion**: 
   - While any data type (including numerical) can be converted to categorical, pandas does not assume numerical values are categories unless explicitly specified.

### _Converting Data to Categorical_
You can convert any column to a categorical data type using the `.astype('category')` method. 

**Example:**
```
df['column_name'] = df['column_name'].astype('category')
```

This allows pandas to treat the column as categorical, optimizing memory usage and enabling efficient operations.

---