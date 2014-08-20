"""Rishen Singh
Assignment 8
Question 2"""
count=0
def pairs(message):
    global count #defines count as a global variable
    if message=='':
        return count #if blank, returns 0
    else:
        
        if(len(message)>1 and message[0]==message[1]): #checks through for pairs
            count=count+1 #increases count
            return pairs(message[2:len(message)]) #checks the rest of the message for pairs
        else:
            return pairs(message[1:len(message)])

user_input=input("Enter a message:\n") #user input  
print("Number of pairs:",pairs(user_input))