'''Assignment8q1, Palindrom finder, Recursion
Kieran Reilly, RLLKIE001
06/07/14'''

def palindromeCheck(userString):
    '''find if an entered string is a palindrome or not'''
    #basecase - does nothing if length is less than 1
    if len(userString) > 1:
        #recursive case - checks current and mirroring character.
        if(userString[0] != userString[-1]):
            return False
        #recursive step - goes through the string by checking a character in the beginning and its mirroring character
        elif(userString[0] == userString[-1]):
            palindromeCheck(userString[1:-1])
            return True
    if len(userString) == 1 or userString == "":
        return True
        
    
def main():
    #where the action happens
    userString = input("Enter a string: \n")
    palin = palindromeCheck(userString)
    
    if palin is True:
        print("Palindrome!")
    else:
        print("Not a palindrome!")
    
    
main()