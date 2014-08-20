'''Program using recursion to test whether or not string is a palindrome
Nkosi Gumede
7 may 2014'''

global quit_length

def palindrome(string):
    string=str(string)    
    if len(string)!=1 and len(string)!=2:
        if string[0]!=string[-1]:
            print("Not a palindrome!")
        elif string[0]==string[-1]:
            palindrome(string[1:-1])
    elif len(string)==2:
        if string[0]!=string[1]:
            print("Not a palindrome!")
        else:
            print("Palindrome!")
    else:
        print("Palindrome!")
    
if __name__=='__main__':
    x=input("Enter a string:\n")
    palindrome(x)