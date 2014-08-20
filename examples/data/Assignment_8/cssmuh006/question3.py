"""Encryption program
Haaroon Cassiem
9 May 2014"""

def encrypt(l):
    #encrypt a string
    if l=="":
        return l
    else:
        done=False
        q=ord(l[0])
        a=ord("a")
        z=ord("z")
        if a<=q<=z:
            q+=1
            done=True
            if q>ord("z"):
                q-=26
        else:
            q=q
                   
            
        q=chr(q)
        return q+encrypt(l[1:])
#call function
if __name__=="__main__":
    l=input("Enter a message:\n")
    print("Encrypted message:\n",encrypt(l),sep="")