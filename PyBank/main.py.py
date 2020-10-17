import os
import csv

csvpath = os.path.join( "Resources","budget_data(1).csv")


with open (csvpath) as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")

	#print(csvreader)

	csv_header = next(csvreader)

	#print(f"CSV Header: {csv_header}")

	for row in csvreader:
		#print(row)

# declare all variables used in code
		total_months = 0
		grand_total = 0
		profit_loss = 0
		avg_change = 0
		g_increase = ["",0]
		g_decrease = ["",9999999]
		month = [0]
		greatest = 0
		least = 0
		month_year_i = ""
		month_year_d = ""
		avg_sum = 0
		avg_change_list = []

 
#movement of files and handling 0/56 = 0   .  56/0 Error
with open (csvpath) as csvfile:

	csvreader = csv.reader(csvfile, delimiter=",")
	Header = next(csvreader)  
	firstrow = next(csvreader)
	previous =int(firstrow[1])
	grand_total = int(firstrow[1])

	
	for row in csvreader :
		total_months = total_months + 1
		grand_total = grand_total + int(row[1])
		profit_loss = int(row[1]) - previous
		previous = int(row[1])
		#print(profit_loss)
		#avg_sum = avg_sum + profit_loss
		avg_change_list.append(profit_loss)

		#calculate the greatest increase, decrease and average over entire period
		if profit_loss > g_increase[1]:
			 g_increase[0] = row[0]
			 g_increase[1] = profit_loss

		if profit_loss < g_decrease[1]:
			 g_decrease[0] = row[0]
			 g_decrease[1] = profit_loss

			 #avg_sum = (avg_sum - previous)
	#avg_change = round((avg_sum)/(total_months -1),2)
	avg_change = sum(avg_change_list)/len(avg_change_list)

output = ""
output +=(f'\n\n')
output+=(f'Financial Analysis\n')
output+=(f'Total_Months: {total_months}\n')
output+=(f'Total: {grand_total}\n')
output+=(f'Average_Change:{avg_change}\n')
output+=(f'Greatest_increase_in_profits: {g_increase[0]} (${g_increase[1]})\n')
output+=(f'Greatest_decrease_in_profits: {g_decrease[0]} (${g_decrease[1]})\n')

#code to print analysis
print(output)
# code to create path for output file
data_output = os.path.join("output","pybank.txt")

#code to write output to output file
with open(data_output, "w", newline="") as txtfile:
	txtfile.write(output)
