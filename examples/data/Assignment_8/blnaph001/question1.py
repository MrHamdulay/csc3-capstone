#palindromes or not?!
#aphiwe baleni
#5 may 2014
def palidrome(message):
    if message=="":
        return ""
    else:
        return message[-1] + palidrome(message[:-1])
string= input("Enter a string:\n")
pal=palidrome(string)
if string == pal:
    print("Palindrome!")
else:
    print("Not a palindrome!")
