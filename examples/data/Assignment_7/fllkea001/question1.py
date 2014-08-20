#Keanon Fll
#1 May 2014
#Assignment 7

#Python program that allows a list of strings to be entered 
#and then prints a new list woth no duplicates

#printing out the prompt for the user of the program
print("Enter strings (end with DONE):")
#initialising empty variables
x= ""
strings=[]

#While loop that allows for input and populates list
while x != "DONE":
    x = input()
    #Using an if condition that would only append unique values to the list
    if not x in strings and x != "DONE":
        strings.append(x)

print()#printing a line
print("Unique list:")
#printing out the unique list
for i in range(len(strings)):
    print(strings[i])