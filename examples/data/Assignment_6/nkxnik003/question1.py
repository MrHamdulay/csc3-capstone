#Comsic Assignment 6
#Question 1
#Nikhil Naik
#23/04/2014


enterString=input("Enter strings (end with DONE):\n") #Enter the strings
enterStringArray=[]
space=0
while enterString != "DONE": #Loop until user enter "DONE"
    enterStringArray.append(enterString)
    enterString=input("")
    if len(enterString) > space: #Gets the length of the longest string for use in right allignment
        space=len(enterString)
print("\nRight-aligned list:")      #Prints title for right alligned list
for enterString in enterStringArray:  #Loop for each number of strings in the list
    print(enterString.rjust(space))  #Prints each number of strings at each iteration of loop