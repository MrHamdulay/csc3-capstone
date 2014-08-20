#katlego Gaveni 
#counting votes
#21st April 2014


print("Independent Electoral Commission")
print("--------------------------------")


#compiling list of parties & votes
parties=[]
p_parties=input("Enter the names of parties (terminated by DONE):\n")

while p_parties != "DONE":
    parties.append(p_parties)
    p_parties=input("")

# removing duplicates in lists
p_parties2=[] 
numbers2=[]

for x in range(len(parties)):
    for y in range(x+1,len(parties)):
        if parties[x] == parties[y]:
            p_parties2.append(parties[x])

merged_votes= sorted(list(set(parties + p_parties2)))



#COUNTING THE NUMBER OF TIMES ITEM APPEARS IN ORIGINAL LIST
numbers=[]
for y in range(len(merged_votes)):
    
    votes=parties.count(merged_votes[y])
    numbers.append(votes)
    
print()
print("Vote counts:")
#FORMAT OF STRING AND PRINTING
for i in range(len(merged_votes)):
    print('{:<11}'.format(merged_votes[i]),"-"," ",numbers[i],sep="")
