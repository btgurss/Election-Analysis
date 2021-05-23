# Election-Analysis

## Purpose
Tom is working to audit and certify election results from a district in Colorado.  He and his company want to be able to use the program that is written to be able to quickly audit results from other districts as well, so he has requested the program be written using Python.  My job was to expand on the already written code to produce several pieces of information.  They included:
The total number of votes
Number of votes each candidate received
The percent of votes each candidate received
The winning candidate and his/her information
All of this information needed to be sent to a txt file that could be easily accessed by whomever needed it.

## Election Audit Results
- Determining in the number of votes
In order to determine the total number of votes cast in the election I used a for loop to cycle through each row in the imported csv file.  Within this for loop I added 1 to a count variable.  This count variable was set equal to zero before the for loop began.  

- Breakdown of Counties
Within the for loop listed above I used an if statement to do several things. 
    1.	Check to see if the county was in my list of counties labeled county_options
    2.	If the county was not in the list I added to the list
    3.	I set that county count to zero if I had just added it to the list
    4.	If the county was already on the list I added one to that counties vote total using a dictionary with the county as the key.
  - I then used a for statement to loop through the different county names
  - Once I had a county name I used the get method to count the number of rows with that county name.
  - Using that information I was able to write a formula to find the percentage of the vote that came from that county
  - Lastly I printed the results using an f statement.  The f statement printed the county name, percentage of total vote (formatted to one decimal place), and the raw total vote amount (formatted to include commas) These results were printed to the terminal and to the election analysis txt file.

- Determining the county with the most votes
 Within the for loop that was cycling through the different counties I wrote an If statement that would check to see if that particular county had the highest vote count.  If it did I set that as the winning county.  If the next county had more, the winning county would change.  If it did not have more, the winning county would stay what it already was.


- Determining the number and percentage of votes cast for each candidate
  - In order to determine the number of votes cast to each candidate I wrote a for loop to cycle through each row in the csv file.  Within this for loop I wrote an if statement to determine if a candidates name had already appeared.  If the name had not appeared I added it to the list of candidates.  I also set the value of that candidate’s name key as zero.  Outside of the if statement I added one to the count total (set as the value of the candidate’s name key).  If the candidate’s name was already in the list, then I only needed to add one to the vote counter dictionary. 
  - To find the percentage I retrieved the candidates vote total and divided by the total number of votes.  This was done by using the get method on the candidate’s name key.  I printed out the results with a format for one decimal place on the percentage and commas in the total count.

- Winning Candidate
To determine the winning candidate I created an if statement inside of the for loop cycling through the candidate names.  The if statement was triggered if the votes and percentage of a particular candidate was more than any other candidate that had already been cycled through.  If they were, that candidate became the winning candidate and the winning amounts were set to his/her values.

## Election Audit Summary
The way this particular program works it would be very easy to make it work with a variety of election results.  The program reads through each column to find the number of candidates and then uses then creates lists and dictionaries based on the amount of different information.  There could be any number of candidates or counties and this program would still be able to sort through and push out information.  There are some changes that would need to be made in certain situations:
If the election commission would like information on precincts instead of counties, we could modify the code with the county code as a template.
The script could also be made longer to accommodate elections that will have multiple questions to be voted on.  We may need to either add another for loop to cycle through each particular question or office to quickly present all of the data the election requires.
