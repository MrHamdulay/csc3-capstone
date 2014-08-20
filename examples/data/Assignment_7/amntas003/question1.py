#AMNTAS003  #Tashfia Amin   #Due Date: 2 May 2014
#Question 1: Assignment 7   #Print list without duplicates

#Create an empty list and empty variable for strings
strings = []
entry = input("Enter strings (end with DONE): \n")

#Create sentinel "DONE" for end of entries into list
while entry != "DONE":
    strings.append(entry)
    entry=input("")

#Print out list without duplicates
print("\nUnique list:")
used = []
for i in strings:
    if i not in used:
        print(i)
        used.append(i)