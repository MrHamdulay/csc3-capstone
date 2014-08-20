#Cecil Hlungwana
#HLNCEC001
#Assignment 7
#Question 1

strings = input("Enter strings (end with DONE):\n") 
List = []
List.append(strings)
while strings != "DONE":
    strings = input("")
    List.append(strings)
List.remove("DONE") #"DONE" is always included in the list, so this removes it.
print()

List_2 = []
print("Unique list:")
for i in List:
    if i not in List_2:
        List_2.append(i)
for j in List_2:
    print(j)