#Assignment 6, Question 1
#Author: Muhammad Sabir Buxsoo (BXSMUH001)
#Class: CSC1015F 2014
#Date Created: 20/04/2014; Modified: 21/04/2014(Updated comments)

#This program is designed to right-align a list of strings with the longest string.

#Pre-condition: Input a list of strings and end the list with "DONE".
#Post-condition: Output list of string, right-aligned with the longest string.

#Creating an empty array stringList to append values of names.
stringList = []

#Header.
print("Enter strings (end with DONE):")

string = ""#Initializing input.

#Creating list of names:
#.#Pre-condition: Input list of names and append each name to stringList.
#.#Post-condition: On entering "DONE", break out of loop.
while (string != "DONE"):
    string = input()
    if(string == "DONE"): #Break out of loop when sentinel "DONE" is reached.
        break
    stringList.append(string) #Append name to list


#Printing list of names.
#.#Pre-condition: Find the name with the maximum length.
#.#Post-condition: Output list, forcing each name to be aligned to the right with the maximum space available(maxLength).
maxLength = 0 #Initializing maximum space for each name

for nameLength in range(len(stringList)): #Finding the name with the longest length and updating maxLength accordingly.
    if(len(stringList[nameLength]) > maxLength):
        maxLength = len(stringList[nameLength])

print("\nRight-aligned list:") 
for names in range(len(stringList)): #Looping throught list and print each name.
    print(('{:>'+str(maxLength)+'}').format(stringList[names])) #Using format to right-align each name and print.