import os
import csv


months = []
profit_loss_changes = []

month_counter = 0
net_profit_loss = 0
previous_month_profit_loss = 0
current_month_profit_loss = 0
profit_loss_change = 0


csv_path = os.path.join('Resources','Budget_Data.csv')
path_out = os.path.join('Analysis','Budget_Analysis.txt')


with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csv_reader)

    for row in csv_reader:
        month_counter += 1

        current_month_profit_loss = int(row[1])
        net_profit_loss += current_month_profit_loss

    
        if (month_counter == 1):
            previous_month_profit_loss = current_month_profit_loss
            
        else:
            profit_loss_change = current_month_profit_loss - previous_month_profit_loss

            months.append(row[0])

            profit_loss_changes.append(profit_loss_change)

            previous_month_profit_loss = current_month_profit_loss

    
    sum_profit_loss = sum(profit_loss_changes)
    average_profit_loss = round(sum_profit_loss/(month_counter - 1), 2)

    highest_change = max(profit_loss_changes)
    lowest_change = min(profit_loss_changes)

    highest_month_index = profit_loss_changes.index(highest_change)
    lowest_month_index = profit_loss_changes.index(lowest_change)

    best_month = months[highest_month_index]
    worst_month = months[lowest_month_index]


print('----------------------------')
print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {month_counter}')
print(f'Total: ${net_profit_loss}')
print(f'Average Change: ${average_profit_loss}')
print(f'Greatest Increase in Profits: {best_month} (${highest_change})')
print(f'Greatest Decrease in Losses: {worst_month} (${lowest_change})')
print('----------------------------')


with open(path_out, 'w') as output:

    output.write('----------------------------\n')
    output.write('Financial Analysis\n')
    output.write('----------------------------\n')
    output.write(f'Total Months: {month_counter}\n')
    output.write(f'Total: ${net_profit_loss}\n')
    output.write(f'Average Change: ${average_profit_loss}\n')
    output.write(f'Greatest Increase in Profits: {best_month} (${highest_change})\n')
    output.write(f'Greatest Decrease in Losses: {worst_month} (${lowest_change})\n')
    output.write('----------------------------\n')