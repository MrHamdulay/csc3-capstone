"""get list with no duplicates
Paul Truter
29 May 2014"""

#get list of strings
strings = []
string = input("Enter strings (end with DONE):\n")
while string != "DONE":
    strings.append(string)
    string = input("")
print()

#remove duplicates
new_string = []
for i in strings:
    if i not in new_string:
        new_string.append(i)
    
#print list
print("Unique list:")
for i in new_string:
    print(i)
