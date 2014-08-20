#bknnao001
#09 may 2014
n=input("Enter a message:\n")
def enc(n):
    if len (n)==0:
        return n 
    elif n[0]=="z":
        return chr(97) + enc(n[1:])
    elif n[0].isalpha() and n[0].islower():
        return chr(ord(n[0])+1) + enc(n[1:])
   
    else:
        return n[0] + enc(n[1:])
print("Encrypted message:")
print(enc(n))


            