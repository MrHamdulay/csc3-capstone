"""CHTGEN002
09/05/2014
Encryption"""

def encryption(sen_input): #function defined
    
    if(sen_input==""):
        return ""
    
    else:
        if( sen_input[0]!="z" and sen_input[0].islower()): #any character except z that is lower case 
            return chr(ord(sen_input[0])+1)+encryption(sen_input[1::])
        
        elif(sen_input[0]=="z" and sen_input[0].islower() ): #for z only
            return "a"+encryption(sen_input[1::])
        
        else:
            return sen_input[0]+encryption(sen_input[1::])

message=input("Enter a message:\n")
print("Encrypted message:",encryption(message),sep='\n')