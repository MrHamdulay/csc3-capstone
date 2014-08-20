#23 April 2014
#Tayla Radmore
#counting votes

print("Independent Electoral Commission")
print("--------------------------------")

#getting inputs
list_of_votes=[]
name_of_party=input("Enter the names of parties (terminated by DONE): \n")
list_of_votes.append(name_of_party)
while name_of_party!="DONE":
    name_of_party=input()
    list_of_votes.append(name_of_party)
#removing done
index_to_remove=len(list_of_votes)-1
del list_of_votes[index_to_remove]
           
#counting the votes
parties=[]
for i in list_of_votes:
    if i not in parties:
        parties.append(i)
        
parties.sort()
print()
print("Vote counts:")

for i in parties:
    x=list_of_votes.count(i)
    print(i," "*(11-len(i)),"- ",x,sep="")
    



