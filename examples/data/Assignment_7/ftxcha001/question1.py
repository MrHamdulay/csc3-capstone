names = []
list_names = input("Enter strings (end with DONE):\n")
while list_names != "DONE": 
    names.append(list_names) #add each to empty list
    list_names = input("")
    
no_repeats=[]
for i in names:
    if i in no_repeats: #if name is in the no_repeats list, continue
        continue
    else: #adds to list if not in.
        no_repeats.append(i)

print()

print("Unique list:")

for j in no_repeats:
    print(j)
    