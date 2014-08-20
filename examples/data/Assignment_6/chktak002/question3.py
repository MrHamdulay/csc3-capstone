print("Independent Electoral Commission")
print("--------------------------------")
x=input("Enter the names of parties (terminated by DONE):\n")
parties={}
while x!="DONE":
    if x in parties:
        parties[x]+=1 #adds items to the dictionary and adds 1 to the value if it is already present
    else:
        parties[x]=1 # adds value and assigns a key of 1 if the item is not present in the dictionary
        
    x=input()
print()
print("Vote counts:")

for key,value in sorted(parties.items()): # sorts the items in the list
    space=11-len(key)
    print(key+ space*" "+"-",str(value))
    