#mknnit002
#question 1 ass 7
#taking away repeated strings in a list

wordlist=[]
list_strings=input("Enter strings (end with DONE):\n")
while list_strings != "DONE":
    wordlist.append(list_strings)
    list_strings=input("")
    
unique=[]
for i in wordlist:
    if i in unique:
        continue
    else:
        unique.append(i)
print()
print ("Unique list:")       

for a in unique:
    print(a)






