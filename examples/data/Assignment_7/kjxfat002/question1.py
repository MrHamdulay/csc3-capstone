"""
Created on May 1st 2014
Unique Strings
KJXFAT002
"""

vote_input = ""
strings = []

print("Enter strings (end with DONE):")

while True: #indefinite loop
    vote_input = input() #enter a new input
    if vote_input == "DONE":
        break
    if vote_input not in strings:
        strings.append(vote_input) #adds to list
        
print("\nUnique list:")
for i in strings:
    print(i)