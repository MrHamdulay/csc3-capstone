"""
Keyoolin Padayachee
Unique Lists
01 May 2014
"""

print("Enter strings (end with DONE):")
strings = []
word = "" #Declared to start the loop
while word!="DONE":
    word = input()
    if word == "DONE": 
        break #Stops the loop
    if word not in strings: 
        strings.append(word) #appends to the unique list
print("\nUnique list:")
for i in range(len(strings)):
    print(strings[i])