# import os module 
import os

# import module for reading csv files 
import csv

# import budget_data from csv file 
csvpath = 'resources/budget_data.csv'

# read the source file (budget_data)
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = '-')
    
    # reset counter for rows counting 
    date_count = 0 
    # loop through rows 
    for row in csvreader:
        date_count = date_count + 1   
      
# print('total months in the budget data:' + total)
print(date_count -1)

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
  
    # Reset counter for net calculation
    net_total = 0
    
     # loop through rows 
    next(csvreader)
    for row in csvreader:
        net_total = int(net_total) + int(row[1])

    print(net_total)


'''
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

for netotal in csvreader:
    netotal = total + 1 

# to calculate th echanges over the entire period 
change[i] = profits[i] - profits[i-1] '''


