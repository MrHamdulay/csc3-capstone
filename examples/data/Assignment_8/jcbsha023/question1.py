#Check whether input from user is a palindrome
#Anthony Jacob
#09 May 2014
                          
word = input ("Enter a string:\n")
def ispalindrome(word):    #define the function 
    if len(word)<2:
        return print("Palindrome!")
    
    else:
        if word[0]==word[-1]:
            return ispalindrome(word[1:-1])
                                            #if string is not palindrome
        else:
            return print("Not a palindrome!")
        
ispalindrome(word)        #calling function