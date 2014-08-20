"""Assignment 8 Question1
Djavan Arrigone 9th May 2014"""

def palindrome (p):
    p = str(p)
    if len(p) == 0 or len(p) == 1: #Base case.
        return True
    elif p[0] != p[-1]: #Check if first character equals last.
        return False
    else: 
        return palindrome(p[1:-1]) #Recursion occurs whereby you return the string from condensed version of itself.


if __name__ == "__main__":
   
    x = input("Enter a string: \n")
    if palindrome(x):
        print("Palindrome!")
    else:
        print("Not a palindrome!")    
    
    
    
