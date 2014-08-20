#Program to create unique list
#Joe Sutton
#23 April 2014

name = input("Enter strings (end with DONE):\n")
listofnames=[] #create empty list
while not name == "DONE":
    listofnames.append(name)
    name = input("")
    
uniquenames=[] #create empty list for unique names

for name in listofnames:
    if name not in uniquenames:
        uniquenames.append(name)

print("\nUnique list:")
for name in uniquenames:
    print(name)