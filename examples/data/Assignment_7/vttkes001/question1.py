"""Enter list of strings
Keshin Vittee
28 April 2014"""

print("Enter strings (end with DONE):")
x = []

while True:
    userin=input("")
    if userin == "DONE":
        break
    elif userin not in x:
        x.append(userin)
        
print()        
print("Unique list:")
for a in x:
    print(a)
    