"""Program to print out votes
Thiloshni Moodley
22 April 2014"""

print("Independent Electoral Commission")
print("-"*32)
party=[]
parties=input("Enter the names of parties (terminated by DONE):\n")
while parties != "DONE": #proceeds if not done
    party.append(parties) #adds the input to the list
    parties=input("")
else:
    print("\nVote counts:")
    new_parties = [] #creating bottom list
    if party != []:
        for i in party:
            if i not in  new_parties: #if name not already in list
                new_parties.append(i) #add the name
    new_parties.sort()    
    for j in new_parties:
        print("{0:<10}".format(j), "-", party.count(j)) #formatting and counting 