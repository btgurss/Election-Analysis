import csv
import os

#Assigning variable to load file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

#Assigning variable to save file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize a total vote counter.
total_votes = 0

#List to hold candidates
candidate_options = []

#Dictionary to hold Candidate vote totals
candidate_votes = {}

#Declaring variables for winning candidate count
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    #Reading the header row
    headers = next(file_reader)

#Print each row in CSV file
    for row in file_reader:
       
        #Adding votes to total
        total_votes += 1

        #Printing candidate name from each row.
        candidate_name = row[2]

        #Using if statement to determine if name is listed
        if candidate_name not in candidate_options:
            
            #Adding candidate name to the candidate list
            candidate_options.append(candidate_name)

            #Tracking candidate vote counts
            candidate_votes[candidate_name] = 0

        #Count the votes
        candidate_votes[candidate_name] += 1

    #Opeing file to write results to
    with open(file_to_save, "w") as txt_file:

        #Print the final vote count to the terminal
        election_results = (
            f"\nElection Results\n"
            f"------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"------------------------\n")
        print(election_results, end="")

        #Sending written results to election_analysis txt file
        txt_file.write(election_results)

        #Figuring vote percentage
        for candidate_name in candidate_votes:
            
            #Retrieve vote count of a candidate.
            votes = candidate_votes[candidate_name]
           
            #Calculate percentage
            vote_percentage = float(votes) / float(total_votes) * 100
            
            #Print candidate name and percentage of votes
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            print(candidate_results)

            #Sending written results to txt file
            txt_file.write(candidate_results)

            #If statement to determine winner
            if(votes>winning_count) and (vote_percentage>winning_percentage):
                winning_count = votes
                winning_percentage = vote_percentage
                winning_candidate = candidate_name

        #Printing winning candidate information    
        winning_candidate_summary = (
            f"--------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"--------------------------\n")

        print (winning_candidate_summary)

        #Sending written information to txt file
        txt_file.write(winning_candidate_summary)

#Closing File  
election_data.close()
