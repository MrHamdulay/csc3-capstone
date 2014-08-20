"""Program in Recursive format,to check if a given string is a palindrome
Nicholas Stephenson
11 April 2014"""

def pdrome(x):
    if x == "": #Allows recursion to take place (""is a palindrome)
        result = True
    else:    
        if (ord(x[0]) - ord(x[len(x)-1])) == 0: #If the string index position at position No. 1 is equal to (=) string index position at position No.2
            return pdrome(x[1:len(x)-1]) #Recursion through the following position in the string
        else: #If not equal therefore, not a palindrome
            result = False
    return result #Returns the result of the function, for use elsewhere in the program



x = input("Enter a string:\n") #This formatting allows the user to enter the string outside of the recursive function
pdrome(x)

if pdrome(x) == True: #If the result is True, as stipulated before
    print("Palindrome!")
else: #If the result is False, then it is not a Palindrome
    print("Not a palindrome!")