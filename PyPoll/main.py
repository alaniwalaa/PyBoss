# import os module 
import os

# import module for reading csv files 
import csv

# import employee_data from csv file 
csvpath = 'resources/election_data.csv'

# setting variables and counters 
vote_count = 0 


# 1- counting votes 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = '-')
    
    # loop through rows 
    next(csvreader)
    for row in csvreader:
        vote_count = vote_count + 1   
      
print("Total Votes: ", vote_count)
csvfile.close()


# 2- list of candidates 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    candidate_dict = {} 
    pre_candidate = None
    current_candidate = ''
    cand_votes = 0
    # loop through rows - start with the second row (skipping the header row)
    next(csvreader)
    for row in csvreader:
        if pre_candidate == None:
            pre_candidate = row[2]
            candidate_dict[pre_candidate] = candidate_dict[pre_candidate] + 1 
        current_candidate = row[2]
        candidate_dict[pre_candidate] = cand_votes
        pre_candidate = current_candidate
    
    print(candidate_dict)

    
    csvfile.close()





'''## test data retrieve 
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

  
    for row in csvreader:
        print(row)'''


'''# import os module 

# 2- calculate the total amount of Profit/Losses
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
     
    # loop through rows - start with the second row (skipping the header row)
    next(csvreader)
    for row in csvreader:
        net_total = int(net_total) + int(row[1])
         
    print("Total: $", net_total)
    csvfile.close()

# 3- calculating changes in profit/losses and finding average
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    
    
    previous_row_value = None
    # loope through rows - skipping the header row 
    next(csvreader)
    for row in csvreader:
        if previous_row_value == None:
            previous_row_value = float(row[1])
            continue
        current_row_value = float(row[1])
        changes = current_row_value - previous_row_value
        sum_of_changes = sum_of_changes + changes

# 4- greatest increase / decrease 
        # finding the INCREASE 
        if gr_increase < changes:
            gr_increase = changes
            date_increase = row[0]


        # finding the DECREASE
        if gr_decrease > changes:
            gr_decrease = changes
            date_decrease = row[0]


        # update previous row
        previous_row_value = current_row_value
        ave_change = sum_of_changes/(date_count-1)
    
    print("Average Change: $", "{:.2f}".format(ave_change))
    print("Greatest Increase in Profits: ", date_increase, "$", gr_increase)
    print("Greatest Decrease in Profits: ", date_decrease, "$", gr_decrease)

    csvfile.close()


# export the outcomes of the dataset to a csv file 
with open('analysis/analized_budget_data.csv', 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow([{
        'Total Monthe': date_count,
        'Total: $': net_total,
        'Average Change:': ave_change, 
        'Greatest Increase in Profits: ': gr_increase, 
        'Greatest Decrease in Profits: ': gr_decrease
    }])'''
