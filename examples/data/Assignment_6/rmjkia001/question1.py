"""Print out a list of strings that are right alligned
Kiara Ramjith
April 2014"""
names=[] #create an array
entName=input("Enter strings (end with DONE):\n")
while (entName != "DONE"): #fill the array
    names.append(entName)
    entName=input("")
longest=-1
for i in range(len(names)): #find the longest name
    if(len(names[i])>longest):
        longest=len(names[i])
for i in range(len(names)): #Make the names have the same spaces
    space=longest-len(names[i])
    name=names[i]
    names[i]=(space*" ")+name
print("\nRight-aligned list:")
for i in range(len(names)):#print the new names
    print(names[i])
    