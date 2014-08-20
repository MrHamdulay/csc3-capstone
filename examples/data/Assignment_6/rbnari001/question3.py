#Ariel Rubin
#RBNARI001
#23 April 2014
# Program that counts the number of votes for different political parties
print("Independent Electoral Commission")
print("--------------------------------")
print("Enter the names of parties (terminated by DONE):")

party = input()

#creates an array
partiesList = []

Diction = {} #creates a dictionary : party/no of votes
longest = 0

while(party != "DONE"):
    
    x = len(party)
    
    if(x > longest):
        longest = x
    
    partiesList.append(party)    #adds a new party to list
    party = input()
    
#counts a vote for a party
for i in partiesList:
    
    if i in Diction:
        Diction[i] += 1
        
    else:
        Diction[i] = 1  
        
print("\nVote counts:")
#sorts parties in alphabetical order
#prints out number of votes for each party
for i in sorted(Diction.keys()):
   
    print (i + ('{:>{x}}'.format('- ' + str(Diction[i]),x=14-len(i))))



