"""print a list of strings in the given order, without duplicates
kamogelo mphela
27 april 2014"""

# create a list from the user's input
strings = input("Enter strings (end with DONE):\n")
list_strings =[]
while strings != "DONE":
    list_strings.append(strings)
    strings = input()

# create a list without duplicates
unique_list = []
K=0
for i in list_strings:
    if i in unique_list:
        continue
    else:
        unique_list.append(i)
    K +=1
        
# print the sorted order of the "unique"list.
print()
print("Unique list:")
for i in unique_list:
    print(i)
