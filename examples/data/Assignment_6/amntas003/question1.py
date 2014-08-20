#AMNTAS003  #Tashfia Amin   #Due Date: 25 April 2014
#Question 1: Assignment 6   #Aligning a list

#Create an empty list and then enter strings into the list
strings =[]
string = input("Enter strings (end with DONE):\n")

#Create a sentinel "DONE" for end of list entries
maximum=0
while string != "DONE":
    strings.append(string)
    string=input("")

#Find longest string in list
maximum = 0
for string in strings:
    if len(string) > maximum:
        maximum=len(string)
    
#Align list to the right according to the length of the longest string
print("\nRight-aligned list:")
for string in strings:
    indentation=maximum - len(string)
    print(" "*indentation, string, sep="")