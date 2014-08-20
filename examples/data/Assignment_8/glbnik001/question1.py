# 9 May 2014
# Nikhil Gilbert
# Checks to see if a string is palindrome

def main():
    n=input("Enter a string:\n")
    palin(n)
    if palin(n) == True:
        print ("Palindrome!")
    else:
        print ("Not a palindrome!")
    

def palin(s):
    if len(s)<1:
        return True
    else:
        if s[0] == s[-1]:
            return palin(s[1:-1])
        else:
            return False

main()