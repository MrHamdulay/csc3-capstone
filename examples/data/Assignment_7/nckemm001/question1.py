# Emmalene Naicker
# nckemm001
# Assignment 7

strings = []

# Get the input words from the user
string = input("Enter strings (end with DONE):\n")

while string.lower() != "done":
    if not string in strings:
        strings.append(string) 
    string = input()
    
# Print the Output list - unique words

print("\nUnique list:")

for string in strings:
    print(string)
    