#Mufaro Chiwara - April 2014

print("Independent Electoral Commission")
print("--------------------------------")
#Get list
party = input("Enter the names of parties (terminated by DONE):\n")
parties=[]

#Count votes
while party != 'DONE':    
    parties.append(party)
    party = input()

print()
print("Vote counts:")
    
#create dictionary
votes={}
for i in parties:
    if i not in votes:
        votes[i]=0
    votes[i]+=1
    

#Print alphabetically
x=len(votes)
while x>0:
    temp = votes
    i=min(temp)
    print(i," "*(10-len(i)), ' - ',votes[i], sep="")
    del(temp[i])
    x-=1
    
    