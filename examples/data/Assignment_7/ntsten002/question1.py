#question1
#Tendani Netshitenzhe
#02May014

#Get first input
strings = input("Enter strings (end with DONE):\n")

#Create empty lists
string_list = []
unique_list = []

#Get a list and add values to list
while strings != "DONE":
    string_list.append(strings)
    strings = input("")
    
print("\nUnique list:")

#Print list without duplicates in order
for i in string_list:
    if i not in unique_list:
        unique_list.append(i)
        print(i)