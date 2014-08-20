""" no duplicates
Tim Mostert
27.4.14"""

the_list = []
print("Enter strings (end with DONE):")
x = ""
while not x == "DONE":
    x = input()
    if x == "DONE":
        break
    if x not in the_list:
        the_list.append(x)
        
print()
print("Unique list:")
for i in the_list:
    print(i)