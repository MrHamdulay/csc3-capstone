#Kiuran Naidoo
#Assignment 6
#Question 1
#24 April 2014

names = [] #list to store names that are inputted
maxLen = 0 #Storing the maximum string length
currentName = input("Enter strings (end with DONE):\n")
while currentName.upper() != "DONE":
    names.append(currentName) #Add names to list
    if len(currentName)>maxLen: #Checking if the maximum string length must be updated
        maxLen = len(currentName)     
    currentName = input("")
   

outputFormat = "{0:>"+str(maxLen)+"}" #Formatting column to length of maximum string length       
print()
print("Right-aligned list:")
for x in names:
    print(outputFormat.format(x))
    