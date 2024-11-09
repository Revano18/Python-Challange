# Dependencies
import csv
import os

#Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources/budget_data.csv")
outputFile = os.path.join("Financial_Analysis.txt")

# Define variables to track the financial data
total_months = 1
total_net = 0
months = []
average_change = []

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Read the header row
    header = next(reader)

    # Extract first row 
    FirstRow = next(reader)

    PreviousNet = float(FirstRow[1])

    # Process each row of data
    for row in reader:

        # Track the total
        total_months += 1

        #calculate net change
        total_net += float(row[1])
        net_change = float(row[1]) - PreviousNet
        average_change.append(net_change)
        PreviousNet = float(row[1])

        #add the first month that change occured
        months.append(row[0])       #month is in index 0

#calculate the average net change
averageChangePerMonth = sum(average_change) / len(average_change)

greatestIncrease = [months[0], average_change[0]]
greatestDecrease = [months[0], average_change[0]]
#use loop to calculate the index of the Greatest and Least monthly change
for m in range(len(average_change)):
    #calculate the Greatest Increase and Decrease
    if(average_change[m] > greatestIncrease[1]):
        greatestIncrease[1] = average_change[m]
        greatestIncrease[0] = months[m]

    if(average_change[m] < greatestDecrease[1]):
        greatestDecrease[1] = average_change[m]
        greatestDecrease[0] = months[m]

#  Generate the output summary
output =f"""
Financial Analysis
----------------------------
Total Months = {total_months}
Total Net = ${total_net:,.2f}
Average Change Per Month = ${averageChangePerMonth:,.2f}
Greatest Increase in Profits = ${greatestIncrease[0]} Amount ${greatestIncrease[1]:,.2f}
Greatest Decrease in Profits = ${greatestDecrease[0]} Amount ${greatestDecrease[1]:,.2f}
"""
      
# Print the output
print(output)

# export the output to the output text file
with open(outputFile, "w") as textfile:
    textfile.write(output)