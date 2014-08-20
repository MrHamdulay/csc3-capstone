"""count votes for given parties
casey o'donnell
21 april 2014"""

parties=[]

#collect votes
print("Independent Electoral Commission\n--------------------------------\nEnter the names of parties (terminated by DONE):")
while True:
    a=input("")
    if a=="DONE":
        break
    else:
        parties.append(a)
        
parties.sort()
partyvotes=[]
while parties!=[]:
    count=parties.count(parties[0])
    partyvotes.append([parties[0],count])
    parties=parties[count:]
    
print()
print("Vote counts:")
for i in range(len(partyvotes)):
    a="{0:<11}-{1:>2}"
    print(a.format(partyvotes[i][0],partyvotes[i][1]))
    
    
        

        

            
    

        

        
