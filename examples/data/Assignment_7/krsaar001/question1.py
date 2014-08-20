# Aaron Krishna
# 02 May 2014
# List with no duplicates

strings=[] #empty list to store strings
string=input('Enter strings (end with DONE):\n')

while string != "DONE": #adds string to list
    if string in strings:
        string = input()
    else:
        strings.append(string)
        string = input()

print()
print("Unique list:")

for string in strings: #prints unique strings in a list
    print(string)