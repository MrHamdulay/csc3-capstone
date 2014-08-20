def isPalindrome (n): #Checking if palindrome
    if len(n) == 1 or len(n) == 2 and n[0] == n[1]: #If one letter or two equal letters
        return True
    if n[0] == n[-1]: #If ends are equal, check middle of string
        return isPalindrome(n[1:-1])
    else: #If ends not equal
        return False
    
if __name__ == '__main__':
    userString = input ("Enter a string:\n") #Printing the result
    if isPalindrome(userString):
        print ("Palindrome!")
    else:
        print ("Not a palindrome!")