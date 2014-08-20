"""Align a list of strings
Kumaran Reddy
24 April 2014"""

name=input("Enter strings (end with DONE):\n") #Get names in list
names=[]
while name != "DONE":
    names.append(name)  #Add name to list
    name=input('')      #Allow for new input by the user

print()    
print("Right-aligned list:")
max=0
for i in names[0:len(names)-1]: #To search every name in list
    if max < len(i):
        max=len(i) #Max length to align all names with
        

for x in names[0:len(names)]:
    print(" "*(max-len(x))+x) #the amount of space to be printed must be whats left after you subtract the length of the word from the max