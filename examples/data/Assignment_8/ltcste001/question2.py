#Stephanie Latchmanan
#5 May 2014
#Assignment 8 (Finding pairs of repeated characters)

#create a recursive function
def pairs(msg):
    if len(msg) == 1: #stop recursion if string has one character left
        return 0
    if len(msg) == 2:  
        if msg[0] == msg[1]:  #check if last 2 characters are pairs
            return 1
        else:
            return 0
    if msg[0] == msg[1]:   #check for pairs
        return 1 + pairs(msg[2:])    #count pair if pair present
    else:
        return pairs(msg[1:])  #seperate current character freom rest of string
    
#input a message
msg = input("Enter a message:\n")
#print the returning function
print("Number of pairs:", pairs(msg))