import os
import csv

csvpath = os.path.join('..', 'PyBank', 'budget_data.csv')

profit = 0
months = 0
maximum = 0
minimum = 0
change = 0
previous = 0
delta_sum = 0

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

    for row in csvreader:
        months += 1
        profit += int(row[1])

        change = int(row[1]) - previous
        previous = int(row[1])

        if months > 1:
            delta_sum = delta_sum + change

        if change > maximum:
            maximum = change
            max_month = row[0]

        if change < minimum:
            minimum = change
            min_month = row[0]     

average = round(delta_sum/(months - 1),2)

print("Financial Analysis")
print("-------------------------")
print("Total Months: " + str(months))

print("Average Change: $" + str(average))
print("Greatest Increase in Profits: " + str(max_month) + " ($" + str(maximum) + ")")
print("Greatest Decrease in Profits: " + str(min_month) + " ($" + str(minimum) + ")")

with open("Bank_Results.txt", "w") as results:
    results.write("Financial Analysis\n")
    results.write("-------------------------\n")
    results.write("Total Months: " + str(months) + "\n")
    results.write("Total: $" + str(profit) + "\n")
    results.write("Average Change: $" + str(average) + "\n")
    results.write("Greatest Increase in Profits: " + str(max_month) + " ($" + str(maximum) + ")\n")
    results.write("Greatest Decrease in Profits: " + str(min_month) + " ($" + str(minimum) + ")")