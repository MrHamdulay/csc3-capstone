# Program prints a given list of names right-alined with the longest name
# Wandile Lesejane
#23 April 2014

name=input("Enter strings (end with DONE):\n")
names=[]
maxwrd=0

# put all names in a list
while name!="DONE":
    names.append(name)
    if len(name)>maxwrd:
        maxwrd=len(name)  
    name=input()

#print them out in a right-aligned list    
print()
print("Right-aligned list:")
for i in names:
    space=" "*(maxwrd-len(i))
    
    print(space,i,sep="")
    