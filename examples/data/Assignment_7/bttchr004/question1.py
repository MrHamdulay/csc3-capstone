"""program to reprint list without duplicates
chris betteridge
28 april 2014"""

unique_list = []
strings_list = []

string = input("Enter strings (end with DONE):\n")
while string != "DONE":
    strings_list.append(string)
    string = input()
    
for i in strings_list:
    if i not in unique_list:
        unique_list.append(i)

print("\nUnique list:")
for i in unique_list:
    print(i)