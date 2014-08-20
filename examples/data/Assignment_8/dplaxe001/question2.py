""" Program to count the number of pairs of letters in a string
Axel du Plessis
09/05/2014"""

def pair(message,counter):
    if len(message)== 1 or len(message)== 0:  
        return counter
    if message[0] == message[1]:
        counter += 1
        return pair(message[2:],counter)
    else:
        return pair(message[1:],counter) 
    
message = input("Enter a message:\n")
print("Number of pairs:",pair(message,0))       