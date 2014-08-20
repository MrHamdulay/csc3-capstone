# Program to count the number of votes for political parties
# Brandon Hall (HLLBRA005)
# 25/04/2014

print("Independent Electoral Commission")
print("--------------------------------")
print("Enter the names of parties (terminated by DONE):")

party = input()

partiesList = []

Diction = {} #dictionary : party/no of votes
longest = 0

while(party != "DONE"):
    
    x = len(party)
    
    if(x > longest):
        longest = x
    
    partiesList.append(party)    #add new party to list
    party = input()
    
for i in partiesList:
    
    if i in Diction:
        Diction[i] += 1
        
    else:
        Diction[i] = 1  
        
print("\nVote counts:")
for i in sorted(Diction.keys()):
   
    print (i + ('{:>{x}}'.format('- ' + str(Diction[i]),x=14-len(i))))



