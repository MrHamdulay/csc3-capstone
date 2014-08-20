#Kalind Ramnarayan
#27 April 2014
#list of strings without duplicates


list=[]                                            #Create a list
string=input("Enter strings (end with DONE):\n")
while string!="DONE":                               # add strings to the list
    list.append(string)
    string=input()
    
newlist=[]
    
for i in list:
    if not i in newlist:
        newlist.append(i)

print()
print("Unique list:")        
for i in newlist:
    print(i)