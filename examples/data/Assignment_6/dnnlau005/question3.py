"""count the number of votes for political parties in an election
Lauren Denny
24 April 2014"""

print("Independent Electoral Commission")
print("--------------------------------")
print("Enter the names of parties (terminated by DONE):")

#create dictionary
parties={}

#ask for party names until sentinel of "DONE"
#add "party name"-"updated vote count" pair to dictionary
while True:
    party=input()
    if party=="DONE":
        break
    elif party in parties:
        parties[party]+=1 #increase vote count by 1 if party already in dictionary
    else:
        parties[party]=1 #if party not yet in dictionary, add as key to dictionary with vote count 1

#sort party names
P=list(parties.keys())
P.sort()

print()
print("Vote counts:")

#print party and corresponding vote count in sorted order (party names at most 10 characters wide)
for party in P:
    print("{0:<10}".format(party),"-",parties[party])