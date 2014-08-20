"""blessings hadebe
calculate whether or not given string is a palindrome #question1.py 
9 may 2014"""

#calculate whether or not given string is a palindrome
def Palindrome(string):
    if string == '':
        return "Palindrome!"
    elif (ord(string[0]) == ord(string[len(string)-1])): #checks if first and last characters of the string are identical
        return Palindrome(string[1:len(string)-1]) #strips off first and last letters and repeats entire process on remaining charaters
    else: 
        return "Not a palindrome!"
        
string=input("Enter a string:\n")
print(Palindrome(string))