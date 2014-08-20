"""Question 3 - suggestion voting vote counter
Jembe Moran
25 April 2014"""
print("Independent Electoral Commission\n--------------------------------")
votes = [] #create ballot box
parties = [] #create voters roll
x=input("Enter the names of parties (terminated by DONE):\n")
while x!="DONE": #sentinel
    votes.append(x)
    if x in parties: #if already on voters roll
        x=input("") #find next vote
    else:
        parties.append(x) #add new party to roll
        x=input("") #find next vote
        
print("\nVote counts:") #UI        
parties.sort()    
for i in range(len(parties)): #go through list of parties
    find_party=parties[i] #find party name
    find_votes=votes.count(find_party) #find votes attached to that party
    r ="{0:<10}".format(find_party) #format column to place party names into
    print(r, "-", find_votes)