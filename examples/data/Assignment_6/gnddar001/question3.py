listing = []
print("Independent Electoral Commission")
print("--------------------------------")
adding = input("Enter the names of parties (terminated by DONE):\n")

#Get the list

while adding != "DONE":
    listing.append(adding)
    adding = input("")  

#Sort the list

listing.sort()

#Initialise my tools

list2 = []
i = 0
count = 1
length = len(listing) - 1

#if the word != the word after, delete the word after. Then increase count to move on
#The single word will remain in the list
#Count gets added to list2 which corresponds to sorted listing

for j in range(length):
    
    if listing[i] == listing[i+1]:
        del listing[i+1]
        count += 1
        
    else:
        i += 1
        list2.append(count)
        count = 1
list2.append(count)

print()
print("Vote counts:")

#Simple format stuff

for i in range(len(listing)):
    form = "{0:" "<10}"
    print(form.format(listing[i]), "-", list2[i])
    
