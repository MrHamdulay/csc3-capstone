"""Program to encrypt string
Sbonelo Mntungwa
9 May 2014"""

message = input("Enter a message:\n")                   #Inputing variables
def start(message):                                     #Defining function start
     
    if (message == '' or  message[0] == message[-1] and message[0]== ' ' and message[-1] == ' '): #if an empty string has been inserted
        nothing = "nothing"                             #Breaking program
    elif message[0] != '':                              
        def encrypt(message,list1):                     #defining function encrypt
    
            if len(message) == 0:                           #Case where there is no character left to encrypt
                list1 = ''.join(list1)                  #joining list
                print("Encrypted message:\n"+list1)     #Output result
        
            elif (ord(message[0])<97 or ord(message[0])>122) :# Case where character is not a lower case alphabet
                list1.append(message[0])
                return encrypt(message[1:],list1)
    
            elif message[0] == "z":                         #Case where character is "z"
                list1.append('a')
                return encrypt(message[1:],list1)
    
            else:                                           #Encrypting a lowercase character
                new_char = ord(message[0])
                new_char = new_char +1
                new_char = chr(new_char)
                list1.append(new_char)
                return encrypt(message[1:],list1)
    

        list1 = []                                      #Entering list
        encrypt(message,list1)                          #Calling function encrypt
    else:
        return start(message[1:])                       #returning start function without message having a first character to see if a different character will appear


start(message)                                      #running start function
  
                                      
                         

