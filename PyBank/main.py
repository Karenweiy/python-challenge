import os
import csv

#import data from resources and calculate the count
csvpath = os.path.join('Resources','budget_data.csv')

month=[]
pro_loss=[]

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    print (csvreader)
    csv.header = next(csvreader)
   

    for row in csvreader:
        month.append(str(row[0]))
        pro_loss.append(int(row[1]))
        
  
    print("Financial Analysis")
    print("Total Months:" + str(len(month)))
    print("Total profit or loss:" + str(sum(pro_loss)))
    print(sum(pro_loss)/len(month))
    print(max(pro_loss))
    print(min(pro_loss))

out = open("budget_summ.txt","w+")

out.write("Total Months: " + str(len(month))+"\n")
out.write("Total Profits: $" + str(sum(pro_loss))+"\n")
out.write("Average Profits: $" + str(sum(pro_loss)/len(month))+"\n")
out.write("Maximum Profits: $" + str(max(pro_loss))+"\n")
out.write("Minimum Profits: $" + str(min(pro_loss))+"\n")