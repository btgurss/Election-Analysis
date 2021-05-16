import csv
import os

#Assigning variable to load file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

#Assigning variable to save file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)
#Print each row in CSV file
   # for row in file_reader:
    #    print(row[0])

with open (file_to_save, "w") as txt_file:

    txt_file.write("Counites in the Election")
    txt_file.write("\n--------------------------")
    txt_file.write("\nArapahoe\nDenver\nJefferson")

#Open election results and read the file
with open(file_to_load) as election_data:
#1. Count the total number of votes cast
#2. List all candidates that received votes
#3. Find Percentage of votes for each candidate
#4. Find total number of votes for each candidate
#5. Who won?
#Close the File
    print(election_data)
election_data.close()
