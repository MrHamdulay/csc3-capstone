"""Question 3 - encrypt string
Jembe Moran
11 May 2014"""
def encrypt(x):
    if x=="":
        return "" #end recursion
    else:
        if (ord(x[0])<97) or ord(x[0])>122: #if not a lowercase letter, leave it
            return(x[0]+encrypt(x[1:])) #encrypt remaining string
        if x[0]=="z": #if z, encrypt to a
            return ("a"+encrypt(x[1:]))
        else:
            p=chr(ord(x[0])+1) #encrypt first letter
            return(p+encrypt(x[1:])) #return encrypted letter and encrpyted rest of string
            
x=input("Enter a message:\n")
word=""
print("Encrypted message:\n", encrypt(x), sep="")
