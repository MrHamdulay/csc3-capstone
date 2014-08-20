"""a program that uses a recursive function to encrypt a message by converting all lowercase characters to the next character
Luvo Fokazi
9 May 2014"""
x=input("Enter a message:\n")
def Scra(dString,d):
    if(d > len(dString)-1):
        return ""
    elif dString==dString.upper():
        return dString
    else:
        var=dString[d]
        if 97<=ord(var)<=122:
            r=ord(var)+1
            if(r>122):
                r=97
            var=chr(r)
        return  var + Scra(dString,d+1)                       
print("Encrypted message:\n",Scra(x,0),sep="")        