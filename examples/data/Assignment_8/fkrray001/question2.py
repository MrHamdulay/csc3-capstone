# Author : Rayaan Fakier FKRRAY001
# Date : 07 - 05 - 2014
# question2.py

def doubles (message, counter):
    # base case - stop when 1 letter left
    
    if message == "":
        return print("Number of pairs:", counter)
    # recursive step - if a double is found
    elif message[:1] == message[1:2]:
        counter+=1
        
        return doubles (message[2:], counter)
    # if no doubles found
    else:
        return doubles (message[1:], counter)

message = input("Enter a message:\n")
counter = 0
doubles (message, counter)