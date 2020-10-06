import os
import csv

budget_data = os.path.join( "Resources", "budget_data.csv")

# Open and read csv
with open(budget_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    header = next(csv_reader)
    #print(f"Header: {csv_header}")

    #Define a variable to hold how many months are included in the Dataset.
    MonthList = []
    #Define a variable to hold the total Profit/Loss
    Total_PL = []
    #Create a list to hold the values of the change in months
    monthly_change = []

    for row in csv_reader:
        #put all the months in a list
        MonthList.append(row[0])
        #Get total Profit in a list
        Total_PL.append(int(row[1]))
        #Highest/Lowest value of Change
        Highest_Value_Date = Total_PL.index(max(Total_PL))
        Lowest_Value_Date = Total_PL.index(min(Total_PL))

   # find monthly change in profit 
    for i in range(len(Total_PL)-1):
        monthly_change.append(Total_PL[i+1]-Total_PL[i])

        greatest_increase = max(monthly_change)
        greatest_decrease = min(monthly_change)

with open("analysis/results.txt",'w') as f:
    f.write(f'Financial Analysis\n')
    f.write(f'-------------------------\n')
    f.write(f'Total Months: {len(MonthList)}\n')
    f.write(f'Total Profit & Loss: {sum(Total_PL)}\n')
    f.write(f'Monthly Change: {sum(monthly_change)/len(monthly_change)}\n')
    f.write(f'Greatest Increase: {MonthList[Highest_Value_Date]} (${greatest_increase})\n')
    f.write(f'Greatest Decrease: {MonthList[Lowest_Value_Date]} (${greatest_decrease})\n')

print(f'Financial Analysis')
print(f'-------------------------')
#print(f'Total Months: {MonthList}')
print(f'Total Months: {len(MonthList)}')
#print(f'Total Profit & Loss List: {Total_PL}')
print(f'Total Profit & Loss: {sum(Total_PL)}')
print(f'Monthly Change: {sum(monthly_change)/len(monthly_change)}')
print(f'Greatest Increase: {MonthList[Highest_Value_Date]} (${greatest_increase})')
print(f'Greatest Decrease: {MonthList[Lowest_Value_Date]} (${greatest_decrease})')
