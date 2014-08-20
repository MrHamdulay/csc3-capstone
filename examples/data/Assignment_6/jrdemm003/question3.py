"""ass. 6, q5 vote counter
emma jordi
25 april 2014"""

print("Independent Electoral Commission")
print("--------------------------------")

party_list=[]
votes=[]

#get input
parties=input("Enter the names of parties (terminated by DONE):\n")

while parties!= "DONE":
    votes.append(parties)
    parties= input()
    
for i in votes:
    if i not in party_list:
        party_list.append(i)
party_list.sort()
#print output
print("\nVote counts:")

for i in party_list:
    votes.count(i)
    #format parties etc
    print(i, (11-len(i))*" ", "- ", votes.count(i), sep="")
    
        