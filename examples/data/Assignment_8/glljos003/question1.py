"""program to check if a series of characters are palindromic
joshua gullan
9 may 2014"""

def palindrome_check(x):
    if x=='': #if no characters, not a palindrome
        print("Not a palindrome!")
    
    elif len(x)==1:  #if only one character, or last step of recursive loop, it is a palindrome
        print("Palindrome!")
    elif len(x)==2:
        if x[0]==x[-1]:
            print("Palindrome!")
        else:
            print("Not a palindrome!")
    elif x[0]==x[-1]:  #if first and last character are same
        return palindrome_check(x[1:-1])  #move onto next character
    else:
        print("Not a palindrome!")
        
    

def main():
    x=input("Enter a string:\n")
    palindrome_check(x)

main()
    
    
    