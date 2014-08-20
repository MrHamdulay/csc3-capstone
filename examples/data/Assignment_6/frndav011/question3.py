print("Independent Electoral Commission\n--------------------------------")
#Creating empty list and dictionary respectively
names = []
amount = {}
#User input
name = input("Enter the names of parties (terminated by DONE):\n")

while name.upper() != "DONE":
    names.append(name)#Adds names to list names
    name = input("")#Allows user to continue I/P
#Checks for duplicate words
for i in names:
    if i in amount:
        amount[i] += 1
    else:
        amount[i] = 1
#Returns/prints words and number of duplicates  
print("\nVote counts:")
for i in sorted(amount):
    print(i.ljust(10),"-",amount[i])    




  
    
        
   