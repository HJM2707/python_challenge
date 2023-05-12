
# importing dependencies
import os
import csv



# Setting a path for the  file
filepath = os.path.join(r'C:\Users\61469\python_challenge\PyPoll\resources\election_data.csv')

# Opening the CSV
with open(filepath, 'r', encoding='utf') as csvfile:

    # CSV reader specifiing the delimiter and variable that holds contents within the file
    csvreader = csv.reader(csvfile, delimiter=',')

    # Reading the first row (header)
    csv_header = next(csvreader)

    # Set Empty Lists for Variables
    total_votes = 0
    candidate_list = []
    unique_candidate = []
    vote_count = []
    vote_percent = []

    # Loop through Data
    for row in csvreader:
        # Count the total number of votes
        total_votes += 1
        # Add the candidate names to candidate_list
        candidate_list.append(row[2])
        # Create a set from the candidatelist to get the unique candidate names
    for name in set(candidate_list):
        unique_candidate.append(name)
        # candidate_vote_count is the total number of votes per candidate
        candidate_vote_count = candidate_list.count(name)
        vote_count.append(candidate_vote_count)
        # candidate_vote_percentage is the percent of total votes per candidate
        candidate_vote_percentage = float(candidate_vote_count)/float(total_votes)*100
        vote_percent.append(candidate_vote_percentage)
           
    winning_vote_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_vote_count)]
 
    # Set up an empty dictionary
    candidate_dict = {}

    # Loop through the candidates and their corresponding vote counts
    for i in range(len(set(unique_candidate))):
        candidate = unique_candidate[i]
        # Store the candidate's name, vote count, and percentage in the dictionary
        # Use the fix mentioned above to avoid the 'TypeError'
        vote_count_for_candidate = vote_count[i]
        vote_percent_for_candidate = vote_percent[i]
        candidate_dict[candidate] = [vote_count_for_candidate, vote_percent_for_candidate]

# Print Results
print("Election Results")   
print("-------------------------")
print(f"Total Votes: {total_votes}")   
print("-------------------------")

# Loop through the dictionary to print the results in the desired order
# Sort the keys of the dictionary to ensure that the results are printed in the desired order
for candidate in sorted(candidate_dict.keys()):
    vote_info = candidate_dict[candidate]
    print(f"{candidate}: {vote_info[1]:.3f}% ({vote_info[0]})")

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Print to a text file: election_results.txt
output_txt = os.path.join(r'C:\Users\61469\python_challenge\PyPoll\analysis\Election_Results.txt')
with open(output_txt, "w") as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write(f"Total Vote: {total_votes}\n")
    text.write("---------------------------------------\n")
    for candidate, vote_info in candidate_dict.items():
        text.write(f"{candidate}: {vote_info[1]:.3f}% ({vote_info[0]})\n")
    text.write("---------------------------------------\n")
    text.write(f"Winner is: {winner}\n")
    text.write("---------------------------------------\n")

   
