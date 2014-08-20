"""This program asks the user to enter a list of strings and print the strings in the same order but without duplicates
Masilela Mduduzi
27 April 2014"""

list_of_strings=[]
string= input("Enter strings (end with DONE):\n")
list_of_strings.append(string)
unique_list = []
while string!="DONE":
    string=input()
    list_of_strings.append(string)
list_of_strings.remove("DONE")
for i in range(len(list_of_strings)):
    if list_of_strings[i] not in unique_list :
        unique_list.append(list_of_strings[i])
print("\nUnique list:")
for i in unique_list:
    print(i)