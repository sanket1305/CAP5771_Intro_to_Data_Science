# Task 3 : Acquisitions (JSON)

## Overview
The acquisitions team employs JSON to store data due to loose structure of the nature of attributes present due to difference in the nature of attributes in each acquisition. We have the acquisitions.json file in the data folder which contains a list of acquisitions. Each object in the list may have different set of keys.

Implement the following functions in `main.py`:

### 1. `analyze_json(directory: str) -> None`
This function takes the path of a directory and prints out all the different keys present in all the json objects and also displays the number of occurrences of each key. The output should print each filename on a new line in alphabetical order.

#### Example
If `example.json` contains the following data:
``` json
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


### 2. `print_json_schema(filename: str) -> None`
This function takes the name of an JSON file as input and prints the schema of the file. The schema of a json is its list of key’s present in all the objects, sorted in alphabetical order. File name and json attributes should be separated by a ": " Remove the file extension from the filename

#### Example
If `sample.json` contains the following structure:
```
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