""" Do not prit strings twice
Lubalethu Dube
7 may 2014"""

def Mr_oncey(n):
    if len(n)== 0:
        return True
    
    elif len(n) == 1:
        return True
    elif n[0] == n [len(n)-1]:
        return Mr_oncey(n[1: len(n)-1])
    
    else:
        return False
n= input("Enter a string:\n")
i= Mr_oncey(n)

if i:
    print("Palindrome!")
else:
    print("Not a palindrome!")
    