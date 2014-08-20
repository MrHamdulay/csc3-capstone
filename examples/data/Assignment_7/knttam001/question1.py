"""program to print a list of strings without duplicates
26 April 2014
Tamsin Kantor"""

# get a list of strings called strings_list
strings = input("Enter strings (end with DONE):\n")
strings_list = []
if strings != "DONE":
    strings_list.append(strings)
    strings = input()
    while strings != "DONE": 
        strings_list.append(strings)
        strings = input()

print()
print("Unique list:")

used_strings = []
for i in strings_list:
    if i not in used_strings:
        print(i)
        used_strings.append(i)
    

