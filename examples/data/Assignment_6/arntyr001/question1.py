"""ARNTYR001
Program to print the names in a list
23 April 2014"""

print("Enter strings (end with DONE):")
name_list = []
max_len = 0
new_name = ""
while new_name != "DONE":
    new_name = input()
    if new_name == "DONE":
        break
    else:
        name_list.append(new_name)
    if len(new_name) > max_len:
        max_len = len(new_name)
    
print()
print("Right-aligned list:")

for i in name_list:
    print(i.rjust(max_len))
