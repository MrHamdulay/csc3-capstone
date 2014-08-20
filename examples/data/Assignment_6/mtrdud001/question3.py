"""polling system a vote of parties
Dudley Mutero
25 April 2014"""

party = []
votes = {}

print("Independent Electoral Commission\n--------------------------------")

entry = input("Enter the names of parties (terminated by DONE):\n")
while entry == "":
        entry = input()
        
while entry.lower() != "done":#checking for input if entry is done or not
        party.append(entry)
        entry = input()
        while entry == "":
                entry = input()#updating empty string in while loop
        
for i in party:
        if i in votes: #check if the word has been inserted in the dictionary
                continue
        else:
                votes[i] = party.count(i)#creates new variable of that pparty and counts the votes associated to that party
entry = []      
print("\nVote counts:") 
for i in votes: #run thru the dictionary with parties in it
        temp = i+ " "*(11-len(i))+"- "+ str(votes[i])
        entry.append(temp)
entry.sort() #sorting the parties in alphabetical order
for i in entry:
        print(i)


        
