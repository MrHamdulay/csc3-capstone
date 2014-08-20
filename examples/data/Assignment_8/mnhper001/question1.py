def palindrome(string):
    if len(string)<=1:
        return "Palindrome!"
    else:
        if string[0]==string[len(string)-1]:
            return palindrome(string[1:len(string)-1])
        else:
            return "Not a palindrome!"

        

print(palindrome(input("Enter a string:\n")))
        
