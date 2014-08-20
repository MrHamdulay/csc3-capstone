string=input("Enter a string:\n")

def reverse(string):
    
    if string=='':
        return ''
    else:
        return string[-1] + reverse(string[:-1])
    
    
def check(string,string1):
    if string==string1:
        print("Palindrome!")
    
    else:
        print("Not a palindrome!")
        

check(string,reverse(string))