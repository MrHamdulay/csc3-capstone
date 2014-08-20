"""a program that prints out a list of names right alignend
nelisile mkhwebane 
assignment 6 
question 1"""

# get the list of names
names= []
name= input("Enter strings (end with DONE):\n")

# loop until the input is "DONE"

while name!= "DONE":
    names.append(name)
    name= input("")
    
#Output the string
print("")
print ("Right-aligned list:")

# Finding the column width
maxlength = 0
for word in names:
    if len(word) > maxlength:
        maxlength = len(word)
        
for word in names:
    space = maxlength - len(word)
    print (" "*space, word, sep="")
        
