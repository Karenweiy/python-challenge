import os
import csv
import pandas as pd

csvpath = os.path.join('Resources','election_data.csv')

election_df = pd.read_csv(csvpath)

voter_count = len(election_df["Voter ID"])
candidates = election_df["Candidate"].unique()

print("Total votes:" + str(voter_count))
votes = election_df.groupby('Candidate').count()

khan_v = round(int(votes.loc["Khan","Voter ID"])*100/voter_count)
correy_v = round(int(votes.loc["Correy","Voter ID"])*100/voter_count)
li_v = round(int(votes.loc["Li","Voter ID"])*100/voter_count)
otooley_v = round(int(votes.loc["O'Tooley","Voter ID"])*100/voter_count)

print("Khan's vote percentage " + str(khan_v) +"%")
print("Correy's vote percentage " + str(correy_v) +"%")
print("Li's vote percentage " + str(li_v) +"%")
print("O'Tooley's vote percentage:" + str(otooley_v) +"%")

if khan_v >= correy_v + li_v + otooley_v:
   print("Winner Khan")
elif correy_v >= khan_v + li_v + otooley_v:
   print("Winner Correy")
elif li_v >= khan_v + correy_v + otooley_v:
   print("Winner Li")
elif otooley_v >= khan_v + correy_v + li_v:
   print("Winner O'Tooley")




out = open("election_summ.txt","w+")
out.write("Election Results " +"\n----------------------\n")
out.write("Total Votes: " + str(voter_count) +"\n----------------------\n")
out.write("Khan's vote percentage: " + str(khan_v) +"%""\n")
out.write("Correy's vote percentage: " + str(correy_v) +"%""\n")
out.write("Li's vote percentage: " + str(li_v) +"%""\n")
out.write("O'Tooley's vote percentage:" + str(otooley_v) +"%""\n")
out.write("Winner Khan!")