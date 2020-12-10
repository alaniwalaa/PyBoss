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
    candidate_list = []
    cand_votes = 0
    cand_win = []
    cand_percent = 0.0
    percent_list = []
    
    # loop through rows - start with the second row (skipping the header row)
    next(csvreader)
    for row in csvreader:
        cand_name = row[2]
        if cand_name not in candidate_list:
            candidate_list.append(cand_name)
            candidate_dict[cand_name] = cand_votes 
            cand_percent = cand_votes / vote_count
            
         
        candidate_dict[cand_name] = candidate_dict[cand_name] + 1

    '''cand_percent = cand_votes/vote_count
    print(cand_percent)''' 
   
    print(candidate_dict)

    # getting the max votes for the winner
    cand_win = max(candidate_dict, key = candidate_dict.get)
    print('Winner: ', cand_win)
    
    csvfile.close()


# export the outcomes of the dataset to a csv file 
with open('analysis/analized_voters_data.csv', 'w', newline='\n') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(['Total Votes: ', vote_count,])
    csvwriter.writerow([candidate_dict, cand_votes])
    csvwriter.writerow(['Winner: ', cand_win])
