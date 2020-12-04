# import os module 
import os

# import module for reading csv files 
import csv

# import employee_data from csv file 
csvpath = 'resources/election_data.csv'

## converting employee rcords to a new format 



## test data retrieve 
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

  
    for row in csvreader:
        print(row)
