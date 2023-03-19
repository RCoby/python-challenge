# total number of months included in the dataset
# net total amount of "Profit/Losses" over the entire period
# changes in "Profit/Losses" over the entire period, and then the average of those changes
# greatest increase in profits (date and amount) over the entire period 
# greatest decrease in profits (date and amount) over the entire period
#----------------------------------------------------------------------------

# Dependencies
import os
import csv

# Path to collect data 
budget_data_csv = os.path.join("..","Resources","budget_data.csv")
#Path to text file 
analysis_file = os.path.join("..","analysis", "budget_analysis.txt")

# Create variables
total_months = 0
net_pnl = 0
prev_pnl = 0
pnl_changes = []
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999999999]
    
# Open CSV file
with open(budget_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip header row
    next(csvreader)

    # Loop through rows in CSV file
    for row in csvreader:

        # Count total number of months
        total_months += 1

         # Calculate net P&L
        net_pnl += int(row[1])

        # Calculate change in P&L
        pnl_change = int(row[1]) - prev_pnl
        prev_pnl = int(row[1])
        pnl_changes.append(pnl_change)

        # Determine greatest increase in profits
        if pnl_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = pnl_change

        # Determine greatest decrease in profits
        if pnl_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = pnl_change

    # Calculate the average change in P&L
    avg_change = sum(pnl_changes) / len(pnl_changes)

    # Print results to the console
    print("Financial Analysis")
    print("------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${net_pnl}")
    print(f"Average Change: ${avg_change:.2f}")
    print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
    print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")


# Write the analysis to the output text file
    with open(analysis_file, "w") as txtfile:
        txtfile.write("Financial Analysis\n")
        txtfile.write("------------------\n")
        txtfile.write(f"Total Months: {total_months}\n")
        txtfile.write(f"Total: ${net_pnl}\n")
        txtfile.write(f"Average Change: ${avg_change:.2f}\n")
        txtfile.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
        txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")