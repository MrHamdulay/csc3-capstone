"""Akhil Singh
SNGAKH004
23 April 2014
Program to store a list of names and then printed out in a right-alignment"""

#get list of names
names=[]
aname=input("Enter strings (end with DONE):\n")
#Appending names to list
while aname != "DONE":
    names.append(aname)
    aname=input ("")

#Determining the longest name
name_length=0
for i in names:
    if len(i)>=name_length:
        name_length= len(i)

#creatibg new lost for right-aligned names
new_names=[]    
#adding spaces to names not equal in length to the longest name
for z in names:
    while len(z)<name_length:
        z=" "+z
    if len(z)==name_length:
            new_names.append(z)  
        
#Print the new list containing right-aligned names
print("\nRight-aligned list:")
for a in new_names:
    print(a)
    