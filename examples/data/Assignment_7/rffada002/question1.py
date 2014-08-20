"""Adam Ruff RFFADA002
27/04/2014
Assignment 7 Question 1

Enter a list of strings, print a list of the unique items in the first list"""

#Construct
words = []
printed = []

#Enter list
print ("Enter strings (end with DONE):")

while True:
    word = input("")
    if word == "DONE":
        break 
    words.append(word)      
    
#Unique list
print ("")
print ("Unique list:")
for i in range(len(words)):
    if words[i] not in printed:
        print (words[i])
        printed.append(words[i])