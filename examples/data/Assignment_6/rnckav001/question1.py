#CSC ass.6 Q1 names
#Kavir Ranchod - rnckav001
#23/04/2014

#Get first name:
name=input("Enter strings (end with DONE):\n")
#initiate the list
names=[]
#Initiate the space variable that will later right-align each name
space=0
#Loop to fetch each new name and add it to the list
while name != "DONE":
    names.append(name)
    name=input("")
    #Set length of longest name
    if len(name) > space:
        space=len(name)
#print list
print("\nRight-aligned list:")
for name in names:
    #right-align each name
    print(name.rjust(space))