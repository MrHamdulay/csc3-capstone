"""Assignment 8-Q3
Nandani Birjanund
5 May 2014"""

input_by_user=input("Enter a message:\n") #user inputs the message

def Encrypt(input_by_user):
   
    if input_by_user =="": #empty string
        return ""
      
    elif input_by_user[0]==" ": #string with space
        return " " + Encrypt(input_by_user[1:]) #space and message string spliced is returned 
   
    elif(ord(input_by_user[0])<97): #first letter by ord becomes number which is < 97
        return input_by_user[0] +Encrypt(input_by_user[1:])
      
    elif(input_by_user[0]=='z'): #string with 'z'
        return "a" + Encrypt(input_by_user[1:]) #gives 'a' where 'z' is
   
    elif not input_by_user[0].isalpha(): #check first letter if it is in the alphabet, then there after...
       
        return input_by_user[0] + Encrypt(input_by_user[1:])
      
    else:   
       
        return chr(ord(input_by_user[0])+1)+Encrypt(input_by_user[1:])#chr function to convert to character
   
function=Encrypt(input_by_user)
print("Encrypted message:\n"+str(function)) #Encrypted message and str function 