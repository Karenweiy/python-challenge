import os
import csv
import pandas as pd

csvpath = os.path.join('Resources','election_data.csv')

election_df = pd.read_csv(csvpath)

voter_count = len(election_df["Voter ID"])
candidates = election_df["Candidate"].unique()

print("Total votes:" + str(voter_count))
votes = election_df.groupby('Candidate').count()

khan_=votes.loc["Khan","Voter ID"]
correy_=votes.loc["Correy","Voter ID"]
li_=votes.loc["Li","Voter ID"]
otooley_=votes.loc["O'Tooley","Voter ID"]

khan_v = round(int(votes.loc["Khan","Voter ID"])*100/voter_count)
correy_v = round(int(votes.loc["Correy","Voter ID"])*100/voter_count)
li_v = round(int(votes.loc["Li","Voter ID"])*100/voter_count)
otooley_v = round(int(votes.loc["O'Tooley","Voter ID"])*100/voter_count)

print("Khan: " + str(khan_v) +"%"+ " (" + str(khan_)+")")
print("Correy: " + str(correy_v) +"%"+ " (" + str(correy_)+")")
print("Li: " + str(li_v) +"%"+ " (" + str(li_)+")")
print("O'Tooley: " + str(otooley_v) +"%"+ " (" + str(otooley_)+")")

if khan_v >= correy_v and khan_v >= li_v and khan_v >= otooley_v:
   print("Winner Khan")
elif correy_v >= khan_v and correy_v >= li_v and correy_v >= otooley_v:
   print("Winner Correy")
elif li_v >= khan_v and li_v >= correy_v and li_v >= otooley_v:
   print("Winner Li")
elif otooley_v >= khan_v and otooley_v >= correy_v and otooley_v >= li_v:
   print("Winner O'Tooley")

out = open("election_summ.txt","w+")
out.write("Election Results " +"\n----------------------\n")
out.write("Total Votes: " + str(voter_count) +"\n----------------------\n")
out.write("Khan's vote percentage: " + str(khan_v) +"%"+" (" + str(khan_)+")""\n")
out.write("Correy's vote percentage: " + str(correy_v) +"%"+" (" + str(correy_)+")""\n")
out.write("Li's vote percentage: " + str(li_v) +"%"+ " (" + str(li_)+")""\n")
out.write("O'Tooley's vote percentage:" + str(otooley_v) +"%"+ " (" + str(otooley_)+")""\n")
out.write("Winner Khan")