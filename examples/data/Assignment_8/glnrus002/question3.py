#GLNRUS002
#ASSIGNMENT 8
#QUESTION 3
#ENCRYPT MSG BY ONE CHARACTER
enc=""#used to accumulate encrypted msg
def encrypt(m):# used to encrypt
    lowercase="abcdefghijklmnopqrstuvwxy"
    global enc
    if m=="":#done through whole string
        return enc
    elif m[0]=="z":#last letter back to a
        enc+="a"
        encrypt(m[1:0])
    elif m[0]==" ":#retain space
        enc+=" "
        encrypt(m[1:])
    elif m[0]in lowercase:#change if lower case
        enc+=chr(ord(m[0])+1)#SHIFT ONE UP
        encrypt(m[1:])
    else:#retain if capital
        enc+=m[0]
        encrypt(m[1:])

msg=input("Enter a message:\n")
encrypt(msg)
print("Encrypted message:\n"+enc)