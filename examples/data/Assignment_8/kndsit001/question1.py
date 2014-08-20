"""Program to Determine Palindrome
Sithasibanzi Kondleka
9 May 2014"""

words = input("Enter a string:\n")

def palindrome(string):
    if string == "": #a message that contains nothing is technically a palindrome
        return "Palindrome!"
    if len(string) == 1:
        return "Palindrome!" #a message that contains 1 letter is technically a palindrome
    else:
        if string[0] == string[-1]: #isolating the letters at the ends
            return palindrome(string[1:-1])
        else:
            return "Not a palindrome!" #should the ends not match it is not a pali-pal
        
print(palindrome(words))