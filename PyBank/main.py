import os
import csv

csvpath = os.path.join('Resources','budget_data.csv')

month=[]
profit=[]
month_profit_change=[]

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
   # print (csvreader)
    csv.header = next(csvreader)
   
    for row in csvreader:
        month.append(str(row[0]))
        profit.append(int(row[1]))
        
for i in range(len(profit)-1):
    #print(i)
    #print(len(profit))
    #print(profit[i])

    month_change=profit[i+1]-profit[i]
    month_profit_change.append(month_change)
  
print("Financial Analysis")
print("Total Months:" + str(len(month)))
print("Total profit or loss:" + str(sum(profit)))
print(sum(month_profit_change)/(len(month)-1))
print(max(month_profit_change))
print(min(month_profit_change))

out = open("budget_summ.txt","w+")

out.write("Total Months: " + str(len(month))+"\n")
out.write("Total Profits: $" + str(sum(profit))+"\n")
out.write("Average Profits: $" + str(sum(month_profit_change)/(len(month)-1))+"\n")
out.write("Maximum Profits: $" + str(max(month_profit_change))+"\n")
out.write("Minimum Profits: $" + str(min(month_profit_change))+"\n")