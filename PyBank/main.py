import os
import csv

csvpath = os.path.join('Resources','budget_data.csv')

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    print (csvreader)
    csv.header = next(csvreader)
    print(f"csv header:{csv.header}")
    for row in csvreader:
        print(row)