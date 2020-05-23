# Importing dependencies needed for the code

import os
import csv

# Setting up path for the csv reader

poll_path = os.path.join("C:\\", "python-challenge", "PyPoll", "Resources", "election_data.csv")
with open(poll_path, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    print(csvreader)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    votes = 0
    khan = 0
    li = 0
    otooley = 0
    correy = 0

    for row in csvreader:

        votes = votes + 1 #verified code skips header
    
        name = row[2]
        can1 = ["Khan"]
        can2 = ["O'Tooley"]
        can3 = ["Li"]
        can4 = ["Correy"]

        if name in can1:
            khan = khan + 1
        elif name in can2:
            otooley = otooley + 1
        elif name in can3:
            li = li + 1
        else:
            correy = correy + 1
    def largest(array,n):
        max = array[0]
        for i in range(1, n):
            if array[i] > max:
                max = array[i]
        return max
    array = [khan, otooley, li, correy]
    n = len(array)
    winner = largest(array, n)
    if winner == khan:
        winner = "Khan"
    elif winner == otooley:
        winner = "O'Tooley"
    elif winner == li:
        winner = "Li"
    else:
        winner = "Correy"


    print("Total Votes: " + str(votes), file=open("pollanalysis.txt", "a"))
    print("-------------------------------------", file=open("pollanalysis.txt", "a"))
    print(f"Li: {round((li / votes) * 100)}% ({li})", file=open("pollanalysis.txt", "a"))
    print(f"O'Tooley: {round((otooley / votes) * 100)}% ({otooley})", file=open("pollanalysis.txt", "a"))
    print(f"Khan: {round((khan / votes) * 100)}% ({khan})", file=open("pollanalysis.txt", "a"))
    print(f"Correy: {round((correy / votes) * 100)}% ({correy})", file=open("pollanalysis.txt", "a"))
    print("-------------------------------------", file=open("pollanalysis.txt", "a"))
    print(winner, file=open("pollanalysis.txt", "a"))

    print("Total Votes: " + str(votes))
    print("-------------------------------------")
    print(f"Li: {round((li / votes) * 100)}% ({li})")
    print(f"O'Tooley: {round((otooley / votes) * 100)}% ({otooley})")
    print(f"Khan: {round((khan / votes) * 100)}% ({khan})")
    print(f"Correy: {round((correy / votes) * 100)}% ({correy})")
    print("-------------------------------------")
    print(f"The winner is {winner}")