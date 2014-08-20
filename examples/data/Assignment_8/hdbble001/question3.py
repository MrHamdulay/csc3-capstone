"""blessings hadebe
encrypts string inputed by user #question3.py 
9 may 2014"""

#encrypts string inputed by user
def encode(string):
    encoded = "" 
    if string.isupper():
        return string
    
    if string == "":
        encoded = ""
        
    elif string[0] !=" ":
        if string[0].isalpha():        
            if string[0]=="z":
                temp="a"    #temp is a temporary string to be added to the encoded string    
            else:
                temp= chr((ord(string[0])+1))  
        else:
            temp=string[0]
        encoded+= temp #for all characters besides spaces and letters, character remains the same
        encoded+= encode(string[1:])
    else:
        encoded+=" "
        encoded+= encode(string[1:])
    return encoded

string=input("Enter a message:\n")
print("Encrypted message:")
print(encode(string))