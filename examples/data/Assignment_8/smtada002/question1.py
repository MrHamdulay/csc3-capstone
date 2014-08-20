'''Assignment 8 question 1 palindrome checker
Adam Smith
5 May 2014'''

def Checker(text): #a recursive function that returns true if it runs through the whole string
    
    if text == "":
        return True
    
    if text[0] == text[-1]:
        return (Checker(text[1:-1]))
    else:
        return False
        
    
UserInput = input("Enter a string:\n")
if Checker(UserInput):
    print("Palindrome!")
else:
    print("Not a palindrome!")