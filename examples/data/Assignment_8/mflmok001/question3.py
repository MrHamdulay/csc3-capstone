'''a program that uses a recursive function to encrypt a message by converting all lowercase characters to the next character
Mokoena M
09 May '14'''
x=input("Enter a message:\n")
def Scramble(strng,d):
    if(d > len(strng)-1):
        return ""
    elif strng==strng.upper():
        return strng
    else:
        strng2=strng[d]
        if 97<=ord(strng2)<=122:
            r=ord(strng2)+1
            if(r>122):
                r=97
            strng2=chr(r)
        return  strng2 + Scramble(strng,d+1)                       
print("Encrypted message:\n",Scramble(x,0),sep="")        