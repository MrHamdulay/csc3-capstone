#Chantel Foot
#Question 3, Assignment 6


print("Independent Electoral Commission") #print heading
print("--------------------------------")

parties=[] #start with empty loop 
list_parties= input("Enter the names of parties (terminated by DONE):\n") #get list of parties from user
while list_parties != "DONE": 
    parties.append(list_parties) #add each to empty list
    list_parties = input("")
    
    # create empty list- no_repeats, loop to check if the item is in parties in the list
    # if it isn't, print the parties item with the count
    # else append the empty list with the item from parties
    
no_repeats=[]
for i in parties:
    if i in no_repeats: #if party is in the no_repeats list, continue
        continue
    else: #adds to list if not in.
        no_repeats.append(i)
        
maximum= 10    #number of spaces. use this to get alignment and spaces after name. Assumed no name more than 10 characters long.
no_repeats.sort() #alphabetical order
print()
print("Vote counts:")
for i in no_repeats: #for parties in no_repeats list 

    print(i,(maximum-len(i))*" ", " - ",parties.count(i),sep="") #counts parties so outputs the number. sort gaps in first part. 
        

