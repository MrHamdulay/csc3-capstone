def pal():
    n=input("Enter a string:\n")
    a="Not a palindrome!"
    b="Palindrome!"
    if n=="":
        return n
    elif n[0]!=n[-1:]:
        return a
    else:
        return b 

print(pal())