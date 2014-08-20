"""program to check palinindrom with recursion
Alexander Whiting
8 may 2014"""

def reverse(sent):#reverses a string
    
    if sent == "":
        return ""
    else:
        return reverse(sent[1:]) + sent[0:1]



sent = input("Enter a string:\n")
rsent = reverse(sent)
if sent == rsent: # checks if reversed string is equal to the string
    print("Palindrome!")
else:
    print("Not a palindrome!")





    