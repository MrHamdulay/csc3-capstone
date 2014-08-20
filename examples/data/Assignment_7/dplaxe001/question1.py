string = input("Enter strings (end with DONE):\n")
strings = []
while string != "DONE":
    if string not in strings:
        strings.append(string)
        
    string = input()

print("\nUnique list:")
for string in strings:
    print(string)   