"""program with a recursive function to calculate whether or not a string is a palindrome
Luvo Fokazi
09 May 2014"""
def alt(n,var,j,count):
    if j>n:
        return count
    else:
        if var%j==0:
            count+=1
        j+=1
        return alt(n,var,j,count)
def Palindrome(dString,n):
    d=(n+1)*-1
    if n+1==len(dString):
        return "Palindrome!"
    if(dString[n]==dString[d]):
        return Palindrome(dString,n+1)
    else:
        return "Not a palindrome!"  
if __name__ == "__main__":
    x=input("Enter a string:\n")
    print(Palindrome(x,0))        