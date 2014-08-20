# question3.py
# Name: Buhlebezwe
# Student Number: MBLBUH001
# Date: 23 April 2014

print("Independent Electoral Commission")
print("--------------------------------")
print("Enter the names of parties (terminated by DONE):")

party_list=[]                                   #create empty voting list
party_name=[]                                   #create empty party names string
while True:
    party=input("")                             #get input from user
    if party=="DONE": break
    else:
        party_list.append(party)                #append party to voting list
        random_variable=1
    for a in range(len(party_list)-1):
        if party!=party_list[a]:
            random_variable=1
        else:
            random_variable=2
            break
    if random_variable==1:
        party_name.append(party)                #append a new party to party_name
party_name.sort()

print()
print("Vote counts:")

for i in party_name:                            #loop to count number of votes for each party
    vote=0
    for j in party_list:
        if i==j:
            vote+=1
    print(i+" "*(10-len(i))+" - "+str(vote))    #print number of votes for each party