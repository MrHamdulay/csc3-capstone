"""program to calculate the number of votes in an election
thushar hariparsad
21 april 2014"""

print("Independent Electoral Commission")
print("--------------------------------")
print("Enter the names of parties (terminated by DONE):")

listV=[] #create a list for party votes
partyN=[] #create a list for party names
while True:
    party=input("")  #get input                       
    if party=="DONE": break   #create sentinel loop            
    else:
        listV.append(party)           
        x=1                   
    for a in range(len(listV)-1):     
        if party!=listV[a]: #check for repeats of parties
            x=1 
        else:
            x=2      
            break
    if x==1:  #(true) 
        partyN.append(party) #add new party
partyN.sort()

print()
print("Vote counts:")
for i in partyN:                        
    vote=0
    for j in listV:                  
        if i==j:
            vote+=1  #count votes for each party
    print(i+" "*(10-len(i))+" - "+str(vote))