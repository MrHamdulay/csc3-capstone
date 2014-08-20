#Progam to encrypt entered messages
#Mila Tshaka
#9 May 2014
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