# import os module 
import os

# import module for reading csv files 
import csv

# import budget_data from csv file 
csvpath = 'resources/budget_data.csv'

date_count = 0 
net_total = 0
changes = 0
sum_of_changes = 0
ave_cahnge = 0
gr_increase = 0 
gr_decrease = 0 
date_increase = ""
date_decrease = ""

# read the source file (budget_data)
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = '-')
    
    # loop through rows 
    for row in csvreader:
        date_count = date_count + 1   
      
# print('total months in the budget data:' + total)
print("Total Months: ", date_count -1)

# calculate the total amount of Profit/Losses
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
     
    # loop through rows 
    next(csvreader)
    for row in csvreader:
        net_total = int(net_total) + int(row[1])
         
    # change[i] = profits[i] - profits[i-1]
    print("Total: $", net_total)


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    next(csvreader)
    for row in csvreader:

        row1 = int(row[1]) 
        row2 = int(row[1])+1
        
        changes = row1 + row2
    

        #changes = int(int(row)+1)[1] + int(row[1])
        sum_of_changes = sum_of_changes + changes
    next
    ave_cahnge = sum_of_changes/(date_count-1)
    print("Average Change: $", ave_cahnge)

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
     
    # loop through rows 
    next(csvreader)
    for row in csvreader:
        #net_total = int(net_total) + int(row[1])

        if gr_increase < int(row[1]):
            gr_increase = int(row[1])
            date_increase = row[0]

        if gr_decrease > int(row[1]):
             gr_decrease = int(row[1])
             date_decrease = row[0]
         
    print("Greatest Increase in Profits: ", date_increase, "$", gr_increase)
    print("Greatest Decrease in Profits: ", date_decrease, "$", gr_decrease)

# export budget_data to a csv file 
output_path = 'analysis/analized_budget_data.csv'

with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow([{
        'Total Monthe': date_count,
        'Total: $': net_total,
        'Average Change:': ave_cahnge, 
        'Greatest Increase in Profits: ': gr_increase , 
        'Greatest Decrease in Profits: ': gr_decrease}])

