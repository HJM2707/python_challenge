# importing the modules

import os
import csv

# creating the file path to import in csv
filepath = os.path.join(r'C:\Users\61469\python_challenge\PyBank\resources\budget_data.csv')

# open the file in the csv
with open(filepath, 'r', encoding='utf') as budegtfie:
    
    
    csv_reader = csv.reader(budegtfie, delimiter=',')
    header = next(csv_reader)

 # adding the list of variables
    months_total = []
    profit_loss = []
    profit_change = []
               
    # Loop through Data
    for row in csv_reader:
        # Add the month to the list of months
        months_total.append(row[0])
        # Add the profit/loss value to the list of profit/loss values
        profit_loss.append(int(row[1]))
    for i in range(len(profit_loss)-1):
        # Calculate the change in profit/loss from one month to the next
        profit_change.append(profit_loss[i+1]-profit_loss[i])
                      
# Find the greatest increase and decrease in profit/loss
increase = max(profit_change)
decrease = min(profit_change)

# Find the month in which the greatest increase and decrease occurred
month_increase = profit_change.index(max(profit_change))+1
month_decrease = profit_change.index(min(profit_change))+1

# Calculate and print the results
print("Financial Analysis")
print("------------------------")
print(f"Total Months: {len(months_total)}")
print(f"Total: ${sum(profit_loss)}")
print(f"Average Change: {round(sum(profit_change)/len(profit_change),2)}")
print(f"Greatest Increase in Profits: {months_total[month_increase]} (${(str(increase))})")
print(f"Greatest Decrease in Profits: {months_total[month_decrease]} (${(str(decrease))})")      

# Create a text file with the results (Financial Analysis)
output_txt = os.path.join(r'C:\Users\61469\python_challenge\PyBank\analysis\Financial_Analysis.txt')
with open(output_txt, "w") as text_file:
    text_file.write("Financial Analysis\n")
    text_file.write("------------------------\n")
    text_file.write(f"Total Months: {len(months_total)}\n")
    text_file.write(f"Total: ${sum(profit_loss)}\n")
    text_file.write(f"Average Change: {round(sum(profit_change)/len(profit_change),2)}\n")
    text_file.write(f"Greatest Increase in Profits: {months_total[month_increase]} (${(str(increase))})\n")
    text_file.write(f"Greatest Decrease in Profits: {months_total[month_decrease]} (${(str(decrease))})\n")