"""Using recursion to encrypt a message
Carla Wilby
4th April 2014"""

string_in = input("Enter a message:\n")
count = 0
encrypted = ""

def encrypt(count,encrypted):
    if count<len(string_in):
        if string_in[count].islower():
            if 97 <= ord(string_in[count]) < 122: #if character is a letter between a and y
                encrypted+=chr(ord(string_in[count])+1) #make it equal to next letter of the alphabet
            elif (ord(string_in[count]) == 122): #if character is a z
                encrypted+=chr(ord(string_in[count])-25)  #make it equal to a
        else:
            encrypted+=string_in[count] #if not a letter, or uppercase, add as is
        count+=1
        encrypt(count,encrypted)
    else:
        print("Encrypted message:\n"+encrypted)

if __name__ == '__main__':     
    encrypt(count,encrypted)