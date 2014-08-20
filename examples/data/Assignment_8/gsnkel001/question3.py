#Recursive function converting all lowercase letteers to the next letter
#Kelly Goosen
#05/08/2014




def encrypt(x):
    if len(x)== 1:
        if x.islower(): #only converts lower
            if x== 'z':return 'a'
            else: return chr(ord(x) + 1)
        
        else:return x
    
    else:return encrypt(x[0]) + encrypt(x[1:]) #function within function therefore recurring

string = input("Enter a message:\n")
print("Encrypted message:")
print(encrypt(string))
