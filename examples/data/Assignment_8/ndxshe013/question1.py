

x = input("Enter a string:\n") 

def CheckString(n):
    if len(n)<1:
        return True
    elif n[0] == n[-1]:
        return CheckString(n[1:-1])
    else:
        return False
if CheckString(x)==True:
    print("Palindrome!")
else:
        print("Not a palindrome!")


        
    