#Assignment 7
#Question 1
#Barry Su
#30 April 2014
#Program where user can enter a list of strings and then print them in the same order without duplicates

#get list of strings
stringList = []
strings = input("Enter strings (end with DONE):\n")
while strings != "DONE":
    stringList.append(strings)
    strings = input("")

#create a new list of strings with no duplicates    
print()
print("Unique list:")
newList = []
for string in stringList:
    if not string in newList:   #if there is not a same string in the list already, add to list
        newList.append(string)

#print the new list of strings from original list without the duplicates
for string in newList:
    print(string)