'''Assignment 8 question 2 Number of pairs
Adam Smith
5 May 2014'''


def Checker(text): #recursive function that increments when there are pairs
    
    if len(text) <= 1:
        return 0
    
    if text[0] == text[1]:
        return (Checker(text[2:])) +1
        
    return (Checker(text[1:]))

print ("Number of pairs:", Checker(input("Enter a message:\n"))) 