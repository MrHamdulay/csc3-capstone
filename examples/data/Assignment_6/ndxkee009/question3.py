"""Keegan Naidoo
NDXKEE009
20 April 2014"""

print("Independent Electoral Commission\n--------------------------------")

list=[]        #Creates an empty list for parties to be stored in
counter={}     #Creates an empty dictionary for votes to be stored in

parties=input("Enter the names of parties (terminated by DONE):\n") #Input parties

while parties!="DONE":         #Loops until 'DONE' is entered
    
    list.append(parties)        #Adds parties to list
    
    parties=input("")           

for i in list:                #Loops through entire list
    if not i in counter:      #If the party doesn't have votes it will add votes
        counter[i]=0
    counter[i]+=1             #adds votes to existing parties
    
print()                           
print("Vote counts:")

for i in sorted(counter.keys()):     #Runs through dictionary in order specified     
    

    print(i," "*(9-len(i)) ,'-',counter[i])    #Prints parties and votes in columns specified