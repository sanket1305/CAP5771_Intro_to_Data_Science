from collections import defaultdict
import json, os

def analyze_json(filename):
  # check if file exists and has valid extension
  if not os.path.exists(filename) or filename[-5:] != '.json':
    print("Invalid filename provided")
  else:
    # dictionary to store freq of each key
    d = defaultdict(int)

    # load json file into variable
    with open(filename, 'r') as f:
      data = json.load(f)
    
    # parse json file and update freq for each key
    for item in data:
      for key in item.keys():
        d[key] += 1
    
    # disply keys in sorted order
    for key, value in sorted(d.items()):
      print(key, end = ": ")
      print(value)

def print_json_schema(filename):
  # check if file exists and has valid extension  
  if not os.path.exists(filename) or filename[-5:] != '.json':
    print("Invalid filename provided")
  else:
    # using set to avoid duplicates
    s = set()

    # load json file into variable
    with open(filename, 'r') as f:
      data = json.load(f)
    
    # parse json file and add each key to set
    for item in data:
      for key in item.keys():
        s.add(key)
    
    # sort unqiue keys
    s = sorted(s)

    # extract filename by removing nested directories 
    # and extension from given path
    filename = filename.split('/')[-1]
    filename = filename.split('.')[0]
    print(filename, end = ": ")

    # display results
    for i in range(len(s)):
      if i != 0:
        print(",", end = " ")
      print(s[i], end = "")
    print()

analyze_json('data/acquisitions.json')
print_json_schema('data/acquisitions.json')