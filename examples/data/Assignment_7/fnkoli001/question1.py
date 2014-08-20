strings = []

#Get input
input_string = input("Enter strings (end with DONE):\n")
strings.append(input_string)

while input_string != "DONE":
    input_string = input("")
    if input_string not in strings:
        strings.append(input_string)
strings = strings[:-1]

print("\nUnique list:")
print("\n".join(strings))