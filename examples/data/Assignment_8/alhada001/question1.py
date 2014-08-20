def isPalindrome (userInput):
    x = True
    y = False
    
    if len(userInput) == 1 or len (userInput) == 0:

        return x

    if userInput[0] == userInput [-1]:

        if isPalindrome (userInput[1:-1]) == True:

            return x

        else:

            return y

    else:

        return y

    

userinput = input ("Enter a string:\n")

if isPalindrome (userinput) == True:

    print ("Palindrome!")

if isPalindrome (userinput) == False:

    print ("Not a palindrome!")

