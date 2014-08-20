def palindrome(phrase):
    
    if len(phrase) <= 1:
        return "Palindrome!"
    elif(phrase[0] != phrase[len(phrase)-1]):
        #print( phrase[0] , phrase[len(phrase)-1])
        return "Not a palindrome!"
    else:
        return palindrome(phrase[1:(len(phrase)-1)])

print(palindrome(input("Enter a string:\n")))

        