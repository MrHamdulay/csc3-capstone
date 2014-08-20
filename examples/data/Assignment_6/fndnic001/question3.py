"""a political party vote counter
nic findlay
22 april 2014"""

parties = []
name = ('')
print("Independent Electoral Commission \n--------------------------------\nEnter the names of parties (terminated by DONE):")

while name != 'DONE': #loop to enter names
    name = input('')
    parties.append(name)

del parties[len(parties)-1]  #deletes 'DONE' from loop
    
parties.sort() #sorts names into alphabetical order
print("\nVote counts:")
votes = {}             #puts the number of votes into a dictionary
for i in parties:
    if i in votes:
        votes[i] += 1
    else: 
        votes[i] = 1

    
for i in sorted(votes):       #sorted sorts the dictionary into alphabetic order
    print(i, " "*(10-len(i)), end='')
    print('-' , votes[i])
    
                 
                