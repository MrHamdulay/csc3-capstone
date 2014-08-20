"""This program calculates the number of votes of each party given by the user
Masilela Mduduzi
25 April 2014"""
print("Independent Electoral Commission")
print("--------------------------------")

parties = [] #An empty list of strings

#ask for the party the user votes for
party = input("Enter the names of parties (terminated by DONE):\n")

parties.append(party) #Add a party to the list

while "DONE" not in party:
    party=input("")
    parties.append(party)

parties.remove("DONE")#remove done in the list

for i in range(len(parties)):
    partyvotes = parties.count(parties[i])
parties=sorted(parties)
   # print(partiessort)
dic_parties={}
for party in parties:
    if party not in dic_parties:
        dic_parties[party]=1
    else:
        dic_parties[party]+=1
counts = []
for x in parties: #making a 2 D array for parties and their votes
    if [x,dic_parties[x]] not in counts :
        counts.append([x,dic_parties[x]])
print('\nVote counts:')
for i in range(len(counts)):
            
    print('%10s - %d'%(counts[i][0].ljust(10),counts[i][1])) 
