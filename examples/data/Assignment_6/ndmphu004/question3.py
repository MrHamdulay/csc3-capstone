#Phumelele Ndimande
#Assignment 6


print("Independent Electoral Commission")
print("--------------------------------")
name=input("Enter the names of parties (terminated by DONE):\n")
parties={}
if name!="DONE":
    parties[name]=parties.get(name,1)

#count entries until user types DONE
while name!="DONE":
    name=input("")
    if name!="DONE":
            parties[name]=parties.get(name,0)+1
print()
print("Vote counts:")
 
 #convert keys in parties into a list  
list_parties=list(parties)

#sort list in alphabetical order
list_parties.sort()

for i in list_parties:
    print(i," "*(9-len(i)),"-",parties[i])