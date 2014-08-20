#ass.7 Q1 Strings
#Kavir Ranchod RNCKAV001
#28/04/2014

#Get list from user
print("Enter strings (end with DONE):")
string = input()
allstrings = []
while string != "DONE":
    allstrings.append(string)
    string = input()
#Remove repeated strings
newstrings = []
for i in allstrings:
    if i not in newstrings:
        newstrings.append(i)
#Print the new list
print("\nUnique list:")
for i in newstrings:
    print(i)