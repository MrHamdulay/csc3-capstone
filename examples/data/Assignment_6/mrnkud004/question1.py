"""entering a list of strings
kennedy muranda
23/4/2014"""

#empty list
list_names = []

#prompt user to add to the list
s = input("Enter strings (end with DONE):\n")

#add strings to the list:
while s!='DONE':
    list_names.append (s)
    s = input("")

print()

#searching for longest string
if len(list_names)>0:
    longest = max(list_names, key = len)
    m = len(longest)
else:
    m=1
    
print("Right-aligned list:")

#aligning list
for s in (list_names):
    print(s.rjust(m))
    
    







