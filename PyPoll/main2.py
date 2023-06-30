import os
import csv


file_path = os.path.join("Resources","election_data.csv")

total_votes = 0
candidates = {}


with open(file_path, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row

    # for ballot_Id,county,candidate in csv_reader:
    #     ballot_Id_list.append(ballot_Id)
    #     candidate_list.append(candidate)

    for row in csv_reader:
        total_votes += 1
        candidate = row[2]

        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1
    

        percentage_votes = {}
    for candidate, votes in candidates.items():
        percentage_votes[candidate] = round((votes / total_votes) * 100, 3)
                     
    winner = max(candidates, key=candidates.get)

    
   


        # print("Election Results")
        # print("--------------------------")
        # print(f"Total Votes: {str(totalvotes)}")
        # print("--------------------------")
        # for i in range(len(candidate_list)):
        #     print(f"{candidate_list[i]}: {str(percentagevotes[i])} ({str(numofvotes[i])})")
        # print("--------------------------")
        # print(f"Winner: {winningcandidate}")
        # print("--------------------------")

output = f'''
    Election Results
    -----------------------------------------
    Total Votes: {total_votes}
    for candidate, votes in candidates.items():
     {candidate}: {percentage_votes[candidate]}% ({votes})
    {candidate}: 
    -------------------------
    Winner: {winner}
    -------------------------


'''
my_report = open("output.txt", "w")
print(output)
my_report.write(output)
