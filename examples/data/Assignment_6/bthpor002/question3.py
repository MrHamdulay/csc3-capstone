#This is a proram that counts the number of votes for certain parties

#Pritn the top parts
print("Independent Electoral Commission")
print("--------------------------------")

#Get list of parties
names_of_parties=[]
party= input("Enter the names of parties (terminated by DONE):\n")
while party != "DONE":
    names_of_parties.append(party)
    party=input("")


print()

#Create list to seperate the various parties
various_parties=[]
for party in names_of_parties:
    if party in various_parties:
        continue
    else:
        various_parties.append(party)


#Count number of votes per party
count={}
for party in names_of_parties:
    if not party in count:
        count[party]=0
    count[party]+=1


#Sort and Print number of votes per party
print("Vote counts:") 
various_parties.sort()
for party in various_parties:
    print(party," "*(10-len(party))," ","- ",count[party], sep="")