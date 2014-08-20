
# Input Data
strings = []
string = input("Enter strings (end with DONE):\n")
while string != "DONE":
    strings.append(string)
    string = input("")

# Leaveing out duplicates
duplicate = []
for string in strings:
    if string not in duplicate:
        duplicate.append(string)

# Printing out list without duplicates
print()
print("Unique list:")
for i in duplicate:
    print(i)
