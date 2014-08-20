"""Program to print an ordered list without duplicates
Carla Wilby
27 April 2014"""

#Get list of strings from user
strings = input("Enter strings (end with DONE):\n")
stringList = []
while strings != "DONE":
#If the string is not already in the list, add it to the list
    if strings not in stringList:
        stringList.append(strings)
    strings = input("")

#Print the list of unique strings
print("\nUnique list:")
for i in stringList:
    print(i)
            