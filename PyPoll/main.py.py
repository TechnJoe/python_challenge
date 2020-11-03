import os
import csv

csvpath = os.path.join("Resources","election_data.csv")


Correy_percent = 0
Khan_percent = 0
Li_percent = 0
Otooley_percent = 0
Correy_votes = 1
Otooley_votes = 1
Khan_votes = 1
Li_votes = 1        
Total_votes_cast = 0
winner = ""
row_count = 0

with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #print(csvreader)
    
    csv_header = next(csvreader)

    #print(f"csv Header: {csv_header}")
    #row_count  = sum(1 for row in csvreader)
    #print (row_count)
    
    for row in csvreader:
        #print(row)
        row_count  = row_count + 1

        #Total number of votes won by each candidate

        #Total_votes_cast = row_count
        
        if (row[2] == "Correy"):
            Correy_votes += 1
        elif(row[2] == "Li"):
            Li_votes += 1
        elif (row[2] == "O'Tooley"):
            Otooley_votes += 1
        elif (row[2] == "Khan"):
            Khan_votes += 1
        
            
    #Total votes cast 
    Total_votes_cast = row_count
        
       #Percentage of votes won by each candidate
    try:
        Correy_percent = round((Correy_votes / Total_votes_cast) *100 )
    except ZeroDivisionError:
        Correy_votes = 0
    
    try:
        Li_percent = round((Li_votes / Total_votes_cast) *100)
    except ZeroDivisionError:
        Li_percent = 0
    
    try:
        Otooley_percent = round((Otooley_votes / Total_votes_cast) *100)
    except ZeroDivisionError:
        Otooley_percent = 0
    
    try:
        Khan_percent = round((Khan_votes / Total_votes_cast) *100)
    except ZeroDivisionError:
        Khan_percent = 0

    
    

    #The winner of the election based on popular vote.

    winner = max(Correy_votes,Li_votes,Otooley_votes,Khan_votes)   
    #winner = max("Correy_votes","Li_votes","Otooley_votes","Khan_vote")
            
    if winner == Correy_votes:
        winner_name = "Correy"
    elif winner == Li_votes:
        winner_name = "Li"
    elif winner == Otooley_votes:
        winner_name = "O'Tooley"
    elif winner == Khan_votes:
        winner_name = "Khan"
    
    #code to create path foroutput file

    output = ""
    output +=(F"\n\n")
    output +=(f"Election_Results\n")
    output +=(f"Total votes cast: { Total_votes_cast }\n")
    output +=(f"Correy: {Correy_percent}% ({Correy_votes})\n")
    output +=(f"Li: {Li_percent}% ({Li_votes})\n")
    output +=(f"O'Tooley: {Otooley_percent}% ({Otooley_votes})\n")
    output +=(f"Khan: {Khan_percent}% ({Khan_votes})\n")
    output +=(f"Winner: {winner_name} - {winner}\n")

    #code to print analysis
    print(output)

# code to create path for output file
data_output = os.path.join("output","pypoll.txt")

#code to write output to output file
with open(data_output, "w", newline="") as txtfile:
    txtfile.write(output)