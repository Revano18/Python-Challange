# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  
candidate = []
candidate_votes = {}  
wincount = 0
wincandidate = "" 

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        if row[2] not in candidate:

            # If the candidate is not already in the candidate list, add them
            candidate.append(row[2])

            # Add a vote to the candidate's count
            candidate_votes[row[2]] = 1
        
        else:
            candidate_votes[row[2]] += 1

    # Print the ouput
    candidate_output = ""

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate in candidate_votes:
            votes = candidate_votes.get(candidate)

            # Get the vote count and calculate the percentage
            voteprcnt = (float(votes) / float(total_votes)) * 100

            candidate_output += f"{candidate}: {voteprcnt:.2f}%: ({votes}) \n"
            # Update the winning candidate if this one has more votes
            if votes > wincount:
                wincount = votes
                wincandidate = candidate
wincandidateoutput = f"Winner: {wincandidate}\n"

# Generate and print the winning candidate summary
output =f"""
Election Results
-------------------------
Total Votes:{total_votes}
-------------------------    
{candidate_output}
-------------------------
{wincandidateoutput}
"""



print(output)

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
