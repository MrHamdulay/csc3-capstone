#enctypting the string entered by a user
#Anthony Jacob
#9 May 2014

m = input("Enter a message:\n")

def encrypt_message(m,f):#defining the function where m=message and f=final_output
    if m=="":   #making m an empty string
        return print(f)
    else:
        position = ord(m[0])#to determine position of each character
        
        if 97<=position<122:
            position+=1
            new = chr(position)
            f = f+new
            return encrypt_message(m[1:],f)
        
        elif position == 122:
            excluding = "a"
            f = f+excluding
            return encrypt_message(m[1:],f)
        
        else:
            f+=chr(position)
            return encrypt_message(m[1:],f)
        
    print(f)# the encrypted message
print("Encrypted message:")

encrypt_message(m,"")  #calling the function