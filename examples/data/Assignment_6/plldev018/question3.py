#Votes in an election
#Devaksha Pillay
#21 April 2014

print("Independent Electoral Commission")
print("-"*32)
parties = []
votes_per_party = []
votes = 0

party_name = input("Enter the names of parties (terminated by DONE):\n")

#Creating a list of a number of inputs

while party_name != "DONE":
    parties.append(party_name)
    party_name = input()

#find out the total number of parties

number_of_parties = []
for i in parties:
    if not i in number_of_parties:
        number_of_parties.append(i)
        
#get the alphabetical order        
number_of_parties.sort()

#Counting the votes
for party in number_of_parties:
    votes = 0
    if parties == number_of_parties:
        votes += 1
        
for i in number_of_parties:
    total_votes = 0
    for j in parties:
        if i == j:
            total_votes = total_votes + 1
    votes_per_party.append(total_votes)

print()
print("Vote counts:")

for i in range(len(number_of_parties)):
    spaces = ((10 - len(party_name))*" ")
    print("{:<10}".format(number_of_parties[i]),"-",votes_per_party[i])