"""Ricky Conn
CNNRIC004
29/04/2014
Allows the user to enter a list of strings and these strings are then printed in the same order but without duplicates."""

userInput = input("Enter strings (end with DONE):\n")
A = []
if(userInput != "DONE"):
    A = [userInput]
    
    found = False
    while( userInput != "DONE"):
        found = False
        for i in A:
            if((userInput == i)):
                found = True
                
        if(not found):
            A.append(userInput)
        userInput = input("")
        
        
print("\nUnique list:")
for i in A:
    print(i)

        
    
