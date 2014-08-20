#mahdi marcus

s = input("Enter a string:\n") #enter the string

def p(s): #define function p
    if len(s)==1: #check if there is a string
        print("Palindrome!")
    elif s[0]!=s[-1]: #if 1st char not equal to last char it is not a palindrome
        print("Not a palindrome!")
    else:
        return p(s[1:-1]) 
    

p(s) #call function
