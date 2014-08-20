# Palindrome, Assignment 8, Question 1
# Michael Sanne
# 2014/05/05

# Returns the reversed String
def reverseString (String, maximum):
    newString = ""
    #Stops at the end of the String (Number)
    if maximum < -len(String):
        return newString
    else:
        return newString + (String[maximum] + reverseString(String, maximum - 1))

#Tests the reversed number to check if it is a palindrome
def palindromeCheck (String, reverse):
    if (String == reverse):
        print ("Palindrome!")
    else:
        print ("Not a palindrome!")

#Asks user for input and starts reverse at the last character of -1        
String = input ("Enter a string:\n")
maximum = -1
reverse = reverseString (String, maximum)

#Final check
palindromeCheck(String, reverse)
