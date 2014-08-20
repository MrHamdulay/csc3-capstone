#Thembekile Dubazana
#dbzphi002
#Assignment 8:Q3

"""Encrypt a message by taking letter to next letter"""

#The inputs
m=input("Enter a message:\n")
newm=""

#The function
def encrypt(m):
    global newm
    punc=[" ",".",","]
    #when do we stop
    if len(m)==0:
        return newm
    if m[0] in punc :#check for puctuation and return it
        newm=newm+m[0]
        return encrypt(m[1:])#check the rest of the letters removing first one
    else:
        if m[0]=="z":#if to check if letter is z and change to a 
            newm=newm+chr(97)
            return encrypt(m[1:])#check the rest of the letters removing first one
        
        else:
            enm=ord(m[0])+1 #encrypt all other letters normally
            newm=newm+chr(enm)
            return encrypt(m[1:])#check the rest of the letters removing first one

#The result if m is not an empty string or upper case
if m==m.upper():
    print("Encrypted message:\n",m,sep="")
else:
    if m!="":
        if m!="":
            print("Encrypted message:\n",encrypt(m),sep="")        
