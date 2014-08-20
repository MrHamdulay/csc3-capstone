def Palindrome(string):
    if string == '':
        return "Palindrome!"
    elif (ord(string[0]) == ord(string[len(string)-1])):
        return Palindrome(string[1:len(string)-1])
    else:
        return "Not a palindrome!"
        
string=input("Enter a string:\n")
print(Palindrome(string))