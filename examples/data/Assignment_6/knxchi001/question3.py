#Assigment 6
#question 3
print("Independent Electoral Commission")
print("--------------------------------")

#Get list of parties
list_of_parties=[]
party= input("Enter the names of parties (terminated by DONE):\n")
while party!= "DONE":
    list_of_parties.append(party)
    party=input("")
#print(list_of_parties)

print()

#Create list to seperate different parties
different_parties=[]
for party in list_of_parties:
    if party in different_parties:
        continue
    else:
        different_parties.append(party)
#print(different_parties)

#Count number of votes per party
counter={}
for party in list_of_parties:
    if not party in counter:
        counter[party]=0
    counter[party]+=1


#Sort and Print number of votes per party
print("Vote counts:") 
different_parties.sort()
for party in different_parties:
    print(party," "*(10-len(party))," ","- ",counter[party], sep="")