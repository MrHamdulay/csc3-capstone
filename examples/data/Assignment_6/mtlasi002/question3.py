#Asil Motala
#MTLASI002
#Assignment 6
#Question 3

print("Independent Electoral Commission")
print("--------------------------------")
print("Enter the names of parties (terminated by DONE):")

party_list=[]                               #initialize voting list
party_name=[]                               #initialize party names string
while True:
    party=input("")                         #get input from user
    if party=="DONE": break                 #create sentinel variable
    else:
        party_list.append(party)            #add to voting list
        random_variable=1                   #assigning truth variable
    for a in range(len(party_list)-1):      #loop through old list of parties
        if party!=party_list[a]:            #check for repeats of parties
            random_variable=1               #true
        else:
            random_variable=2               #false
            break
    if random_variable==1:                  #no repeats
        party_name.append(party)            #add new party
party_name.sort()

print()
print("Vote counts:")
for i in party_name:                        #loop through different parties
    vote=0
    for j in party_list:                    #loop through votes
        if i==j:
            vote+=1                         #count votes for each party
    print(i+" "*(10-len(i))+" - "+str(vote))#print votes for each party