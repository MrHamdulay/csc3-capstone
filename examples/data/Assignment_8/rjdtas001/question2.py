#Tashiq Rajdev
#Pairs
#Assingment 8 Question 2
def pairs(message):
    if len(message)==0 or len(message)==1:
        return 0
    elif message[0]==message[1]:
        return 1+pairs(message[2:])
    else:
        return pairs(message[1:])
    
    
    
    
    
    
    
    
    
message=input("Enter a message:\n")
print("Number of pairs:",pairs(message))

#Try do using list