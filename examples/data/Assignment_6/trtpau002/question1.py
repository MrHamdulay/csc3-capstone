"""Right-align list of stings
Paul Truter
22 April 2014"""

#get list of names
names = []
name = input("Enter strings (end with DONE):\n")
while name != "DONE":
    names.append(name)
    name = input("")
print()
#find word with most letters
max_name=0
for i in range(len(names)):
    if len(names[i]) > max_name:
        max_name = len(names[i])


#right align words
print("Right-aligned list:")
for name in names:
    print(("{0:>"+str(max_name)+"}").format(name))