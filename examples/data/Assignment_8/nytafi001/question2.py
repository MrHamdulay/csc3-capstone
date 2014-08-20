""" A program that uses a recursive function to count the number of pairs of repeated characters in a string.
Author: Afika Nyati
Date: 5th May 2014"""


def pairs(message): # A recursive function that counts the number of pairs of repeated characters in a string.
    
    if message == "": # The stopping condition occurs when the recursive function reaches the end of the string.
        return 0    # It returns 0
    
    elif message[:1] == message[1:2]:   # This checks whether the first letter of the string is equal to the second letter of the string.
        return 1 + pairs(message[2:]) # If the condition is true, it adds a count of one and adds it to the sum of the count of the rest of the string placed in the same function.
    
    else:   # If they aren't the same, the function checks if there are any other pairs in the string by calling itself.
        return pairs(message[2:])
    
    

def main():
    
    message = input("Enter a message: \n")  # Asks user for a message.
    
    print("Number of pairs:", pairs(message))   # Prints the result of the number of pairs.
    

main()
    
