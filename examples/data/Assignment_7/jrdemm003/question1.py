"""assignment 7, q1- add strings to a unique list
emma jordi
27 april 2014"""

#create empty lists
listall=[]
uniquelist=[]
#get input
strings=input("Enter strings (end with DONE):\n")

while strings!= "DONE":
    #add input to listall
    listall.append(strings)
    strings=input("")
    
#go through listall, if in uniquelist continue, else add to uniquelist
for string in listall:
    if string in uniquelist:
        continue
    else:
        uniquelist.append(string)
print()
print("Unique list:")
#print uniquelist
for string in uniquelist:
    print(string)