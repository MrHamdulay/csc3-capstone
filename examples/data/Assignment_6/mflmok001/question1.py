"""Mokoena Mafologele
program to align stirngs to the right in order
22/04/2014"""
str_List=[] #Create an empty list
max_length=0#initialise maximum length
i=0
#get strings from user
name=input("Enter strings (end with DONE):\n")
while name!="done" and name!="DONE":
    str_List.append(name) #populates array of strings
    i+=1
    if max_length<len(name):
        max_length=len(name)
    name=input()
formater="{0:>"+str(max_length)+"}"
print("\nRight-aligned list:")
for j in str_List:
    print(formater.format(j))
