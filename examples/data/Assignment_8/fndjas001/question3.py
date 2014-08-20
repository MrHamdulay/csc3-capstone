"""A recursive program to encrypt a message
Jason Findlay
07/05/2014"""

mes=input("Enter a message:\n")
def encrypt(mes):
    alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    #Base case
    if len(mes)==1:
        if mes in alpha:
            if mes=="z":
                mes="a"
                return mes
            else:
                return chr(ord(mes)+1)
        else:
            return mes
    else:
        k=mes[0]
        #Changes z's to a's
        if k in alpha:
            if k == "z":
                k="a"
            #Shifts all other characters one character down
            else:
                k=chr(ord(k)+1)
        return k+encrypt(mes[1:])

print("Encrypted message:")
print(encrypt(mes))
