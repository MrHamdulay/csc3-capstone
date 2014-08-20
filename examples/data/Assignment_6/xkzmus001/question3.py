"""question3.py
Author : Musa Xakaza
Date : 19/04/2014"""

print("Independent Electoral Commission")
print("--------------------------------")

#get a list of parties & terminate when "DONE" is entered.
parties = []
party = input("Enter the names of parties (terminated by DONE):\n")
while party != "DONE":
        parties.append(party)
        party = input()

#Sort parties
parties.sort()
out = "{0: <11}"
results = ''
for i in range(len(parties)):
        party = parties[i]
        line = out.format(party)+"- "+str(parties.count(party))
        #Check whether party has been counted or not
        if results.find(line) == -1:
                results += line+"\n"
print("\nVote counts:")
if results: print(results[:-1])