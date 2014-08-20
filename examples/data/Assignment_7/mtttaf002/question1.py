"""program to print out list without duplicates
tafara mtutu
29 april 2014"""

list = []
string = input("Enter strings (end with DONE):\n")
while string.lower() != "done":
    if string not in list:
        list.append(string)
    string = input()
print()    
print("Unique list:")
for i in list:
    print(i, end = "\n")
    