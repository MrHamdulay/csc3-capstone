# Emmalene Naicker
# NCKEMM001
# Assignment 6 : Question1 

# List
strings = []

# Strings
string = input("Enter strings (end with DONE):\n")
while string.lower() != "done":
    strings.append(string)
    string = input()

# Get the longest word
x = 0
for string in strings:
    if len(string) > x:
        x = len(string)

print("\nRight-aligned list:")

for string in strings:
    while len(string) < x:
        string = " " + string
    print(string)