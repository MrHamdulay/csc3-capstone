"""reneshan naidoo
ndxren013
7 May 2014"""

def encrypt(string,y):
    if len(string)==0:#checking if the strings length is 0
        return print("Encrypted message:\n"+y) 
    else:
        if 97<=ord(string[0])<=122:#making sure everything is in lowercase
            encrypt(string[1:],y + chr(((ord(string[0]) - 97) + 1) % 26 + 97))
        else:
            y+=string[0]
            encrypt(string[1:],y)

def main():

    user=input("Enter a message:\n")#getting user input
    encrypt(user,"")

main()

            
            
            
            
        
    

        
        
