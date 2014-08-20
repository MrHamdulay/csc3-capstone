#program to to right align a list of strings with the longest one
#Lebogang masila
#20 April 2014

names=[]
print("Enter strings (end with DONE):")
name=input()
if name != "DONE":
    names.append(name) #add string to the list
while name != "DONE":
    name=input()
    if name != "DONE":
        names.append(name)
print()
print("Right-aligned list:")

highstring=0

for i in range(len(names)):
    if(len(names[i])>highstring):
        highstring=len(names[i])
        
for f in range(len(names)):
    y=highstring-len(names[f])
    space=" " *y 
    print(" " *y,names[f],sep="")
    

    