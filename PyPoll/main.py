import os
import csv

#import data from resources and calculate the count
csvpath = os.path.join('Resources','election_data.csv')

def print_candiate(election_data):
    # For readability, it can help to assign your values to variables with descriptive names
    voter_ID = str(election_data[0])
    county = str(election_data[1])
    candidate = str(election_data[2])
    
    total_vote = (voter_ID).count
    print(candidate)

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        print_candiate(csvpath)