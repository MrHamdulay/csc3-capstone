# Encryption through recursion
# Danielle Sher

x = input("Enter a message:\n")
print ("Encrypted message:")
def encrypt(x):
    if x.isupper() == True:
        return x
    if x == "" or x == ".":
        return x
    if x[0] != " " and x[0] != 'z':
        return chr(ord(x[0])+1) + encrypt(x[1:])
    if x[0] == 'z':
        return 'a' + encrypt(x[1:])
    if x[0] == " ":
        return " " + encrypt(x[1:])
                            
print (encrypt(x))
