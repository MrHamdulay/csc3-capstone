"""Prints out unique elements in a list
Shane Robinson
27 April 2014"""

print("Enter strings (end with DONE):")
string = input()
string_list = []

#create list of strings

while string!="DONE":
    string_list.append(string)
    string = input()

new_string_list = []

#create a new list from old

for i in string_list:
    if i in new_string_list:
        continue
    else:
        new_string_list.append(i)

print()
print("Unique list:")

#print unique list

for j in new_string_list:
    print(j)