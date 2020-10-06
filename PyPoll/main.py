import os
import csv

election_data = os.path.join( "Resources", "election_data.csv")

# Open and read csv
with open(election_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    header = next(csv_reader)
    #print(f"Header: {csv_header}")

    PercentageList = []
    CandidateList = []

    for row in csv_reader:
        CandidateList.append(row[2])
        
Khan = CandidateList.count("Khan")
Correy = CandidateList.count("Correy")
Li = CandidateList.count("Li")
OTooley = CandidateList.count('O\'Tooley')

if Khan > Correy and Khan > Li and Khan > OTooley:
    Winner = "Khan"

if Correy > Khan and Correy > Li and Correy > OTooley:
    Winner = "Correy"

if Li > Khan and Li > Correy and Li > OTooley:
    Winner = "Li"

if OTooley > Khan and OTooley > Correy and OTooley > Li:
    Winner = "O'Tooley"

Khan_Votes = round((Khan/len(CandidateList)) * 100, 3)
Correy_Votes = round((Correy/len(CandidateList)) * 100, 3)
Li_Votes = round((Li/len(CandidateList)) * 100, 3)
OTooley_Votes = round((OTooley/len(CandidateList)) * 100, 3)

with open("analysis/results.txt",'w') as f:
    f.write(f'Election Results')
    f.write(f'---------------------')
    f.write(f'Total Votes: {len(CandidateList)}')
    f.write(f'---------------------')
    f.write(f'Khan: {Khan_Votes:.3f}% ({Khan})')
    f.write(f'Correy: {Correy_Votes:.3f}% ({Correy})')
    f.write(f'Li: {Li_Votes:.3f}% ({Li})')
    f.write(f'O\'Tooley: {OTooley_Votes:.3f}% ({OTooley})')
    f.write(f'----------------------')
    f.write(f'Winner: {Winner}')


print(f'Election Results')
print(f'---------------------')
print(f'Total Votes: {len(CandidateList)}')
print(f'---------------------')
print(f'Khan: {Khan_Votes:.3f}% ({Khan})')
print(f'Correy: {Correy_Votes:.3f}% ({Correy})')
print(f'Li: {Li_Votes:.3f}% ({Li})')
print(f'O\'Tooley: {OTooley_Votes:.3f}% ({OTooley})')
print(f'----------------------')
print(f'Winner: {Winner}')
