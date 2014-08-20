"""recursive program to encrypt message
Rofhiwa Liphauphau
8 May 2014"""


words=input("Enter a message:\n")
y=words.lower()
def comp(e):
    if e=="":
        return ""
    if e!="":
        if e[0]==".":
            return "."
        if e[0]==" ":
            return " "+comp(e[1:])
        if e[0]=="z":
            return "a" +comp(e[1:])       
        else:
            y=ord(e[0])+1
            z=chr(y)
            return z +comp(e[1:])
if words==y:
    print("Encrypted message:\n",comp(words),sep="")
else:
    print("Encrypted message:\n",words,sep="")