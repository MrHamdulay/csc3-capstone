'''Program to encrypt message by converting all lowercase letters to next letter alphabetically
nkosi gumede
8 may 2014'''

D={'a':'b','b':'c','c':'d','d':'e','e':'f','f':'g','g':'h','h':'i','i':'j','j':'k','k':'l','l':'m','m':'n','n':'o','o':'p','p':'q','q':'r','r':'s','s':'t','t':'u','u':'v','v':'w','w':'x','x':'y','y':'z','z':'a',' ':' ','.':'.'}

listed=[]
def encrypt(message):
    if message=="":
        print("Encrypted message:")
        print("".join(listed))
    elif message[0] in D:
        listed.append(D[message[0]])
        encrypt(message[1:])
    else:
        listed.append(message[0])
        encrypt(message[1:])
    
if __name__=='__main__':
    x=input("Enter a message:\n")
    encrypt(x)