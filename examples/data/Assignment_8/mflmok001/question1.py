"""recursive program for Palindromes
Mokoepa Mafologele
09/05/2014"""
def alt(p,var,i,cnt):
    if i>p:
        return cnt
    else:
        if var%i==0:
            cnt+=1
        i+=1
        return alt(p,var,i,cnt)
def Palindrome(dString,p):
    d=(p+1)*-1
    if p+1==len(dString):
        return "Palindrome!"
    if(dString[p]==dString[d]):
        return Palindrome(dString,p+1)
    else:
        return "Not a palindrome!"  
if __name__ == "__main__":
    x=input("Enter a string:\n")
    print(Palindrome(x,0))        
