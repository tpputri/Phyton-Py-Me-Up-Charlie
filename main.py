# import os and csv modules, set path
import os
import csv
pypollpath = os.path.join('Resources', 'election_data.csv')

# declare initial variables
voter_id=[]
county=[]
voted_for=[]

# open and read
with open (pypollpath, newline='') as analysisfile:

    filereader = csv.reader(analysisfile, delimiter = ',')
    file_header = next (filereader)
    #check if header is loaded
    #print(f"headers: {file_header}")
    
    for row in filereader:
        #check if rows are loaded
        #print(row)
        voter_id.append(row[0])
        county.append((row[1]))
        voted_for.append((row[2]))

# The total number of votes cast
total_votes = len (voter_id)

# A complete list of unique candidates who received votes
candidate_list = []
i = 0
for name in voted_for:
    if name not in candidate_list:
        candidate_list.append(voted_for[i])
    i += 1

# The total number of votes each candidate won
candidate_votes = []
c_max = len (candidate_list)
for j in range (c_max):
    candidate_votes.append(0)
    for k in range (total_votes):
        if candidate_list[j] == voted_for [k]:
            candidate_votes[j] = int(candidate_votes[j]) + 1

# The percentage of votes each candidate won
candidate_percent = []
list_max = len (candidate_votes)
for j in range (list_max):
    percent =  format(float(((candidate_votes[j])/total_votes)*100), '.3f')
    candidate_percent.append(percent)

# The winner of the election based on popular vote.
winner_index = 0
for j in range (c_max):
    if candidate_votes[j] > candidate_votes[winner_index]:
        winner_index = j

winner = candidate_list[winner_index]

# print to terminal
print (f"""
Election Results
----------------------------
Total Votes: {total_votes}
----------------------------""")

for j in range(c_max):
    print (f"{candidate_list[j]}: {candidate_percent[j]}% ({candidate_votes[j]})")

print (f"""----------------------------
 Winner {winner}
----------------------------""")

# print to text file
output_path = os.path.join("pypoll_output.txt")
with open(output_path, 'a') as txt_file:
    txt_file.write (f"Election Results"+'\n')
    txt_file.write(f"-------------------------" + '\n')
    txt_file.write(f"Total Votes: {total_votes}" + '\n')
    for j in range(c_max):
        txt_file.write(f"{candidate_list[j]}: {candidate_percent[j]}% ({candidate_votes[j]})" + '\n')
    txt_file.write("--------------------------" + '\n')
    txt_file.write(f"Winner: {winner}")
