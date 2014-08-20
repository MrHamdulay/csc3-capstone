"""determing if a string is a palindrome using recursion
Haaroon Cassiem
8 May 2014"""

def reverse(l):
    #reverse string
    if l=="":
        return l
    else:
        return l[-1]+reverse(l[:-1])

#call functions
if __name__=="__main__":
    s=input("Enter a string:\n")
    q=reverse(s)
    if q==s:
        print("Palindrome!")
    else:
        print("Not a palindrome!")    
