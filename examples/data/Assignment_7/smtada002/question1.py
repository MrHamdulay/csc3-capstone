'''Assignment 7 question 1 No Repeats
Adam Smith
27 April 2014'''

Strings = [] #creates list to store names of strings
Strings = [input("Enter strings (end with DONE):\n")]

while "DONE" not in Strings: 
    UserInput = input()
    if UserInput == "DONE": #breaks the loop if the user inputs DONE
        break
    
    elif UserInput not in Strings: #if the string does not exist add it to the list
        Strings.append(UserInput)

print()
print("Unique list:")
for output in Strings: #outputs the list
    if output!= "DONE":
        
        print(output)