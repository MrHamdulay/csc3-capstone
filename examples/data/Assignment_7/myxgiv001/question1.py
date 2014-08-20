strings =[]
string = input("Enter strings (end with DONE):\n")

while string != "DONE":
    if string not in strings:
        strings.append(string)
    string = input()
#print(strings)
print()
print("Unique list:")
for i in strings:
    print(i)
