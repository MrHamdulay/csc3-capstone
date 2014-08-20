"""Saijil Nemchund 
NMCSAI001
Question 1
program that is aligning lists to the right"""


#Creating a blank list
names=[] 
entName=input("Enter strings (end with DONE):\n")
while (entName != "DONE"): #occupying the list 
    names.append(entName)
    entName=input("")
longest=-1
for i in range(len(names)): #find the longest name
    if(len(names[i])>longest):
        longest=len(names[i])
for i in range(len(names)): 
    space=longest-len(names[i])
    name=names[i]
    names[i]=(space*" ")+name
print("\nRight-aligned list:")
for i in range(len(names)):  #using the print function to print the new names
    print(names[i])
    