 import os and csv modules, set path
import os
import csv
pybankpath = os.path.join('Resources', 'budget_data.csv')

# declare initial variables
months = []
profitloss = []
net_total = 0

# indices in changes[] will be lagging by 1 month from months[] and profitloss[].
changes = []

total_change = 0
increase_index = 0
decrease_index = 0
greatest_increase = 0
greatest_decrease = 0

# open and read
with open (pybankpath, newline='') as analysisfile:

    filereader = csv.reader(analysisfile, delimiter = ',')
    file_header = next (filereader)
    
    for row in filereader:
        months.append(row[0])
        profitloss.append(int(row[1]))

# The total number of months included in the dataset
num_months = len(months)


# The net total amount of "Profit/Losses" over the entire period
net_total = sum(profitloss)

# Create a list of monthly changes
i = 0
j = len (profitloss)
for i in range (j):
    current_amount = int (profitloss[i])
    if i > 0:
        previous_amount = int(profitloss[i-1])
        change_amount = current_amount - previous_amount
        changes.append(change_amount)
    
# The average of the changes in "Profit/Losses" over the entire period
l = len (changes)

total_change = sum (changes)
average_change= round(total_change / l, 2)

# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period
k = 0
for k in range (l):
    if changes[k] > greatest_increase:
        greatest_increase = changes[k]
        # add one to index to make sure the indices correspond to the correct month
        increase_index = k + 1
    if changes[k] < greatest_decrease:
        greatest_decrease = changes[k]
        # add one to index to make sure the indices correspond to the correct month
        decrease_index = k + 1
increase_month = months[increase_index]
decrease_month = months[decrease_index]

# Print to terminal
print (f"""
Financial Analysis
----------------------------
Total Months: {num_months}
Total: ${net_total}
Average Change: ${average_change}
Greatest Increase in Profits: {increase_month} (${greatest_increase})
Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})""")

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.
output_path = os.path.join("pybank_output.txt")

# print to text file
output_path = os.path.join("pybank_output.txt")
with open(output_path, 'a') as txt_file:
    txt_file.write (f"Financial Analysis"+'\n')
    txt_file.write(f"-------------------------" + '\n')
    txt_file.write(f"Total Months: {num_months}" + '\n')
    txt_file.write(f"Total: ${net_total}" + '\n')
    txt_file.write(f"Average Change: ${average_change} " + '\n')
    txt_file.write(f"Greatest Increase in Profits: {increase_month} (${greatest_increase})" + '\n')
    txt_file.write(f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})")
