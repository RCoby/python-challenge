# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote
#-------------------------------------------------------

# Dependencies
import os
import csv

# Path to collect data 
election_data_csv = os.path.join("..","Resources","election_data.csv")

#Path to text file 
analysis_file = os.path.join("..","analysis", "election_analysis.txt")

# Create variables
total_votes = 0
candidates = []
candidate_votes = {}

# Open CSV file
with open(election_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip header row
    next(csvreader)

    # Loop through each row in CSV file
    for row in csvreader:

        #Count total votes
        total_votes += 1

        # Add candidate name to list of candidates, if not already present
        candidate = row[2]
        if candidate not in candidates:
           candidates.append(candidate)
           candidate_votes[candidate] = 0
    
        # Count the total number of votes each candidate won
        candidate_votes[candidate] += 1   
    
    
    # Open the analysis file and write the results
    with open(analysis_file, "w") as txtfile:
        # Print the results to the terminal
        print("Election Results")
        print("-------------------------")
        print(f"Total Votes: {total_votes}")
        print("-------------------------")
        txtfile.write("Election Results\n")
        txtfile.write("-------------------------\n")
        txtfile.write(f"Total Votes: {total_votes}\n")
        txtfile.write("-------------------------\n")

        # Loop through each candidate and calculate their vote percentage
        for candidate in candidates:
            vote_percentage = candidate_votes[candidate] / total_votes * 100
        
            # Print the candidate results to the terminal
            print(f"{candidate}: {vote_percentage:.3f}% ({candidate_votes[candidate]})")
        
            # Write the candidate results to the analysis file
            txtfile.write(f"{candidate}: {vote_percentage:.3f}% ({candidate_votes[candidate]})\n")
    
        # Determine the winner of the election based on popular vote
        winner = max(candidate_votes, key=candidate_votes.get)
    
        # Print the winner to the terminal
        print("-------------------------")
        print(f"Winner: {winner}")
        print("-------------------------")

        # Write the winner to the analysis file
        txtfile.write("-------------------------\n")
        txtfile.write(f"Winner: {winner}\n")
        txtfile.write("-------------------------\n")