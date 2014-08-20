#Question 2 - Assignment 8
#Riya Desai
#7 May 2014


#ask the user to type in a message
message=input("Enter a message:\n")


#define the function "Pairs"
def Pairs(message):
    
    if message=="":
        return 0
    elif(len(message)==1):
        return 0
    
    else:
        
        #search for pairs of letters
        if message[0]==message[1]:
            message=message[2:]
            return 1+Pairs(message)
        else:
            return Pairs(message[1:])
   
        
number=Pairs(message)
print("Number of pairs: " +str(number))