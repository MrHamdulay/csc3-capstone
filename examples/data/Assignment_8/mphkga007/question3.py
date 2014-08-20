"""encrypt a message by converting all lower  caset to the next character
kenneth mphele
6 may 2014"""
encrypted=''

def encrypt(string):
    letters=("a b c d e f g h i j k l m n o p q r s t u v w x y")
    letters=letters.split(' ')
    # checks if the string is not an empty string
    if string=="":
        return ""
    else:
        if string[0]==string[0].lower(): #checks if the string is in lower case
            if string[0]=="z":
                new="a"
            elif string[0]==" ":
                new=" "
            elif string[0] in letters:
                
                first=string[0]
                first=ord(first)+1
                new=chr(first)
            else:
                new=string[0]
                
            return new+encrypt(string[1:])
        else:
            return string
        
       
            
  
string=input("Enter a message:\n")
print("Encrypted message:")
print(encrypt(string))

            