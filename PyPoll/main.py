import os
import csv

csvpath = os.path.join('..', 'PyPoll', 'election_data.csv')

total_votes = 0
candidates = []
unique_candidates = []
O_Tooley_votes = 0
Khan_votes = 0
Correy_votes = 0
Li_votes = 0

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

    for row in csvreader:

        total_votes += 1

        candidates.append(row[2])
        
        if row[2] == "O'Tooley":
            O_Tooley_votes += 1

        elif row[2] == "Khan":
            Khan_votes += 1
 
        elif row[2] == "Correy":
            Correy_votes += 1

        else:
            Li_votes += 1

O_Tooley_Pct = round(O_Tooley_votes/total_votes*100,2)

Khan_Pct = round(Khan_votes/total_votes*100,2)

Correy_Pct = round(Correy_votes/total_votes*100,2)

Li_Pct = round(Li_votes/total_votes*100,2)

Winner = max(O_Tooley_votes, Khan_votes, Correy_votes, Li_votes)

print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")
print("Here is a list of the candidates that received votes: " + str(set(candidates)))
print("-------------------------")
print("Khan: " + str(Khan_Pct) + "% " + "(" + str(Khan_votes) + ")")
print("Correy: " + str(Correy_Pct) + "% " + "(" + str(Correy_votes) + ")")
print("Li: " + str(Li_Pct) + "% " + "(" + str(Li_votes) + ")")
print("O'Tooley: " + str(O_Tooley_Pct) + "% " + "(" + str(O_Tooley_votes) + ")")
print("-------------------------")

if Winner == Correy_votes:
    print("Winner: Correy with " + str(Correy_votes) + " votes")
elif Winner == Khan_votes:
    print("Winner: Khan with " + str(Khan_votes) + " votes")
elif Winner == Li_votes:
    print("Winner: Li with " + str(Li_votes) + " votes")
else:
    print("Winner: O'Tooley with " + str(O_Tooley_votes) + " votes")

with open("Election_Results.txt", "w") as results:

    results.write("Election Results\n")
    results.write("-------------------------\n")
    results.write("Total Votes: " + str(total_votes) + "\n")
    results.write("-------------------------\n")
    results.write("Here is a list of the candidates that received votes: " + str(set(candidates)) + "\n")
    results.write("-------------------------\n")
    results.write("Khan: " + str(Khan_Pct) + "% " + "(" + str(Khan_votes) + ")\n")
    results.write("Correy: " + str(Correy_Pct) + "% " + "(" + str(Correy_votes) + ")\n")
    results.write("Li: " + str(Li_Pct) + "% " + "(" + str(Li_votes) + ")\n")
    results.write("O'Tooley: " + str(O_Tooley_Pct) + "% " + "(" + str(O_Tooley_votes) + ")\n")
    results.write("-------------------------\n")
    
    if Winner == Correy_votes:
        results.write("Winner: Correy with " + str(Correy_votes) + " votes")
    elif Winner == Khan_votes:
        results.write("Winner: Khan with " + str(Khan_votes) + " votes")
    elif Winner == Li_votes:
        results.write("Winner: Li with " + str(Li_votes) + " votes")
    else:
        results.write("Winner: O'Tooley with " + str(O_Tooley_votes) + " votes")