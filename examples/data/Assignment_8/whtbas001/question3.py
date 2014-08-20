#CSC1015F
#ASSIGNMENT 8
#QUESTION 3
#06/05/2014
#WHTBAS001  
#THOMAS WHITEHEAD

def encrypt_next(x):
    if x == "": #exit criteria/base case
        return x    
    else:
        if x[0] == ' ': #do nothing to a space
            return x[0] + encrypt_next(x[1:])
        elif x[0] == '.':   #do nothing to a fullstop
            return x[0] + encrypt_next(x[1:])           
        elif x[0] != x[0].lower():  #do nothing to a capital
            return x[0] + encrypt_next(x[1:])
        elif x[0] != 'z':     #shift the z to an a
            return chr(ord(x[0])+1) + encrypt_next(x[1:])   
        else:   #shift all other letters +1
            return 'a' + encrypt_next(x[1:])    

def main():	#main function to get input and run reverse function.
    string = input("Enter a message:\n")
    print("Encrypted message:")
    print(encrypt_next(string))

main()