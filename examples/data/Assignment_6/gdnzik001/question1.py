"""a program to right-align a list of strings entered by the user with the longest string
by Zikho Godana
23 April 2014"""

#first make an empty list
names=[]
lengths=[]
#ask the user to type in strings
name=input("Enter strings (end with DONE):\n")
print()

#add the strings entered by the user to the list
while name!="DONE":
    names.append(name)
    name=input("")

#find the length of each name 
print("Right-aligned list:")
for name in names:
    length=len(name)
    lengths.append(length)
    width=max(lengths) #find the longest string entered by the user
    output="{0:>"+str(width)+"}" 
    print(output.format(name))    
    