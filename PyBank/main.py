# Importing dependencies needed for the code

import os
import csv

# Setting up path for the csv reader

budget_path = os.path.join("C:\\", "python-challenge", "PyBank", "Resources", "budget_data.csv")
with open(budget_path, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    print(csvreader)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")
    # for row in csvreader:
    #     print(row)
# Setting start values for all of my data counts
    months = 0
    net = 0
    greatest = 0
    greatloss = 0

# Creating my program that runs through my csv file to gather my data
    for row in csvreader:
       
        months = months + 1 # This will gather the total months for the budget
        net = net + int(row[1]) # This will create a total gain/lost and can account for negatives
        
        if int(row[1]) > greatest: # I had to get creative on how to determine the largest gain or lost so I figured this would be reliable
            greatest = int(row[1])

        if int(row[1]) < greatloss:
            greatloss = int(row[1])
    avg_change = net / months

    print("Total Months: " + str(months))
    print("Average Change: " + str(avg_change))
    print("Profit/Loss: " + str(net))
    print("Biggest Gain: " + str(greatest))
    print("Biggest Loss: " + str(greatloss))  #Final Prints

    print("Total Months: " + str(months), file=open("Analysis.txt", "a"))
    print("Average Change: $" + str(avg_change), file=open("Analysis.txt", "a"))
    print("Profit/Loss: $" + str(net), file=open("Analysis.txt", "a"))
    print("Biggest Gain: $" + str(greatest), file=open("Analysis.txt", "a"))
    print("Biggest Loss: $" + str(greatloss), file=open("Analysis.txt", "a"))


