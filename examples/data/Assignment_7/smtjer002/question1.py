"""A program to remove duplicates from a list
by Jeremy Smith SMTJER002
1 May 2014"""

#create a empty list and build the list from string inputs
list_strings = []
list_input = input("Enter strings (end with DONE):\n")
list_strings.append(list_input)
while list_input != "DONE":
    list_input = input()
    list_strings.append(list_input)

del list_strings[-1]

#create a new list from all the unique strings in the original list
final_list = []
for i in list_strings:
    if i not in final_list:
        final_list.append(i)
        
#print the new list with the unique strings
print("\nUnique list:")
for i in final_list:
    print(i)