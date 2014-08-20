# BLKAT005
# Kate Bell
# 6 May 2014 

def palindrome(s):
    if len(s)==1:
        print("Palindrome!") 
    elif len(s)==2:
        if s[0]==s[1]:
            print("Palindrome!")
        else:
            print("Not a palindrome!")
    elif s[0]==s[-1]:
        palindrome(s[1:-1])
    else:
        print("Not a palindrome!")

sentence = input("Enter a string:\n")
palindrome(sentence)