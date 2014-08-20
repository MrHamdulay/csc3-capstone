def isItAPalindrome (word):
    if len(word) == 1 or len (word) == 0:
        return True
    if word[0] == word [-1]:
        if isItAPalindrome (word[1:-1]) == True:
            return True
        else:
            return False
    else:
        return False
   
user = input ("Enter a string:\n")
if isItAPalindrome (user) == True:
    print ("Palindrome!")
if isItAPalindrome (user) == False:
    print ("Not a palindrome!")