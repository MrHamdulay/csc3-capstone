"""assignment 8 question 1
shannon clacey
8 may 2014"""

def palindrome(string): #creates funciton
    if len(string) == 1 or len(string) == 0: #checks for single character or empty string
        return True #returns true if it is 
    elif string[len(string) -1]==string[0]: # checks if first and last letters are the same
        return palindrome (string[1:len(string)-1])
    else: #checks if neither of the above cases hold and the string is as a result not a palindrome 
        return False
    
user_input = input ("Enter a string: \n")
if palindrome(user_input) == True:
       print("Palindrome!")
else:
       print("Not a palindrome!")
        
        