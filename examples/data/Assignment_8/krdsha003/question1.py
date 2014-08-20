"""Assignment 8 Question 1
calculate whether or not a string is a palindrome
Shaheen Karodia
KRDSHA003
2014-05-04"""

def palin(string):
    """checks if a string is a palindrome recursively"""
    
    if len(string)<2:    #Base case #if string is less than two it is automaticalllya palindrome
        return True
    
    elif string[0]==string[-1]:         #checks the first character against the last character in the string
            return palin(string[1:-1]) #return the function checking through a smaller string 
        
    else:
        return False
    
    
def main():
    x=input("Enter a string:\n")
    if palin(x)==True:
        print("Palindrome!")
    else:
        print("Not a palindrome!")


if __name__=="__main__":
    main()           
        
                         